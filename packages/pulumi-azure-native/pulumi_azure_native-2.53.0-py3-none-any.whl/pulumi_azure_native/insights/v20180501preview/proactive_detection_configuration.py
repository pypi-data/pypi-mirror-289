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
from ._inputs import *

__all__ = ['ProactiveDetectionConfigurationArgs', 'ProactiveDetectionConfiguration']

@pulumi.input_type
class ProactiveDetectionConfigurationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 configuration_id: Optional[pulumi.Input[str]] = None,
                 custom_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rule_definitions: Optional[pulumi.Input['ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgs']] = None,
                 send_emails_to_subscription_owners: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ProactiveDetectionConfiguration resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name: The name of the Application Insights component resource.
        :param pulumi.Input[str] configuration_id: The ProactiveDetection configuration ID. This is unique within a Application Insights component.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_emails: Custom email addresses for this rule notifications
        :param pulumi.Input[bool] enabled: A flag that indicates whether this rule is enabled by the user
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] name: Azure resource name
        :param pulumi.Input['ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgs'] rule_definitions: Static definitions of the ProactiveDetection configuration rule (same values for all components).
        :param pulumi.Input[bool] send_emails_to_subscription_owners: A flag that indicated whether notifications on this rule should be sent to subscription owners
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if configuration_id is not None:
            pulumi.set(__self__, "configuration_id", configuration_id)
        if custom_emails is not None:
            pulumi.set(__self__, "custom_emails", custom_emails)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rule_definitions is not None:
            pulumi.set(__self__, "rule_definitions", rule_definitions)
        if send_emails_to_subscription_owners is not None:
            pulumi.set(__self__, "send_emails_to_subscription_owners", send_emails_to_subscription_owners)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the Application Insights component resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ProactiveDetection configuration ID. This is unique within a Application Insights component.
        """
        return pulumi.get(self, "configuration_id")

    @configuration_id.setter
    def configuration_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_id", value)

    @property
    @pulumi.getter(name="customEmails")
    def custom_emails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Custom email addresses for this rule notifications
        """
        return pulumi.get(self, "custom_emails")

    @custom_emails.setter
    def custom_emails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "custom_emails", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag that indicates whether this rule is enabled by the user
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ruleDefinitions")
    def rule_definitions(self) -> Optional[pulumi.Input['ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgs']]:
        """
        Static definitions of the ProactiveDetection configuration rule (same values for all components).
        """
        return pulumi.get(self, "rule_definitions")

    @rule_definitions.setter
    def rule_definitions(self, value: Optional[pulumi.Input['ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgs']]):
        pulumi.set(self, "rule_definitions", value)

    @property
    @pulumi.getter(name="sendEmailsToSubscriptionOwners")
    def send_emails_to_subscription_owners(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag that indicated whether notifications on this rule should be sent to subscription owners
        """
        return pulumi.get(self, "send_emails_to_subscription_owners")

    @send_emails_to_subscription_owners.setter
    def send_emails_to_subscription_owners(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_emails_to_subscription_owners", value)


class ProactiveDetectionConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_id: Optional[pulumi.Input[str]] = None,
                 custom_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 rule_definitions: Optional[pulumi.Input[Union['ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgs', 'ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgsDict']]] = None,
                 send_emails_to_subscription_owners: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        A ProactiveDetection configuration definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] configuration_id: The ProactiveDetection configuration ID. This is unique within a Application Insights component.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_emails: Custom email addresses for this rule notifications
        :param pulumi.Input[bool] enabled: A flag that indicates whether this rule is enabled by the user
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] name: Azure resource name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the Application Insights component resource.
        :param pulumi.Input[Union['ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgs', 'ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgsDict']] rule_definitions: Static definitions of the ProactiveDetection configuration rule (same values for all components).
        :param pulumi.Input[bool] send_emails_to_subscription_owners: A flag that indicated whether notifications on this rule should be sent to subscription owners
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProactiveDetectionConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A ProactiveDetection configuration definition.

        :param str resource_name: The name of the resource.
        :param ProactiveDetectionConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProactiveDetectionConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_id: Optional[pulumi.Input[str]] = None,
                 custom_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 rule_definitions: Optional[pulumi.Input[Union['ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgs', 'ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgsDict']]] = None,
                 send_emails_to_subscription_owners: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProactiveDetectionConfigurationArgs.__new__(ProactiveDetectionConfigurationArgs)

            __props__.__dict__["configuration_id"] = configuration_id
            __props__.__dict__["custom_emails"] = custom_emails
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["rule_definitions"] = rule_definitions
            __props__.__dict__["send_emails_to_subscription_owners"] = send_emails_to_subscription_owners
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights:ProactiveDetectionConfiguration"), pulumi.Alias(type_="azure-native:insights/v20150501:ProactiveDetectionConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ProactiveDetectionConfiguration, __self__).__init__(
            'azure-native:insights/v20180501preview:ProactiveDetectionConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProactiveDetectionConfiguration':
        """
        Get an existing ProactiveDetectionConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProactiveDetectionConfigurationArgs.__new__(ProactiveDetectionConfigurationArgs)

        __props__.__dict__["custom_emails"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["rule_definitions"] = None
        __props__.__dict__["send_emails_to_subscription_owners"] = None
        __props__.__dict__["type"] = None
        return ProactiveDetectionConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customEmails")
    def custom_emails(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Custom email addresses for this rule notifications
        """
        return pulumi.get(self, "custom_emails")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        A flag that indicates whether this rule is enabled by the user
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        The last time this rule was updated
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The rule name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ruleDefinitions")
    def rule_definitions(self) -> pulumi.Output[Optional['outputs.ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesResponseRuleDefinitions']]:
        """
        Static definitions of the ProactiveDetection configuration rule (same values for all components).
        """
        return pulumi.get(self, "rule_definitions")

    @property
    @pulumi.getter(name="sendEmailsToSubscriptionOwners")
    def send_emails_to_subscription_owners(self) -> pulumi.Output[Optional[bool]]:
        """
        A flag that indicated whether notifications on this rule should be sent to subscription owners
        """
        return pulumi.get(self, "send_emails_to_subscription_owners")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

