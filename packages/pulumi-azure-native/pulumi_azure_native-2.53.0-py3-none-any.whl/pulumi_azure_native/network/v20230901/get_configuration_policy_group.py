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

__all__ = [
    'GetConfigurationPolicyGroupResult',
    'AwaitableGetConfigurationPolicyGroupResult',
    'get_configuration_policy_group',
    'get_configuration_policy_group_output',
]

@pulumi.output_type
class GetConfigurationPolicyGroupResult:
    """
    VpnServerConfigurationPolicyGroup Resource.
    """
    def __init__(__self__, etag=None, id=None, is_default=None, name=None, p2_s_connection_configurations=None, policy_members=None, priority=None, provisioning_state=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_default and not isinstance(is_default, bool):
            raise TypeError("Expected argument 'is_default' to be a bool")
        pulumi.set(__self__, "is_default", is_default)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if p2_s_connection_configurations and not isinstance(p2_s_connection_configurations, list):
            raise TypeError("Expected argument 'p2_s_connection_configurations' to be a list")
        pulumi.set(__self__, "p2_s_connection_configurations", p2_s_connection_configurations)
        if policy_members and not isinstance(policy_members, list):
            raise TypeError("Expected argument 'policy_members' to be a list")
        pulumi.set(__self__, "policy_members", policy_members)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[bool]:
        """
        Shows if this is a Default VpnServerConfigurationPolicyGroup or not.
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="p2SConnectionConfigurations")
    def p2_s_connection_configurations(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to P2SConnectionConfigurations.
        """
        return pulumi.get(self, "p2_s_connection_configurations")

    @property
    @pulumi.getter(name="policyMembers")
    def policy_members(self) -> Optional[Sequence['outputs.VpnServerConfigurationPolicyGroupMemberResponse']]:
        """
        Multiple PolicyMembers for VpnServerConfigurationPolicyGroup.
        """
        return pulumi.get(self, "policy_members")

    @property
    @pulumi.getter
    def priority(self) -> Optional[int]:
        """
        Priority for VpnServerConfigurationPolicyGroup.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the VpnServerConfigurationPolicyGroup resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetConfigurationPolicyGroupResult(GetConfigurationPolicyGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationPolicyGroupResult(
            etag=self.etag,
            id=self.id,
            is_default=self.is_default,
            name=self.name,
            p2_s_connection_configurations=self.p2_s_connection_configurations,
            policy_members=self.policy_members,
            priority=self.priority,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_configuration_policy_group(configuration_policy_group_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   vpn_server_configuration_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationPolicyGroupResult:
    """
    Retrieves the details of a ConfigurationPolicyGroup.


    :param str configuration_policy_group_name: The name of the ConfigurationPolicyGroup being retrieved.
    :param str resource_group_name: The resource group name of the VpnServerConfiguration.
    :param str vpn_server_configuration_name: The name of the VpnServerConfiguration.
    """
    __args__ = dict()
    __args__['configurationPolicyGroupName'] = configuration_policy_group_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['vpnServerConfigurationName'] = vpn_server_configuration_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230901:getConfigurationPolicyGroup', __args__, opts=opts, typ=GetConfigurationPolicyGroupResult).value

    return AwaitableGetConfigurationPolicyGroupResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        is_default=pulumi.get(__ret__, 'is_default'),
        name=pulumi.get(__ret__, 'name'),
        p2_s_connection_configurations=pulumi.get(__ret__, 'p2_s_connection_configurations'),
        policy_members=pulumi.get(__ret__, 'policy_members'),
        priority=pulumi.get(__ret__, 'priority'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_configuration_policy_group)
def get_configuration_policy_group_output(configuration_policy_group_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          vpn_server_configuration_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationPolicyGroupResult]:
    """
    Retrieves the details of a ConfigurationPolicyGroup.


    :param str configuration_policy_group_name: The name of the ConfigurationPolicyGroup being retrieved.
    :param str resource_group_name: The resource group name of the VpnServerConfiguration.
    :param str vpn_server_configuration_name: The name of the VpnServerConfiguration.
    """
    ...
