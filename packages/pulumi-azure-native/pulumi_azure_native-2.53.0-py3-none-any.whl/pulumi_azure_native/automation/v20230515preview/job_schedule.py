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
from ._inputs import *

__all__ = ['JobScheduleArgs', 'JobSchedule']

@pulumi.input_type
class JobScheduleArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 runbook: pulumi.Input['RunbookAssociationPropertyArgs'],
                 schedule: pulumi.Input['ScheduleAssociationPropertyArgs'],
                 job_schedule_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 run_on: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a JobSchedule resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input['RunbookAssociationPropertyArgs'] runbook: Gets or sets the runbook.
        :param pulumi.Input['ScheduleAssociationPropertyArgs'] schedule: Gets or sets the schedule.
        :param pulumi.Input[str] job_schedule_id: The job schedule name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Gets or sets a list of job properties.
        :param pulumi.Input[str] run_on: Gets or sets the hybrid worker group that the scheduled job should run on.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "runbook", runbook)
        pulumi.set(__self__, "schedule", schedule)
        if job_schedule_id is not None:
            pulumi.set(__self__, "job_schedule_id", job_schedule_id)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if run_on is not None:
            pulumi.set(__self__, "run_on", run_on)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def runbook(self) -> pulumi.Input['RunbookAssociationPropertyArgs']:
        """
        Gets or sets the runbook.
        """
        return pulumi.get(self, "runbook")

    @runbook.setter
    def runbook(self, value: pulumi.Input['RunbookAssociationPropertyArgs']):
        pulumi.set(self, "runbook", value)

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Input['ScheduleAssociationPropertyArgs']:
        """
        Gets or sets the schedule.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: pulumi.Input['ScheduleAssociationPropertyArgs']):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="jobScheduleId")
    def job_schedule_id(self) -> Optional[pulumi.Input[str]]:
        """
        The job schedule name.
        """
        return pulumi.get(self, "job_schedule_id")

    @job_schedule_id.setter
    def job_schedule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_schedule_id", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets a list of job properties.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="runOn")
    def run_on(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the hybrid worker group that the scheduled job should run on.
        """
        return pulumi.get(self, "run_on")

    @run_on.setter
    def run_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_on", value)


class JobSchedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 job_schedule_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_on: Optional[pulumi.Input[str]] = None,
                 runbook: Optional[pulumi.Input[Union['RunbookAssociationPropertyArgs', 'RunbookAssociationPropertyArgsDict']]] = None,
                 schedule: Optional[pulumi.Input[Union['ScheduleAssociationPropertyArgs', 'ScheduleAssociationPropertyArgsDict']]] = None,
                 __props__=None):
        """
        Definition of the job schedule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] job_schedule_id: The job schedule name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Gets or sets a list of job properties.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[str] run_on: Gets or sets the hybrid worker group that the scheduled job should run on.
        :param pulumi.Input[Union['RunbookAssociationPropertyArgs', 'RunbookAssociationPropertyArgsDict']] runbook: Gets or sets the runbook.
        :param pulumi.Input[Union['ScheduleAssociationPropertyArgs', 'ScheduleAssociationPropertyArgsDict']] schedule: Gets or sets the schedule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the job schedule.

        :param str resource_name: The name of the resource.
        :param JobScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 job_schedule_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_on: Optional[pulumi.Input[str]] = None,
                 runbook: Optional[pulumi.Input[Union['RunbookAssociationPropertyArgs', 'RunbookAssociationPropertyArgsDict']]] = None,
                 schedule: Optional[pulumi.Input[Union['ScheduleAssociationPropertyArgs', 'ScheduleAssociationPropertyArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobScheduleArgs.__new__(JobScheduleArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            __props__.__dict__["job_schedule_id"] = job_schedule_id
            __props__.__dict__["parameters"] = parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["run_on"] = run_on
            if runbook is None and not opts.urn:
                raise TypeError("Missing required property 'runbook'")
            __props__.__dict__["runbook"] = runbook
            if schedule is None and not opts.urn:
                raise TypeError("Missing required property 'schedule'")
            __props__.__dict__["schedule"] = schedule
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:automation:JobSchedule"), pulumi.Alias(type_="azure-native:automation/v20151031:JobSchedule"), pulumi.Alias(type_="azure-native:automation/v20190601:JobSchedule"), pulumi.Alias(type_="azure-native:automation/v20200113preview:JobSchedule"), pulumi.Alias(type_="azure-native:automation/v20220808:JobSchedule"), pulumi.Alias(type_="azure-native:automation/v20231101:JobSchedule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(JobSchedule, __self__).__init__(
            'azure-native:automation/v20230515preview:JobSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JobSchedule':
        """
        Get an existing JobSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobScheduleArgs.__new__(JobScheduleArgs)

        __props__.__dict__["job_schedule_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["run_on"] = None
        __props__.__dict__["runbook"] = None
        __props__.__dict__["schedule"] = None
        __props__.__dict__["type"] = None
        return JobSchedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="jobScheduleId")
    def job_schedule_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the id of job schedule.
        """
        return pulumi.get(self, "job_schedule_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the name of the variable.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Gets or sets the parameters of the job schedule.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="runOn")
    def run_on(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the hybrid worker group that the scheduled job should run on.
        """
        return pulumi.get(self, "run_on")

    @property
    @pulumi.getter
    def runbook(self) -> pulumi.Output[Optional['outputs.RunbookAssociationPropertyResponse']]:
        """
        Gets or sets the runbook.
        """
        return pulumi.get(self, "runbook")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional['outputs.ScheduleAssociationPropertyResponse']]:
        """
        Gets or sets the schedule.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

