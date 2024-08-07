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
    'GetWorkspaceTagProductLinkResult',
    'AwaitableGetWorkspaceTagProductLinkResult',
    'get_workspace_tag_product_link',
    'get_workspace_tag_product_link_output',
]

@pulumi.output_type
class GetWorkspaceTagProductLinkResult:
    """
    Tag-product link details.
    """
    def __init__(__self__, id=None, name=None, product_id=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if product_id and not isinstance(product_id, str):
            raise TypeError("Expected argument 'product_id' to be a str")
        pulumi.set(__self__, "product_id", product_id)
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
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        """
        Full resource Id of a product.
        """
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceTagProductLinkResult(GetWorkspaceTagProductLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceTagProductLinkResult(
            id=self.id,
            name=self.name,
            product_id=self.product_id,
            type=self.type)


def get_workspace_tag_product_link(product_link_id: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   service_name: Optional[str] = None,
                                   tag_id: Optional[str] = None,
                                   workspace_id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceTagProductLinkResult:
    """
    Gets the product link for the tag.


    :param str product_link_id: Tag-product link identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    __args__ = dict()
    __args__['productLinkId'] = product_link_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['tagId'] = tag_id
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230301preview:getWorkspaceTagProductLink', __args__, opts=opts, typ=GetWorkspaceTagProductLinkResult).value

    return AwaitableGetWorkspaceTagProductLinkResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        product_id=pulumi.get(__ret__, 'product_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace_tag_product_link)
def get_workspace_tag_product_link_output(product_link_id: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          service_name: Optional[pulumi.Input[str]] = None,
                                          tag_id: Optional[pulumi.Input[str]] = None,
                                          workspace_id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceTagProductLinkResult]:
    """
    Gets the product link for the tag.


    :param str product_link_id: Tag-product link identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    ...
