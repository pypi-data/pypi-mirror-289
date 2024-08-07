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
from .. import _utilities
from . import outputs

__all__ = [
    'ListUserAssignedIdentityAssociatedResourcesResult',
    'AwaitableListUserAssignedIdentityAssociatedResourcesResult',
    'list_user_assigned_identity_associated_resources',
    'list_user_assigned_identity_associated_resources_output',
]

@pulumi.output_type
class ListUserAssignedIdentityAssociatedResourcesResult:
    """
    Azure resources returned by the resource action to get a list of assigned resources.
    """
    def __init__(__self__, next_link=None, total_count=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if total_count and not isinstance(total_count, float):
            raise TypeError("Expected argument 'total_count' to be a float")
        pulumi.set(__self__, "total_count", total_count)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        The url to get the next page of results, if any.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter(name="totalCount")
    def total_count(self) -> float:
        """
        Total number of Azure resources assigned to the identity.
        """
        return pulumi.get(self, "total_count")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.AzureResourceResponse']:
        """
        The collection of Azure resources returned by the resource action to get a list of assigned resources.
        """
        return pulumi.get(self, "value")


class AwaitableListUserAssignedIdentityAssociatedResourcesResult(ListUserAssignedIdentityAssociatedResourcesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListUserAssignedIdentityAssociatedResourcesResult(
            next_link=self.next_link,
            total_count=self.total_count,
            value=self.value)


def list_user_assigned_identity_associated_resources(filter: Optional[str] = None,
                                                     orderby: Optional[str] = None,
                                                     resource_group_name: Optional[str] = None,
                                                     resource_name: Optional[str] = None,
                                                     skip: Optional[int] = None,
                                                     skiptoken: Optional[str] = None,
                                                     top: Optional[int] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListUserAssignedIdentityAssociatedResourcesResult:
    """
    Lists the associated resources for this identity.
    Azure REST API version: 2022-01-31-preview.


    :param str filter: OData filter expression to apply to the query.
    :param str orderby: OData orderBy expression to apply to the query.
    :param str resource_group_name: The name of the Resource Group to which the identity belongs.
    :param str resource_name: The name of the identity resource.
    :param int skip: Number of records to skip.
    :param str skiptoken: A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    :param int top: Number of records to return.
    """
    __args__ = dict()
    __args__['filter'] = filter
    __args__['orderby'] = orderby
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    __args__['skip'] = skip
    __args__['skiptoken'] = skiptoken
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managedidentity:listUserAssignedIdentityAssociatedResources', __args__, opts=opts, typ=ListUserAssignedIdentityAssociatedResourcesResult).value

    return AwaitableListUserAssignedIdentityAssociatedResourcesResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        total_count=pulumi.get(__ret__, 'total_count'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_user_assigned_identity_associated_resources)
def list_user_assigned_identity_associated_resources_output(filter: Optional[pulumi.Input[Optional[str]]] = None,
                                                            orderby: Optional[pulumi.Input[Optional[str]]] = None,
                                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                                            resource_name: Optional[pulumi.Input[str]] = None,
                                                            skip: Optional[pulumi.Input[Optional[int]]] = None,
                                                            skiptoken: Optional[pulumi.Input[Optional[str]]] = None,
                                                            top: Optional[pulumi.Input[Optional[int]]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListUserAssignedIdentityAssociatedResourcesResult]:
    """
    Lists the associated resources for this identity.
    Azure REST API version: 2022-01-31-preview.


    :param str filter: OData filter expression to apply to the query.
    :param str orderby: OData orderBy expression to apply to the query.
    :param str resource_group_name: The name of the Resource Group to which the identity belongs.
    :param str resource_name: The name of the identity resource.
    :param int skip: Number of records to skip.
    :param str skiptoken: A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    :param int top: Number of records to return.
    """
    ...
