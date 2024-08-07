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

__all__ = [
    'GetIpFirewallRuleResult',
    'AwaitableGetIpFirewallRuleResult',
    'get_ip_firewall_rule',
    'get_ip_firewall_rule_output',
]

@pulumi.output_type
class GetIpFirewallRuleResult:
    """
    IP firewall rule
    """
    def __init__(__self__, end_ip_address=None, id=None, name=None, provisioning_state=None, start_ip_address=None, type=None):
        if end_ip_address and not isinstance(end_ip_address, str):
            raise TypeError("Expected argument 'end_ip_address' to be a str")
        pulumi.set(__self__, "end_ip_address", end_ip_address)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if start_ip_address and not isinstance(start_ip_address, str):
            raise TypeError("Expected argument 'start_ip_address' to be a str")
        pulumi.set(__self__, "start_ip_address", start_ip_address)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> Optional[str]:
        """
        The end IP address of the firewall rule. Must be IPv4 format. Must be greater than or equal to startIpAddress
        """
        return pulumi.get(self, "end_ip_address")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Resource provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> Optional[str]:
        """
        The start IP address of the firewall rule. Must be IPv4 format
        """
        return pulumi.get(self, "start_ip_address")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetIpFirewallRuleResult(GetIpFirewallRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpFirewallRuleResult(
            end_ip_address=self.end_ip_address,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            start_ip_address=self.start_ip_address,
            type=self.type)


def get_ip_firewall_rule(resource_group_name: Optional[str] = None,
                         rule_name: Optional[str] = None,
                         workspace_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpFirewallRuleResult:
    """
    Get a firewall rule


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str rule_name: The IP firewall rule name
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleName'] = rule_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:synapse/v20210601preview:getIpFirewallRule', __args__, opts=opts, typ=GetIpFirewallRuleResult).value

    return AwaitableGetIpFirewallRuleResult(
        end_ip_address=pulumi.get(__ret__, 'end_ip_address'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        start_ip_address=pulumi.get(__ret__, 'start_ip_address'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_ip_firewall_rule)
def get_ip_firewall_rule_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                rule_name: Optional[pulumi.Input[str]] = None,
                                workspace_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIpFirewallRuleResult]:
    """
    Get a firewall rule


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str rule_name: The IP firewall rule name
    :param str workspace_name: The name of the workspace.
    """
    ...
