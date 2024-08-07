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
    'AddActionGroupsResponse',
    'AlertProcessingRulePropertiesResponse',
    'ConditionResponse',
    'CorrelateAlertsResponse',
    'CorrelateByResponse',
    'DailyRecurrenceResponse',
    'MonthlyRecurrenceResponse',
    'RemoveAllActionGroupsResponse',
    'ScheduleResponse',
    'SystemDataResponse',
    'WeeklyRecurrenceResponse',
]

@pulumi.output_type
class AddActionGroupsResponse(dict):
    """
    Add action groups to alert processing rule.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionGroupIds":
            suggest = "action_group_ids"
        elif key == "actionType":
            suggest = "action_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AddActionGroupsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AddActionGroupsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AddActionGroupsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_group_ids: Sequence[str],
                 action_type: str):
        """
        Add action groups to alert processing rule.
        :param Sequence[str] action_group_ids: List of action group Ids to add to alert processing rule.
        :param str action_type: Action that should be applied.
               Expected value is 'AddActionGroups'.
        """
        pulumi.set(__self__, "action_group_ids", action_group_ids)
        pulumi.set(__self__, "action_type", 'AddActionGroups')

    @property
    @pulumi.getter(name="actionGroupIds")
    def action_group_ids(self) -> Sequence[str]:
        """
        List of action group Ids to add to alert processing rule.
        """
        return pulumi.get(self, "action_group_ids")

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> str:
        """
        Action that should be applied.
        Expected value is 'AddActionGroups'.
        """
        return pulumi.get(self, "action_type")


@pulumi.output_type
class AlertProcessingRulePropertiesResponse(dict):
    """
    Alert processing rule properties defining scopes, conditions and scheduling logic for alert processing rule.
    """
    def __init__(__self__, *,
                 actions: Sequence[Any],
                 scopes: Sequence[str],
                 conditions: Optional[Sequence['outputs.ConditionResponse']] = None,
                 description: Optional[str] = None,
                 enabled: Optional[bool] = None,
                 schedule: Optional['outputs.ScheduleResponse'] = None):
        """
        Alert processing rule properties defining scopes, conditions and scheduling logic for alert processing rule.
        :param Sequence[Union['AddActionGroupsResponse', 'CorrelateAlertsResponse', 'RemoveAllActionGroupsResponse']] actions: Actions to be applied.
        :param Sequence[str] scopes: Scopes on which alert processing rule will apply.
        :param Sequence['ConditionResponse'] conditions: Conditions on which alerts will be filtered.
        :param str description: Description of alert processing rule.
        :param bool enabled: Indicates if the given alert processing rule is enabled or disabled.
        :param 'ScheduleResponse' schedule: Scheduling for alert processing rule.
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "scopes", scopes)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is None:
            enabled = True
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)

    @property
    @pulumi.getter
    def actions(self) -> Sequence[Any]:
        """
        Actions to be applied.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def scopes(self) -> Sequence[str]:
        """
        Scopes on which alert processing rule will apply.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence['outputs.ConditionResponse']]:
        """
        Conditions on which alerts will be filtered.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of alert processing rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Indicates if the given alert processing rule is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.ScheduleResponse']:
        """
        Scheduling for alert processing rule.
        """
        return pulumi.get(self, "schedule")


@pulumi.output_type
class ConditionResponse(dict):
    """
    Condition to trigger an alert processing rule.
    """
    def __init__(__self__, *,
                 field: Optional[str] = None,
                 operator: Optional[str] = None,
                 values: Optional[Sequence[str]] = None):
        """
        Condition to trigger an alert processing rule.
        :param str field: Field for a given condition.
        :param str operator: Operator for a given condition.
        :param Sequence[str] values: List of values to match for a given condition.
        """
        if field is not None:
            pulumi.set(__self__, "field", field)
        if operator is not None:
            pulumi.set(__self__, "operator", operator)
        if values is not None:
            pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def field(self) -> Optional[str]:
        """
        Field for a given condition.
        """
        return pulumi.get(self, "field")

    @property
    @pulumi.getter
    def operator(self) -> Optional[str]:
        """
        Operator for a given condition.
        """
        return pulumi.get(self, "operator")

    @property
    @pulumi.getter
    def values(self) -> Optional[Sequence[str]]:
        """
        List of values to match for a given condition.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class CorrelateAlertsResponse(dict):
    """
    Add logic for alerts correlation.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionType":
            suggest = "action_type"
        elif key == "correlateBy":
            suggest = "correlate_by"
        elif key == "correlationInterval":
            suggest = "correlation_interval"
        elif key == "notificationsForCorrelatedAlerts":
            suggest = "notifications_for_correlated_alerts"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CorrelateAlertsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CorrelateAlertsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CorrelateAlertsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_type: str,
                 correlate_by: Sequence['outputs.CorrelateByResponse'],
                 correlation_interval: str,
                 priority: int,
                 notifications_for_correlated_alerts: Optional[str] = None):
        """
        Add logic for alerts correlation.
        :param str action_type: Action that should be applied.
               Expected value is 'CorrelateAlerts'.
        :param Sequence['CorrelateByResponse'] correlate_by: The list of conditions for the alerts correlations.
        :param str correlation_interval: The required duration (in ISO8601 format) for the alerts correlation.
        :param int priority: The priority of this correlation.
        :param str notifications_for_correlated_alerts: Indicates how to handle child alerts notifications.
        """
        pulumi.set(__self__, "action_type", 'CorrelateAlerts')
        pulumi.set(__self__, "correlate_by", correlate_by)
        pulumi.set(__self__, "correlation_interval", correlation_interval)
        pulumi.set(__self__, "priority", priority)
        if notifications_for_correlated_alerts is None:
            notifications_for_correlated_alerts = 'SuppressAlways'
        if notifications_for_correlated_alerts is not None:
            pulumi.set(__self__, "notifications_for_correlated_alerts", notifications_for_correlated_alerts)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> str:
        """
        Action that should be applied.
        Expected value is 'CorrelateAlerts'.
        """
        return pulumi.get(self, "action_type")

    @property
    @pulumi.getter(name="correlateBy")
    def correlate_by(self) -> Sequence['outputs.CorrelateByResponse']:
        """
        The list of conditions for the alerts correlations.
        """
        return pulumi.get(self, "correlate_by")

    @property
    @pulumi.getter(name="correlationInterval")
    def correlation_interval(self) -> str:
        """
        The required duration (in ISO8601 format) for the alerts correlation.
        """
        return pulumi.get(self, "correlation_interval")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        The priority of this correlation.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="notificationsForCorrelatedAlerts")
    def notifications_for_correlated_alerts(self) -> Optional[str]:
        """
        Indicates how to handle child alerts notifications.
        """
        return pulumi.get(self, "notifications_for_correlated_alerts")


@pulumi.output_type
class CorrelateByResponse(dict):
    """
    The logic for the correlation.
    """
    def __init__(__self__, *,
                 field: Optional[str] = None):
        """
        The logic for the correlation.
        :param str field: The JPath of the property that the alerts should be correlated by.
        """
        if field is not None:
            pulumi.set(__self__, "field", field)

    @property
    @pulumi.getter
    def field(self) -> Optional[str]:
        """
        The JPath of the property that the alerts should be correlated by.
        """
        return pulumi.get(self, "field")


@pulumi.output_type
class DailyRecurrenceResponse(dict):
    """
    Daily recurrence object.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endTime":
            suggest = "end_time"
        elif key == "recurrenceType":
            suggest = "recurrence_type"
        elif key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DailyRecurrenceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DailyRecurrenceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DailyRecurrenceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 end_time: str,
                 recurrence_type: str,
                 start_time: str):
        """
        Daily recurrence object.
        :param str end_time: End time for recurrence.
        :param str recurrence_type: Specifies when the recurrence should be applied.
               Expected value is 'Daily'.
        :param str start_time: Start time for recurrence.
        """
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "recurrence_type", 'Daily')
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        End time for recurrence.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> str:
        """
        Specifies when the recurrence should be applied.
        Expected value is 'Daily'.
        """
        return pulumi.get(self, "recurrence_type")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        Start time for recurrence.
        """
        return pulumi.get(self, "start_time")


@pulumi.output_type
class MonthlyRecurrenceResponse(dict):
    """
    Monthly recurrence object.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "daysOfMonth":
            suggest = "days_of_month"
        elif key == "recurrenceType":
            suggest = "recurrence_type"
        elif key == "endTime":
            suggest = "end_time"
        elif key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MonthlyRecurrenceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MonthlyRecurrenceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MonthlyRecurrenceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days_of_month: Sequence[int],
                 recurrence_type: str,
                 end_time: Optional[str] = None,
                 start_time: Optional[str] = None):
        """
        Monthly recurrence object.
        :param Sequence[int] days_of_month: Specifies the values for monthly recurrence pattern.
        :param str recurrence_type: Specifies when the recurrence should be applied.
               Expected value is 'Monthly'.
        :param str end_time: End time for recurrence.
        :param str start_time: Start time for recurrence.
        """
        pulumi.set(__self__, "days_of_month", days_of_month)
        pulumi.set(__self__, "recurrence_type", 'Monthly')
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="daysOfMonth")
    def days_of_month(self) -> Sequence[int]:
        """
        Specifies the values for monthly recurrence pattern.
        """
        return pulumi.get(self, "days_of_month")

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> str:
        """
        Specifies when the recurrence should be applied.
        Expected value is 'Monthly'.
        """
        return pulumi.get(self, "recurrence_type")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[str]:
        """
        End time for recurrence.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        Start time for recurrence.
        """
        return pulumi.get(self, "start_time")


@pulumi.output_type
class RemoveAllActionGroupsResponse(dict):
    """
    Indicates if all action groups should be removed.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionType":
            suggest = "action_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RemoveAllActionGroupsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RemoveAllActionGroupsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RemoveAllActionGroupsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_type: str):
        """
        Indicates if all action groups should be removed.
        :param str action_type: Action that should be applied.
               Expected value is 'RemoveAllActionGroups'.
        """
        pulumi.set(__self__, "action_type", 'RemoveAllActionGroups')

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> str:
        """
        Action that should be applied.
        Expected value is 'RemoveAllActionGroups'.
        """
        return pulumi.get(self, "action_type")


@pulumi.output_type
class ScheduleResponse(dict):
    """
    Scheduling configuration for a given alert processing rule.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "effectiveFrom":
            suggest = "effective_from"
        elif key == "effectiveUntil":
            suggest = "effective_until"
        elif key == "timeZone":
            suggest = "time_zone"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 effective_from: Optional[str] = None,
                 effective_until: Optional[str] = None,
                 recurrences: Optional[Sequence[Any]] = None,
                 time_zone: Optional[str] = None):
        """
        Scheduling configuration for a given alert processing rule.
        :param str effective_from: Scheduling effective from time. Date-Time in ISO-8601 format without timezone suffix.
        :param str effective_until: Scheduling effective until time. Date-Time in ISO-8601 format without timezone suffix.
        :param Sequence[Union['DailyRecurrenceResponse', 'MonthlyRecurrenceResponse', 'WeeklyRecurrenceResponse']] recurrences: List of recurrences.
        :param str time_zone: Scheduling time zone.
        """
        if effective_from is not None:
            pulumi.set(__self__, "effective_from", effective_from)
        if effective_until is not None:
            pulumi.set(__self__, "effective_until", effective_until)
        if recurrences is not None:
            pulumi.set(__self__, "recurrences", recurrences)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="effectiveFrom")
    def effective_from(self) -> Optional[str]:
        """
        Scheduling effective from time. Date-Time in ISO-8601 format without timezone suffix.
        """
        return pulumi.get(self, "effective_from")

    @property
    @pulumi.getter(name="effectiveUntil")
    def effective_until(self) -> Optional[str]:
        """
        Scheduling effective until time. Date-Time in ISO-8601 format without timezone suffix.
        """
        return pulumi.get(self, "effective_until")

    @property
    @pulumi.getter
    def recurrences(self) -> Optional[Sequence[Any]]:
        """
        List of recurrences.
        """
        return pulumi.get(self, "recurrences")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[str]:
        """
        Scheduling time zone.
        """
        return pulumi.get(self, "time_zone")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class WeeklyRecurrenceResponse(dict):
    """
    Weekly recurrence object.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "daysOfWeek":
            suggest = "days_of_week"
        elif key == "recurrenceType":
            suggest = "recurrence_type"
        elif key == "endTime":
            suggest = "end_time"
        elif key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WeeklyRecurrenceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WeeklyRecurrenceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WeeklyRecurrenceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days_of_week: Sequence[str],
                 recurrence_type: str,
                 end_time: Optional[str] = None,
                 start_time: Optional[str] = None):
        """
        Weekly recurrence object.
        :param Sequence[str] days_of_week: Specifies the values for weekly recurrence pattern.
        :param str recurrence_type: Specifies when the recurrence should be applied.
               Expected value is 'Weekly'.
        :param str end_time: End time for recurrence.
        :param str start_time: Start time for recurrence.
        """
        pulumi.set(__self__, "days_of_week", days_of_week)
        pulumi.set(__self__, "recurrence_type", 'Weekly')
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Sequence[str]:
        """
        Specifies the values for weekly recurrence pattern.
        """
        return pulumi.get(self, "days_of_week")

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> str:
        """
        Specifies when the recurrence should be applied.
        Expected value is 'Weekly'.
        """
        return pulumi.get(self, "recurrence_type")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[str]:
        """
        End time for recurrence.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        Start time for recurrence.
        """
        return pulumi.get(self, "start_time")


