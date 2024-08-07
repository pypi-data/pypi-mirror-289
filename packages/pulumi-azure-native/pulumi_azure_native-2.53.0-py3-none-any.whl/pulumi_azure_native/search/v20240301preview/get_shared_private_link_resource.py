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
    'GetSharedPrivateLinkResourceResult',
    'AwaitableGetSharedPrivateLinkResourceResult',
    'get_shared_private_link_resource',
    'get_shared_private_link_resource_output',
]

@pulumi.output_type
class GetSharedPrivateLinkResourceResult:
    """
    Describes a shared private link resource managed by the Azure AI Search service.
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
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
    def properties(self) -> 'outputs.SharedPrivateLinkResourcePropertiesResponse':
        """
        Describes the properties of a shared private link resource managed by the Azure AI Search service.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSharedPrivateLinkResourceResult(GetSharedPrivateLinkResourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSharedPrivateLinkResourceResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_shared_private_link_resource(resource_group_name: Optional[str] = None,
                                     search_service_name: Optional[str] = None,
                                     shared_private_link_resource_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSharedPrivateLinkResourceResult:
    """
    Gets the details of the shared private link resource managed by the search service in the given resource group.


    :param str resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str search_service_name: The name of the Azure AI Search service associated with the specified resource group.
    :param str shared_private_link_resource_name: The name of the shared private link resource managed by the Azure AI Search service within the specified resource group.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['searchServiceName'] = search_service_name
    __args__['sharedPrivateLinkResourceName'] = shared_private_link_resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:search/v20240301preview:getSharedPrivateLinkResource', __args__, opts=opts, typ=GetSharedPrivateLinkResourceResult).value

    return AwaitableGetSharedPrivateLinkResourceResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_shared_private_link_resource)
def get_shared_private_link_resource_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                            search_service_name: Optional[pulumi.Input[str]] = None,
                                            shared_private_link_resource_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSharedPrivateLinkResourceResult]:
    """
    Gets the details of the shared private link resource managed by the search service in the given resource group.


    :param str resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str search_service_name: The name of the Azure AI Search service associated with the specified resource group.
    :param str shared_private_link_resource_name: The name of the shared private link resource managed by the Azure AI Search service within the specified resource group.
    """
    ...
