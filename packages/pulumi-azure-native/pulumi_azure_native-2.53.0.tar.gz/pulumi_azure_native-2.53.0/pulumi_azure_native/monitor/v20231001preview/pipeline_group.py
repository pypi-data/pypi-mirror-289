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

__all__ = ['PipelineGroupArgs', 'PipelineGroup']

@pulumi.input_type
class PipelineGroupArgs:
    def __init__(__self__, *,
                 exporters: pulumi.Input[Sequence[pulumi.Input['ExporterArgs']]],
                 processors: pulumi.Input[Sequence[pulumi.Input['ProcessorArgs']]],
                 receivers: pulumi.Input[Sequence[pulumi.Input['ReceiverArgs']]],
                 resource_group_name: pulumi.Input[str],
                 service: pulumi.Input['ServiceArgs'],
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 networking_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkingConfigurationArgs']]]] = None,
                 pipeline_group_name: Optional[pulumi.Input[str]] = None,
                 replicas: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PipelineGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['ExporterArgs']]] exporters: The exporters specified for a pipeline group instance.
        :param pulumi.Input[Sequence[pulumi.Input['ProcessorArgs']]] processors: The processors specified for a pipeline group instance.
        :param pulumi.Input[Sequence[pulumi.Input['ReceiverArgs']]] receivers: The receivers specified for a pipeline group instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ServiceArgs'] service: The service section for a given pipeline group instance.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location for given pipeline group.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input['NetworkingConfigurationArgs']]] networking_configurations: Networking configurations for the pipeline group instance.
        :param pulumi.Input[str] pipeline_group_name: The name of pipeline group. The name is case insensitive.
        :param pulumi.Input[int] replicas: Defines the amount of replicas of the pipeline group instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "exporters", exporters)
        pulumi.set(__self__, "processors", processors)
        pulumi.set(__self__, "receivers", receivers)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service", service)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if networking_configurations is not None:
            pulumi.set(__self__, "networking_configurations", networking_configurations)
        if pipeline_group_name is not None:
            pulumi.set(__self__, "pipeline_group_name", pipeline_group_name)
        if replicas is not None:
            pulumi.set(__self__, "replicas", replicas)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def exporters(self) -> pulumi.Input[Sequence[pulumi.Input['ExporterArgs']]]:
        """
        The exporters specified for a pipeline group instance.
        """
        return pulumi.get(self, "exporters")

    @exporters.setter
    def exporters(self, value: pulumi.Input[Sequence[pulumi.Input['ExporterArgs']]]):
        pulumi.set(self, "exporters", value)

    @property
    @pulumi.getter
    def processors(self) -> pulumi.Input[Sequence[pulumi.Input['ProcessorArgs']]]:
        """
        The processors specified for a pipeline group instance.
        """
        return pulumi.get(self, "processors")

    @processors.setter
    def processors(self, value: pulumi.Input[Sequence[pulumi.Input['ProcessorArgs']]]):
        pulumi.set(self, "processors", value)

    @property
    @pulumi.getter
    def receivers(self) -> pulumi.Input[Sequence[pulumi.Input['ReceiverArgs']]]:
        """
        The receivers specified for a pipeline group instance.
        """
        return pulumi.get(self, "receivers")

    @receivers.setter
    def receivers(self, value: pulumi.Input[Sequence[pulumi.Input['ReceiverArgs']]]):
        pulumi.set(self, "receivers", value)

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
    def service(self) -> pulumi.Input['ServiceArgs']:
        """
        The service section for a given pipeline group instance.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: pulumi.Input['ServiceArgs']):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extended location for given pipeline group.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

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
    @pulumi.getter(name="networkingConfigurations")
    def networking_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkingConfigurationArgs']]]]:
        """
        Networking configurations for the pipeline group instance.
        """
        return pulumi.get(self, "networking_configurations")

    @networking_configurations.setter
    def networking_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkingConfigurationArgs']]]]):
        pulumi.set(self, "networking_configurations", value)

    @property
    @pulumi.getter(name="pipelineGroupName")
    def pipeline_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of pipeline group. The name is case insensitive.
        """
        return pulumi.get(self, "pipeline_group_name")

    @pipeline_group_name.setter
    def pipeline_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_group_name", value)

    @property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[int]]:
        """
        Defines the amount of replicas of the pipeline group instance.
        """
        return pulumi.get(self, "replicas")

    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "replicas", value)

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


class PipelineGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exporters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ExporterArgs', 'ExporterArgsDict']]]]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 networking_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NetworkingConfigurationArgs', 'NetworkingConfigurationArgsDict']]]]] = None,
                 pipeline_group_name: Optional[pulumi.Input[str]] = None,
                 processors: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ProcessorArgs', 'ProcessorArgsDict']]]]] = None,
                 receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ReceiverArgs', 'ReceiverArgsDict']]]]] = None,
                 replicas: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[Union['ServiceArgs', 'ServiceArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A pipeline group definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ExporterArgs', 'ExporterArgsDict']]]] exporters: The exporters specified for a pipeline group instance.
        :param pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']] extended_location: The extended location for given pipeline group.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input[Union['NetworkingConfigurationArgs', 'NetworkingConfigurationArgsDict']]]] networking_configurations: Networking configurations for the pipeline group instance.
        :param pulumi.Input[str] pipeline_group_name: The name of pipeline group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ProcessorArgs', 'ProcessorArgsDict']]]] processors: The processors specified for a pipeline group instance.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ReceiverArgs', 'ReceiverArgsDict']]]] receivers: The receivers specified for a pipeline group instance.
        :param pulumi.Input[int] replicas: Defines the amount of replicas of the pipeline group instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['ServiceArgs', 'ServiceArgsDict']] service: The service section for a given pipeline group instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A pipeline group definition.

        :param str resource_name: The name of the resource.
        :param PipelineGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exporters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ExporterArgs', 'ExporterArgsDict']]]]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 networking_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NetworkingConfigurationArgs', 'NetworkingConfigurationArgsDict']]]]] = None,
                 pipeline_group_name: Optional[pulumi.Input[str]] = None,
                 processors: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ProcessorArgs', 'ProcessorArgsDict']]]]] = None,
                 receivers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ReceiverArgs', 'ReceiverArgsDict']]]]] = None,
                 replicas: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[Union['ServiceArgs', 'ServiceArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineGroupArgs.__new__(PipelineGroupArgs)

            if exporters is None and not opts.urn:
                raise TypeError("Missing required property 'exporters'")
            __props__.__dict__["exporters"] = exporters
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            __props__.__dict__["networking_configurations"] = networking_configurations
            __props__.__dict__["pipeline_group_name"] = pipeline_group_name
            if processors is None and not opts.urn:
                raise TypeError("Missing required property 'processors'")
            __props__.__dict__["processors"] = processors
            if receivers is None and not opts.urn:
                raise TypeError("Missing required property 'receivers'")
            __props__.__dict__["receivers"] = receivers
            __props__.__dict__["replicas"] = replicas
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service is None and not opts.urn:
                raise TypeError("Missing required property 'service'")
            __props__.__dict__["service"] = service
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:monitor:PipelineGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PipelineGroup, __self__).__init__(
            'azure-native:monitor/v20231001preview:PipelineGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PipelineGroup':
        """
        Get an existing PipelineGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PipelineGroupArgs.__new__(PipelineGroupArgs)

        __props__.__dict__["exporters"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["networking_configurations"] = None
        __props__.__dict__["processors"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["receivers"] = None
        __props__.__dict__["replicas"] = None
        __props__.__dict__["service"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return PipelineGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def exporters(self) -> pulumi.Output[Sequence['outputs.ExporterResponse']]:
        """
        The exporters specified for a pipeline group instance.
        """
        return pulumi.get(self, "exporters")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extended location for given pipeline group.
        """
        return pulumi.get(self, "extended_location")

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
    @pulumi.getter(name="networkingConfigurations")
    def networking_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkingConfigurationResponse']]]:
        """
        Networking configurations for the pipeline group instance.
        """
        return pulumi.get(self, "networking_configurations")

    @property
    @pulumi.getter
    def processors(self) -> pulumi.Output[Sequence['outputs.ProcessorResponse']]:
        """
        The processors specified for a pipeline group instance.
        """
        return pulumi.get(self, "processors")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of a pipeline group instance. Set to Succeeded if everything is healthy.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def receivers(self) -> pulumi.Output[Sequence['outputs.ReceiverResponse']]:
        """
        The receivers specified for a pipeline group instance.
        """
        return pulumi.get(self, "receivers")

    @property
    @pulumi.getter
    def replicas(self) -> pulumi.Output[Optional[int]]:
        """
        Defines the amount of replicas of the pipeline group instance.
        """
        return pulumi.get(self, "replicas")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output['outputs.ServiceResponse']:
        """
        The service section for a given pipeline group instance.
        """
        return pulumi.get(self, "service")

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

