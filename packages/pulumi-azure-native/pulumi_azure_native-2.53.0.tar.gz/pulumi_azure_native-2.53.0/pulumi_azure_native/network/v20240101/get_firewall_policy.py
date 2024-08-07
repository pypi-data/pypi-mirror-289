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
    def __init__(__self__, base_policy=None, child_policies=None, dns_settings=None, etag=None, explicit_proxy=None, firewalls=None, id=None, identity=None, insights=None, intrusion_detection=None, location=None, name=None, provisioning_state=None, rule_collection_groups=None, size=None, sku=None, snat=None, sql=None, tags=None, threat_intel_mode=None, threat_intel_whitelist=None, transport_security=None, type=None):
        if base_policy and not isinstance(base_policy, dict):
            raise TypeError("Expected argument 'base_policy' to be a dict")
        pulumi.set(__self__, "base_policy", base_policy)
        if child_policies and not isinstance(child_policies, list):
            raise TypeError("Expected argument 'child_policies' to be a list")
        pulumi.set(__self__, "child_policies", child_policies)
        if dns_settings and not isinstance(dns_settings, dict):
            raise TypeError("Expected argument 'dns_settings' to be a dict")
        pulumi.set(__self__, "dns_settings", dns_settings)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if explicit_proxy and not isinstance(explicit_proxy, dict):
            raise TypeError("Expected argument 'explicit_proxy' to be a dict")
        pulumi.set(__self__, "explicit_proxy", explicit_proxy)
        if firewalls and not isinstance(firewalls, list):
            raise TypeError("Expected argument 'firewalls' to be a list")
        pulumi.set(__self__, "firewalls", firewalls)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if insights and not isinstance(insights, dict):
            raise TypeError("Expected argument 'insights' to be a dict")
        pulumi.set(__self__, "insights", insights)
        if intrusion_detection and not isinstance(intrusion_detection, dict):
            raise TypeError("Expected argument 'intrusion_detection' to be a dict")
        pulumi.set(__self__, "intrusion_detection", intrusion_detection)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rule_collection_groups and not isinstance(rule_collection_groups, list):
            raise TypeError("Expected argument 'rule_collection_groups' to be a list")
        pulumi.set(__self__, "rule_collection_groups", rule_collection_groups)
        if size and not isinstance(size, str):
            raise TypeError("Expected argument 'size' to be a str")
        pulumi.set(__self__, "size", size)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if snat and not isinstance(snat, dict):
            raise TypeError("Expected argument 'snat' to be a dict")
        pulumi.set(__self__, "snat", snat)
        if sql and not isinstance(sql, dict):
            raise TypeError("Expected argument 'sql' to be a dict")
        pulumi.set(__self__, "sql", sql)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if threat_intel_mode and not isinstance(threat_intel_mode, str):
            raise TypeError("Expected argument 'threat_intel_mode' to be a str")
        pulumi.set(__self__, "threat_intel_mode", threat_intel_mode)
        if threat_intel_whitelist and not isinstance(threat_intel_whitelist, dict):
            raise TypeError("Expected argument 'threat_intel_whitelist' to be a dict")
        pulumi.set(__self__, "threat_intel_whitelist", threat_intel_whitelist)
        if transport_security and not isinstance(transport_security, dict):
            raise TypeError("Expected argument 'transport_security' to be a dict")
        pulumi.set(__self__, "transport_security", transport_security)
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
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional['outputs.DnsSettingsResponse']:
        """
        DNS Proxy Settings definition.
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="explicitProxy")
    def explicit_proxy(self) -> Optional['outputs.ExplicitProxyResponse']:
        """
        Explicit Proxy Settings definition.
        """
        return pulumi.get(self, "explicit_proxy")

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
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        The identity of the firewall policy.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def insights(self) -> Optional['outputs.FirewallPolicyInsightsResponse']:
        """
        Insights on Firewall Policy.
        """
        return pulumi.get(self, "insights")

    @property
    @pulumi.getter(name="intrusionDetection")
    def intrusion_detection(self) -> Optional['outputs.FirewallPolicyIntrusionDetectionResponse']:
        """
        The configuration for Intrusion detection.
        """
        return pulumi.get(self, "intrusion_detection")

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
    @pulumi.getter(name="ruleCollectionGroups")
    def rule_collection_groups(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to FirewallPolicyRuleCollectionGroups.
        """
        return pulumi.get(self, "rule_collection_groups")

    @property
    @pulumi.getter
    def size(self) -> str:
        """
        A read-only string that represents the size of the FirewallPolicyPropertiesFormat in MB. (ex 0.5MB)
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.FirewallPolicySkuResponse']:
        """
        The Firewall Policy SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def snat(self) -> Optional['outputs.FirewallPolicySNATResponse']:
        """
        The private IP addresses/IP ranges to which traffic will not be SNAT.
        """
        return pulumi.get(self, "snat")

    @property
    @pulumi.getter
    def sql(self) -> Optional['outputs.FirewallPolicySQLResponse']:
        """
        SQL Settings definition.
        """
        return pulumi.get(self, "sql")

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
    @pulumi.getter(name="transportSecurity")
    def transport_security(self) -> Optional['outputs.FirewallPolicyTransportSecurityResponse']:
        """
        TLS Configuration definition.
        """
        return pulumi.get(self, "transport_security")

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
            dns_settings=self.dns_settings,
            etag=self.etag,
            explicit_proxy=self.explicit_proxy,
            firewalls=self.firewalls,
            id=self.id,
            identity=self.identity,
            insights=self.insights,
            intrusion_detection=self.intrusion_detection,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            rule_collection_groups=self.rule_collection_groups,
            size=self.size,
            sku=self.sku,
            snat=self.snat,
            sql=self.sql,
            tags=self.tags,
            threat_intel_mode=self.threat_intel_mode,
            threat_intel_whitelist=self.threat_intel_whitelist,
            transport_security=self.transport_security,
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
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20240101:getFirewallPolicy', __args__, opts=opts, typ=GetFirewallPolicyResult).value

    return AwaitableGetFirewallPolicyResult(
        base_policy=pulumi.get(__ret__, 'base_policy'),
        child_policies=pulumi.get(__ret__, 'child_policies'),
        dns_settings=pulumi.get(__ret__, 'dns_settings'),
        etag=pulumi.get(__ret__, 'etag'),
        explicit_proxy=pulumi.get(__ret__, 'explicit_proxy'),
        firewalls=pulumi.get(__ret__, 'firewalls'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        insights=pulumi.get(__ret__, 'insights'),
        intrusion_detection=pulumi.get(__ret__, 'intrusion_detection'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rule_collection_groups=pulumi.get(__ret__, 'rule_collection_groups'),
        size=pulumi.get(__ret__, 'size'),
        sku=pulumi.get(__ret__, 'sku'),
        snat=pulumi.get(__ret__, 'snat'),
        sql=pulumi.get(__ret__, 'sql'),
        tags=pulumi.get(__ret__, 'tags'),
        threat_intel_mode=pulumi.get(__ret__, 'threat_intel_mode'),
        threat_intel_whitelist=pulumi.get(__ret__, 'threat_intel_whitelist'),
        transport_security=pulumi.get(__ret__, 'transport_security'),
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
