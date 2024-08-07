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
    'GetWorkspaceManagerAssignmentResult',
    'AwaitableGetWorkspaceManagerAssignmentResult',
    'get_workspace_manager_assignment',
    'get_workspace_manager_assignment_output',
]

@pulumi.output_type
class GetWorkspaceManagerAssignmentResult:
    """
    The workspace manager assignment
    """
    def __init__(__self__, etag=None, id=None, items=None, last_job_end_time=None, last_job_provisioning_state=None, name=None, system_data=None, target_resource_name=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if last_job_end_time and not isinstance(last_job_end_time, str):
            raise TypeError("Expected argument 'last_job_end_time' to be a str")
        pulumi.set(__self__, "last_job_end_time", last_job_end_time)
        if last_job_provisioning_state and not isinstance(last_job_provisioning_state, str):
            raise TypeError("Expected argument 'last_job_provisioning_state' to be a str")
        pulumi.set(__self__, "last_job_provisioning_state", last_job_provisioning_state)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if target_resource_name and not isinstance(target_resource_name, str):
            raise TypeError("Expected argument 'target_resource_name' to be a str")
        pulumi.set(__self__, "target_resource_name", target_resource_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.AssignmentItemResponse']:
        """
        List of resources included in this workspace manager assignment
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="lastJobEndTime")
    def last_job_end_time(self) -> str:
        """
        The time the last job associated to this assignment ended at
        """
        return pulumi.get(self, "last_job_end_time")

    @property
    @pulumi.getter(name="lastJobProvisioningState")
    def last_job_provisioning_state(self) -> str:
        """
        State of the last job associated to this assignment
        """
        return pulumi.get(self, "last_job_provisioning_state")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> str:
        """
        The resource name of the workspace manager group targeted by the workspace manager assignment
        """
        return pulumi.get(self, "target_resource_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceManagerAssignmentResult(GetWorkspaceManagerAssignmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceManagerAssignmentResult(
            etag=self.etag,
            id=self.id,
            items=self.items,
            last_job_end_time=self.last_job_end_time,
            last_job_provisioning_state=self.last_job_provisioning_state,
            name=self.name,
            system_data=self.system_data,
            target_resource_name=self.target_resource_name,
            type=self.type)


def get_workspace_manager_assignment(resource_group_name: Optional[str] = None,
                                     workspace_manager_assignment_name: Optional[str] = None,
                                     workspace_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceManagerAssignmentResult:
    """
    Gets a workspace manager assignment


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_manager_assignment_name: The name of the workspace manager assignment
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceManagerAssignmentName'] = workspace_manager_assignment_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20240101preview:getWorkspaceManagerAssignment', __args__, opts=opts, typ=GetWorkspaceManagerAssignmentResult).value

    return AwaitableGetWorkspaceManagerAssignmentResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        last_job_end_time=pulumi.get(__ret__, 'last_job_end_time'),
        last_job_provisioning_state=pulumi.get(__ret__, 'last_job_provisioning_state'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        target_resource_name=pulumi.get(__ret__, 'target_resource_name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace_manager_assignment)
def get_workspace_manager_assignment_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                            workspace_manager_assignment_name: Optional[pulumi.Input[str]] = None,
                                            workspace_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceManagerAssignmentResult]:
    """
    Gets a workspace manager assignment


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_manager_assignment_name: The name of the workspace manager assignment
    :param str workspace_name: The name of the workspace.
    """
    ...
