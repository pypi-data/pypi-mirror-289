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

__all__ = ['FirewallArgs', 'Firewall']

@pulumi.input_type
class FirewallArgs:
    def __init__(__self__, *,
                 dns_settings: pulumi.Input['DNSSettingsArgs'],
                 marketplace_details: pulumi.Input['MarketplaceDetailsArgs'],
                 network_profile: pulumi.Input['NetworkProfileArgs'],
                 plan_data: pulumi.Input['PlanDataArgs'],
                 resource_group_name: pulumi.Input[str],
                 associated_rulestack: Optional[pulumi.Input['RulestackDetailsArgs']] = None,
                 firewall_name: Optional[pulumi.Input[str]] = None,
                 front_end_settings: Optional[pulumi.Input[Sequence[pulumi.Input['FrontendSettingArgs']]]] = None,
                 identity: Optional[pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs']] = None,
                 is_panorama_managed: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pan_etag: Optional[pulumi.Input[str]] = None,
                 panorama_config: Optional[pulumi.Input['PanoramaConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Firewall resource.
        :param pulumi.Input['DNSSettingsArgs'] dns_settings: DNS settings for Firewall
        :param pulumi.Input['MarketplaceDetailsArgs'] marketplace_details: Marketplace details
        :param pulumi.Input['NetworkProfileArgs'] network_profile: Network settings
        :param pulumi.Input['PlanDataArgs'] plan_data: Billing plan information.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['RulestackDetailsArgs'] associated_rulestack: Associated Rulestack
        :param pulumi.Input[str] firewall_name: Firewall resource name
        :param pulumi.Input[Sequence[pulumi.Input['FrontendSettingArgs']]] front_end_settings: Frontend settings for Firewall
        :param pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs'] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[Union[str, 'BooleanEnum']] is_panorama_managed: Panorama Managed: Default is False. Default will be CloudSec managed
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] pan_etag: panEtag info
        :param pulumi.Input['PanoramaConfigArgs'] panorama_config: Panorama Configuration
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "dns_settings", dns_settings)
        pulumi.set(__self__, "marketplace_details", marketplace_details)
        pulumi.set(__self__, "network_profile", network_profile)
        pulumi.set(__self__, "plan_data", plan_data)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if associated_rulestack is not None:
            pulumi.set(__self__, "associated_rulestack", associated_rulestack)
        if firewall_name is not None:
            pulumi.set(__self__, "firewall_name", firewall_name)
        if front_end_settings is not None:
            pulumi.set(__self__, "front_end_settings", front_end_settings)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if is_panorama_managed is not None:
            pulumi.set(__self__, "is_panorama_managed", is_panorama_managed)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if pan_etag is not None:
            pulumi.set(__self__, "pan_etag", pan_etag)
        if panorama_config is not None:
            pulumi.set(__self__, "panorama_config", panorama_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Input['DNSSettingsArgs']:
        """
        DNS settings for Firewall
        """
        return pulumi.get(self, "dns_settings")

    @dns_settings.setter
    def dns_settings(self, value: pulumi.Input['DNSSettingsArgs']):
        pulumi.set(self, "dns_settings", value)

    @property
    @pulumi.getter(name="marketplaceDetails")
    def marketplace_details(self) -> pulumi.Input['MarketplaceDetailsArgs']:
        """
        Marketplace details
        """
        return pulumi.get(self, "marketplace_details")

    @marketplace_details.setter
    def marketplace_details(self, value: pulumi.Input['MarketplaceDetailsArgs']):
        pulumi.set(self, "marketplace_details", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Input['NetworkProfileArgs']:
        """
        Network settings
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: pulumi.Input['NetworkProfileArgs']):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="planData")
    def plan_data(self) -> pulumi.Input['PlanDataArgs']:
        """
        Billing plan information.
        """
        return pulumi.get(self, "plan_data")

    @plan_data.setter
    def plan_data(self, value: pulumi.Input['PlanDataArgs']):
        pulumi.set(self, "plan_data", value)

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
    @pulumi.getter(name="associatedRulestack")
    def associated_rulestack(self) -> Optional[pulumi.Input['RulestackDetailsArgs']]:
        """
        Associated Rulestack
        """
        return pulumi.get(self, "associated_rulestack")

    @associated_rulestack.setter
    def associated_rulestack(self, value: Optional[pulumi.Input['RulestackDetailsArgs']]):
        pulumi.set(self, "associated_rulestack", value)

    @property
    @pulumi.getter(name="firewallName")
    def firewall_name(self) -> Optional[pulumi.Input[str]]:
        """
        Firewall resource name
        """
        return pulumi.get(self, "firewall_name")

    @firewall_name.setter
    def firewall_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "firewall_name", value)

    @property
    @pulumi.getter(name="frontEndSettings")
    def front_end_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FrontendSettingArgs']]]]:
        """
        Frontend settings for Firewall
        """
        return pulumi.get(self, "front_end_settings")

    @front_end_settings.setter
    def front_end_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FrontendSettingArgs']]]]):
        pulumi.set(self, "front_end_settings", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="isPanoramaManaged")
    def is_panorama_managed(self) -> Optional[pulumi.Input[Union[str, 'BooleanEnum']]]:
        """
        Panorama Managed: Default is False. Default will be CloudSec managed
        """
        return pulumi.get(self, "is_panorama_managed")

    @is_panorama_managed.setter
    def is_panorama_managed(self, value: Optional[pulumi.Input[Union[str, 'BooleanEnum']]]):
        pulumi.set(self, "is_panorama_managed", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> Optional[pulumi.Input[str]]:
        """
        panEtag info
        """
        return pulumi.get(self, "pan_etag")

    @pan_etag.setter
    def pan_etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pan_etag", value)

    @property
    @pulumi.getter(name="panoramaConfig")
    def panorama_config(self) -> Optional[pulumi.Input['PanoramaConfigArgs']]:
        """
        Panorama Configuration
        """
        return pulumi.get(self, "panorama_config")

    @panorama_config.setter
    def panorama_config(self, value: Optional[pulumi.Input['PanoramaConfigArgs']]):
        pulumi.set(self, "panorama_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Firewall(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_rulestack: Optional[pulumi.Input[Union['RulestackDetailsArgs', 'RulestackDetailsArgsDict']]] = None,
                 dns_settings: Optional[pulumi.Input[Union['DNSSettingsArgs', 'DNSSettingsArgsDict']]] = None,
                 firewall_name: Optional[pulumi.Input[str]] = None,
                 front_end_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union['FrontendSettingArgs', 'FrontendSettingArgsDict']]]]] = None,
                 identity: Optional[pulumi.Input[Union['AzureResourceManagerManagedIdentityPropertiesArgs', 'AzureResourceManagerManagedIdentityPropertiesArgsDict']]] = None,
                 is_panorama_managed: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 marketplace_details: Optional[pulumi.Input[Union['MarketplaceDetailsArgs', 'MarketplaceDetailsArgsDict']]] = None,
                 network_profile: Optional[pulumi.Input[Union['NetworkProfileArgs', 'NetworkProfileArgsDict']]] = None,
                 pan_etag: Optional[pulumi.Input[str]] = None,
                 panorama_config: Optional[pulumi.Input[Union['PanoramaConfigArgs', 'PanoramaConfigArgsDict']]] = None,
                 plan_data: Optional[pulumi.Input[Union['PlanDataArgs', 'PlanDataArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        PaloAltoNetworks Firewall

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['RulestackDetailsArgs', 'RulestackDetailsArgsDict']] associated_rulestack: Associated Rulestack
        :param pulumi.Input[Union['DNSSettingsArgs', 'DNSSettingsArgsDict']] dns_settings: DNS settings for Firewall
        :param pulumi.Input[str] firewall_name: Firewall resource name
        :param pulumi.Input[Sequence[pulumi.Input[Union['FrontendSettingArgs', 'FrontendSettingArgsDict']]]] front_end_settings: Frontend settings for Firewall
        :param pulumi.Input[Union['AzureResourceManagerManagedIdentityPropertiesArgs', 'AzureResourceManagerManagedIdentityPropertiesArgsDict']] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[Union[str, 'BooleanEnum']] is_panorama_managed: Panorama Managed: Default is False. Default will be CloudSec managed
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union['MarketplaceDetailsArgs', 'MarketplaceDetailsArgsDict']] marketplace_details: Marketplace details
        :param pulumi.Input[Union['NetworkProfileArgs', 'NetworkProfileArgsDict']] network_profile: Network settings
        :param pulumi.Input[str] pan_etag: panEtag info
        :param pulumi.Input[Union['PanoramaConfigArgs', 'PanoramaConfigArgsDict']] panorama_config: Panorama Configuration
        :param pulumi.Input[Union['PlanDataArgs', 'PlanDataArgsDict']] plan_data: Billing plan information.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        PaloAltoNetworks Firewall

        :param str resource_name: The name of the resource.
        :param FirewallArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_rulestack: Optional[pulumi.Input[Union['RulestackDetailsArgs', 'RulestackDetailsArgsDict']]] = None,
                 dns_settings: Optional[pulumi.Input[Union['DNSSettingsArgs', 'DNSSettingsArgsDict']]] = None,
                 firewall_name: Optional[pulumi.Input[str]] = None,
                 front_end_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union['FrontendSettingArgs', 'FrontendSettingArgsDict']]]]] = None,
                 identity: Optional[pulumi.Input[Union['AzureResourceManagerManagedIdentityPropertiesArgs', 'AzureResourceManagerManagedIdentityPropertiesArgsDict']]] = None,
                 is_panorama_managed: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 marketplace_details: Optional[pulumi.Input[Union['MarketplaceDetailsArgs', 'MarketplaceDetailsArgsDict']]] = None,
                 network_profile: Optional[pulumi.Input[Union['NetworkProfileArgs', 'NetworkProfileArgsDict']]] = None,
                 pan_etag: Optional[pulumi.Input[str]] = None,
                 panorama_config: Optional[pulumi.Input[Union['PanoramaConfigArgs', 'PanoramaConfigArgsDict']]] = None,
                 plan_data: Optional[pulumi.Input[Union['PlanDataArgs', 'PlanDataArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallArgs.__new__(FirewallArgs)

            __props__.__dict__["associated_rulestack"] = associated_rulestack
            if dns_settings is None and not opts.urn:
                raise TypeError("Missing required property 'dns_settings'")
            __props__.__dict__["dns_settings"] = dns_settings
            __props__.__dict__["firewall_name"] = firewall_name
            __props__.__dict__["front_end_settings"] = front_end_settings
            __props__.__dict__["identity"] = identity
            __props__.__dict__["is_panorama_managed"] = is_panorama_managed
            __props__.__dict__["location"] = location
            if marketplace_details is None and not opts.urn:
                raise TypeError("Missing required property 'marketplace_details'")
            __props__.__dict__["marketplace_details"] = marketplace_details
            if network_profile is None and not opts.urn:
                raise TypeError("Missing required property 'network_profile'")
            __props__.__dict__["network_profile"] = network_profile
            __props__.__dict__["pan_etag"] = pan_etag
            __props__.__dict__["panorama_config"] = panorama_config
            if plan_data is None and not opts.urn:
                raise TypeError("Missing required property 'plan_data'")
            __props__.__dict__["plan_data"] = plan_data
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cloudngfw:Firewall"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829:Firewall"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829preview:Firewall"), pulumi.Alias(type_="azure-native:cloudngfw/v20230901:Firewall"), pulumi.Alias(type_="azure-native:cloudngfw/v20231010preview:Firewall"), pulumi.Alias(type_="azure-native:cloudngfw/v20240119preview:Firewall"), pulumi.Alias(type_="azure-native:cloudngfw/v20240207preview:Firewall")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Firewall, __self__).__init__(
            'azure-native:cloudngfw/v20230901preview:Firewall',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Firewall':
        """
        Get an existing Firewall resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FirewallArgs.__new__(FirewallArgs)

        __props__.__dict__["associated_rulestack"] = None
        __props__.__dict__["dns_settings"] = None
        __props__.__dict__["front_end_settings"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["is_panorama_managed"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["marketplace_details"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["pan_etag"] = None
        __props__.__dict__["panorama_config"] = None
        __props__.__dict__["plan_data"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Firewall(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedRulestack")
    def associated_rulestack(self) -> pulumi.Output[Optional['outputs.RulestackDetailsResponse']]:
        """
        Associated Rulestack
        """
        return pulumi.get(self, "associated_rulestack")

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output['outputs.DNSSettingsResponse']:
        """
        DNS settings for Firewall
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter(name="frontEndSettings")
    def front_end_settings(self) -> pulumi.Output[Optional[Sequence['outputs.FrontendSettingResponse']]]:
        """
        Frontend settings for Firewall
        """
        return pulumi.get(self, "front_end_settings")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.AzureResourceManagerManagedIdentityPropertiesResponse']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="isPanoramaManaged")
    def is_panorama_managed(self) -> pulumi.Output[Optional[str]]:
        """
        Panorama Managed: Default is False. Default will be CloudSec managed
        """
        return pulumi.get(self, "is_panorama_managed")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="marketplaceDetails")
    def marketplace_details(self) -> pulumi.Output['outputs.MarketplaceDetailsResponse']:
        """
        Marketplace details
        """
        return pulumi.get(self, "marketplace_details")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output['outputs.NetworkProfileResponse']:
        """
        Network settings
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> pulumi.Output[Optional[str]]:
        """
        panEtag info
        """
        return pulumi.get(self, "pan_etag")

    @property
    @pulumi.getter(name="panoramaConfig")
    def panorama_config(self) -> pulumi.Output[Optional['outputs.PanoramaConfigResponse']]:
        """
        Panorama Configuration
        """
        return pulumi.get(self, "panorama_config")

    @property
    @pulumi.getter(name="planData")
    def plan_data(self) -> pulumi.Output['outputs.PlanDataResponse']:
        """
        Billing plan information.
        """
        return pulumi.get(self, "plan_data")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

