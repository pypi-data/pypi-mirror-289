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

__all__ = ['OpenAIArgs', 'OpenAI']

@pulumi.input_type
class OpenAIArgs:
    def __init__(__self__, *,
                 monitor_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 integration_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['OpenAIIntegrationPropertiesArgs']] = None):
        """
        The set of arguments for constructing a OpenAI resource.
        :param pulumi.Input[str] monitor_name: Monitor resource name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] integration_name: OpenAI Integration name
        :param pulumi.Input['OpenAIIntegrationPropertiesArgs'] properties: Open AI Integration details.
        """
        pulumi.set(__self__, "monitor_name", monitor_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if integration_name is not None:
            pulumi.set(__self__, "integration_name", integration_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Input[str]:
        """
        Monitor resource name
        """
        return pulumi.get(self, "monitor_name")

    @monitor_name.setter
    def monitor_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "monitor_name", value)

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
    @pulumi.getter(name="integrationName")
    def integration_name(self) -> Optional[pulumi.Input[str]]:
        """
        OpenAI Integration name
        """
        return pulumi.get(self, "integration_name")

    @integration_name.setter
    def integration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['OpenAIIntegrationPropertiesArgs']]:
        """
        Open AI Integration details.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['OpenAIIntegrationPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class OpenAI(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 integration_name: Optional[pulumi.Input[str]] = None,
                 monitor_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['OpenAIIntegrationPropertiesArgs', 'OpenAIIntegrationPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Capture properties of Open AI resource Integration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] integration_name: OpenAI Integration name
        :param pulumi.Input[str] monitor_name: Monitor resource name
        :param pulumi.Input[Union['OpenAIIntegrationPropertiesArgs', 'OpenAIIntegrationPropertiesArgsDict']] properties: Open AI Integration details.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OpenAIArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Capture properties of Open AI resource Integration.

        :param str resource_name: The name of the resource.
        :param OpenAIArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OpenAIArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 integration_name: Optional[pulumi.Input[str]] = None,
                 monitor_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['OpenAIIntegrationPropertiesArgs', 'OpenAIIntegrationPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OpenAIArgs.__new__(OpenAIArgs)

            __props__.__dict__["integration_name"] = integration_name
            if monitor_name is None and not opts.urn:
                raise TypeError("Missing required property 'monitor_name'")
            __props__.__dict__["monitor_name"] = monitor_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:elastic:OpenAI"), pulumi.Alias(type_="azure-native:elastic/v20240101preview:OpenAI"), pulumi.Alias(type_="azure-native:elastic/v20240301:OpenAI"), pulumi.Alias(type_="azure-native:elastic/v20240615preview:OpenAI")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OpenAI, __self__).__init__(
            'azure-native:elastic/v20240501preview:OpenAI',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OpenAI':
        """
        Get an existing OpenAI resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OpenAIArgs.__new__(OpenAIArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return OpenAI(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the integration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.OpenAIIntegrationPropertiesResponse']:
        """
        Open AI Integration details.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the integration.
        """
        return pulumi.get(self, "type")

