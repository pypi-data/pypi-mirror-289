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
    'GetEnvironmentResult',
    'AwaitableGetEnvironmentResult',
    'get_environment',
    'get_environment_output',
]

@pulumi.output_type
class GetEnvironmentResult:
    """
    Environment entity.
    """
    def __init__(__self__, custom_properties=None, description=None, id=None, kind=None, name=None, onboarding=None, server=None, system_data=None, title=None, type=None):
        if custom_properties and not isinstance(custom_properties, dict):
            raise TypeError("Expected argument 'custom_properties' to be a dict")
        pulumi.set(__self__, "custom_properties", custom_properties)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if onboarding and not isinstance(onboarding, dict):
            raise TypeError("Expected argument 'onboarding' to be a dict")
        pulumi.set(__self__, "onboarding", onboarding)
        if server and not isinstance(server, dict):
            raise TypeError("Expected argument 'server' to be a dict")
        pulumi.set(__self__, "server", server)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Any]:
        """
        The custom metadata defined for API catalog entities.
        """
        return pulumi.get(self, "custom_properties")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The environment description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Environment kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def onboarding(self) -> Optional['outputs.OnboardingResponse']:
        """
        Environment onboarding information
        """
        return pulumi.get(self, "onboarding")

    @property
    @pulumi.getter
    def server(self) -> Optional['outputs.EnvironmentServerResponse']:
        """
        Server information of the environment.
        """
        return pulumi.get(self, "server")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Environment title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentResult(
            custom_properties=self.custom_properties,
            description=self.description,
            id=self.id,
            kind=self.kind,
            name=self.name,
            onboarding=self.onboarding,
            server=self.server,
            system_data=self.system_data,
            title=self.title,
            type=self.type)


def get_environment(environment_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    service_name: Optional[str] = None,
                    workspace_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentResult:
    """
    Returns details of the environment.


    :param str environment_name: The name of the environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of Azure API Center service.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apicenter/v20240301:getEnvironment', __args__, opts=opts, typ=GetEnvironmentResult).value

    return AwaitableGetEnvironmentResult(
        custom_properties=pulumi.get(__ret__, 'custom_properties'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        onboarding=pulumi.get(__ret__, 'onboarding'),
        server=pulumi.get(__ret__, 'server'),
        system_data=pulumi.get(__ret__, 'system_data'),
        title=pulumi.get(__ret__, 'title'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_environment)
def get_environment_output(environment_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           service_name: Optional[pulumi.Input[str]] = None,
                           workspace_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvironmentResult]:
    """
    Returns details of the environment.


    :param str environment_name: The name of the environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of Azure API Center service.
    :param str workspace_name: The name of the workspace.
    """
    ...
