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
from ._enums import *

__all__ = [
    'ActivityTimelineItemResponse',
    'AnomalyTimelineItemResponse',
    'BookmarkTimelineItemResponse',
    'EntityInsightItemResponse',
    'EntityInsightItemResponseQueryTimeInterval',
    'GetInsightsErrorKindResponse',
    'GetInsightsResultsMetadataResponse',
    'InsightsTableResultResponse',
    'InsightsTableResultResponseColumns',
    'RepoResponse',
    'SecurityAlertTimelineItemResponse',
    'TimelineAggregationResponse',
    'TimelineErrorResponse',
    'TimelineResultsMetadataResponse',
    'UserInfoResponse',
]

@pulumi.output_type
class ActivityTimelineItemResponse(dict):
    """
    Represents Activity timeline item.
    """
    def __init__(__self__, *,
                 bucket_end_time_utc: str,
                 bucket_start_time_utc: str,
                 content: str,
                 first_activity_time_utc: str,
                 kind: str,
                 last_activity_time_utc: str,
                 query_id: str,
                 title: str):
        """
        Represents Activity timeline item.
        :param str bucket_end_time_utc: The grouping bucket end time.
        :param str bucket_start_time_utc: The grouping bucket start time.
        :param str content: The activity timeline content.
        :param str first_activity_time_utc: The time of the first activity in the grouping bucket.
        :param str kind: The entity query kind
               Expected value is 'Activity'.
        :param str last_activity_time_utc: The time of the last activity in the grouping bucket.
        :param str query_id: The activity query id.
        :param str title: The activity timeline title.
        """
        pulumi.set(__self__, "bucket_end_time_utc", bucket_end_time_utc)
        pulumi.set(__self__, "bucket_start_time_utc", bucket_start_time_utc)
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "first_activity_time_utc", first_activity_time_utc)
        pulumi.set(__self__, "kind", 'Activity')
        pulumi.set(__self__, "last_activity_time_utc", last_activity_time_utc)
        pulumi.set(__self__, "query_id", query_id)
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter(name="bucketEndTimeUTC")
    def bucket_end_time_utc(self) -> str:
        """
        The grouping bucket end time.
        """
        return pulumi.get(self, "bucket_end_time_utc")

    @property
    @pulumi.getter(name="bucketStartTimeUTC")
    def bucket_start_time_utc(self) -> str:
        """
        The grouping bucket start time.
        """
        return pulumi.get(self, "bucket_start_time_utc")

    @property
    @pulumi.getter
    def content(self) -> str:
        """
        The activity timeline content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="firstActivityTimeUTC")
    def first_activity_time_utc(self) -> str:
        """
        The time of the first activity in the grouping bucket.
        """
        return pulumi.get(self, "first_activity_time_utc")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The entity query kind
        Expected value is 'Activity'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastActivityTimeUTC")
    def last_activity_time_utc(self) -> str:
        """
        The time of the last activity in the grouping bucket.
        """
        return pulumi.get(self, "last_activity_time_utc")

    @property
    @pulumi.getter(name="queryId")
    def query_id(self) -> str:
        """
        The activity query id.
        """
        return pulumi.get(self, "query_id")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        The activity timeline title.
        """
        return pulumi.get(self, "title")


@pulumi.output_type
class AnomalyTimelineItemResponse(dict):
    """
    Represents anomaly timeline item.
    """
    def __init__(__self__, *,
                 azure_resource_id: str,
                 display_name: str,
                 end_time_utc: str,
                 kind: str,
                 start_time_utc: str,
                 time_generated: str,
                 description: Optional[str] = None,
                 intent: Optional[str] = None,
                 product_name: Optional[str] = None,
                 reasons: Optional[Sequence[str]] = None,
                 techniques: Optional[Sequence[str]] = None,
                 vendor: Optional[str] = None):
        """
        Represents anomaly timeline item.
        :param str azure_resource_id: The anomaly azure resource id.
        :param str display_name: The anomaly name.
        :param str end_time_utc: The anomaly end time.
        :param str kind: The entity query kind
               Expected value is 'Anomaly'.
        :param str start_time_utc: The anomaly start time.
        :param str time_generated: The anomaly generated time.
        :param str description: The anomaly description.
        :param str intent: The intent of the anomaly.
        :param str product_name: The anomaly product name.
        :param Sequence[str] reasons: The reasons that cause the anomaly.
        :param Sequence[str] techniques: The techniques of the anomaly.
        :param str vendor: The name of the anomaly vendor.
        """
        pulumi.set(__self__, "azure_resource_id", azure_resource_id)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "end_time_utc", end_time_utc)
        pulumi.set(__self__, "kind", 'Anomaly')
        pulumi.set(__self__, "start_time_utc", start_time_utc)
        pulumi.set(__self__, "time_generated", time_generated)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if intent is not None:
            pulumi.set(__self__, "intent", intent)
        if product_name is not None:
            pulumi.set(__self__, "product_name", product_name)
        if reasons is not None:
            pulumi.set(__self__, "reasons", reasons)
        if techniques is not None:
            pulumi.set(__self__, "techniques", techniques)
        if vendor is not None:
            pulumi.set(__self__, "vendor", vendor)

    @property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> str:
        """
        The anomaly azure resource id.
        """
        return pulumi.get(self, "azure_resource_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The anomaly name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> str:
        """
        The anomaly end time.
        """
        return pulumi.get(self, "end_time_utc")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The entity query kind
        Expected value is 'Anomaly'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> str:
        """
        The anomaly start time.
        """
        return pulumi.get(self, "start_time_utc")

    @property
    @pulumi.getter(name="timeGenerated")
    def time_generated(self) -> str:
        """
        The anomaly generated time.
        """
        return pulumi.get(self, "time_generated")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The anomaly description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def intent(self) -> Optional[str]:
        """
        The intent of the anomaly.
        """
        return pulumi.get(self, "intent")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[str]:
        """
        The anomaly product name.
        """
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter
    def reasons(self) -> Optional[Sequence[str]]:
        """
        The reasons that cause the anomaly.
        """
        return pulumi.get(self, "reasons")

    @property
    @pulumi.getter
    def techniques(self) -> Optional[Sequence[str]]:
        """
        The techniques of the anomaly.
        """
        return pulumi.get(self, "techniques")

    @property
    @pulumi.getter
    def vendor(self) -> Optional[str]:
        """
        The name of the anomaly vendor.
        """
        return pulumi.get(self, "vendor")


@pulumi.output_type
class BookmarkTimelineItemResponse(dict):
    """
    Represents bookmark timeline item.
    """
    def __init__(__self__, *,
                 azure_resource_id: str,
                 kind: str,
                 created_by: Optional['outputs.UserInfoResponse'] = None,
                 display_name: Optional[str] = None,
                 end_time_utc: Optional[str] = None,
                 event_time: Optional[str] = None,
                 labels: Optional[Sequence[str]] = None,
                 notes: Optional[str] = None,
                 start_time_utc: Optional[str] = None):
        """
        Represents bookmark timeline item.
        :param str azure_resource_id: The bookmark azure resource id.
        :param str kind: The entity query kind
               Expected value is 'Bookmark'.
        :param 'UserInfoResponse' created_by: Describes a user that created the bookmark
        :param str display_name: The bookmark display name.
        :param str end_time_utc: The bookmark end time.
        :param str event_time: The bookmark event time.
        :param Sequence[str] labels: List of labels relevant to this bookmark
        :param str notes: The notes of the bookmark
        :param str start_time_utc: The bookmark start time.
        """
        pulumi.set(__self__, "azure_resource_id", azure_resource_id)
        pulumi.set(__self__, "kind", 'Bookmark')
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if end_time_utc is not None:
            pulumi.set(__self__, "end_time_utc", end_time_utc)
        if event_time is not None:
            pulumi.set(__self__, "event_time", event_time)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if start_time_utc is not None:
            pulumi.set(__self__, "start_time_utc", start_time_utc)

    @property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> str:
        """
        The bookmark azure resource id.
        """
        return pulumi.get(self, "azure_resource_id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The entity query kind
        Expected value is 'Bookmark'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional['outputs.UserInfoResponse']:
        """
        Describes a user that created the bookmark
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The bookmark display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> Optional[str]:
        """
        The bookmark end time.
        """
        return pulumi.get(self, "end_time_utc")

    @property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> Optional[str]:
        """
        The bookmark event time.
        """
        return pulumi.get(self, "event_time")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[str]]:
        """
        List of labels relevant to this bookmark
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        """
        The notes of the bookmark
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> Optional[str]:
        """
        The bookmark start time.
        """
        return pulumi.get(self, "start_time_utc")


@pulumi.output_type
class EntityInsightItemResponse(dict):
    """
    Entity insight Item.
    """
    def __init__(__self__, *,
                 chart_query_results: Optional[Sequence['outputs.InsightsTableResultResponse']] = None,
                 query_id: Optional[str] = None,
                 query_time_interval: Optional['outputs.EntityInsightItemResponseQueryTimeInterval'] = None,
                 table_query_results: Optional['outputs.InsightsTableResultResponse'] = None):
        """
        Entity insight Item.
        :param Sequence['InsightsTableResultResponse'] chart_query_results: Query results for table insights query.
        :param str query_id: The query id of the insight
        :param 'EntityInsightItemResponseQueryTimeInterval' query_time_interval: The Time interval that the query actually executed on.
        :param 'InsightsTableResultResponse' table_query_results: Query results for table insights query.
        """
        if chart_query_results is not None:
            pulumi.set(__self__, "chart_query_results", chart_query_results)
        if query_id is not None:
            pulumi.set(__self__, "query_id", query_id)
        if query_time_interval is not None:
            pulumi.set(__self__, "query_time_interval", query_time_interval)
        if table_query_results is not None:
            pulumi.set(__self__, "table_query_results", table_query_results)

    @property
    @pulumi.getter(name="chartQueryResults")
    def chart_query_results(self) -> Optional[Sequence['outputs.InsightsTableResultResponse']]:
        """
        Query results for table insights query.
        """
        return pulumi.get(self, "chart_query_results")

    @property
    @pulumi.getter(name="queryId")
    def query_id(self) -> Optional[str]:
        """
        The query id of the insight
        """
        return pulumi.get(self, "query_id")

    @property
    @pulumi.getter(name="queryTimeInterval")
    def query_time_interval(self) -> Optional['outputs.EntityInsightItemResponseQueryTimeInterval']:
        """
        The Time interval that the query actually executed on.
        """
        return pulumi.get(self, "query_time_interval")

    @property
    @pulumi.getter(name="tableQueryResults")
    def table_query_results(self) -> Optional['outputs.InsightsTableResultResponse']:
        """
        Query results for table insights query.
        """
        return pulumi.get(self, "table_query_results")


@pulumi.output_type
class EntityInsightItemResponseQueryTimeInterval(dict):
    """
    The Time interval that the query actually executed on.
    """
    def __init__(__self__, *,
                 end_time: Optional[str] = None,
                 start_time: Optional[str] = None):
        """
        The Time interval that the query actually executed on.
        :param str end_time: Insight query end time
        :param str start_time: Insight query start time
        """
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[str]:
        """
        Insight query end time
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        Insight query start time
        """
        return pulumi.get(self, "start_time")


@pulumi.output_type
class GetInsightsErrorKindResponse(dict):
    """
    GetInsights Query Errors.
    """
    def __init__(__self__, *,
                 error_message: str,
                 kind: str,
                 query_id: Optional[str] = None):
        """
        GetInsights Query Errors.
        :param str error_message: the error message
        :param str kind: the query kind
        :param str query_id: the query id
        """
        pulumi.set(__self__, "error_message", error_message)
        pulumi.set(__self__, "kind", kind)
        if query_id is not None:
            pulumi.set(__self__, "query_id", query_id)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        """
        the error message
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        the query kind
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="queryId")
    def query_id(self) -> Optional[str]:
        """
        the query id
        """
        return pulumi.get(self, "query_id")


@pulumi.output_type
class GetInsightsResultsMetadataResponse(dict):
    """
    Get Insights result metadata.
    """
    def __init__(__self__, *,
                 total_count: int,
                 errors: Optional[Sequence['outputs.GetInsightsErrorKindResponse']] = None):
        """
        Get Insights result metadata.
        :param int total_count: the total items found for the insights request
        :param Sequence['GetInsightsErrorKindResponse'] errors: information about the failed queries
        """
        pulumi.set(__self__, "total_count", total_count)
        if errors is not None:
            pulumi.set(__self__, "errors", errors)

    @property
    @pulumi.getter(name="totalCount")
    def total_count(self) -> int:
        """
        the total items found for the insights request
        """
        return pulumi.get(self, "total_count")

    @property
    @pulumi.getter
    def errors(self) -> Optional[Sequence['outputs.GetInsightsErrorKindResponse']]:
        """
        information about the failed queries
        """
        return pulumi.get(self, "errors")


@pulumi.output_type
class InsightsTableResultResponse(dict):
    """
    Query results for table insights query.
    """
    def __init__(__self__, *,
                 columns: Optional[Sequence['outputs.InsightsTableResultResponseColumns']] = None,
                 rows: Optional[Sequence[Sequence[str]]] = None):
        """
        Query results for table insights query.
        :param Sequence['InsightsTableResultResponseColumns'] columns: Columns Metadata of the table
        :param Sequence[Sequence[str]] rows: Rows data of the table
        """
        if columns is not None:
            pulumi.set(__self__, "columns", columns)
        if rows is not None:
            pulumi.set(__self__, "rows", rows)

    @property
    @pulumi.getter
    def columns(self) -> Optional[Sequence['outputs.InsightsTableResultResponseColumns']]:
        """
        Columns Metadata of the table
        """
        return pulumi.get(self, "columns")

    @property
    @pulumi.getter
    def rows(self) -> Optional[Sequence[Sequence[str]]]:
        """
        Rows data of the table
        """
        return pulumi.get(self, "rows")


@pulumi.output_type
class InsightsTableResultResponseColumns(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str name: the name of the colum
        :param str type: the type of the colum
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        the name of the colum
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        the type of the colum
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class RepoResponse(dict):
    """
    Represents a repository.
    """
    def __init__(__self__, *,
                 branches: Optional[Sequence[str]] = None,
                 full_name: Optional[str] = None,
                 url: Optional[str] = None):
        """
        Represents a repository.
        :param Sequence[str] branches: Array of branches.
        :param str full_name: The name of the repository.
        :param str url: The url to access the repository.
        """
        if branches is not None:
            pulumi.set(__self__, "branches", branches)
        if full_name is not None:
            pulumi.set(__self__, "full_name", full_name)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def branches(self) -> Optional[Sequence[str]]:
        """
        Array of branches.
        """
        return pulumi.get(self, "branches")

    @property
    @pulumi.getter(name="fullName")
    def full_name(self) -> Optional[str]:
        """
        The name of the repository.
        """
        return pulumi.get(self, "full_name")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The url to access the repository.
        """
        return pulumi.get(self, "url")


@pulumi.output_type
class SecurityAlertTimelineItemResponse(dict):
    """
    Represents security alert timeline item.
    """
    def __init__(__self__, *,
                 alert_type: str,
                 azure_resource_id: str,
                 display_name: str,
                 end_time_utc: str,
                 kind: str,
                 severity: str,
                 start_time_utc: str,
                 time_generated: str,
                 description: Optional[str] = None,
                 product_name: Optional[str] = None):
        """
        Represents security alert timeline item.
        :param str alert_type: The name of the alert type.
        :param str azure_resource_id: The alert azure resource id.
        :param str display_name: The alert name.
        :param str end_time_utc: The alert end time.
        :param str kind: The entity query kind
               Expected value is 'SecurityAlert'.
        :param str severity: The alert severity.
        :param str start_time_utc: The alert start time.
        :param str time_generated: The alert generated time.
        :param str description: The alert description.
        :param str product_name: The alert product name.
        """
        pulumi.set(__self__, "alert_type", alert_type)
        pulumi.set(__self__, "azure_resource_id", azure_resource_id)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "end_time_utc", end_time_utc)
        pulumi.set(__self__, "kind", 'SecurityAlert')
        pulumi.set(__self__, "severity", severity)
        pulumi.set(__self__, "start_time_utc", start_time_utc)
        pulumi.set(__self__, "time_generated", time_generated)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if product_name is not None:
            pulumi.set(__self__, "product_name", product_name)

    @property
    @pulumi.getter(name="alertType")
    def alert_type(self) -> str:
        """
        The name of the alert type.
        """
        return pulumi.get(self, "alert_type")

    @property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> str:
        """
        The alert azure resource id.
        """
        return pulumi.get(self, "azure_resource_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The alert name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> str:
        """
        The alert end time.
        """
        return pulumi.get(self, "end_time_utc")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The entity query kind
        Expected value is 'SecurityAlert'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def severity(self) -> str:
        """
        The alert severity.
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> str:
        """
        The alert start time.
        """
        return pulumi.get(self, "start_time_utc")

    @property
    @pulumi.getter(name="timeGenerated")
    def time_generated(self) -> str:
        """
        The alert generated time.
        """
        return pulumi.get(self, "time_generated")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The alert description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[str]:
        """
        The alert product name.
        """
        return pulumi.get(self, "product_name")


@pulumi.output_type
class TimelineAggregationResponse(dict):
    """
    timeline aggregation information per kind
    """
    def __init__(__self__, *,
                 count: int,
                 kind: str):
        """
        timeline aggregation information per kind
        :param int count: the total items found for a kind
        :param str kind: the query kind
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        the total items found for a kind
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        the query kind
        """
        return pulumi.get(self, "kind")


@pulumi.output_type
class TimelineErrorResponse(dict):
    """
    Timeline Query Errors.
    """
    def __init__(__self__, *,
                 error_message: str,
                 kind: str,
                 query_id: Optional[str] = None):
        """
        Timeline Query Errors.
        :param str error_message: the error message
        :param str kind: the query kind
        :param str query_id: the query id
        """
        pulumi.set(__self__, "error_message", error_message)
        pulumi.set(__self__, "kind", kind)
        if query_id is not None:
            pulumi.set(__self__, "query_id", query_id)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        """
        the error message
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        the query kind
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="queryId")
    def query_id(self) -> Optional[str]:
        """
        the query id
        """
        return pulumi.get(self, "query_id")


@pulumi.output_type
class TimelineResultsMetadataResponse(dict):
    """
    Expansion result metadata.
    """
    def __init__(__self__, *,
                 aggregations: Sequence['outputs.TimelineAggregationResponse'],
                 total_count: int,
                 errors: Optional[Sequence['outputs.TimelineErrorResponse']] = None):
        """
        Expansion result metadata.
        :param Sequence['TimelineAggregationResponse'] aggregations: timeline aggregation per kind
        :param int total_count: the total items found for the timeline request
        :param Sequence['TimelineErrorResponse'] errors: information about the failure queries
        """
        pulumi.set(__self__, "aggregations", aggregations)
        pulumi.set(__self__, "total_count", total_count)
        if errors is not None:
            pulumi.set(__self__, "errors", errors)

    @property
    @pulumi.getter
    def aggregations(self) -> Sequence['outputs.TimelineAggregationResponse']:
        """
        timeline aggregation per kind
        """
        return pulumi.get(self, "aggregations")

    @property
    @pulumi.getter(name="totalCount")
    def total_count(self) -> int:
        """
        the total items found for the timeline request
        """
        return pulumi.get(self, "total_count")

    @property
    @pulumi.getter
    def errors(self) -> Optional[Sequence['outputs.TimelineErrorResponse']]:
        """
        information about the failure queries
        """
        return pulumi.get(self, "errors")


@pulumi.output_type
class UserInfoResponse(dict):
    """
    User information that made some action
    """
    def __init__(__self__, *,
                 email: str,
                 name: str,
                 object_id: Optional[str] = None):
        """
        User information that made some action
        :param str email: The email of the user.
        :param str name: The name of the user.
        :param str object_id: The object id of the user.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "name", name)
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email of the user.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the user.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[str]:
        """
        The object id of the user.
        """
        return pulumi.get(self, "object_id")


