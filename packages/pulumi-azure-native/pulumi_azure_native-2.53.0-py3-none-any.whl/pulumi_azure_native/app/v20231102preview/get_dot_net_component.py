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
    'GetDotNetComponentResult',
    'AwaitableGetDotNetComponentResult',
    'get_dot_net_component',
    'get_dot_net_component_output',
]

@pulumi.output_type
class GetDotNetComponentResult:
    """
    .NET Component.
    """
    def __init__(__self__, component_type=None, configurations=None, id=None, name=None, provisioning_state=None, service_binds=None, system_data=None, type=None):
        if component_type and not isinstance(component_type, str):
            raise TypeError("Expected argument 'component_type' to be a str")
        pulumi.set(__self__, "component_type", component_type)
        if configurations and not isinstance(configurations, list):
            raise TypeError("Expected argument 'configurations' to be a list")
        pulumi.set(__self__, "configurations", configurations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_binds and not isinstance(service_binds, list):
            raise TypeError("Expected argument 'service_binds' to be a list")
        pulumi.set(__self__, "service_binds", service_binds)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[str]:
        """
        Type of the .NET Component.
        """
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence['outputs.DotNetComponentConfigurationPropertyResponse']]:
        """
        List of .NET Components configuration properties
        """
        return pulumi.get(self, "configurations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the .NET Component.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[Sequence['outputs.DotNetComponentServiceBindResponse']]:
        """
        List of .NET Components that are bound to the .NET component
        """
        return pulumi.get(self, "service_binds")

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


class AwaitableGetDotNetComponentResult(GetDotNetComponentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDotNetComponentResult(
            component_type=self.component_type,
            configurations=self.configurations,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            service_binds=self.service_binds,
            system_data=self.system_data,
            type=self.type)


def get_dot_net_component(environment_name: Optional[str] = None,
                          name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDotNetComponentResult:
    """
    .NET Component.


    :param str environment_name: Name of the Managed Environment.
    :param str name: Name of the .NET Component.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20231102preview:getDotNetComponent', __args__, opts=opts, typ=GetDotNetComponentResult).value

    return AwaitableGetDotNetComponentResult(
        component_type=pulumi.get(__ret__, 'component_type'),
        configurations=pulumi.get(__ret__, 'configurations'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        service_binds=pulumi.get(__ret__, 'service_binds'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_dot_net_component)
def get_dot_net_component_output(environment_name: Optional[pulumi.Input[str]] = None,
                                 name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDotNetComponentResult]:
    """
    .NET Component.


    :param str environment_name: Name of the Managed Environment.
    :param str name: Name of the .NET Component.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
