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

__all__ = ['ConfigurationPolicyGroupArgs', 'ConfigurationPolicyGroup']

@pulumi.input_type
class ConfigurationPolicyGroupArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 vpn_server_configuration_name: pulumi.Input[str],
                 configuration_policy_group_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_members: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigurationPolicyGroupMemberArgs']]]] = None,
                 priority: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ConfigurationPolicyGroup resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the ConfigurationPolicyGroup.
        :param pulumi.Input[str] vpn_server_configuration_name: The name of the VpnServerConfiguration.
        :param pulumi.Input[str] configuration_policy_group_name: The name of the ConfigurationPolicyGroup.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[bool] is_default: Shows if this is a Default VpnServerConfigurationPolicyGroup or not.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[Sequence[pulumi.Input['VpnServerConfigurationPolicyGroupMemberArgs']]] policy_members: Multiple PolicyMembers for VpnServerConfigurationPolicyGroup.
        :param pulumi.Input[int] priority: Priority for VpnServerConfigurationPolicyGroup.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vpn_server_configuration_name", vpn_server_configuration_name)
        if configuration_policy_group_name is not None:
            pulumi.set(__self__, "configuration_policy_group_name", configuration_policy_group_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if is_default is not None:
            pulumi.set(__self__, "is_default", is_default)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_members is not None:
            pulumi.set(__self__, "policy_members", policy_members)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the ConfigurationPolicyGroup.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="vpnServerConfigurationName")
    def vpn_server_configuration_name(self) -> pulumi.Input[str]:
        """
        The name of the VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_server_configuration_name")

    @vpn_server_configuration_name.setter
    def vpn_server_configuration_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpn_server_configuration_name", value)

    @property
    @pulumi.getter(name="configurationPolicyGroupName")
    def configuration_policy_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ConfigurationPolicyGroup.
        """
        return pulumi.get(self, "configuration_policy_group_name")

    @configuration_policy_group_name.setter
    def configuration_policy_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_policy_group_name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[bool]]:
        """
        Shows if this is a Default VpnServerConfigurationPolicyGroup or not.
        """
        return pulumi.get(self, "is_default")

    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyMembers")
    def policy_members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigurationPolicyGroupMemberArgs']]]]:
        """
        Multiple PolicyMembers for VpnServerConfigurationPolicyGroup.
        """
        return pulumi.get(self, "policy_members")

    @policy_members.setter
    def policy_members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnServerConfigurationPolicyGroupMemberArgs']]]]):
        pulumi.set(self, "policy_members", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority for VpnServerConfigurationPolicyGroup.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)


class ConfigurationPolicyGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_policy_group_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_members: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpnServerConfigurationPolicyGroupMemberArgs', 'VpnServerConfigurationPolicyGroupMemberArgsDict']]]]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vpn_server_configuration_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        VpnServerConfigurationPolicyGroup Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] configuration_policy_group_name: The name of the ConfigurationPolicyGroup.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[bool] is_default: Shows if this is a Default VpnServerConfigurationPolicyGroup or not.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['VpnServerConfigurationPolicyGroupMemberArgs', 'VpnServerConfigurationPolicyGroupMemberArgsDict']]]] policy_members: Multiple PolicyMembers for VpnServerConfigurationPolicyGroup.
        :param pulumi.Input[int] priority: Priority for VpnServerConfigurationPolicyGroup.
        :param pulumi.Input[str] resource_group_name: The resource group name of the ConfigurationPolicyGroup.
        :param pulumi.Input[str] vpn_server_configuration_name: The name of the VpnServerConfiguration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationPolicyGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        VpnServerConfigurationPolicyGroup Resource.

        :param str resource_name: The name of the resource.
        :param ConfigurationPolicyGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationPolicyGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_policy_group_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_members: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpnServerConfigurationPolicyGroupMemberArgs', 'VpnServerConfigurationPolicyGroupMemberArgsDict']]]]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vpn_server_configuration_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationPolicyGroupArgs.__new__(ConfigurationPolicyGroupArgs)

            __props__.__dict__["configuration_policy_group_name"] = configuration_policy_group_name
            __props__.__dict__["id"] = id
            __props__.__dict__["is_default"] = is_default
            __props__.__dict__["name"] = name
            __props__.__dict__["policy_members"] = policy_members
            __props__.__dict__["priority"] = priority
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if vpn_server_configuration_name is None and not opts.urn:
                raise TypeError("Missing required property 'vpn_server_configuration_name'")
            __props__.__dict__["vpn_server_configuration_name"] = vpn_server_configuration_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["p2_s_connection_configurations"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20210801:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20220101:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20220501:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20220701:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20220901:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20221101:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20230201:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20230401:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20230501:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20230601:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20230901:ConfigurationPolicyGroup"), pulumi.Alias(type_="azure-native:network/v20240101:ConfigurationPolicyGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConfigurationPolicyGroup, __self__).__init__(
            'azure-native:network/v20231101:ConfigurationPolicyGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfigurationPolicyGroup':
        """
        Get an existing ConfigurationPolicyGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigurationPolicyGroupArgs.__new__(ConfigurationPolicyGroupArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["is_default"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["p2_s_connection_configurations"] = None
        __props__.__dict__["policy_members"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return ConfigurationPolicyGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[Optional[bool]]:
        """
        Shows if this is a Default VpnServerConfigurationPolicyGroup or not.
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="p2SConnectionConfigurations")
    def p2_s_connection_configurations(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        List of references to P2SConnectionConfigurations.
        """
        return pulumi.get(self, "p2_s_connection_configurations")

    @property
    @pulumi.getter(name="policyMembers")
    def policy_members(self) -> pulumi.Output[Optional[Sequence['outputs.VpnServerConfigurationPolicyGroupMemberResponse']]]:
        """
        Multiple PolicyMembers for VpnServerConfigurationPolicyGroup.
        """
        return pulumi.get(self, "policy_members")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Priority for VpnServerConfigurationPolicyGroup.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the VpnServerConfigurationPolicyGroup resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

