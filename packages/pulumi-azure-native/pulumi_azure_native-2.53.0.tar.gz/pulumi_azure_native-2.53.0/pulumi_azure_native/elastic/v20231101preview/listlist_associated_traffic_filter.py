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
    'ListlistAssociatedTrafficFilterResult',
    'AwaitableListlistAssociatedTrafficFilterResult',
    'listlist_associated_traffic_filter',
    'listlist_associated_traffic_filter_output',
]

@pulumi.output_type
class ListlistAssociatedTrafficFilterResult:
    """
    List of elastic traffic filters in the account
    """
    def __init__(__self__, rulesets=None):
        if rulesets and not isinstance(rulesets, list):
            raise TypeError("Expected argument 'rulesets' to be a list")
        pulumi.set(__self__, "rulesets", rulesets)

    @property
    @pulumi.getter
    def rulesets(self) -> Optional[Sequence['outputs.ElasticTrafficFilterResponse']]:
        """
        List of elastic traffic filters in the account
        """
        return pulumi.get(self, "rulesets")


class AwaitableListlistAssociatedTrafficFilterResult(ListlistAssociatedTrafficFilterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListlistAssociatedTrafficFilterResult(
            rulesets=self.rulesets)


def listlist_associated_traffic_filter(monitor_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListlistAssociatedTrafficFilterResult:
    """
    List of elastic traffic filters in the account


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic/v20231101preview:listlistAssociatedTrafficFilter', __args__, opts=opts, typ=ListlistAssociatedTrafficFilterResult).value

    return AwaitableListlistAssociatedTrafficFilterResult(
        rulesets=pulumi.get(__ret__, 'rulesets'))


@_utilities.lift_output_func(listlist_associated_traffic_filter)
def listlist_associated_traffic_filter_output(monitor_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListlistAssociatedTrafficFilterResult]:
    """
    List of elastic traffic filters in the account


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
