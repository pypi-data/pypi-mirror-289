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

__all__ = ['EnterpriseChannelArgs', 'EnterpriseChannel']

@pulumi.input_type
class EnterpriseChannelArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['EnterpriseChannelPropertiesArgs']] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a EnterpriseChannel resource.
        :param pulumi.Input[str] resource_group_name: The name of the Bot resource group in the user subscription.
        :param pulumi.Input[Union[str, 'Kind']] kind: Required. Gets or sets the Kind of the resource.
        :param pulumi.Input[str] location: Specifies the location of the resource.
        :param pulumi.Input['EnterpriseChannelPropertiesArgs'] properties: The set of properties specific to an Enterprise Channel resource.
        :param pulumi.Input[str] resource_name: The name of the Bot resource.
        :param pulumi.Input['SkuArgs'] sku: Gets or sets the SKU of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Contains resource tags defined as key/value pairs.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Bot resource group in the user subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'Kind']]]:
        """
        Required. Gets or sets the Kind of the resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'Kind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['EnterpriseChannelPropertiesArgs']]:
        """
        The set of properties specific to an Enterprise Channel resource.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['EnterpriseChannelPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Bot resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        Gets or sets the SKU of the resource.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class EnterpriseChannel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['EnterpriseChannelPropertiesArgs', 'EnterpriseChannelPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Enterprise Channel resource definition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'Kind']] kind: Required. Gets or sets the Kind of the resource.
        :param pulumi.Input[str] location: Specifies the location of the resource.
        :param pulumi.Input[Union['EnterpriseChannelPropertiesArgs', 'EnterpriseChannelPropertiesArgsDict']] properties: The set of properties specific to an Enterprise Channel resource.
        :param pulumi.Input[str] resource_group_name: The name of the Bot resource group in the user subscription.
        :param pulumi.Input[str] resource_name_: The name of the Bot resource.
        :param pulumi.Input[Union['SkuArgs', 'SkuArgsDict']] sku: Gets or sets the SKU of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Contains resource tags defined as key/value pairs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnterpriseChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Enterprise Channel resource definition

        :param str resource_name: The name of the resource.
        :param EnterpriseChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnterpriseChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['EnterpriseChannelPropertiesArgs', 'EnterpriseChannelPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnterpriseChannelArgs.__new__(EnterpriseChannelArgs)

            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        super(EnterpriseChannel, __self__).__init__(
            'azure-native:botservice/v20180712:EnterpriseChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EnterpriseChannel':
        """
        Get an existing EnterpriseChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnterpriseChannelArgs.__new__(EnterpriseChannelArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return EnterpriseChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Entity Tag
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Required. Gets or sets the Kind of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.EnterpriseChannelPropertiesResponse']:
        """
        The set of properties specific to an Enterprise Channel resource.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        Gets or sets the SKU of the resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Specifies the type of the resource.
        """
        return pulumi.get(self, "type")

