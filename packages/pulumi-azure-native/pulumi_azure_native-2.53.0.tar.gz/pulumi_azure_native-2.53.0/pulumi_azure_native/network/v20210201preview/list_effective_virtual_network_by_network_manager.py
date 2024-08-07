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
    'ListEffectiveVirtualNetworkByNetworkManagerResult',
    'AwaitableListEffectiveVirtualNetworkByNetworkManagerResult',
    'list_effective_virtual_network_by_network_manager',
    'list_effective_virtual_network_by_network_manager_output',
]

@pulumi.output_type
class ListEffectiveVirtualNetworkByNetworkManagerResult:
    """
    Result of the request to list Effective Virtual Network. It contains a list of groups and a URL link to get the next set of results.
    """
    def __init__(__self__, skip_token=None, value=None):
        if skip_token and not isinstance(skip_token, str):
            raise TypeError("Expected argument 'skip_token' to be a str")
        pulumi.set(__self__, "skip_token", skip_token)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[str]:
        """
        When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.
        """
        return pulumi.get(self, "skip_token")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.EffectiveVirtualNetworkResponse']]:
        """
        Gets a page of EffectiveVirtualNetwork
        """
        return pulumi.get(self, "value")


class AwaitableListEffectiveVirtualNetworkByNetworkManagerResult(ListEffectiveVirtualNetworkByNetworkManagerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListEffectiveVirtualNetworkByNetworkManagerResult(
            skip_token=self.skip_token,
            value=self.value)


def list_effective_virtual_network_by_network_manager(conditional_members: Optional[str] = None,
                                                      network_manager_name: Optional[str] = None,
                                                      resource_group_name: Optional[str] = None,
                                                      skip_token: Optional[str] = None,
                                                      top: Optional[int] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListEffectiveVirtualNetworkByNetworkManagerResult:
    """
    List effective virtual networks in a network manager.


    :param str conditional_members: Conditional Members.
    :param str network_manager_name: The name of the network manager.
    :param str resource_group_name: The name of the resource group.
    :param str skip_token: Continuation token for pagination, capturing the next page size and offset, as well as the context of the query.
    :param int top: An optional query parameter which specifies the maximum number of records to be returned by the server.
    """
    __args__ = dict()
    __args__['conditionalMembers'] = conditional_members
    __args__['networkManagerName'] = network_manager_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['skipToken'] = skip_token
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20210201preview:listEffectiveVirtualNetworkByNetworkManager', __args__, opts=opts, typ=ListEffectiveVirtualNetworkByNetworkManagerResult).value

    return AwaitableListEffectiveVirtualNetworkByNetworkManagerResult(
        skip_token=pulumi.get(__ret__, 'skip_token'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_effective_virtual_network_by_network_manager)
def list_effective_virtual_network_by_network_manager_output(conditional_members: Optional[pulumi.Input[Optional[str]]] = None,
                                                             network_manager_name: Optional[pulumi.Input[str]] = None,
                                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                                             skip_token: Optional[pulumi.Input[Optional[str]]] = None,
                                                             top: Optional[pulumi.Input[Optional[int]]] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListEffectiveVirtualNetworkByNetworkManagerResult]:
    """
    List effective virtual networks in a network manager.


    :param str conditional_members: Conditional Members.
    :param str network_manager_name: The name of the network manager.
    :param str resource_group_name: The name of the resource group.
    :param str skip_token: Continuation token for pagination, capturing the next page size and offset, as well as the context of the query.
    :param int top: An optional query parameter which specifies the maximum number of records to be returned by the server.
    """
    ...
