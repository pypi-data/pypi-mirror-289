import asyncio

from airflow.triggers.base import BaseTrigger, TriggerEvent

from environment_info.gcp_env import get_gcp_project_id, deploy_region
from hooks.custom_datapro_hook_v2 import CustomDataProcHookV2


class DataprocClusterTrigger(BaseTrigger):

    def __init__(self,
                 operation_name,
                 project_id=None,
                 region=None,
                 *args,
                 **kwargs):
        super().__init__()
        self.operation_name = operation_name
        self.project_id = project_id
        self.region = region

    def serialize(self):
        return ("airflow_custom_trigger_dv01.dataproc_trigger.DataprocClusterTrigger",
                {"operation_name": self.operation_name,
                 "project_id": self.project_id,
                 "region": self.region})

    async def run(self):
        hook = CustomDataProcHookV2(self.region)
        operation = hook.get_operation_object(self.operation_name)
        while not operation.create_cluster_done:
            await asyncio.sleep(30)
            operation.update_operation()
        yield TriggerEvent({"operation_name": self.operation_name})


class DataprocJobTrigger(BaseTrigger):

    def __init__(self,
                 operation_name,
                 project_id=None,
                 region=None,
                 *args,
                 **kwargs):
        super().__init__()
        self.operation_name = operation_name
        self.project_id = project_id
        self.region = region or deploy_region()

    def serialize(self):
        return ("airflow_custom_trigger_dv01.dataproc_trigger.DataprocJobTrigger",
                {"operation_name": self.operation_name,
                 "project_id": self.project_id,
                 "region": self.region})

    async def run(self):
        hook = CustomDataProcHookV2(self.region)
        operation = hook.get_operation_object(self.operation_name)
        operation.update_operation()
        while not operation.get_result():
            await asyncio.sleep(30)
            operation.update_operation()
        yield TriggerEvent({"operation_name": self.operation_name})
