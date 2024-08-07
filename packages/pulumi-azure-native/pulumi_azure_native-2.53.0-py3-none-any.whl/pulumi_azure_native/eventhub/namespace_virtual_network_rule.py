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

__all__ = ['NamespaceVirtualNetworkRuleArgs', 'NamespaceVirtualNetworkRule']

@pulumi.input_type
class NamespaceVirtualNetworkRuleArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 virtual_network_rule_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_subnet_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NamespaceVirtualNetworkRule resource.
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        :param pulumi.Input[str] virtual_network_rule_name: The Virtual Network Rule name.
        :param pulumi.Input[str] virtual_network_subnet_id: ARM ID of Virtual Network Subnet
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if virtual_network_rule_name is not None:
            pulumi.set(__self__, "virtual_network_rule_name", virtual_network_rule_name)
        if virtual_network_subnet_id is not None:
            pulumi.set(__self__, "virtual_network_subnet_id", virtual_network_subnet_id)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The Namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group within the azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualNetworkRuleName")
    def virtual_network_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Virtual Network Rule name.
        """
        return pulumi.get(self, "virtual_network_rule_name")

    @virtual_network_rule_name.setter
    def virtual_network_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_rule_name", value)

    @property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM ID of Virtual Network Subnet
        """
        return pulumi.get(self, "virtual_network_subnet_id")

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_subnet_id", value)


class NamespaceVirtualNetworkRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_rule_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Single item in a List or Get VirtualNetworkRules operation
        Azure REST API version: 2018-01-01-preview. Prior API version in Azure Native 1.x: 2018-01-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        :param pulumi.Input[str] virtual_network_rule_name: The Virtual Network Rule name.
        :param pulumi.Input[str] virtual_network_subnet_id: ARM ID of Virtual Network Subnet
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceVirtualNetworkRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Single item in a List or Get VirtualNetworkRules operation
        Azure REST API version: 2018-01-01-preview. Prior API version in Azure Native 1.x: 2018-01-01-preview.

        :param str resource_name: The name of the resource.
        :param NamespaceVirtualNetworkRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceVirtualNetworkRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_rule_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceVirtualNetworkRuleArgs.__new__(NamespaceVirtualNetworkRuleArgs)

            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["virtual_network_rule_name"] = virtual_network_rule_name
            __props__.__dict__["virtual_network_subnet_id"] = virtual_network_subnet_id
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventhub/v20180101preview:NamespaceVirtualNetworkRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NamespaceVirtualNetworkRule, __self__).__init__(
            'azure-native:eventhub:NamespaceVirtualNetworkRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NamespaceVirtualNetworkRule':
        """
        Get an existing NamespaceVirtualNetworkRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceVirtualNetworkRuleArgs.__new__(NamespaceVirtualNetworkRuleArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network_subnet_id"] = None
        return NamespaceVirtualNetworkRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM ID of Virtual Network Subnet
        """
        return pulumi.get(self, "virtual_network_subnet_id")

