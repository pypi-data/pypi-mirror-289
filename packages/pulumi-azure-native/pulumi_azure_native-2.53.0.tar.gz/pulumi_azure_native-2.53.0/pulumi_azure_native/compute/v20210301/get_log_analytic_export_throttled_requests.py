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
    'GetLogAnalyticExportThrottledRequestsResult',
    'AwaitableGetLogAnalyticExportThrottledRequestsResult',
    'get_log_analytic_export_throttled_requests',
    'get_log_analytic_export_throttled_requests_output',
]

@pulumi.output_type
class GetLogAnalyticExportThrottledRequestsResult:
    """
    LogAnalytics operation status response
    """
    def __init__(__self__, properties=None):
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.LogAnalyticsOutputResponse':
        """
        LogAnalyticsOutput
        """
        return pulumi.get(self, "properties")


class AwaitableGetLogAnalyticExportThrottledRequestsResult(GetLogAnalyticExportThrottledRequestsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogAnalyticExportThrottledRequestsResult(
            properties=self.properties)


def get_log_analytic_export_throttled_requests(blob_container_sas_uri: Optional[str] = None,
                                               from_time: Optional[str] = None,
                                               group_by_client_application_id: Optional[bool] = None,
                                               group_by_operation_name: Optional[bool] = None,
                                               group_by_resource_name: Optional[bool] = None,
                                               group_by_throttle_policy: Optional[bool] = None,
                                               group_by_user_agent: Optional[bool] = None,
                                               location: Optional[str] = None,
                                               to_time: Optional[str] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogAnalyticExportThrottledRequestsResult:
    """
    Export logs that show total throttled Api requests for this subscription in the given time window.


    :param str blob_container_sas_uri: SAS Uri of the logging blob container to which LogAnalytics Api writes output logs to.
    :param str from_time: From time of the query
    :param bool group_by_client_application_id: Group query result by Client Application ID.
    :param bool group_by_operation_name: Group query result by Operation Name.
    :param bool group_by_resource_name: Group query result by Resource Name.
    :param bool group_by_throttle_policy: Group query result by Throttle Policy applied.
    :param bool group_by_user_agent: Group query result by User Agent.
    :param str location: The location upon which virtual-machine-sizes is queried.
    :param str to_time: To time of the query
    """
    __args__ = dict()
    __args__['blobContainerSasUri'] = blob_container_sas_uri
    __args__['fromTime'] = from_time
    __args__['groupByClientApplicationId'] = group_by_client_application_id
    __args__['groupByOperationName'] = group_by_operation_name
    __args__['groupByResourceName'] = group_by_resource_name
    __args__['groupByThrottlePolicy'] = group_by_throttle_policy
    __args__['groupByUserAgent'] = group_by_user_agent
    __args__['location'] = location
    __args__['toTime'] = to_time
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20210301:getLogAnalyticExportThrottledRequests', __args__, opts=opts, typ=GetLogAnalyticExportThrottledRequestsResult).value

    return AwaitableGetLogAnalyticExportThrottledRequestsResult(
        properties=pulumi.get(__ret__, 'properties'))


@_utilities.lift_output_func(get_log_analytic_export_throttled_requests)
def get_log_analytic_export_throttled_requests_output(blob_container_sas_uri: Optional[pulumi.Input[str]] = None,
                                                      from_time: Optional[pulumi.Input[str]] = None,
                                                      group_by_client_application_id: Optional[pulumi.Input[Optional[bool]]] = None,
                                                      group_by_operation_name: Optional[pulumi.Input[Optional[bool]]] = None,
                                                      group_by_resource_name: Optional[pulumi.Input[Optional[bool]]] = None,
                                                      group_by_throttle_policy: Optional[pulumi.Input[Optional[bool]]] = None,
                                                      group_by_user_agent: Optional[pulumi.Input[Optional[bool]]] = None,
                                                      location: Optional[pulumi.Input[str]] = None,
                                                      to_time: Optional[pulumi.Input[str]] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLogAnalyticExportThrottledRequestsResult]:
    """
    Export logs that show total throttled Api requests for this subscription in the given time window.


    :param str blob_container_sas_uri: SAS Uri of the logging blob container to which LogAnalytics Api writes output logs to.
    :param str from_time: From time of the query
    :param bool group_by_client_application_id: Group query result by Client Application ID.
    :param bool group_by_operation_name: Group query result by Operation Name.
    :param bool group_by_resource_name: Group query result by Resource Name.
    :param bool group_by_throttle_policy: Group query result by Throttle Policy applied.
    :param bool group_by_user_agent: Group query result by User Agent.
    :param str location: The location upon which virtual-machine-sizes is queried.
    :param str to_time: To time of the query
    """
    ...
