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
    'ListHypervSitesControllerHealthSummaryResult',
    'AwaitableListHypervSitesControllerHealthSummaryResult',
    'list_hyperv_sites_controller_health_summary',
    'list_hyperv_sites_controller_health_summary_output',
]

@pulumi.output_type
class ListHypervSitesControllerHealthSummaryResult:
    """
    Collection of SiteHealthSummary.
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
    def next_link(self) -> str:
        """
        Gets the value of next link.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.SiteHealthSummaryResponse']:
        """
        Gets the list of SiteHealthSummary.
        """
        return pulumi.get(self, "value")


class AwaitableListHypervSitesControllerHealthSummaryResult(ListHypervSitesControllerHealthSummaryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListHypervSitesControllerHealthSummaryResult(
            next_link=self.next_link,
            value=self.value)


def list_hyperv_sites_controller_health_summary(resource_group_name: Optional[str] = None,
                                                site_name: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListHypervSitesControllerHealthSummaryResult:
    """
    Method to get site health summary.
    Azure REST API version: 2023-06-06.

    Other available API versions: 2023-10-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['siteName'] = site_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:offazure:listHypervSitesControllerHealthSummary', __args__, opts=opts, typ=ListHypervSitesControllerHealthSummaryResult).value

    return AwaitableListHypervSitesControllerHealthSummaryResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_hyperv_sites_controller_health_summary)
def list_hyperv_sites_controller_health_summary_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                       site_name: Optional[pulumi.Input[str]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListHypervSitesControllerHealthSummaryResult]:
    """
    Method to get site health summary.
    Azure REST API version: 2023-06-06.

    Other available API versions: 2023-10-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    """
    ...
