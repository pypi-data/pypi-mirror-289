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
    'GetFirewallPolicyResult',
    'AwaitableGetFirewallPolicyResult',
    'get_firewall_policy',
    'get_firewall_policy_output',
]

@pulumi.output_type
class GetFirewallPolicyResult:
    """
    FirewallPolicy Resource.
    """
    def __init__(__self__, base_policy=None, child_policies=None, etag=None, firewalls=None, id=None, location=None, name=None, provisioning_state=None, rule_groups=None, tags=None, threat_intel_mode=None, threat_intel_whitelist=None, type=None):
        if base_policy and not isinstance(base_policy, dict):
            raise TypeError("Expected argument 'base_policy' to be a dict")
        pulumi.set(__self__, "base_policy", base_policy)
        if child_policies and not isinstance(child_policies, list):
            raise TypeError("Expected argument 'child_policies' to be a list")
        pulumi.set(__self__, "child_policies", child_policies)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if firewalls and not isinstance(firewalls, list):
            raise TypeError("Expected argument 'firewalls' to be a list")
        pulumi.set(__self__, "firewalls", firewalls)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rule_groups and not isinstance(rule_groups, list):
            raise TypeError("Expected argument 'rule_groups' to be a list")
        pulumi.set(__self__, "rule_groups", rule_groups)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if threat_intel_mode and not isinstance(threat_intel_mode, str):
            raise TypeError("Expected argument 'threat_intel_mode' to be a str")
        pulumi.set(__self__, "threat_intel_mode", threat_intel_mode)
        if threat_intel_whitelist and not isinstance(threat_intel_whitelist, dict):
            raise TypeError("Expected argument 'threat_intel_whitelist' to be a dict")
        pulumi.set(__self__, "threat_intel_whitelist", threat_intel_whitelist)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="basePolicy")
    def base_policy(self) -> Optional['outputs.SubResourceResponse']:
        """
        The parent firewall policy from which rules are inherited.
        """
        return pulumi.get(self, "base_policy")

    @property
    @pulumi.getter(name="childPolicies")
    def child_policies(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to Child Firewall Policies.
        """
        return pulumi.get(self, "child_policies")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def firewalls(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to Azure Firewalls that this Firewall Policy is associated with.
        """
        return pulumi.get(self, "firewalls")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the firewall policy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleGroups")
    def rule_groups(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to FirewallPolicyRuleGroups.
        """
        return pulumi.get(self, "rule_groups")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> Optional[str]:
        """
        The operation mode for Threat Intelligence.
        """
        return pulumi.get(self, "threat_intel_mode")

    @property
    @pulumi.getter(name="threatIntelWhitelist")
    def threat_intel_whitelist(self) -> Optional['outputs.FirewallPolicyThreatIntelWhitelistResponse']:
        """
        ThreatIntel Whitelist for Firewall Policy.
        """
        return pulumi.get(self, "threat_intel_whitelist")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetFirewallPolicyResult(GetFirewallPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallPolicyResult(
            base_policy=self.base_policy,
            child_policies=self.child_policies,
            etag=self.etag,
            firewalls=self.firewalls,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            rule_groups=self.rule_groups,
            tags=self.tags,
            threat_intel_mode=self.threat_intel_mode,
            threat_intel_whitelist=self.threat_intel_whitelist,
            type=self.type)


def get_firewall_policy(expand: Optional[str] = None,
                        firewall_policy_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallPolicyResult:
    """
    Gets the specified Firewall Policy.


    :param str expand: Expands referenced resources.
    :param str firewall_policy_name: The name of the Firewall Policy.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['firewallPolicyName'] = firewall_policy_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20200401:getFirewallPolicy', __args__, opts=opts, typ=GetFirewallPolicyResult).value

    return AwaitableGetFirewallPolicyResult(
        base_policy=pulumi.get(__ret__, 'base_policy'),
        child_policies=pulumi.get(__ret__, 'child_policies'),
        etag=pulumi.get(__ret__, 'etag'),
        firewalls=pulumi.get(__ret__, 'firewalls'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rule_groups=pulumi.get(__ret__, 'rule_groups'),
        tags=pulumi.get(__ret__, 'tags'),
        threat_intel_mode=pulumi.get(__ret__, 'threat_intel_mode'),
        threat_intel_whitelist=pulumi.get(__ret__, 'threat_intel_whitelist'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_firewall_policy)
def get_firewall_policy_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                               firewall_policy_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallPolicyResult]:
    """
    Gets the specified Firewall Policy.


    :param str expand: Expands referenced resources.
    :param str firewall_policy_name: The name of the Firewall Policy.
    :param str resource_group_name: The name of the resource group.
    """
    ...
