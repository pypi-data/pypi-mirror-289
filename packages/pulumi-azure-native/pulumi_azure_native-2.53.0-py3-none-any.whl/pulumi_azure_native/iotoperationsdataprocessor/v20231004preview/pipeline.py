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

__all__ = ['PipelineArgs', 'Pipeline']

@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 input: pulumi.Input['PipelineInputArgs'],
                 instance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 stages: pulumi.Input[Mapping[str, pulumi.Input['PipelineStageArgs']]],
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Pipeline resource.
        :param pulumi.Input[bool] enabled: Flag indicating whether the pipeline should be running or not.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: Edge location of the resource.
        :param pulumi.Input['PipelineInputArgs'] input: Information about where to pull input data from.
        :param pulumi.Input[str] instance_name: Name of instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input['PipelineStageArgs']]] stages: Map of stage ids to stage configurations for all pipeline processing and output stages.
        :param pulumi.Input[str] description: Detailed description of the Pipeline.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] pipeline_name: Name of pipeline
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "input", input)
        pulumi.set(__self__, "instance_name", instance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "stages", stages)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if pipeline_name is not None:
            pulumi.set(__self__, "pipeline_name", pipeline_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Flag indicating whether the pipeline should be running or not.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        Edge location of the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter
    def input(self) -> pulumi.Input['PipelineInputArgs']:
        """
        Information about where to pull input data from.
        """
        return pulumi.get(self, "input")

    @input.setter
    def input(self, value: pulumi.Input['PipelineInputArgs']):
        pulumi.set(self, "input", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[str]:
        """
        Name of instance.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_name", value)

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
    @pulumi.getter
    def stages(self) -> pulumi.Input[Mapping[str, pulumi.Input['PipelineStageArgs']]]:
        """
        Map of stage ids to stage configurations for all pipeline processing and output stages.
        """
        return pulumi.get(self, "stages")

    @stages.setter
    def stages(self, value: pulumi.Input[Mapping[str, pulumi.Input['PipelineStageArgs']]]):
        pulumi.set(self, "stages", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Detailed description of the Pipeline.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

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
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of pipeline
        """
        return pulumi.get(self, "pipeline_name")

    @pipeline_name.setter
    def pipeline_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 input: Optional[pulumi.Input[Union['PipelineInputArgs', 'PipelineInputArgsDict']]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 stages: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['PipelineStageArgs', 'PipelineStageArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A Pipeline resource belonging to an Instance resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Detailed description of the Pipeline.
        :param pulumi.Input[bool] enabled: Flag indicating whether the pipeline should be running or not.
        :param pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']] extended_location: Edge location of the resource.
        :param pulumi.Input[Union['PipelineInputArgs', 'PipelineInputArgsDict']] input: Information about where to pull input data from.
        :param pulumi.Input[str] instance_name: Name of instance.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] pipeline_name: Name of pipeline
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['PipelineStageArgs', 'PipelineStageArgsDict']]]] stages: Map of stage ids to stage configurations for all pipeline processing and output stages.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Pipeline resource belonging to an Instance resource.

        :param str resource_name: The name of the resource.
        :param PipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 input: Optional[pulumi.Input[Union['PipelineInputArgs', 'PipelineInputArgsDict']]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 stages: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['PipelineStageArgs', 'PipelineStageArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineArgs.__new__(PipelineArgs)

            __props__.__dict__["description"] = description
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            if input is None and not opts.urn:
                raise TypeError("Missing required property 'input'")
            __props__.__dict__["input"] = input
            if instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'instance_name'")
            __props__.__dict__["instance_name"] = instance_name
            __props__.__dict__["location"] = location
            __props__.__dict__["pipeline_name"] = pipeline_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if stages is None and not opts.urn:
                raise TypeError("Missing required property 'stages'")
            __props__.__dict__["stages"] = stages
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:iotoperationsdataprocessor:Pipeline")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Pipeline, __self__).__init__(
            'azure-native:iotoperationsdataprocessor/v20231004preview:Pipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Pipeline':
        """
        Get an existing Pipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PipelineArgs.__new__(PipelineArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["input"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["stages"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Pipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Detailed description of the Pipeline.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Flag indicating whether the pipeline should be running or not.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        Edge location of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def input(self) -> pulumi.Output['outputs.PipelineInputResponse']:
        """
        Information about where to pull input data from.
        """
        return pulumi.get(self, "input")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
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
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def stages(self) -> pulumi.Output[Mapping[str, 'outputs.PipelineStageResponse']]:
        """
        Map of stage ids to stage configurations for all pipeline processing and output stages.
        """
        return pulumi.get(self, "stages")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

