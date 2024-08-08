# backend_singularity.py: reflects new Singularity SDK as of Jul-03-2024

import os
import json
import time
import urllib
from xtlib.backends.backend_aml import AzureML
from xtlib import utils

from azure.identity import InteractiveBrowserCredential, TokenCachePersistenceOptions, AuthenticationRecord
from azureml.core.authentication import TokenAuthentication
from azure.ai.ml import command
from azure.ai.ml.entities import Environment
from azure.ai.ml import MLClient, Input, Output
from azure.ai.ml.constants import AssetTypes, InputOutputModes
from azure.ai.ml.entities import UserIdentityConfiguration

# we leverage the AzureML class to handle common AzureML operations
# and only override the needed methods

class Singularity(AzureML):
    def __init__(self, compute, compute_def, core, config, username=None, arg_dict=None):
        super().__init__(compute, compute_def, core, config, username, arg_dict)

    # API call

    def collect_env_vars(self, job_id, workspace, aml_ws_name, xt_exper_name, aml_exper_name, run_name, node_index,
        node_run, compute_target, username, description, aggregate_dest, args):
        
        node_id = utils.node_id(node_index)

        env_vars = self.build_env_vars(workspace, aml_ws_name, xt_exper_name, aml_exper_name, run_name, job_id=job_id, 
            compute_target=compute_target, username=username, description=description, aggregate_dest=aggregate_dest, 
            node_id=node_id, args=args)
        
        is_direct_run = args["direct_run"]

        box_secret = None     # obsoleted
        batch_key = None      # doesn't apply to AML
        direct_cmd = None
        if is_direct_run:
            run_specs = node_run["run_specs"]
            direct_cmd = run_specs["run_cmd"]

        # 2/2 calls to this (TODO: remove one)
        # this second call really updates the env_vars to be passed to singularity for this node run
        self.get_controller_env_vars(env_vars, node_run, node_index, args)

        return env_vars

    def submit_node_run(self, job_id, node_run, xt_ws_name, aml_ws_name, xt_exper_name, aml_exper_name, 
        compute_def, resume_name, repeat_count, using_hp, target, runs_by_box, code_dir, node_index, 
        show_aml_run_name, nodes, args):
        '''
        Submit a node run to the specified Singularity compute target.
        Args:
            job_id: the job id (e.g., "job30")
            node_run: the node run to submit (dict of run info)
            xt_ws_name: the XT workspace name (e.g., "xlm")
            aml_ws_name: the name of workspace we will use for Singularity (e.g., "xt-sing-workspace")
            xt_exper_name: the name of the XT experiment as specified by the user (e.g., "rfernand-job55")
            aml_exper_name: unsure of purpose vs.  (e.g., "rfernand__ws5__rfernand-job345")
            compute_def: the compute definition (dict)
            resume_name: the name of the resume file (e.g., "run648.0.r1")
            repeat_count: the number of times to repeat the run (e.g., 1)
            using_hp: whether or not this is an AML hyperparameter run (e.g., False)
            target: the name of the compute target specified by the user (e.g., sing-h100)
            runs_by_box: the runs by box (dict)
            code_dir: the temp. directory containing the code to run (e.g., "C:\\Users\\roland\\appData\local\temp\\...")
            node_index: the index of the node (e.g., 0)
            show_aml_run_name: should the AML run name be displayed on the console (e.g., True)
            nodes: the number of nodes being submitted with this job (e.g., 6)
            args: the arguments for this XT run command
        '''
        credential = self.config.get_credential()

        # xt singularity workspace account info
        vm_size = compute_def["vm-size"]
        vc_name = compute_def["compute"]
        docker_name = compute_def["docker"]

        service_info = self.config.get_service(aml_ws_name)
        vc_info = self.config.get_service(vc_name)

        subscription_id = service_info["subscription-id"]
        resource_group = service_info["resource-group"]

        # configure vc / compute
        compute = vc_name
        compute_subscription_id = vc_info["subscription-id"]
        compute_resource_group = vc_info["resource-group"]
        
        compute_config = f"/subscriptions/{compute_subscription_id}/resourceGroups/{compute_resource_group}/providers/Microsoft.MachineLearningServices/virtualclusters/{vc_name}"

        vc_config = {
            "instance_type": vm_size,
            "instance_count": 1, #Set instance 
            "properties": {
                "AISuperComputer": {
                    "interactive": True,
                    "slaTier": "Premium",            # recommended by GCR (enabled SSH to container)
                    "enableAzmlInt": False,
                    "tensorboardLogDirectory": "/scratch/tensorboard_logs",
                    "scalePolicy": {
                        "autoScaleIntervalInSec": 120,
                        "maxInstanceTypeCount": 1,
                        "minInstanceTypeCount": 1, 
                    },
                }
            }
        }

        # use the connected AML datastore as output
        #output_path = "azureml://datastores/ericdatastoretest/paths/"
        output_path = "azureml://datastores/00_aml_datastore/paths/"

        docker_image, login_server, docker_registry, _ = self.config.get_docker_info(target, docker_name, required=False)

        docker_image_url = f"{login_server}/{docker_image}"
        environment = Environment(image=docker_image_url)

        display_name = args["display_name"]
        run_name = node_run["run_name"]
        display_name = utils.expand_xt_vars(display_name, job_id=job_id, run_id=run_name, node_index=node_index)

        muai_id = args["user_assigned_managed_identity"]
        identity = UserIdentityConfiguration()

        # /bin/bash', '--login', '__node_script__.sh'
        cmd_parts = node_run["run_specs"]["cmd_parts"]
        cmd_line = cmd_parts[-1]         # last part is the command to run (rest is __aml_shim__ stuff)                   

        username = args["username"]
        description = args["description"]
        aggregate_dest = args["aggregate_dest"]

        env_vars_dict = self.collect_env_vars(job_id, xt_ws_name, aml_ws_name, xt_exper_name, aml_exper_name, run_name, 
            node_index, node_run, target, username, description, aggregate_dest, args)

        env_vars_dict["JOB_EXECUTION_MODE"] = "basic"
        env_vars_dict["AZUREML_COMPUTE_USE_COMMON_RUNTIME"] = "true"

        job = command(
            code=code_dir,       # local path where the code is stored (these files will be uploaded to our aml workspace)
            command=cmd_line,
            outputs = {"output_data": Output(type=AssetTypes.URI_FOLDER, path=output_path, mode=InputOutputModes.RW_MOUNT)},

            environment=environment,
            environment_variables=env_vars_dict,
            experiment_name= xt_exper_name,    # rfernand_sing_testing", 
            display_name=display_name,
            compute=compute_config,
            distribution={
                "type": "PyTorch",
                "process_count_per_instance": 1,                 # How many GPUs
            },
            #identity=identity,
            resources=vc_config)  

        # create the MLCient object, for submitting our job
        ml_client = MLClient(credential, subscription_id=subscription_id, resource_group_name=resource_group, workspace_name=aml_ws_name)
        returned_job = ml_client.jobs.create_or_update(job)      # submit the command
        print(returned_job.studio_url) 

        # # test singularity workspace by listings runs for a given experiment
        # experiment_name = "rfernand-job55"
        # ws = Workspace.get(name=ws_name, subscription_id=subscription_id, resource_group=resource_group, auth=ws_cred) 
        # experiment = Experiment(ws, name=experiment_name)

        # runs = experiment.get_runs()
        # count = len(list(runs))
        # print("found {:,} runs in experiment '{}'".format(count, experiment_name))  

        print("singularity job submitted: experiment={}, job={}".format(job.experiment_name, job.display_name))

        # return node_info: all info needed for this backend (singularity) to later retrieve info about this run
        run_name = node_run["run_name"]
        node_info = {"ws": xt_ws_name, "aml_ws": aml_ws_name, "run_name": run_name, "job_id": job_id, "node_id": utils.node_id(node_index)}

        node_info["aml_exper_name"] = xt_exper_name         # aml_exper_name
        node_info["aml_run_number"] = returned_job.name     # aml_run_number
        node_info["aml_run_id"] = returned_job.name         # aml_run_id

        return node_info

    # def get_log_reader(self, service_node_info):
    #     log_reader = SingularityLogReader(self.store, self, service_node_info)
    #     return log_reader

# class SingularityLogReader():
#     def __init__(self, store, sing_backend, service_node_info, encoding='utf-8'):
#         self.store = store
#         self.sing_backend = sing_backend
#         self.service_node_info = service_node_info
#         self.encoding = encoding

#         self.start_offset = 0
#         self.end_offset = 1024*1024*1024*16     # 16 GB should be big enough for a log file
#         self.log_name = None
#         self.log_source = None
#         self.request = None
#         self.last_node_started_msg = None

#         self.run = self.get_run()

#     def get_run(self):
#         for r in range(3):
#             # try 3 times, then just bail
#             try:
#                 run = self.sing_backend.get_node_run(self.service_node_info)
#                 break
#             except BaseException as ex:
#                 print("error during get_node_run(): {}".format(ex))
#                 time.sleep(2)

#         if not run:
#             errors.env_error(msg="unable to get run for node: {}".format(service_node_info))

#         return run

#     def read(self):
#         '''
#         used by the "xt montior" command to read the log file for a Singularity running job
#         '''
#         # FN_STDOUT_LOG = "azureml-logs/00_stdout.txt"
#         # FN_STDOUT2_LOG = "azureml-logs/70_driver_log.txt"
#         # FN_STD_OUT_TXT = "user_logs/std_out.txt"
#         # FN_STD_LOG_TXT = "user_logs/std_log.txt"

#         run = self.run
#         service_node_info = self.service_node_info

#         from_storage = True

#         job_id = utils.safe_value(service_node_info, "job_id", service_node_info["aml_exper_name"].split("-")[-1])
#         node_id =  utils.safe_value(service_node_info, "node_id", "node0")
#         workspace = service_node_info["ws"]

#         new_text = None
#         node_status = "queued"
#         next_offset = None
#         found_file = False
        
#         if self.log_name is None:
#             # exact default log name: std_log_process_0.txt   (will the "0" change?)
#             file_path = "std_log"     # prefix only for now
#         else:
#             file_path = self.log_name

#         if self.log_source != "live":
#             # try to read log from job storage (task has completed)
#             node_index = utils.node_index(node_id) 

#             job_path = "nodes/node{}/after/service_logs/{}".format(node_index, file_path)
#             if self.store.does_job_file_exist(workspace, job_id, job_path):
#                 new_text = self.store.read_job_file(workspace, job_id, job_path)
#                 aml_status = "completed"
#                 simple_status = "completed"
#                 found_file = True
#                 self.log_source = "after_logs"

#         if not found_file:
#             # read URL of log file from singularity service
#             current_details = run.get_details() 
#             aml_status = current_details["status"] 
#             simple_status = self.sing_backend.get_simple_status(aml_status)
            
#             available_logs = None
#             next_log = None
#             self.log_name = file_path
#             from_storage = False
#             self.log_source = "live"

#             if self.log_name:
#                 # reuse request for better perf (hopefully)
#                 log_files = current_details["logFiles"]
#                 aml_log_path = "user_logs/" + self.log_name

#                 # try to read one of Singularity-hosted service logs
#                 url = None
#                 for log_path in [self.log_name, aml_log_path]:
#                     for lf_name in log_files:
#                         if lf_name.startswith(log_path):         # match prefix
#                             url = log_files[lf_name]
#                             break

#                     if url:
#                         # create the request object to read the URL
#                         if not self.request:
#                             self.request = urllib.request.Request(url)
#                         elif self.request.full_url != url:
#                             #self.request.close()
#                             range_hdr = {"Range": f"bytes={self.start_offset}-"}
#                             self.request = urllib.request.Request(url=url, headers=range_hdr)

#                         try:
#                             # read the URL
#                             with urllib.request.urlopen(self.request) as response:
#                                 all_bytes = response.read()
#                         except BaseException as ex:
#                             # note: we get exception "invalid range" if no new data is available
#                             # treat any error as "no new data"
#                             all_bytes = b""

#                         # since we are now reading with range header, we only get new bytes
#                         new_bytes = all_bytes[0:]   #    [start_offset:]
#                         new_count = len(new_bytes)

#                         # not sure if we have new acceptable text yet, so default to "none found"
#                         next_offset = self.start_offset

#                         if new_count:
#                             # found some new text
#                             text = new_bytes.decode(self.encoding)
#                             found_new_text = True   

#                             # workaround for wierdness in singularity: find "node started" message and ensure it is different
#                             ns_marker = "Node started:"
                            
#                             if ns_marker in text:
#                                 index = text.find(ns_marker)
#                                 index2 = text.find("\n", index)
#                                 ns_line = text[index:index2]

#                                 #print("ns_line: {}\nlast_node_started_msg: {}".format(ns_line, self.last_node_started_msg))

#                                 if self.last_node_started_msg == ns_line:
#                                     # discard this text (its a repeat of old log); new node log is coming
#                                     found_new_text = False
#                                     #print("found repeated text; ignoring...")
#                                 else:
#                                     self.last_node_started_msg = ns_line

#                             if found_new_text:
#                                 self.start_offset += new_count
#                                 new_text = text

#                             # debug
#                             #print("url:", url)
#                         break

#         return {"new_text": new_text, "simple_status": simple_status, "log_name": self.log_name, 
#             "service_status": aml_status, "from_storage": from_storage, "log_source": self.log_source}

