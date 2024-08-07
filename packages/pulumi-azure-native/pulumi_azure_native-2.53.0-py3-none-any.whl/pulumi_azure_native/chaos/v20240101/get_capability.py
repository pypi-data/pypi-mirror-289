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
    'GetCapabilityResult',
    'AwaitableGetCapabilityResult',
    'get_capability',
    'get_capability_output',
]

@pulumi.output_type
class GetCapabilityResult:
    """
    Model that represents a Capability resource.
    """
    def __init__(__self__, id=None, name=None, properties=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
    @pulumi.getter
    def properties(self) -> 'outputs.CapabilityPropertiesResponse':
        """
        The properties of a capability resource.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The standard system metadata of a resource type.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetCapabilityResult(GetCapabilityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCapabilityResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_capability(capability_name: Optional[str] = None,
                   parent_provider_namespace: Optional[str] = None,
                   parent_resource_name: Optional[str] = None,
                   parent_resource_type: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   target_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCapabilityResult:
    """
    Get a Capability resource that extends a Target resource.


    :param str capability_name: String that represents a Capability resource name.
    :param str parent_provider_namespace: String that represents a resource provider namespace.
    :param str parent_resource_name: String that represents a resource name.
    :param str parent_resource_type: String that represents a resource type.
    :param str resource_group_name: String that represents an Azure resource group.
    :param str target_name: String that represents a Target resource name.
    """
    __args__ = dict()
    __args__['capabilityName'] = capability_name
    __args__['parentProviderNamespace'] = parent_provider_namespace
    __args__['parentResourceName'] = parent_resource_name
    __args__['parentResourceType'] = parent_resource_type
    __args__['resourceGroupName'] = resource_group_name
    __args__['targetName'] = target_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:chaos/v20240101:getCapability', __args__, opts=opts, typ=GetCapabilityResult).value

    return AwaitableGetCapabilityResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_capability)
def get_capability_output(capability_name: Optional[pulumi.Input[str]] = None,
                          parent_provider_namespace: Optional[pulumi.Input[str]] = None,
                          parent_resource_name: Optional[pulumi.Input[str]] = None,
                          parent_resource_type: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          target_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCapabilityResult]:
    """
    Get a Capability resource that extends a Target resource.


    :param str capability_name: String that represents a Capability resource name.
    :param str parent_provider_namespace: String that represents a resource provider namespace.
    :param str parent_resource_name: String that represents a resource name.
    :param str parent_resource_type: String that represents a resource type.
    :param str resource_group_name: String that represents an Azure resource group.
    :param str target_name: String that represents a Target resource name.
    """
    ...
