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

__all__ = ['JobArgs', 'Job']

@pulumi.input_type
class JobArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 input: pulumi.Input[Union['JobInputAssetArgs', 'JobInputClipArgs', 'JobInputHttpArgs', 'JobInputSequenceArgs', 'JobInputsArgs']],
                 outputs: pulumi.Input[Sequence[pulumi.Input['JobOutputAssetArgs']]],
                 resource_group_name: pulumi.Input[str],
                 transform_name: pulumi.Input[str],
                 correlation_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[Union[str, 'Priority']]] = None):
        """
        The set of arguments for constructing a Job resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[Union['JobInputAssetArgs', 'JobInputClipArgs', 'JobInputHttpArgs', 'JobInputSequenceArgs', 'JobInputsArgs']] input: The inputs for the Job.
        :param pulumi.Input[Sequence[pulumi.Input['JobOutputAssetArgs']]] outputs: The outputs for the Job.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[str] transform_name: The Transform name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] correlation_data: Customer provided key, value pairs that will be returned in Job and JobOutput state events.
        :param pulumi.Input[str] description: Optional customer supplied description of the Job.
        :param pulumi.Input[str] job_name: The Job name.
        :param pulumi.Input[Union[str, 'Priority']] priority: Priority with which the job should be processed. Higher priority jobs are processed before lower priority jobs. If not set, the default is normal.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "input", input)
        pulumi.set(__self__, "outputs", outputs)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "transform_name", transform_name)
        if correlation_data is not None:
            pulumi.set(__self__, "correlation_data", correlation_data)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if job_name is not None:
            pulumi.set(__self__, "job_name", job_name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The Media Services account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def input(self) -> pulumi.Input[Union['JobInputAssetArgs', 'JobInputClipArgs', 'JobInputHttpArgs', 'JobInputSequenceArgs', 'JobInputsArgs']]:
        """
        The inputs for the Job.
        """
        return pulumi.get(self, "input")

    @input.setter
    def input(self, value: pulumi.Input[Union['JobInputAssetArgs', 'JobInputClipArgs', 'JobInputHttpArgs', 'JobInputSequenceArgs', 'JobInputsArgs']]):
        pulumi.set(self, "input", value)

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Input[Sequence[pulumi.Input['JobOutputAssetArgs']]]:
        """
        The outputs for the Job.
        """
        return pulumi.get(self, "outputs")

    @outputs.setter
    def outputs(self, value: pulumi.Input[Sequence[pulumi.Input['JobOutputAssetArgs']]]):
        pulumi.set(self, "outputs", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="transformName")
    def transform_name(self) -> pulumi.Input[str]:
        """
        The Transform name.
        """
        return pulumi.get(self, "transform_name")

    @transform_name.setter
    def transform_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "transform_name", value)

    @property
    @pulumi.getter(name="correlationData")
    def correlation_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Customer provided key, value pairs that will be returned in Job and JobOutput state events.
        """
        return pulumi.get(self, "correlation_data")

    @correlation_data.setter
    def correlation_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "correlation_data", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional customer supplied description of the Job.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Job name.
        """
        return pulumi.get(self, "job_name")

    @job_name.setter
    def job_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[Union[str, 'Priority']]]:
        """
        Priority with which the job should be processed. Higher priority jobs are processed before lower priority jobs. If not set, the default is normal.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[Union[str, 'Priority']]]):
        pulumi.set(self, "priority", value)


class Job(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 correlation_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 input: Optional[pulumi.Input[Union[Union['JobInputAssetArgs', 'JobInputAssetArgsDict'], Union['JobInputClipArgs', 'JobInputClipArgsDict'], Union['JobInputHttpArgs', 'JobInputHttpArgsDict'], Union['JobInputSequenceArgs', 'JobInputSequenceArgsDict'], Union['JobInputsArgs', 'JobInputsArgsDict']]]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 outputs: Optional[pulumi.Input[Sequence[pulumi.Input[Union['JobOutputAssetArgs', 'JobOutputAssetArgsDict']]]]] = None,
                 priority: Optional[pulumi.Input[Union[str, 'Priority']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 transform_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Job resource type. The progress and state can be obtained by polling a Job or subscribing to events using EventGrid.
        Azure REST API version: 2022-07-01. Prior API version in Azure Native 1.x: 2020-05-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] correlation_data: Customer provided key, value pairs that will be returned in Job and JobOutput state events.
        :param pulumi.Input[str] description: Optional customer supplied description of the Job.
        :param pulumi.Input[Union[Union['JobInputAssetArgs', 'JobInputAssetArgsDict'], Union['JobInputClipArgs', 'JobInputClipArgsDict'], Union['JobInputHttpArgs', 'JobInputHttpArgsDict'], Union['JobInputSequenceArgs', 'JobInputSequenceArgsDict'], Union['JobInputsArgs', 'JobInputsArgsDict']]] input: The inputs for the Job.
        :param pulumi.Input[str] job_name: The Job name.
        :param pulumi.Input[Sequence[pulumi.Input[Union['JobOutputAssetArgs', 'JobOutputAssetArgsDict']]]] outputs: The outputs for the Job.
        :param pulumi.Input[Union[str, 'Priority']] priority: Priority with which the job should be processed. Higher priority jobs are processed before lower priority jobs. If not set, the default is normal.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[str] transform_name: The Transform name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Job resource type. The progress and state can be obtained by polling a Job or subscribing to events using EventGrid.
        Azure REST API version: 2022-07-01. Prior API version in Azure Native 1.x: 2020-05-01.

        :param str resource_name: The name of the resource.
        :param JobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 correlation_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 input: Optional[pulumi.Input[Union[Union['JobInputAssetArgs', 'JobInputAssetArgsDict'], Union['JobInputClipArgs', 'JobInputClipArgsDict'], Union['JobInputHttpArgs', 'JobInputHttpArgsDict'], Union['JobInputSequenceArgs', 'JobInputSequenceArgsDict'], Union['JobInputsArgs', 'JobInputsArgsDict']]]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 outputs: Optional[pulumi.Input[Sequence[pulumi.Input[Union['JobOutputAssetArgs', 'JobOutputAssetArgsDict']]]]] = None,
                 priority: Optional[pulumi.Input[Union[str, 'Priority']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 transform_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobArgs.__new__(JobArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["correlation_data"] = correlation_data
            __props__.__dict__["description"] = description
            if input is None and not opts.urn:
                raise TypeError("Missing required property 'input'")
            __props__.__dict__["input"] = input
            __props__.__dict__["job_name"] = job_name
            if outputs is None and not opts.urn:
                raise TypeError("Missing required property 'outputs'")
            __props__.__dict__["outputs"] = outputs
            __props__.__dict__["priority"] = priority
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if transform_name is None and not opts.urn:
                raise TypeError("Missing required property 'transform_name'")
            __props__.__dict__["transform_name"] = transform_name
            __props__.__dict__["created"] = None
            __props__.__dict__["end_time"] = None
            __props__.__dict__["last_modified"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["start_time"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:media/v20180330preview:Job"), pulumi.Alias(type_="azure-native:media/v20180601preview:Job"), pulumi.Alias(type_="azure-native:media/v20180701:Job"), pulumi.Alias(type_="azure-native:media/v20200501:Job"), pulumi.Alias(type_="azure-native:media/v20210601:Job"), pulumi.Alias(type_="azure-native:media/v20211101:Job"), pulumi.Alias(type_="azure-native:media/v20220501preview:Job"), pulumi.Alias(type_="azure-native:media/v20220701:Job")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Job, __self__).__init__(
            'azure-native:media:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Job':
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobArgs.__new__(JobArgs)

        __props__.__dict__["correlation_data"] = None
        __props__.__dict__["created"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["end_time"] = None
        __props__.__dict__["input"] = None
        __props__.__dict__["last_modified"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["outputs"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Job(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="correlationData")
    def correlation_data(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Customer provided key, value pairs that will be returned in Job and JobOutput state events.
        """
        return pulumi.get(self, "correlation_data")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        The UTC date and time when the customer has created the Job, in 'YYYY-MM-DDThh:mm:ssZ' format.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Optional customer supplied description of the Job.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[str]:
        """
        The UTC date and time at which this Job finished processing.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def input(self) -> pulumi.Output[Any]:
        """
        The inputs for the Job.
        """
        return pulumi.get(self, "input")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The UTC date and time when the customer has last updated the Job, in 'YYYY-MM-DDThh:mm:ssZ' format.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Sequence['outputs.JobOutputAssetResponse']]:
        """
        The outputs for the Job.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[str]]:
        """
        Priority with which the job should be processed. Higher priority jobs are processed before lower priority jobs. If not set, the default is normal.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        The UTC date and time at which this Job began processing.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the job.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

