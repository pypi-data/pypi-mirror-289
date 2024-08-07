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
from ._inputs import *

__all__ = ['NetworkFunctionDefinitionGroupArgs', 'NetworkFunctionDefinitionGroup']

@pulumi.input_type
class NetworkFunctionDefinitionGroupArgs:
    def __init__(__self__, *,
                 publisher_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 network_function_definition_group_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['NetworkFunctionDefinitionGroupPropertiesFormatArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkFunctionDefinitionGroup resource.
        :param pulumi.Input[str] publisher_name: The name of the publisher.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] network_function_definition_group_name: The name of the network function definition group.
        :param pulumi.Input['NetworkFunctionDefinitionGroupPropertiesFormatArgs'] properties: Network function definition group properties.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "publisher_name", publisher_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_function_definition_group_name is not None:
            pulumi.set(__self__, "network_function_definition_group_name", network_function_definition_group_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="publisherName")
    def publisher_name(self) -> pulumi.Input[str]:
        """
        The name of the publisher.
        """
        return pulumi.get(self, "publisher_name")

    @publisher_name.setter
    def publisher_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "publisher_name", value)

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
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="networkFunctionDefinitionGroupName")
    def network_function_definition_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network function definition group.
        """
        return pulumi.get(self, "network_function_definition_group_name")

    @network_function_definition_group_name.setter
    def network_function_definition_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_function_definition_group_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['NetworkFunctionDefinitionGroupPropertiesFormatArgs']]:
        """
        Network function definition group properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['NetworkFunctionDefinitionGroupPropertiesFormatArgs']]):
        pulumi.set(self, "properties", value)

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


class NetworkFunctionDefinitionGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_function_definition_group_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['NetworkFunctionDefinitionGroupPropertiesFormatArgs', 'NetworkFunctionDefinitionGroupPropertiesFormatArgsDict']]] = None,
                 publisher_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Network function definition group resource.
        Azure REST API version: 2023-09-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] network_function_definition_group_name: The name of the network function definition group.
        :param pulumi.Input[Union['NetworkFunctionDefinitionGroupPropertiesFormatArgs', 'NetworkFunctionDefinitionGroupPropertiesFormatArgsDict']] properties: Network function definition group properties.
        :param pulumi.Input[str] publisher_name: The name of the publisher.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkFunctionDefinitionGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Network function definition group resource.
        Azure REST API version: 2023-09-01.

        :param str resource_name: The name of the resource.
        :param NetworkFunctionDefinitionGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkFunctionDefinitionGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_function_definition_group_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['NetworkFunctionDefinitionGroupPropertiesFormatArgs', 'NetworkFunctionDefinitionGroupPropertiesFormatArgsDict']]] = None,
                 publisher_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkFunctionDefinitionGroupArgs.__new__(NetworkFunctionDefinitionGroupArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["network_function_definition_group_name"] = network_function_definition_group_name
            __props__.__dict__["properties"] = properties
            if publisher_name is None and not opts.urn:
                raise TypeError("Missing required property 'publisher_name'")
            __props__.__dict__["publisher_name"] = publisher_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybridnetwork/v20230901:NetworkFunctionDefinitionGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkFunctionDefinitionGroup, __self__).__init__(
            'azure-native:hybridnetwork:NetworkFunctionDefinitionGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkFunctionDefinitionGroup':
        """
        Get an existing NetworkFunctionDefinitionGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkFunctionDefinitionGroupArgs.__new__(NetworkFunctionDefinitionGroupArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return NetworkFunctionDefinitionGroup(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.NetworkFunctionDefinitionGroupPropertiesFormatResponse']:
        """
        Network function definition group properties.
        """
        return pulumi.get(self, "properties")

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

