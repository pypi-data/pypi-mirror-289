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
    'GetServiceFabricScheduleResult',
    'AwaitableGetServiceFabricScheduleResult',
    'get_service_fabric_schedule',
    'get_service_fabric_schedule_output',
]

@pulumi.output_type
class GetServiceFabricScheduleResult:
    """
    A schedule.
    """
    def __init__(__self__, created_date=None, daily_recurrence=None, hourly_recurrence=None, id=None, location=None, name=None, notification_settings=None, provisioning_state=None, status=None, tags=None, target_resource_id=None, task_type=None, time_zone_id=None, type=None, unique_identifier=None, weekly_recurrence=None):
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if daily_recurrence and not isinstance(daily_recurrence, dict):
            raise TypeError("Expected argument 'daily_recurrence' to be a dict")
        pulumi.set(__self__, "daily_recurrence", daily_recurrence)
        if hourly_recurrence and not isinstance(hourly_recurrence, dict):
            raise TypeError("Expected argument 'hourly_recurrence' to be a dict")
        pulumi.set(__self__, "hourly_recurrence", hourly_recurrence)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notification_settings and not isinstance(notification_settings, dict):
            raise TypeError("Expected argument 'notification_settings' to be a dict")
        pulumi.set(__self__, "notification_settings", notification_settings)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_resource_id and not isinstance(target_resource_id, str):
            raise TypeError("Expected argument 'target_resource_id' to be a str")
        pulumi.set(__self__, "target_resource_id", target_resource_id)
        if task_type and not isinstance(task_type, str):
            raise TypeError("Expected argument 'task_type' to be a str")
        pulumi.set(__self__, "task_type", task_type)
        if time_zone_id and not isinstance(time_zone_id, str):
            raise TypeError("Expected argument 'time_zone_id' to be a str")
        pulumi.set(__self__, "time_zone_id", time_zone_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_identifier and not isinstance(unique_identifier, str):
            raise TypeError("Expected argument 'unique_identifier' to be a str")
        pulumi.set(__self__, "unique_identifier", unique_identifier)
        if weekly_recurrence and not isinstance(weekly_recurrence, dict):
            raise TypeError("Expected argument 'weekly_recurrence' to be a dict")
        pulumi.set(__self__, "weekly_recurrence", weekly_recurrence)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        """
        The creation date of the schedule.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(self) -> Optional['outputs.DayDetailsResponse']:
        """
        If the schedule will occur once each day of the week, specify the daily recurrence.
        """
        return pulumi.get(self, "daily_recurrence")

    @property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(self) -> Optional['outputs.HourDetailsResponse']:
        """
        If the schedule will occur multiple times a day, specify the hourly recurrence.
        """
        return pulumi.get(self, "hourly_recurrence")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> Optional['outputs.NotificationSettingsResponse']:
        """
        Notification settings.
        """
        return pulumi.get(self, "notification_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the schedule (i.e. Enabled, Disabled)
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[str]:
        """
        The resource ID to which the schedule belongs
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter(name="taskType")
    def task_type(self) -> Optional[str]:
        """
        The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart).
        """
        return pulumi.get(self, "task_type")

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[str]:
        """
        The time zone ID (e.g. China Standard Time, Greenland Standard Time, Pacific Standard time, etc.). The possible values for this property can be found in `IReadOnlyCollection<string> TimeZoneConverter.TZConvert.KnownWindowsTimeZoneIds` (https://github.com/mattjohnsonpint/TimeZoneConverter/blob/main/README.md)
        """
        return pulumi.get(self, "time_zone_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> str:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(self) -> Optional['outputs.WeekDetailsResponse']:
        """
        If the schedule will occur only some days of the week, specify the weekly recurrence.
        """
        return pulumi.get(self, "weekly_recurrence")


class AwaitableGetServiceFabricScheduleResult(GetServiceFabricScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceFabricScheduleResult(
            created_date=self.created_date,
            daily_recurrence=self.daily_recurrence,
            hourly_recurrence=self.hourly_recurrence,
            id=self.id,
            location=self.location,
            name=self.name,
            notification_settings=self.notification_settings,
            provisioning_state=self.provisioning_state,
            status=self.status,
            tags=self.tags,
            target_resource_id=self.target_resource_id,
            task_type=self.task_type,
            time_zone_id=self.time_zone_id,
            type=self.type,
            unique_identifier=self.unique_identifier,
            weekly_recurrence=self.weekly_recurrence)


def get_service_fabric_schedule(expand: Optional[str] = None,
                                lab_name: Optional[str] = None,
                                name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                service_fabric_name: Optional[str] = None,
                                user_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceFabricScheduleResult:
    """
    Get schedule.


    :param str expand: Specify the $expand query. Example: 'properties($select=status)'
    :param str lab_name: The name of the lab.
    :param str name: The name of the schedule.
    :param str resource_group_name: The name of the resource group.
    :param str service_fabric_name: The name of the service fabric.
    :param str user_name: The name of the user profile.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['labName'] = lab_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceFabricName'] = service_fabric_name
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devtestlab/v20180915:getServiceFabricSchedule', __args__, opts=opts, typ=GetServiceFabricScheduleResult).value

    return AwaitableGetServiceFabricScheduleResult(
        created_date=pulumi.get(__ret__, 'created_date'),
        daily_recurrence=pulumi.get(__ret__, 'daily_recurrence'),
        hourly_recurrence=pulumi.get(__ret__, 'hourly_recurrence'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        notification_settings=pulumi.get(__ret__, 'notification_settings'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        target_resource_id=pulumi.get(__ret__, 'target_resource_id'),
        task_type=pulumi.get(__ret__, 'task_type'),
        time_zone_id=pulumi.get(__ret__, 'time_zone_id'),
        type=pulumi.get(__ret__, 'type'),
        unique_identifier=pulumi.get(__ret__, 'unique_identifier'),
        weekly_recurrence=pulumi.get(__ret__, 'weekly_recurrence'))


@_utilities.lift_output_func(get_service_fabric_schedule)
def get_service_fabric_schedule_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                       lab_name: Optional[pulumi.Input[str]] = None,
                                       name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       service_fabric_name: Optional[pulumi.Input[str]] = None,
                                       user_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceFabricScheduleResult]:
    """
    Get schedule.


    :param str expand: Specify the $expand query. Example: 'properties($select=status)'
    :param str lab_name: The name of the lab.
    :param str name: The name of the schedule.
    :param str resource_group_name: The name of the resource group.
    :param str service_fabric_name: The name of the service fabric.
    :param str user_name: The name of the user profile.
    """
    ...
