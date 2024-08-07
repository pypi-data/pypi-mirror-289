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
    'ListListPendingFlowResult',
    'AwaitableListListPendingFlowResult',
    'list_list_pending_flow',
    'list_list_pending_flow_output',
]

@pulumi.output_type
class ListListPendingFlowResult:
    """
    The connections list result.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        Link to next results
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.PendingFlowResponse']]:
        """
        flows array.
        """
        return pulumi.get(self, "value")


class AwaitableListListPendingFlowResult(ListListPendingFlowResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListListPendingFlowResult(
            next_link=self.next_link,
            value=self.value)


def list_list_pending_flow(connection_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListListPendingFlowResult:
    """
    Lists all pending flows for a connection.


    :param str connection_name: The name for the connection that is to be requested.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['connectionName'] = connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azuredatatransfer/v20231011preview:listListPendingFlow', __args__, opts=opts, typ=ListListPendingFlowResult).value

    return AwaitableListListPendingFlowResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_list_pending_flow)
def list_list_pending_flow_output(connection_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListListPendingFlowResult]:
    """
    Lists all pending flows for a connection.


    :param str connection_name: The name for the connection that is to be requested.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
