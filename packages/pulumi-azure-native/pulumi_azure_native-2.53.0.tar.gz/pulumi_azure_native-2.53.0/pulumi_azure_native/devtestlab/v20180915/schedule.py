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
from ._inputs import *

__all__ = ['ScheduleArgs', 'Schedule']

@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *,
                 lab_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 daily_recurrence: Optional[pulumi.Input['DayDetailsArgs']] = None,
                 hourly_recurrence: Optional[pulumi.Input['HourDetailsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input['NotificationSettingsArgs']] = None,
                 status: Optional[pulumi.Input[Union[str, 'EnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 task_type: Optional[pulumi.Input[str]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 weekly_recurrence: Optional[pulumi.Input['WeekDetailsArgs']] = None):
        """
        The set of arguments for constructing a Schedule resource.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['DayDetailsArgs'] daily_recurrence: If the schedule will occur once each day of the week, specify the daily recurrence.
        :param pulumi.Input['HourDetailsArgs'] hourly_recurrence: If the schedule will occur multiple times a day, specify the hourly recurrence.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the schedule.
        :param pulumi.Input['NotificationSettingsArgs'] notification_settings: Notification settings.
        :param pulumi.Input[Union[str, 'EnableStatus']] status: The status of the schedule (i.e. Enabled, Disabled)
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] target_resource_id: The resource ID to which the schedule belongs
        :param pulumi.Input[str] task_type: The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart).
        :param pulumi.Input[str] time_zone_id: The time zone ID (e.g. China Standard Time, Greenland Standard Time, Pacific Standard time, etc.). The possible values for this property can be found in `IReadOnlyCollection<string> TimeZoneConverter.TZConvert.KnownWindowsTimeZoneIds` (https://github.com/mattjohnsonpint/TimeZoneConverter/blob/main/README.md)
        :param pulumi.Input['WeekDetailsArgs'] weekly_recurrence: If the schedule will occur only some days of the week, specify the weekly recurrence.
        """
        pulumi.set(__self__, "lab_name", lab_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if daily_recurrence is not None:
            pulumi.set(__self__, "daily_recurrence", daily_recurrence)
        if hourly_recurrence is not None:
            pulumi.set(__self__, "hourly_recurrence", hourly_recurrence)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_settings is not None:
            pulumi.set(__self__, "notification_settings", notification_settings)
        if status is None:
            status = 'Disabled'
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_resource_id is not None:
            pulumi.set(__self__, "target_resource_id", target_resource_id)
        if task_type is not None:
            pulumi.set(__self__, "task_type", task_type)
        if time_zone_id is not None:
            pulumi.set(__self__, "time_zone_id", time_zone_id)
        if weekly_recurrence is not None:
            pulumi.set(__self__, "weekly_recurrence", weekly_recurrence)

    @property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[str]:
        """
        The name of the lab.
        """
        return pulumi.get(self, "lab_name")

    @lab_name.setter
    def lab_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "lab_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(self) -> Optional[pulumi.Input['DayDetailsArgs']]:
        """
        If the schedule will occur once each day of the week, specify the daily recurrence.
        """
        return pulumi.get(self, "daily_recurrence")

    @daily_recurrence.setter
    def daily_recurrence(self, value: Optional[pulumi.Input['DayDetailsArgs']]):
        pulumi.set(self, "daily_recurrence", value)

    @property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(self) -> Optional[pulumi.Input['HourDetailsArgs']]:
        """
        If the schedule will occur multiple times a day, specify the hourly recurrence.
        """
        return pulumi.get(self, "hourly_recurrence")

    @hourly_recurrence.setter
    def hourly_recurrence(self, value: Optional[pulumi.Input['HourDetailsArgs']]):
        pulumi.set(self, "hourly_recurrence", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the schedule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> Optional[pulumi.Input['NotificationSettingsArgs']]:
        """
        Notification settings.
        """
        return pulumi.get(self, "notification_settings")

    @notification_settings.setter
    def notification_settings(self, value: Optional[pulumi.Input['NotificationSettingsArgs']]):
        pulumi.set(self, "notification_settings", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'EnableStatus']]]:
        """
        The status of the schedule (i.e. Enabled, Disabled)
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'EnableStatus']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID to which the schedule belongs
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter(name="taskType")
    def task_type(self) -> Optional[pulumi.Input[str]]:
        """
        The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart).
        """
        return pulumi.get(self, "task_type")

    @task_type.setter
    def task_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "task_type", value)

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The time zone ID (e.g. China Standard Time, Greenland Standard Time, Pacific Standard time, etc.). The possible values for this property can be found in `IReadOnlyCollection<string> TimeZoneConverter.TZConvert.KnownWindowsTimeZoneIds` (https://github.com/mattjohnsonpint/TimeZoneConverter/blob/main/README.md)
        """
        return pulumi.get(self, "time_zone_id")

    @time_zone_id.setter
    def time_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone_id", value)

    @property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(self) -> Optional[pulumi.Input['WeekDetailsArgs']]:
        """
        If the schedule will occur only some days of the week, specify the weekly recurrence.
        """
        return pulumi.get(self, "weekly_recurrence")

    @weekly_recurrence.setter
    def weekly_recurrence(self, value: Optional[pulumi.Input['WeekDetailsArgs']]):
        pulumi.set(self, "weekly_recurrence", value)


class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 daily_recurrence: Optional[pulumi.Input[Union['DayDetailsArgs', 'DayDetailsArgsDict']]] = None,
                 hourly_recurrence: Optional[pulumi.Input[Union['HourDetailsArgs', 'HourDetailsArgsDict']]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input[Union['NotificationSettingsArgs', 'NotificationSettingsArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'EnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 task_type: Optional[pulumi.Input[str]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 weekly_recurrence: Optional[pulumi.Input[Union['WeekDetailsArgs', 'WeekDetailsArgsDict']]] = None,
                 __props__=None):
        """
        A schedule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['DayDetailsArgs', 'DayDetailsArgsDict']] daily_recurrence: If the schedule will occur once each day of the week, specify the daily recurrence.
        :param pulumi.Input[Union['HourDetailsArgs', 'HourDetailsArgsDict']] hourly_recurrence: If the schedule will occur multiple times a day, specify the hourly recurrence.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the schedule.
        :param pulumi.Input[Union['NotificationSettingsArgs', 'NotificationSettingsArgsDict']] notification_settings: Notification settings.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'EnableStatus']] status: The status of the schedule (i.e. Enabled, Disabled)
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] target_resource_id: The resource ID to which the schedule belongs
        :param pulumi.Input[str] task_type: The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart).
        :param pulumi.Input[str] time_zone_id: The time zone ID (e.g. China Standard Time, Greenland Standard Time, Pacific Standard time, etc.). The possible values for this property can be found in `IReadOnlyCollection<string> TimeZoneConverter.TZConvert.KnownWindowsTimeZoneIds` (https://github.com/mattjohnsonpint/TimeZoneConverter/blob/main/README.md)
        :param pulumi.Input[Union['WeekDetailsArgs', 'WeekDetailsArgsDict']] weekly_recurrence: If the schedule will occur only some days of the week, specify the weekly recurrence.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A schedule.

        :param str resource_name: The name of the resource.
        :param ScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 daily_recurrence: Optional[pulumi.Input[Union['DayDetailsArgs', 'DayDetailsArgsDict']]] = None,
                 hourly_recurrence: Optional[pulumi.Input[Union['HourDetailsArgs', 'HourDetailsArgsDict']]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input[Union['NotificationSettingsArgs', 'NotificationSettingsArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'EnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 task_type: Optional[pulumi.Input[str]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 weekly_recurrence: Optional[pulumi.Input[Union['WeekDetailsArgs', 'WeekDetailsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduleArgs.__new__(ScheduleArgs)

            __props__.__dict__["daily_recurrence"] = daily_recurrence
            __props__.__dict__["hourly_recurrence"] = hourly_recurrence
            if lab_name is None and not opts.urn:
                raise TypeError("Missing required property 'lab_name'")
            __props__.__dict__["lab_name"] = lab_name
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["notification_settings"] = notification_settings
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if status is None:
                status = 'Disabled'
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["target_resource_id"] = target_resource_id
            __props__.__dict__["task_type"] = task_type
            __props__.__dict__["time_zone_id"] = time_zone_id
            __props__.__dict__["weekly_recurrence"] = weekly_recurrence
            __props__.__dict__["created_date"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["unique_identifier"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devtestlab:Schedule"), pulumi.Alias(type_="azure-native:devtestlab/v20150521preview:Schedule"), pulumi.Alias(type_="azure-native:devtestlab/v20160515:Schedule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Schedule, __self__).__init__(
            'azure-native:devtestlab/v20180915:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Schedule':
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduleArgs.__new__(ScheduleArgs)

        __props__.__dict__["created_date"] = None
        __props__.__dict__["daily_recurrence"] = None
        __props__.__dict__["hourly_recurrence"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_settings"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_resource_id"] = None
        __props__.__dict__["task_type"] = None
        __props__.__dict__["time_zone_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["unique_identifier"] = None
        __props__.__dict__["weekly_recurrence"] = None
        return Schedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        The creation date of the schedule.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(self) -> pulumi.Output[Optional['outputs.DayDetailsResponse']]:
        """
        If the schedule will occur once each day of the week, specify the daily recurrence.
        """
        return pulumi.get(self, "daily_recurrence")

    @property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(self) -> pulumi.Output[Optional['outputs.HourDetailsResponse']]:
        """
        If the schedule will occur multiple times a day, specify the hourly recurrence.
        """
        return pulumi.get(self, "hourly_recurrence")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> pulumi.Output[Optional['outputs.NotificationSettingsResponse']]:
        """
        Notification settings.
        """
        return pulumi.get(self, "notification_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the schedule (i.e. Enabled, Disabled)
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID to which the schedule belongs
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Output[Optional[str]]:
        """
        The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart).
        """
        return pulumi.get(self, "task_type")

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        The time zone ID (e.g. China Standard Time, Greenland Standard Time, Pacific Standard time, etc.). The possible values for this property can be found in `IReadOnlyCollection<string> TimeZoneConverter.TZConvert.KnownWindowsTimeZoneIds` (https://github.com/mattjohnsonpint/TimeZoneConverter/blob/main/README.md)
        """
        return pulumi.get(self, "time_zone_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> pulumi.Output[str]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(self) -> pulumi.Output[Optional['outputs.WeekDetailsResponse']]:
        """
        If the schedule will occur only some days of the week, specify the weekly recurrence.
        """
        return pulumi.get(self, "weekly_recurrence")

