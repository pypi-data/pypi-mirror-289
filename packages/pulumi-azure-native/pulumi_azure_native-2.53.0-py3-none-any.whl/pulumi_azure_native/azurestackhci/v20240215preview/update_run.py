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

__all__ = ['UpdateRunArgs', 'UpdateRun']

@pulumi.input_type
class UpdateRunArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 update_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 duration: Optional[pulumi.Input[str]] = None,
                 end_time_utc: Optional[pulumi.Input[str]] = None,
                 error_message: Optional[pulumi.Input[str]] = None,
                 last_updated_time: Optional[pulumi.Input[str]] = None,
                 last_updated_time_utc: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 start_time_utc: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'UpdateRunPropertiesState']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 steps: Optional[pulumi.Input[Sequence[pulumi.Input['StepArgs']]]] = None,
                 time_started: Optional[pulumi.Input[str]] = None,
                 update_run_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UpdateRun resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] update_name: The name of the Update
        :param pulumi.Input[str] description: More detailed description of the step.
        :param pulumi.Input[str] duration: Duration of the update run.
        :param pulumi.Input[str] end_time_utc: When the step reached a terminal state.
        :param pulumi.Input[str] error_message: Error message, specified if the step is in a failed state.
        :param pulumi.Input[str] last_updated_time: Timestamp of the most recently completed step in the update run.
        :param pulumi.Input[str] last_updated_time_utc: Completion time of this step or the last completed sub-step.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] name: Name of the step.
        :param pulumi.Input[str] start_time_utc: When the step started, or empty if it has not started executing.
        :param pulumi.Input[Union[str, 'UpdateRunPropertiesState']] state: State of the update run.
        :param pulumi.Input[str] status: Status of the step, bubbled up from the ECE action plan for installation attempts. Values are: 'Success', 'Error', 'InProgress', and 'Unknown status'.
        :param pulumi.Input[Sequence[pulumi.Input['StepArgs']]] steps: Recursive model for child steps of this step.
        :param pulumi.Input[str] time_started: Timestamp of the update run was started.
        :param pulumi.Input[str] update_run_name: The name of the Update Run
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "update_name", update_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if duration is not None:
            pulumi.set(__self__, "duration", duration)
        if end_time_utc is not None:
            pulumi.set(__self__, "end_time_utc", end_time_utc)
        if error_message is not None:
            pulumi.set(__self__, "error_message", error_message)
        if last_updated_time is not None:
            pulumi.set(__self__, "last_updated_time", last_updated_time)
        if last_updated_time_utc is not None:
            pulumi.set(__self__, "last_updated_time_utc", last_updated_time_utc)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if start_time_utc is not None:
            pulumi.set(__self__, "start_time_utc", start_time_utc)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if steps is not None:
            pulumi.set(__self__, "steps", steps)
        if time_started is not None:
            pulumi.set(__self__, "time_started", time_started)
        if update_run_name is not None:
            pulumi.set(__self__, "update_run_name", update_run_name)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="updateName")
    def update_name(self) -> pulumi.Input[str]:
        """
        The name of the Update
        """
        return pulumi.get(self, "update_name")

    @update_name.setter
    def update_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "update_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        More detailed description of the step.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[str]]:
        """
        Duration of the update run.
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        When the step reached a terminal state.
        """
        return pulumi.get(self, "end_time_utc")

    @end_time_utc.setter
    def end_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time_utc", value)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[str]]:
        """
        Error message, specified if the step is in a failed state.
        """
        return pulumi.get(self, "error_message")

    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "error_message", value)

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp of the most recently completed step in the update run.
        """
        return pulumi.get(self, "last_updated_time")

    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated_time", value)

    @property
    @pulumi.getter(name="lastUpdatedTimeUtc")
    def last_updated_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Completion time of this step or the last completed sub-step.
        """
        return pulumi.get(self, "last_updated_time_utc")

    @last_updated_time_utc.setter
    def last_updated_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated_time_utc", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the step.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        When the step started, or empty if it has not started executing.
        """
        return pulumi.get(self, "start_time_utc")

    @start_time_utc.setter
    def start_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time_utc", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'UpdateRunPropertiesState']]]:
        """
        State of the update run.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'UpdateRunPropertiesState']]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the step, bubbled up from the ECE action plan for installation attempts. Values are: 'Success', 'Error', 'InProgress', and 'Unknown status'.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StepArgs']]]]:
        """
        Recursive model for child steps of this step.
        """
        return pulumi.get(self, "steps")

    @steps.setter
    def steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StepArgs']]]]):
        pulumi.set(self, "steps", value)

    @property
    @pulumi.getter(name="timeStarted")
    def time_started(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp of the update run was started.
        """
        return pulumi.get(self, "time_started")

    @time_started.setter
    def time_started(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_started", value)

    @property
    @pulumi.getter(name="updateRunName")
    def update_run_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Update Run
        """
        return pulumi.get(self, "update_run_name")

    @update_run_name.setter
    def update_run_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_run_name", value)


class UpdateRun(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 duration: Optional[pulumi.Input[str]] = None,
                 end_time_utc: Optional[pulumi.Input[str]] = None,
                 error_message: Optional[pulumi.Input[str]] = None,
                 last_updated_time: Optional[pulumi.Input[str]] = None,
                 last_updated_time_utc: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 start_time_utc: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'UpdateRunPropertiesState']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 steps: Optional[pulumi.Input[Sequence[pulumi.Input[Union['StepArgs', 'StepArgsDict']]]]] = None,
                 time_started: Optional[pulumi.Input[str]] = None,
                 update_name: Optional[pulumi.Input[str]] = None,
                 update_run_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Details of an Update run

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[str] description: More detailed description of the step.
        :param pulumi.Input[str] duration: Duration of the update run.
        :param pulumi.Input[str] end_time_utc: When the step reached a terminal state.
        :param pulumi.Input[str] error_message: Error message, specified if the step is in a failed state.
        :param pulumi.Input[str] last_updated_time: Timestamp of the most recently completed step in the update run.
        :param pulumi.Input[str] last_updated_time_utc: Completion time of this step or the last completed sub-step.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] name: Name of the step.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] start_time_utc: When the step started, or empty if it has not started executing.
        :param pulumi.Input[Union[str, 'UpdateRunPropertiesState']] state: State of the update run.
        :param pulumi.Input[str] status: Status of the step, bubbled up from the ECE action plan for installation attempts. Values are: 'Success', 'Error', 'InProgress', and 'Unknown status'.
        :param pulumi.Input[Sequence[pulumi.Input[Union['StepArgs', 'StepArgsDict']]]] steps: Recursive model for child steps of this step.
        :param pulumi.Input[str] time_started: Timestamp of the update run was started.
        :param pulumi.Input[str] update_name: The name of the Update
        :param pulumi.Input[str] update_run_name: The name of the Update Run
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UpdateRunArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Details of an Update run

        :param str resource_name: The name of the resource.
        :param UpdateRunArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UpdateRunArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 duration: Optional[pulumi.Input[str]] = None,
                 end_time_utc: Optional[pulumi.Input[str]] = None,
                 error_message: Optional[pulumi.Input[str]] = None,
                 last_updated_time: Optional[pulumi.Input[str]] = None,
                 last_updated_time_utc: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 start_time_utc: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'UpdateRunPropertiesState']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 steps: Optional[pulumi.Input[Sequence[pulumi.Input[Union['StepArgs', 'StepArgsDict']]]]] = None,
                 time_started: Optional[pulumi.Input[str]] = None,
                 update_name: Optional[pulumi.Input[str]] = None,
                 update_run_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UpdateRunArgs.__new__(UpdateRunArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["description"] = description
            __props__.__dict__["duration"] = duration
            __props__.__dict__["end_time_utc"] = end_time_utc
            __props__.__dict__["error_message"] = error_message
            __props__.__dict__["last_updated_time"] = last_updated_time
            __props__.__dict__["last_updated_time_utc"] = last_updated_time_utc
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["start_time_utc"] = start_time_utc
            __props__.__dict__["state"] = state
            __props__.__dict__["status"] = status
            __props__.__dict__["steps"] = steps
            __props__.__dict__["time_started"] = time_started
            if update_name is None and not opts.urn:
                raise TypeError("Missing required property 'update_name'")
            __props__.__dict__["update_name"] = update_name
            __props__.__dict__["update_run_name"] = update_run_name
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20221201:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20230201:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20230301:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20230601:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20230801:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20230801preview:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20231101preview:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20240101:UpdateRun"), pulumi.Alias(type_="azure-native:azurestackhci/v20240401:UpdateRun")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(UpdateRun, __self__).__init__(
            'azure-native:azurestackhci/v20240215preview:UpdateRun',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UpdateRun':
        """
        Get an existing UpdateRun resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UpdateRunArgs.__new__(UpdateRunArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["duration"] = None
        __props__.__dict__["end_time_utc"] = None
        __props__.__dict__["error_message"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["last_updated_time_utc"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["start_time_utc"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["steps"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["time_started"] = None
        __props__.__dict__["type"] = None
        return UpdateRun(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        More detailed description of the step.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Output[Optional[str]]:
        """
        Duration of the update run.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> pulumi.Output[Optional[str]]:
        """
        When the step reached a terminal state.
        """
        return pulumi.get(self, "end_time_utc")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[Optional[str]]:
        """
        Error message, specified if the step is in a failed state.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[Optional[str]]:
        """
        Timestamp of the most recently completed step in the update run.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="lastUpdatedTimeUtc")
    def last_updated_time_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Completion time of this step or the last completed sub-step.
        """
        return pulumi.get(self, "last_updated_time_utc")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the UpdateRuns proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> pulumi.Output[Optional[str]]:
        """
        When the step started, or empty if it has not started executing.
        """
        return pulumi.get(self, "start_time_utc")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        State of the update run.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Status of the step, bubbled up from the ECE action plan for installation attempts. Values are: 'Success', 'Error', 'InProgress', and 'Unknown status'.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def steps(self) -> pulumi.Output[Optional[Sequence['outputs.StepResponse']]]:
        """
        Recursive model for child steps of this step.
        """
        return pulumi.get(self, "steps")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="timeStarted")
    def time_started(self) -> pulumi.Output[Optional[str]]:
        """
        Timestamp of the update run was started.
        """
        return pulumi.get(self, "time_started")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

