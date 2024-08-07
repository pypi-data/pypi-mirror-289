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
from ._enums import *
from ._inputs import *

__all__ = ['JobDefinitionArgs', 'JobDefinition']

@pulumi.input_type
class JobDefinitionArgs:
    def __init__(__self__, *,
                 data_manager_name: pulumi.Input[str],
                 data_service_name: pulumi.Input[str],
                 data_sink_id: pulumi.Input[str],
                 data_source_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 state: pulumi.Input['State'],
                 customer_secrets: Optional[pulumi.Input[Sequence[pulumi.Input['CustomerSecretArgs']]]] = None,
                 data_service_input: Optional[Any] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 last_modified_time: Optional[pulumi.Input[str]] = None,
                 run_location: Optional[pulumi.Input['RunLocation']] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input['ScheduleArgs']]]] = None,
                 user_confirmation: Optional[pulumi.Input['UserConfirmation']] = None):
        """
        The set of arguments for constructing a JobDefinition resource.
        :param pulumi.Input[str] data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        :param pulumi.Input[str] data_service_name: The data service type of the job definition.
        :param pulumi.Input[str] data_sink_id: Data Sink Id associated to the job definition.
        :param pulumi.Input[str] data_source_id: Data Source Id associated to the job definition.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name
        :param pulumi.Input['State'] state: State of the job definition.
        :param pulumi.Input[Sequence[pulumi.Input['CustomerSecretArgs']]] customer_secrets: List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        :param Any data_service_input: A generic json used differently by each data service type.
        :param pulumi.Input[str] job_definition_name: The job definition name to be created or updated.
        :param pulumi.Input[str] last_modified_time: Last modified time of the job definition.
        :param pulumi.Input['RunLocation'] run_location: This is the preferred geo location for the job to run.
        :param pulumi.Input[Sequence[pulumi.Input['ScheduleArgs']]] schedules: Schedule for running the job definition
        :param pulumi.Input['UserConfirmation'] user_confirmation: Enum to detect if user confirmation is required. If not passed will default to NotRequired.
        """
        pulumi.set(__self__, "data_manager_name", data_manager_name)
        pulumi.set(__self__, "data_service_name", data_service_name)
        pulumi.set(__self__, "data_sink_id", data_sink_id)
        pulumi.set(__self__, "data_source_id", data_source_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "state", state)
        if customer_secrets is not None:
            pulumi.set(__self__, "customer_secrets", customer_secrets)
        if data_service_input is not None:
            pulumi.set(__self__, "data_service_input", data_service_input)
        if job_definition_name is not None:
            pulumi.set(__self__, "job_definition_name", job_definition_name)
        if last_modified_time is not None:
            pulumi.set(__self__, "last_modified_time", last_modified_time)
        if run_location is not None:
            pulumi.set(__self__, "run_location", run_location)
        if schedules is not None:
            pulumi.set(__self__, "schedules", schedules)
        if user_confirmation is None:
            user_confirmation = 'NotRequired'
        if user_confirmation is not None:
            pulumi.set(__self__, "user_confirmation", user_confirmation)

    @property
    @pulumi.getter(name="dataManagerName")
    def data_manager_name(self) -> pulumi.Input[str]:
        """
        The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        """
        return pulumi.get(self, "data_manager_name")

    @data_manager_name.setter
    def data_manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_manager_name", value)

    @property
    @pulumi.getter(name="dataServiceName")
    def data_service_name(self) -> pulumi.Input[str]:
        """
        The data service type of the job definition.
        """
        return pulumi.get(self, "data_service_name")

    @data_service_name.setter
    def data_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_service_name", value)

    @property
    @pulumi.getter(name="dataSinkId")
    def data_sink_id(self) -> pulumi.Input[str]:
        """
        Data Sink Id associated to the job definition.
        """
        return pulumi.get(self, "data_sink_id")

    @data_sink_id.setter
    def data_sink_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_sink_id", value)

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Input[str]:
        """
        Data Source Id associated to the job definition.
        """
        return pulumi.get(self, "data_source_id")

    @data_source_id.setter
    def data_source_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_source_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Resource Group Name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def state(self) -> pulumi.Input['State']:
        """
        State of the job definition.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: pulumi.Input['State']):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="customerSecrets")
    def customer_secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomerSecretArgs']]]]:
        """
        List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        """
        return pulumi.get(self, "customer_secrets")

    @customer_secrets.setter
    def customer_secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomerSecretArgs']]]]):
        pulumi.set(self, "customer_secrets", value)

    @property
    @pulumi.getter(name="dataServiceInput")
    def data_service_input(self) -> Optional[Any]:
        """
        A generic json used differently by each data service type.
        """
        return pulumi.get(self, "data_service_input")

    @data_service_input.setter
    def data_service_input(self, value: Optional[Any]):
        pulumi.set(self, "data_service_input", value)

    @property
    @pulumi.getter(name="jobDefinitionName")
    def job_definition_name(self) -> Optional[pulumi.Input[str]]:
        """
        The job definition name to be created or updated.
        """
        return pulumi.get(self, "job_definition_name")

    @job_definition_name.setter
    def job_definition_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_definition_name", value)

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[str]]:
        """
        Last modified time of the job definition.
        """
        return pulumi.get(self, "last_modified_time")

    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_time", value)

    @property
    @pulumi.getter(name="runLocation")
    def run_location(self) -> Optional[pulumi.Input['RunLocation']]:
        """
        This is the preferred geo location for the job to run.
        """
        return pulumi.get(self, "run_location")

    @run_location.setter
    def run_location(self, value: Optional[pulumi.Input['RunLocation']]):
        pulumi.set(self, "run_location", value)

    @property
    @pulumi.getter
    def schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScheduleArgs']]]]:
        """
        Schedule for running the job definition
        """
        return pulumi.get(self, "schedules")

    @schedules.setter
    def schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScheduleArgs']]]]):
        pulumi.set(self, "schedules", value)

    @property
    @pulumi.getter(name="userConfirmation")
    def user_confirmation(self) -> Optional[pulumi.Input['UserConfirmation']]:
        """
        Enum to detect if user confirmation is required. If not passed will default to NotRequired.
        """
        return pulumi.get(self, "user_confirmation")

    @user_confirmation.setter
    def user_confirmation(self, value: Optional[pulumi.Input['UserConfirmation']]):
        pulumi.set(self, "user_confirmation", value)


class JobDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CustomerSecretArgs', 'CustomerSecretArgsDict']]]]] = None,
                 data_manager_name: Optional[pulumi.Input[str]] = None,
                 data_service_input: Optional[Any] = None,
                 data_service_name: Optional[pulumi.Input[str]] = None,
                 data_sink_id: Optional[pulumi.Input[str]] = None,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 last_modified_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_location: Optional[pulumi.Input['RunLocation']] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScheduleArgs', 'ScheduleArgsDict']]]]] = None,
                 state: Optional[pulumi.Input['State']] = None,
                 user_confirmation: Optional[pulumi.Input['UserConfirmation']] = None,
                 __props__=None):
        """
        Job Definition.
        Azure REST API version: 2019-06-01. Prior API version in Azure Native 1.x: 2019-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CustomerSecretArgs', 'CustomerSecretArgsDict']]]] customer_secrets: List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        :param pulumi.Input[str] data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        :param Any data_service_input: A generic json used differently by each data service type.
        :param pulumi.Input[str] data_service_name: The data service type of the job definition.
        :param pulumi.Input[str] data_sink_id: Data Sink Id associated to the job definition.
        :param pulumi.Input[str] data_source_id: Data Source Id associated to the job definition.
        :param pulumi.Input[str] job_definition_name: The job definition name to be created or updated.
        :param pulumi.Input[str] last_modified_time: Last modified time of the job definition.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name
        :param pulumi.Input['RunLocation'] run_location: This is the preferred geo location for the job to run.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ScheduleArgs', 'ScheduleArgsDict']]]] schedules: Schedule for running the job definition
        :param pulumi.Input['State'] state: State of the job definition.
        :param pulumi.Input['UserConfirmation'] user_confirmation: Enum to detect if user confirmation is required. If not passed will default to NotRequired.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Job Definition.
        Azure REST API version: 2019-06-01. Prior API version in Azure Native 1.x: 2019-06-01.

        :param str resource_name: The name of the resource.
        :param JobDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CustomerSecretArgs', 'CustomerSecretArgsDict']]]]] = None,
                 data_manager_name: Optional[pulumi.Input[str]] = None,
                 data_service_input: Optional[Any] = None,
                 data_service_name: Optional[pulumi.Input[str]] = None,
                 data_sink_id: Optional[pulumi.Input[str]] = None,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 last_modified_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_location: Optional[pulumi.Input['RunLocation']] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScheduleArgs', 'ScheduleArgsDict']]]]] = None,
                 state: Optional[pulumi.Input['State']] = None,
                 user_confirmation: Optional[pulumi.Input['UserConfirmation']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobDefinitionArgs.__new__(JobDefinitionArgs)

            __props__.__dict__["customer_secrets"] = customer_secrets
            if data_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_manager_name'")
            __props__.__dict__["data_manager_name"] = data_manager_name
            __props__.__dict__["data_service_input"] = data_service_input
            if data_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_service_name'")
            __props__.__dict__["data_service_name"] = data_service_name
            if data_sink_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_sink_id'")
            __props__.__dict__["data_sink_id"] = data_sink_id
            if data_source_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_source_id'")
            __props__.__dict__["data_source_id"] = data_source_id
            __props__.__dict__["job_definition_name"] = job_definition_name
            __props__.__dict__["last_modified_time"] = last_modified_time
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["run_location"] = run_location
            __props__.__dict__["schedules"] = schedules
            if state is None and not opts.urn:
                raise TypeError("Missing required property 'state'")
            __props__.__dict__["state"] = state
            if user_confirmation is None:
                user_confirmation = 'NotRequired'
            __props__.__dict__["user_confirmation"] = user_confirmation
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybriddata/v20160601:JobDefinition"), pulumi.Alias(type_="azure-native:hybriddata/v20190601:JobDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(JobDefinition, __self__).__init__(
            'azure-native:hybriddata:JobDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JobDefinition':
        """
        Get an existing JobDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobDefinitionArgs.__new__(JobDefinitionArgs)

        __props__.__dict__["customer_secrets"] = None
        __props__.__dict__["data_service_input"] = None
        __props__.__dict__["data_sink_id"] = None
        __props__.__dict__["data_source_id"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["run_location"] = None
        __props__.__dict__["schedules"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_confirmation"] = None
        return JobDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customerSecrets")
    def customer_secrets(self) -> pulumi.Output[Optional[Sequence['outputs.CustomerSecretResponse']]]:
        """
        List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        """
        return pulumi.get(self, "customer_secrets")

    @property
    @pulumi.getter(name="dataServiceInput")
    def data_service_input(self) -> pulumi.Output[Optional[Any]]:
        """
        A generic json used differently by each data service type.
        """
        return pulumi.get(self, "data_service_input")

    @property
    @pulumi.getter(name="dataSinkId")
    def data_sink_id(self) -> pulumi.Output[str]:
        """
        Data Sink Id associated to the job definition.
        """
        return pulumi.get(self, "data_sink_id")

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Output[str]:
        """
        Data Source Id associated to the job definition.
        """
        return pulumi.get(self, "data_source_id")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        Last modified time of the job definition.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="runLocation")
    def run_location(self) -> pulumi.Output[Optional[str]]:
        """
        This is the preferred geo location for the job to run.
        """
        return pulumi.get(self, "run_location")

    @property
    @pulumi.getter
    def schedules(self) -> pulumi.Output[Optional[Sequence['outputs.ScheduleResponse']]]:
        """
        Schedule for running the job definition
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the job definition.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userConfirmation")
    def user_confirmation(self) -> pulumi.Output[Optional[str]]:
        """
        Enum to detect if user confirmation is required. If not passed will default to NotRequired.
        """
        return pulumi.get(self, "user_confirmation")

