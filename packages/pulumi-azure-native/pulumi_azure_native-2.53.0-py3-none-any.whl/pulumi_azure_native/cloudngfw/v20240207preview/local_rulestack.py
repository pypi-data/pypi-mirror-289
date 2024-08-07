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

__all__ = ['LocalRulestackArgs', 'LocalRulestack']

@pulumi.input_type
class LocalRulestackArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 associated_subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_mode: Optional[pulumi.Input[Union[str, 'DefaultMode']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs']] = None,
                 local_rulestack_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 min_app_id_version: Optional[pulumi.Input[str]] = None,
                 pan_etag: Optional[pulumi.Input[str]] = None,
                 pan_location: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[Union[str, 'ScopeType']]] = None,
                 security_services: Optional[pulumi.Input['SecurityServicesArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LocalRulestack resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_subscriptions: subscription scope of global rulestack
        :param pulumi.Input[Union[str, 'DefaultMode']] default_mode: Mode for default rules creation
        :param pulumi.Input[str] description: rulestack description
        :param pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs'] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[str] local_rulestack_name: LocalRulestack resource name
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] min_app_id_version: minimum version
        :param pulumi.Input[str] pan_etag: PanEtag info
        :param pulumi.Input[str] pan_location: Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks
        :param pulumi.Input[Union[str, 'ScopeType']] scope: Rulestack Type
        :param pulumi.Input['SecurityServicesArgs'] security_services: Security Profile
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if associated_subscriptions is not None:
            pulumi.set(__self__, "associated_subscriptions", associated_subscriptions)
        if default_mode is not None:
            pulumi.set(__self__, "default_mode", default_mode)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if local_rulestack_name is not None:
            pulumi.set(__self__, "local_rulestack_name", local_rulestack_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if min_app_id_version is not None:
            pulumi.set(__self__, "min_app_id_version", min_app_id_version)
        if pan_etag is not None:
            pulumi.set(__self__, "pan_etag", pan_etag)
        if pan_location is not None:
            pulumi.set(__self__, "pan_location", pan_location)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if security_services is not None:
            pulumi.set(__self__, "security_services", security_services)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="associatedSubscriptions")
    def associated_subscriptions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        subscription scope of global rulestack
        """
        return pulumi.get(self, "associated_subscriptions")

    @associated_subscriptions.setter
    def associated_subscriptions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "associated_subscriptions", value)

    @property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[pulumi.Input[Union[str, 'DefaultMode']]]:
        """
        Mode for default rules creation
        """
        return pulumi.get(self, "default_mode")

    @default_mode.setter
    def default_mode(self, value: Optional[pulumi.Input[Union[str, 'DefaultMode']]]):
        pulumi.set(self, "default_mode", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        rulestack description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

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
    @pulumi.getter(name="localRulestackName")
    def local_rulestack_name(self) -> Optional[pulumi.Input[str]]:
        """
        LocalRulestack resource name
        """
        return pulumi.get(self, "local_rulestack_name")

    @local_rulestack_name.setter
    def local_rulestack_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "local_rulestack_name", value)

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
    @pulumi.getter(name="minAppIdVersion")
    def min_app_id_version(self) -> Optional[pulumi.Input[str]]:
        """
        minimum version
        """
        return pulumi.get(self, "min_app_id_version")

    @min_app_id_version.setter
    def min_app_id_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "min_app_id_version", value)

    @property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> Optional[pulumi.Input[str]]:
        """
        PanEtag info
        """
        return pulumi.get(self, "pan_etag")

    @pan_etag.setter
    def pan_etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pan_etag", value)

    @property
    @pulumi.getter(name="panLocation")
    def pan_location(self) -> Optional[pulumi.Input[str]]:
        """
        Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks
        """
        return pulumi.get(self, "pan_location")

    @pan_location.setter
    def pan_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pan_location", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[Union[str, 'ScopeType']]]:
        """
        Rulestack Type
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[Union[str, 'ScopeType']]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="securityServices")
    def security_services(self) -> Optional[pulumi.Input['SecurityServicesArgs']]:
        """
        Security Profile
        """
        return pulumi.get(self, "security_services")

    @security_services.setter
    def security_services(self, value: Optional[pulumi.Input['SecurityServicesArgs']]):
        pulumi.set(self, "security_services", value)

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


class LocalRulestack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_mode: Optional[pulumi.Input[Union[str, 'DefaultMode']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['AzureResourceManagerManagedIdentityPropertiesArgs', 'AzureResourceManagerManagedIdentityPropertiesArgsDict']]] = None,
                 local_rulestack_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 min_app_id_version: Optional[pulumi.Input[str]] = None,
                 pan_etag: Optional[pulumi.Input[str]] = None,
                 pan_location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[Union[str, 'ScopeType']]] = None,
                 security_services: Optional[pulumi.Input[Union['SecurityServicesArgs', 'SecurityServicesArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        PaloAltoNetworks LocalRulestack

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_subscriptions: subscription scope of global rulestack
        :param pulumi.Input[Union[str, 'DefaultMode']] default_mode: Mode for default rules creation
        :param pulumi.Input[str] description: rulestack description
        :param pulumi.Input[Union['AzureResourceManagerManagedIdentityPropertiesArgs', 'AzureResourceManagerManagedIdentityPropertiesArgsDict']] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[str] local_rulestack_name: LocalRulestack resource name
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] min_app_id_version: minimum version
        :param pulumi.Input[str] pan_etag: PanEtag info
        :param pulumi.Input[str] pan_location: Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'ScopeType']] scope: Rulestack Type
        :param pulumi.Input[Union['SecurityServicesArgs', 'SecurityServicesArgsDict']] security_services: Security Profile
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocalRulestackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        PaloAltoNetworks LocalRulestack

        :param str resource_name: The name of the resource.
        :param LocalRulestackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocalRulestackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_mode: Optional[pulumi.Input[Union[str, 'DefaultMode']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['AzureResourceManagerManagedIdentityPropertiesArgs', 'AzureResourceManagerManagedIdentityPropertiesArgsDict']]] = None,
                 local_rulestack_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 min_app_id_version: Optional[pulumi.Input[str]] = None,
                 pan_etag: Optional[pulumi.Input[str]] = None,
                 pan_location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[Union[str, 'ScopeType']]] = None,
                 security_services: Optional[pulumi.Input[Union['SecurityServicesArgs', 'SecurityServicesArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocalRulestackArgs.__new__(LocalRulestackArgs)

            __props__.__dict__["associated_subscriptions"] = associated_subscriptions
            __props__.__dict__["default_mode"] = default_mode
            __props__.__dict__["description"] = description
            __props__.__dict__["identity"] = identity
            __props__.__dict__["local_rulestack_name"] = local_rulestack_name
            __props__.__dict__["location"] = location
            __props__.__dict__["min_app_id_version"] = min_app_id_version
            __props__.__dict__["pan_etag"] = pan_etag
            __props__.__dict__["pan_location"] = pan_location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scope"] = scope
            __props__.__dict__["security_services"] = security_services
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cloudngfw:LocalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829:LocalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829preview:LocalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20230901:LocalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20230901preview:LocalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20231010preview:LocalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20240119preview:LocalRulestack")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LocalRulestack, __self__).__init__(
            'azure-native:cloudngfw/v20240207preview:LocalRulestack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocalRulestack':
        """
        Get an existing LocalRulestack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocalRulestackArgs.__new__(LocalRulestackArgs)

        __props__.__dict__["associated_subscriptions"] = None
        __props__.__dict__["default_mode"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["min_app_id_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pan_etag"] = None
        __props__.__dict__["pan_location"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["security_services"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return LocalRulestack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedSubscriptions")
    def associated_subscriptions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        subscription scope of global rulestack
        """
        return pulumi.get(self, "associated_subscriptions")

    @property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Mode for default rules creation
        """
        return pulumi.get(self, "default_mode")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        rulestack description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.AzureResourceManagerManagedIdentityPropertiesResponse']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minAppIdVersion")
    def min_app_id_version(self) -> pulumi.Output[Optional[str]]:
        """
        minimum version
        """
        return pulumi.get(self, "min_app_id_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> pulumi.Output[Optional[str]]:
        """
        PanEtag info
        """
        return pulumi.get(self, "pan_etag")

    @property
    @pulumi.getter(name="panLocation")
    def pan_location(self) -> pulumi.Output[Optional[str]]:
        """
        Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks
        """
        return pulumi.get(self, "pan_location")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        Rulestack Type
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="securityServices")
    def security_services(self) -> pulumi.Output[Optional['outputs.SecurityServicesResponse']]:
        """
        Security Profile
        """
        return pulumi.get(self, "security_services")

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

