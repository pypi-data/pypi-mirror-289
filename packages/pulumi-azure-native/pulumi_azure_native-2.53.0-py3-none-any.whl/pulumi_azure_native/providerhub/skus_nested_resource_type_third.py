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

__all__ = ['SkusNestedResourceTypeThirdArgs', 'SkusNestedResourceTypeThird']

@pulumi.input_type
class SkusNestedResourceTypeThirdArgs:
    def __init__(__self__, *,
                 nested_resource_type_first: pulumi.Input[str],
                 nested_resource_type_second: pulumi.Input[str],
                 nested_resource_type_third: pulumi.Input[str],
                 provider_namespace: pulumi.Input[str],
                 resource_type: pulumi.Input[str],
                 properties: Optional[pulumi.Input['SkuResourcePropertiesArgs']] = None,
                 sku: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SkusNestedResourceTypeThird resource.
        :param pulumi.Input[str] nested_resource_type_first: The first child resource type.
        :param pulumi.Input[str] nested_resource_type_second: The second child resource type.
        :param pulumi.Input[str] nested_resource_type_third: The third child resource type.
        :param pulumi.Input[str] provider_namespace: The name of the resource provider hosted within ProviderHub.
        :param pulumi.Input[str] resource_type: The resource type.
        :param pulumi.Input[str] sku: The SKU.
        """
        pulumi.set(__self__, "nested_resource_type_first", nested_resource_type_first)
        pulumi.set(__self__, "nested_resource_type_second", nested_resource_type_second)
        pulumi.set(__self__, "nested_resource_type_third", nested_resource_type_third)
        pulumi.set(__self__, "provider_namespace", provider_namespace)
        pulumi.set(__self__, "resource_type", resource_type)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)

    @property
    @pulumi.getter(name="nestedResourceTypeFirst")
    def nested_resource_type_first(self) -> pulumi.Input[str]:
        """
        The first child resource type.
        """
        return pulumi.get(self, "nested_resource_type_first")

    @nested_resource_type_first.setter
    def nested_resource_type_first(self, value: pulumi.Input[str]):
        pulumi.set(self, "nested_resource_type_first", value)

    @property
    @pulumi.getter(name="nestedResourceTypeSecond")
    def nested_resource_type_second(self) -> pulumi.Input[str]:
        """
        The second child resource type.
        """
        return pulumi.get(self, "nested_resource_type_second")

    @nested_resource_type_second.setter
    def nested_resource_type_second(self, value: pulumi.Input[str]):
        pulumi.set(self, "nested_resource_type_second", value)

    @property
    @pulumi.getter(name="nestedResourceTypeThird")
    def nested_resource_type_third(self) -> pulumi.Input[str]:
        """
        The third child resource type.
        """
        return pulumi.get(self, "nested_resource_type_third")

    @nested_resource_type_third.setter
    def nested_resource_type_third(self, value: pulumi.Input[str]):
        pulumi.set(self, "nested_resource_type_third", value)

    @property
    @pulumi.getter(name="providerNamespace")
    def provider_namespace(self) -> pulumi.Input[str]:
        """
        The name of the resource provider hosted within ProviderHub.
        """
        return pulumi.get(self, "provider_namespace")

    @provider_namespace.setter
    def provider_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_namespace", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['SkuResourcePropertiesArgs']]:
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['SkuResourcePropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[str]]:
        """
        The SKU.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku", value)


class SkusNestedResourceTypeThird(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 nested_resource_type_first: Optional[pulumi.Input[str]] = None,
                 nested_resource_type_second: Optional[pulumi.Input[str]] = None,
                 nested_resource_type_third: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['SkuResourcePropertiesArgs', 'SkuResourcePropertiesArgsDict']]] = None,
                 provider_namespace: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure REST API version: 2021-09-01-preview. Prior API version in Azure Native 1.x: 2020-11-20.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] nested_resource_type_first: The first child resource type.
        :param pulumi.Input[str] nested_resource_type_second: The second child resource type.
        :param pulumi.Input[str] nested_resource_type_third: The third child resource type.
        :param pulumi.Input[str] provider_namespace: The name of the resource provider hosted within ProviderHub.
        :param pulumi.Input[str] resource_type: The resource type.
        :param pulumi.Input[str] sku: The SKU.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SkusNestedResourceTypeThirdArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure REST API version: 2021-09-01-preview. Prior API version in Azure Native 1.x: 2020-11-20.

        :param str resource_name: The name of the resource.
        :param SkusNestedResourceTypeThirdArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SkusNestedResourceTypeThirdArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 nested_resource_type_first: Optional[pulumi.Input[str]] = None,
                 nested_resource_type_second: Optional[pulumi.Input[str]] = None,
                 nested_resource_type_third: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['SkuResourcePropertiesArgs', 'SkuResourcePropertiesArgsDict']]] = None,
                 provider_namespace: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SkusNestedResourceTypeThirdArgs.__new__(SkusNestedResourceTypeThirdArgs)

            if nested_resource_type_first is None and not opts.urn:
                raise TypeError("Missing required property 'nested_resource_type_first'")
            __props__.__dict__["nested_resource_type_first"] = nested_resource_type_first
            if nested_resource_type_second is None and not opts.urn:
                raise TypeError("Missing required property 'nested_resource_type_second'")
            __props__.__dict__["nested_resource_type_second"] = nested_resource_type_second
            if nested_resource_type_third is None and not opts.urn:
                raise TypeError("Missing required property 'nested_resource_type_third'")
            __props__.__dict__["nested_resource_type_third"] = nested_resource_type_third
            __props__.__dict__["properties"] = properties
            if provider_namespace is None and not opts.urn:
                raise TypeError("Missing required property 'provider_namespace'")
            __props__.__dict__["provider_namespace"] = provider_namespace
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["sku"] = sku
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:providerhub/v20201120:SkusNestedResourceTypeThird"), pulumi.Alias(type_="azure-native:providerhub/v20210501preview:SkusNestedResourceTypeThird"), pulumi.Alias(type_="azure-native:providerhub/v20210601preview:SkusNestedResourceTypeThird"), pulumi.Alias(type_="azure-native:providerhub/v20210901preview:SkusNestedResourceTypeThird")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SkusNestedResourceTypeThird, __self__).__init__(
            'azure-native:providerhub:SkusNestedResourceTypeThird',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SkusNestedResourceTypeThird':
        """
        Get an existing SkusNestedResourceTypeThird resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SkusNestedResourceTypeThirdArgs.__new__(SkusNestedResourceTypeThirdArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SkusNestedResourceTypeThird(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.SkuResourceResponseProperties']:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

