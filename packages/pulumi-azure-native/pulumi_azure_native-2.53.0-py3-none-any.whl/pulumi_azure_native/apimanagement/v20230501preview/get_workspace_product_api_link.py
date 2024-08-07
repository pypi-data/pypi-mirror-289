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

__all__ = [
    'GetWorkspaceProductApiLinkResult',
    'AwaitableGetWorkspaceProductApiLinkResult',
    'get_workspace_product_api_link',
    'get_workspace_product_api_link_output',
]

@pulumi.output_type
class GetWorkspaceProductApiLinkResult:
    """
    Product-API link details.
    """
    def __init__(__self__, api_id=None, id=None, name=None, type=None):
        if api_id and not isinstance(api_id, str):
            raise TypeError("Expected argument 'api_id' to be a str")
        pulumi.set(__self__, "api_id", api_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> str:
        """
        Full resource Id of an API.
        """
        return pulumi.get(self, "api_id")

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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceProductApiLinkResult(GetWorkspaceProductApiLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceProductApiLinkResult(
            api_id=self.api_id,
            id=self.id,
            name=self.name,
            type=self.type)


def get_workspace_product_api_link(api_link_id: Optional[str] = None,
                                   product_id: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   service_name: Optional[str] = None,
                                   workspace_id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceProductApiLinkResult:
    """
    Gets the API link for the product.


    :param str api_link_id: Product-API link identifier. Must be unique in the current API Management service instance.
    :param str product_id: Product identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    __args__ = dict()
    __args__['apiLinkId'] = api_link_id
    __args__['productId'] = product_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230501preview:getWorkspaceProductApiLink', __args__, opts=opts, typ=GetWorkspaceProductApiLinkResult).value

    return AwaitableGetWorkspaceProductApiLinkResult(
        api_id=pulumi.get(__ret__, 'api_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace_product_api_link)
def get_workspace_product_api_link_output(api_link_id: Optional[pulumi.Input[str]] = None,
                                          product_id: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          service_name: Optional[pulumi.Input[str]] = None,
                                          workspace_id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceProductApiLinkResult]:
    """
    Gets the API link for the product.


    :param str api_link_id: Product-API link identifier. Must be unique in the current API Management service instance.
    :param str product_id: Product identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    ...
