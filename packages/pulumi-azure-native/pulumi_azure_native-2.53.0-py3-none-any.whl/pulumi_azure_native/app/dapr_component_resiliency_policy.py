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

__all__ = ['DaprComponentResiliencyPolicyArgs', 'DaprComponentResiliencyPolicy']

@pulumi.input_type
class DaprComponentResiliencyPolicyArgs:
    def __init__(__self__, *,
                 component_name: pulumi.Input[str],
                 environment_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 inbound_policy: Optional[pulumi.Input['DaprComponentResiliencyPolicyConfigurationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outbound_policy: Optional[pulumi.Input['DaprComponentResiliencyPolicyConfigurationArgs']] = None):
        """
        The set of arguments for constructing a DaprComponentResiliencyPolicy resource.
        :param pulumi.Input[str] component_name: Name of the Dapr Component.
        :param pulumi.Input[str] environment_name: Name of the Managed Environment.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['DaprComponentResiliencyPolicyConfigurationArgs'] inbound_policy: The optional inbound component resiliency policy configuration
        :param pulumi.Input[str] name: Name of the Dapr Component Resiliency Policy.
        :param pulumi.Input['DaprComponentResiliencyPolicyConfigurationArgs'] outbound_policy: The optional outbound component resiliency policy configuration
        """
        pulumi.set(__self__, "component_name", component_name)
        pulumi.set(__self__, "environment_name", environment_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if inbound_policy is not None:
            pulumi.set(__self__, "inbound_policy", inbound_policy)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if outbound_policy is not None:
            pulumi.set(__self__, "outbound_policy", outbound_policy)

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> pulumi.Input[str]:
        """
        Name of the Dapr Component.
        """
        return pulumi.get(self, "component_name")

    @component_name.setter
    def component_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "component_name", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[str]:
        """
        Name of the Managed Environment.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_name", value)

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
    @pulumi.getter(name="inboundPolicy")
    def inbound_policy(self) -> Optional[pulumi.Input['DaprComponentResiliencyPolicyConfigurationArgs']]:
        """
        The optional inbound component resiliency policy configuration
        """
        return pulumi.get(self, "inbound_policy")

    @inbound_policy.setter
    def inbound_policy(self, value: Optional[pulumi.Input['DaprComponentResiliencyPolicyConfigurationArgs']]):
        pulumi.set(self, "inbound_policy", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Dapr Component Resiliency Policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="outboundPolicy")
    def outbound_policy(self) -> Optional[pulumi.Input['DaprComponentResiliencyPolicyConfigurationArgs']]:
        """
        The optional outbound component resiliency policy configuration
        """
        return pulumi.get(self, "outbound_policy")

    @outbound_policy.setter
    def outbound_policy(self, value: Optional[pulumi.Input['DaprComponentResiliencyPolicyConfigurationArgs']]):
        pulumi.set(self, "outbound_policy", value)


class DaprComponentResiliencyPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 component_name: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 inbound_policy: Optional[pulumi.Input[Union['DaprComponentResiliencyPolicyConfigurationArgs', 'DaprComponentResiliencyPolicyConfigurationArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outbound_policy: Optional[pulumi.Input[Union['DaprComponentResiliencyPolicyConfigurationArgs', 'DaprComponentResiliencyPolicyConfigurationArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Dapr Component Resiliency Policy.
        Azure REST API version: 2023-08-01-preview.

        Other available API versions: 2023-11-02-preview, 2024-02-02-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] component_name: Name of the Dapr Component.
        :param pulumi.Input[str] environment_name: Name of the Managed Environment.
        :param pulumi.Input[Union['DaprComponentResiliencyPolicyConfigurationArgs', 'DaprComponentResiliencyPolicyConfigurationArgsDict']] inbound_policy: The optional inbound component resiliency policy configuration
        :param pulumi.Input[str] name: Name of the Dapr Component Resiliency Policy.
        :param pulumi.Input[Union['DaprComponentResiliencyPolicyConfigurationArgs', 'DaprComponentResiliencyPolicyConfigurationArgsDict']] outbound_policy: The optional outbound component resiliency policy configuration
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DaprComponentResiliencyPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Dapr Component Resiliency Policy.
        Azure REST API version: 2023-08-01-preview.

        Other available API versions: 2023-11-02-preview, 2024-02-02-preview.

        :param str resource_name: The name of the resource.
        :param DaprComponentResiliencyPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DaprComponentResiliencyPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 component_name: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 inbound_policy: Optional[pulumi.Input[Union['DaprComponentResiliencyPolicyConfigurationArgs', 'DaprComponentResiliencyPolicyConfigurationArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outbound_policy: Optional[pulumi.Input[Union['DaprComponentResiliencyPolicyConfigurationArgs', 'DaprComponentResiliencyPolicyConfigurationArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DaprComponentResiliencyPolicyArgs.__new__(DaprComponentResiliencyPolicyArgs)

            if component_name is None and not opts.urn:
                raise TypeError("Missing required property 'component_name'")
            __props__.__dict__["component_name"] = component_name
            if environment_name is None and not opts.urn:
                raise TypeError("Missing required property 'environment_name'")
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["inbound_policy"] = inbound_policy
            __props__.__dict__["name"] = name
            __props__.__dict__["outbound_policy"] = outbound_policy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app/v20230801preview:DaprComponentResiliencyPolicy"), pulumi.Alias(type_="azure-native:app/v20231102preview:DaprComponentResiliencyPolicy"), pulumi.Alias(type_="azure-native:app/v20240202preview:DaprComponentResiliencyPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DaprComponentResiliencyPolicy, __self__).__init__(
            'azure-native:app:DaprComponentResiliencyPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DaprComponentResiliencyPolicy':
        """
        Get an existing DaprComponentResiliencyPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DaprComponentResiliencyPolicyArgs.__new__(DaprComponentResiliencyPolicyArgs)

        __props__.__dict__["inbound_policy"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["outbound_policy"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return DaprComponentResiliencyPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="inboundPolicy")
    def inbound_policy(self) -> pulumi.Output[Optional['outputs.DaprComponentResiliencyPolicyConfigurationResponse']]:
        """
        The optional inbound component resiliency policy configuration
        """
        return pulumi.get(self, "inbound_policy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outboundPolicy")
    def outbound_policy(self) -> pulumi.Output[Optional['outputs.DaprComponentResiliencyPolicyConfigurationResponse']]:
        """
        The optional outbound component resiliency policy configuration
        """
        return pulumi.get(self, "outbound_policy")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

