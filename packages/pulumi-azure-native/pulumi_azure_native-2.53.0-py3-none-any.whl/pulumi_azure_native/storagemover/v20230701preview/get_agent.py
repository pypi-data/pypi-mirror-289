# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from ... import _utilities
from . import outputs

__all__ = [
    'GetAgentResult',
    'AwaitableGetAgentResult',
    'get_agent',
    'get_agent_output',
]

@pulumi.output_type
class GetAgentResult:
    """
    The Agent resource.
    """
    def __init__(__self__, agent_status=None, agent_version=None, arc_resource_id=None, arc_vm_uuid=None, description=None, error_details=None, id=None, last_status_update=None, local_ip_address=None, memory_in_mb=None, name=None, number_of_cores=None, provisioning_state=None, system_data=None, type=None, uptime_in_seconds=None):
        if agent_status and not isinstance(agent_status, str):
            raise TypeError("Expected argument 'agent_status' to be a str")
        pulumi.set(__self__, "agent_status", agent_status)
        if agent_version and not isinstance(agent_version, str):
            raise TypeError("Expected argument 'agent_version' to be a str")
        pulumi.set(__self__, "agent_version", agent_version)
        if arc_resource_id and not isinstance(arc_resource_id, str):
            raise TypeError("Expected argument 'arc_resource_id' to be a str")
        pulumi.set(__self__, "arc_resource_id", arc_resource_id)
        if arc_vm_uuid and not isinstance(arc_vm_uuid, str):
            raise TypeError("Expected argument 'arc_vm_uuid' to be a str")
        pulumi.set(__self__, "arc_vm_uuid", arc_vm_uuid)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if error_details and not isinstance(error_details, dict):
            raise TypeError("Expected argument 'error_details' to be a dict")
        pulumi.set(__self__, "error_details", error_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_status_update and not isinstance(last_status_update, str):
            raise TypeError("Expected argument 'last_status_update' to be a str")
        pulumi.set(__self__, "last_status_update", last_status_update)
        if local_ip_address and not isinstance(local_ip_address, str):
            raise TypeError("Expected argument 'local_ip_address' to be a str")
        pulumi.set(__self__, "local_ip_address", local_ip_address)
        if memory_in_mb and not isinstance(memory_in_mb, float):
            raise TypeError("Expected argument 'memory_in_mb' to be a float")
        pulumi.set(__self__, "memory_in_mb", memory_in_mb)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if number_of_cores and not isinstance(number_of_cores, float):
            raise TypeError("Expected argument 'number_of_cores' to be a float")
        pulumi.set(__self__, "number_of_cores", number_of_cores)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uptime_in_seconds and not isinstance(uptime_in_seconds, float):
            raise TypeError("Expected argument 'uptime_in_seconds' to be a float")
        pulumi.set(__self__, "uptime_in_seconds", uptime_in_seconds)

    @property
    @pulumi.getter(name="agentStatus")
    def agent_status(self) -> str:
        """
        The Agent status.
        """
        return pulumi.get(self, "agent_status")

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> str:
        """
        The Agent version.
        """
        return pulumi.get(self, "agent_version")

    @property
    @pulumi.getter(name="arcResourceId")
    def arc_resource_id(self) -> str:
        """
        The fully qualified resource ID of the Hybrid Compute resource for the Agent.
        """
        return pulumi.get(self, "arc_resource_id")

    @property
    @pulumi.getter(name="arcVmUuid")
    def arc_vm_uuid(self) -> str:
        """
        The VM UUID of the Hybrid Compute resource for the Agent.
        """
        return pulumi.get(self, "arc_vm_uuid")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the Agent.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> 'outputs.AgentPropertiesResponseErrorDetails':
        return pulumi.get(self, "error_details")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastStatusUpdate")
    def last_status_update(self) -> str:
        """
        The last updated time of the Agent status.
        """
        return pulumi.get(self, "last_status_update")

    @property
    @pulumi.getter(name="localIPAddress")
    def local_ip_address(self) -> str:
        """
        Local IP address reported by the Agent.
        """
        return pulumi.get(self, "local_ip_address")

    @property
    @pulumi.getter(name="memoryInMB")
    def memory_in_mb(self) -> float:
        """
        Available memory reported by the Agent, in MB.
        """
        return pulumi.get(self, "memory_in_mb")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfCores")
    def number_of_cores(self) -> float:
        """
        Available compute cores reported by the Agent.
        """
        return pulumi.get(self, "number_of_cores")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of this resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uptimeInSeconds")
    def uptime_in_seconds(self) -> float:
        """
        Uptime of the Agent in seconds.
        """
        return pulumi.get(self, "uptime_in_seconds")


class AwaitableGetAgentResult(GetAgentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentResult(
            agent_status=self.agent_status,
            agent_version=self.agent_version,
            arc_resource_id=self.arc_resource_id,
            arc_vm_uuid=self.arc_vm_uuid,
            description=self.description,
            error_details=self.error_details,
            id=self.id,
            last_status_update=self.last_status_update,
            local_ip_address=self.local_ip_address,
            memory_in_mb=self.memory_in_mb,
            name=self.name,
            number_of_cores=self.number_of_cores,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type,
            uptime_in_seconds=self.uptime_in_seconds)


def get_agent(agent_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              storage_mover_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentResult:
    """
    Gets an Agent resource.


    :param str agent_name: The name of the Agent resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str storage_mover_name: The name of the Storage Mover resource.
    """
    __args__ = dict()
    __args__['agentName'] = agent_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['storageMoverName'] = storage_mover_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storagemover/v20230701preview:getAgent', __args__, opts=opts, typ=GetAgentResult).value

    return AwaitableGetAgentResult(
        agent_status=pulumi.get(__ret__, 'agent_status'),
        agent_version=pulumi.get(__ret__, 'agent_version'),
        arc_resource_id=pulumi.get(__ret__, 'arc_resource_id'),
        arc_vm_uuid=pulumi.get(__ret__, 'arc_vm_uuid'),
        description=pulumi.get(__ret__, 'description'),
        error_details=pulumi.get(__ret__, 'error_details'),
        id=pulumi.get(__ret__, 'id'),
        last_status_update=pulumi.get(__ret__, 'last_status_update'),
        local_ip_address=pulumi.get(__ret__, 'local_ip_address'),
        memory_in_mb=pulumi.get(__ret__, 'memory_in_mb'),
        name=pulumi.get(__ret__, 'name'),
        number_of_cores=pulumi.get(__ret__, 'number_of_cores'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        uptime_in_seconds=pulumi.get(__ret__, 'uptime_in_seconds'))


@_utilities.lift_output_func(get_agent)
def get_agent_output(agent_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     storage_mover_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentResult]:
    """
    Gets an Agent resource.


    :param str agent_name: The name of the Agent resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str storage_mover_name: The name of the Storage Mover resource.
    """
    ...
