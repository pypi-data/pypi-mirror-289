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
    'GetWorkspaceManagerConfigurationResult',
    'AwaitableGetWorkspaceManagerConfigurationResult',
    'get_workspace_manager_configuration',
    'get_workspace_manager_configuration_output',
]

@pulumi.output_type
class GetWorkspaceManagerConfigurationResult:
    """
    The workspace manager configuration
    """
    def __init__(__self__, etag=None, id=None, mode=None, name=None, system_data=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
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
    def mode(self) -> str:
        """
        The current mode of the workspace manager configuration
        """
        return pulumi.get(self, "mode")

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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceManagerConfigurationResult(GetWorkspaceManagerConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceManagerConfigurationResult(
            etag=self.etag,
            id=self.id,
            mode=self.mode,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_workspace_manager_configuration(resource_group_name: Optional[str] = None,
                                        workspace_manager_configuration_name: Optional[str] = None,
                                        workspace_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceManagerConfigurationResult:
    """
    Gets a workspace manager configuration


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_manager_configuration_name: The name of the workspace manager configuration
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceManagerConfigurationName'] = workspace_manager_configuration_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20230801preview:getWorkspaceManagerConfiguration', __args__, opts=opts, typ=GetWorkspaceManagerConfigurationResult).value

    return AwaitableGetWorkspaceManagerConfigurationResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        mode=pulumi.get(__ret__, 'mode'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace_manager_configuration)
def get_workspace_manager_configuration_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                               workspace_manager_configuration_name: Optional[pulumi.Input[str]] = None,
                                               workspace_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceManagerConfigurationResult]:
    """
    Gets a workspace manager configuration


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_manager_configuration_name: The name of the workspace manager configuration
    :param str workspace_name: The name of the workspace.
    """
    ...
