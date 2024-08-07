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

__all__ = ['CapabilityArgs', 'Capability']

@pulumi.input_type
class CapabilityArgs:
    def __init__(__self__, *,
                 parent_provider_namespace: pulumi.Input[str],
                 parent_resource_name: pulumi.Input[str],
                 parent_resource_type: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 target_name: pulumi.Input[str],
                 capability_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Capability resource.
        :param pulumi.Input[str] parent_provider_namespace: String that represents a resource provider namespace.
        :param pulumi.Input[str] parent_resource_name: String that represents a resource name.
        :param pulumi.Input[str] parent_resource_type: String that represents a resource type.
        :param pulumi.Input[str] resource_group_name: String that represents an Azure resource group.
        :param pulumi.Input[str] target_name: String that represents a Target resource name.
        :param pulumi.Input[str] capability_name: String that represents a Capability resource name.
        """
        pulumi.set(__self__, "parent_provider_namespace", parent_provider_namespace)
        pulumi.set(__self__, "parent_resource_name", parent_resource_name)
        pulumi.set(__self__, "parent_resource_type", parent_resource_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "target_name", target_name)
        if capability_name is not None:
            pulumi.set(__self__, "capability_name", capability_name)

    @property
    @pulumi.getter(name="parentProviderNamespace")
    def parent_provider_namespace(self) -> pulumi.Input[str]:
        """
        String that represents a resource provider namespace.
        """
        return pulumi.get(self, "parent_provider_namespace")

    @parent_provider_namespace.setter
    def parent_provider_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_provider_namespace", value)

    @property
    @pulumi.getter(name="parentResourceName")
    def parent_resource_name(self) -> pulumi.Input[str]:
        """
        String that represents a resource name.
        """
        return pulumi.get(self, "parent_resource_name")

    @parent_resource_name.setter
    def parent_resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_resource_name", value)

    @property
    @pulumi.getter(name="parentResourceType")
    def parent_resource_type(self) -> pulumi.Input[str]:
        """
        String that represents a resource type.
        """
        return pulumi.get(self, "parent_resource_type")

    @parent_resource_type.setter
    def parent_resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_resource_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        String that represents an Azure resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Input[str]:
        """
        String that represents a Target resource name.
        """
        return pulumi.get(self, "target_name")

    @target_name.setter
    def target_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_name", value)

    @property
    @pulumi.getter(name="capabilityName")
    def capability_name(self) -> Optional[pulumi.Input[str]]:
        """
        String that represents a Capability resource name.
        """
        return pulumi.get(self, "capability_name")

    @capability_name.setter
    def capability_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capability_name", value)


class Capability(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capability_name: Optional[pulumi.Input[str]] = None,
                 parent_provider_namespace: Optional[pulumi.Input[str]] = None,
                 parent_resource_name: Optional[pulumi.Input[str]] = None,
                 parent_resource_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Model that represents a Capability resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capability_name: String that represents a Capability resource name.
        :param pulumi.Input[str] parent_provider_namespace: String that represents a resource provider namespace.
        :param pulumi.Input[str] parent_resource_name: String that represents a resource name.
        :param pulumi.Input[str] parent_resource_type: String that represents a resource type.
        :param pulumi.Input[str] resource_group_name: String that represents an Azure resource group.
        :param pulumi.Input[str] target_name: String that represents a Target resource name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CapabilityArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Model that represents a Capability resource.

        :param str resource_name: The name of the resource.
        :param CapabilityArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CapabilityArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capability_name: Optional[pulumi.Input[str]] = None,
                 parent_provider_namespace: Optional[pulumi.Input[str]] = None,
                 parent_resource_name: Optional[pulumi.Input[str]] = None,
                 parent_resource_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CapabilityArgs.__new__(CapabilityArgs)

            __props__.__dict__["capability_name"] = capability_name
            if parent_provider_namespace is None and not opts.urn:
                raise TypeError("Missing required property 'parent_provider_namespace'")
            __props__.__dict__["parent_provider_namespace"] = parent_provider_namespace
            if parent_resource_name is None and not opts.urn:
                raise TypeError("Missing required property 'parent_resource_name'")
            __props__.__dict__["parent_resource_name"] = parent_resource_name
            if parent_resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'parent_resource_type'")
            __props__.__dict__["parent_resource_type"] = parent_resource_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if target_name is None and not opts.urn:
                raise TypeError("Missing required property 'target_name'")
            __props__.__dict__["target_name"] = target_name
            __props__.__dict__["name"] = None
            __props__.__dict__["properties"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:chaos:Capability"), pulumi.Alias(type_="azure-native:chaos/v20210915preview:Capability"), pulumi.Alias(type_="azure-native:chaos/v20220701preview:Capability"), pulumi.Alias(type_="azure-native:chaos/v20221001preview:Capability"), pulumi.Alias(type_="azure-native:chaos/v20230401preview:Capability"), pulumi.Alias(type_="azure-native:chaos/v20230415preview:Capability"), pulumi.Alias(type_="azure-native:chaos/v20230901preview:Capability"), pulumi.Alias(type_="azure-native:chaos/v20231027preview:Capability"), pulumi.Alias(type_="azure-native:chaos/v20240101:Capability"), pulumi.Alias(type_="azure-native:chaos/v20240322preview:Capability")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Capability, __self__).__init__(
            'azure-native:chaos/v20231101:Capability',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Capability':
        """
        Get an existing Capability resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CapabilityArgs.__new__(CapabilityArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Capability(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.CapabilityPropertiesResponse']:
        """
        The properties of a capability resource.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The standard system metadata of a resource type.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

