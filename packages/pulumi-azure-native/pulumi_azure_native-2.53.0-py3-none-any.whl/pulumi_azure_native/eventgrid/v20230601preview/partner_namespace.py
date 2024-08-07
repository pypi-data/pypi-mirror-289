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

__all__ = ['PartnerNamespaceArgs', 'PartnerNamespace']

@pulumi.input_type
class PartnerNamespaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version_allowed: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 partner_namespace_name: Optional[pulumi.Input[str]] = None,
                 partner_registration_fully_qualified_id: Optional[pulumi.Input[str]] = None,
                 partner_topic_routing_mode: Optional[pulumi.Input[Union[str, 'PartnerTopicRoutingMode']]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PartnerNamespace resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[bool] disable_local_auth: This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the partner namespace.
        :param pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]] inbound_ip_rules: This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[Union[str, 'TlsVersion']] minimum_tls_version_allowed: Minimum TLS version of the publisher allowed to publish to this partner namespace
        :param pulumi.Input[str] partner_namespace_name: Name of the partner namespace.
        :param pulumi.Input[str] partner_registration_fully_qualified_id: The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format:
               /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}.
        :param pulumi.Input[Union[str, 'PartnerTopicRoutingMode']] partner_topic_routing_mode: This determines if events published to this partner namespace should use the source attribute in the event payload
               or use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled.
               You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PartnerNamespaceProperties.InboundIpRules" />
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if disable_local_auth is None:
            disable_local_auth = False
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if inbound_ip_rules is not None:
            pulumi.set(__self__, "inbound_ip_rules", inbound_ip_rules)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if minimum_tls_version_allowed is not None:
            pulumi.set(__self__, "minimum_tls_version_allowed", minimum_tls_version_allowed)
        if partner_namespace_name is not None:
            pulumi.set(__self__, "partner_namespace_name", partner_namespace_name)
        if partner_registration_fully_qualified_id is not None:
            pulumi.set(__self__, "partner_registration_fully_qualified_id", partner_registration_fully_qualified_id)
        if partner_topic_routing_mode is None:
            partner_topic_routing_mode = 'SourceEventAttribute'
        if partner_topic_routing_mode is not None:
            pulumi.set(__self__, "partner_topic_routing_mode", partner_topic_routing_mode)
        if public_network_access is None:
            public_network_access = 'Enabled'
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the partner namespace.
        """
        return pulumi.get(self, "disable_local_auth")

    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_local_auth", value)

    @property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]]]:
        """
        This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        """
        return pulumi.get(self, "inbound_ip_rules")

    @inbound_ip_rules.setter
    def inbound_ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]]]):
        pulumi.set(self, "inbound_ip_rules", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> Optional[pulumi.Input[Union[str, 'TlsVersion']]]:
        """
        Minimum TLS version of the publisher allowed to publish to this partner namespace
        """
        return pulumi.get(self, "minimum_tls_version_allowed")

    @minimum_tls_version_allowed.setter
    def minimum_tls_version_allowed(self, value: Optional[pulumi.Input[Union[str, 'TlsVersion']]]):
        pulumi.set(self, "minimum_tls_version_allowed", value)

    @property
    @pulumi.getter(name="partnerNamespaceName")
    def partner_namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the partner namespace.
        """
        return pulumi.get(self, "partner_namespace_name")

    @partner_namespace_name.setter
    def partner_namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_namespace_name", value)

    @property
    @pulumi.getter(name="partnerRegistrationFullyQualifiedId")
    def partner_registration_fully_qualified_id(self) -> Optional[pulumi.Input[str]]:
        """
        The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format:
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}.
        """
        return pulumi.get(self, "partner_registration_fully_qualified_id")

    @partner_registration_fully_qualified_id.setter
    def partner_registration_fully_qualified_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_registration_fully_qualified_id", value)

    @property
    @pulumi.getter(name="partnerTopicRoutingMode")
    def partner_topic_routing_mode(self) -> Optional[pulumi.Input[Union[str, 'PartnerTopicRoutingMode']]]:
        """
        This determines if events published to this partner namespace should use the source attribute in the event payload
        or use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic.
        """
        return pulumi.get(self, "partner_topic_routing_mode")

    @partner_topic_routing_mode.setter
    def partner_topic_routing_mode(self, value: Optional[pulumi.Input[Union[str, 'PartnerTopicRoutingMode']]]):
        pulumi.set(self, "partner_topic_routing_mode", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PartnerNamespaceProperties.InboundIpRules" />
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class PartnerNamespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['InboundIpRuleArgs', 'InboundIpRuleArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version_allowed: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 partner_namespace_name: Optional[pulumi.Input[str]] = None,
                 partner_registration_fully_qualified_id: Optional[pulumi.Input[str]] = None,
                 partner_topic_routing_mode: Optional[pulumi.Input[Union[str, 'PartnerTopicRoutingMode']]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        EventGrid Partner Namespace.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_local_auth: This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the partner namespace.
        :param pulumi.Input[Sequence[pulumi.Input[Union['InboundIpRuleArgs', 'InboundIpRuleArgsDict']]]] inbound_ip_rules: This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[Union[str, 'TlsVersion']] minimum_tls_version_allowed: Minimum TLS version of the publisher allowed to publish to this partner namespace
        :param pulumi.Input[str] partner_namespace_name: Name of the partner namespace.
        :param pulumi.Input[str] partner_registration_fully_qualified_id: The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format:
               /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}.
        :param pulumi.Input[Union[str, 'PartnerTopicRoutingMode']] partner_topic_routing_mode: This determines if events published to this partner namespace should use the source attribute in the event payload
               or use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled.
               You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PartnerNamespaceProperties.InboundIpRules" />
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PartnerNamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        EventGrid Partner Namespace.

        :param str resource_name: The name of the resource.
        :param PartnerNamespaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PartnerNamespaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['InboundIpRuleArgs', 'InboundIpRuleArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version_allowed: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 partner_namespace_name: Optional[pulumi.Input[str]] = None,
                 partner_registration_fully_qualified_id: Optional[pulumi.Input[str]] = None,
                 partner_topic_routing_mode: Optional[pulumi.Input[Union[str, 'PartnerTopicRoutingMode']]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PartnerNamespaceArgs.__new__(PartnerNamespaceArgs)

            if disable_local_auth is None:
                disable_local_auth = False
            __props__.__dict__["disable_local_auth"] = disable_local_auth
            __props__.__dict__["inbound_ip_rules"] = inbound_ip_rules
            __props__.__dict__["location"] = location
            __props__.__dict__["minimum_tls_version_allowed"] = minimum_tls_version_allowed
            __props__.__dict__["partner_namespace_name"] = partner_namespace_name
            __props__.__dict__["partner_registration_fully_qualified_id"] = partner_registration_fully_qualified_id
            if partner_topic_routing_mode is None:
                partner_topic_routing_mode = 'SourceEventAttribute'
            __props__.__dict__["partner_topic_routing_mode"] = partner_topic_routing_mode
            if public_network_access is None:
                public_network_access = 'Enabled'
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["endpoint"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid:PartnerNamespace"), pulumi.Alias(type_="azure-native:eventgrid/v20200401preview:PartnerNamespace"), pulumi.Alias(type_="azure-native:eventgrid/v20201015preview:PartnerNamespace"), pulumi.Alias(type_="azure-native:eventgrid/v20210601preview:PartnerNamespace"), pulumi.Alias(type_="azure-native:eventgrid/v20211015preview:PartnerNamespace"), pulumi.Alias(type_="azure-native:eventgrid/v20220615:PartnerNamespace"), pulumi.Alias(type_="azure-native:eventgrid/v20231215preview:PartnerNamespace"), pulumi.Alias(type_="azure-native:eventgrid/v20240601preview:PartnerNamespace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PartnerNamespace, __self__).__init__(
            'azure-native:eventgrid/v20230601preview:PartnerNamespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PartnerNamespace':
        """
        Get an existing PartnerNamespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PartnerNamespaceArgs.__new__(PartnerNamespaceArgs)

        __props__.__dict__["disable_local_auth"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["inbound_ip_rules"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["minimum_tls_version_allowed"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_registration_fully_qualified_id"] = None
        __props__.__dict__["partner_topic_routing_mode"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return PartnerNamespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the partner namespace.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        Endpoint for the partner namespace.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> pulumi.Output[Optional[Sequence['outputs.InboundIpRuleResponse']]]:
        """
        This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        """
        return pulumi.get(self, "inbound_ip_rules")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> pulumi.Output[Optional[str]]:
        """
        Minimum TLS version of the publisher allowed to publish to this partner namespace
        """
        return pulumi.get(self, "minimum_tls_version_allowed")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerRegistrationFullyQualifiedId")
    def partner_registration_fully_qualified_id(self) -> pulumi.Output[Optional[str]]:
        """
        The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format:
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}.
        """
        return pulumi.get(self, "partner_registration_fully_qualified_id")

    @property
    @pulumi.getter(name="partnerTopicRoutingMode")
    def partner_topic_routing_mode(self) -> pulumi.Output[Optional[str]]:
        """
        This determines if events published to this partner namespace should use the source attribute in the event payload
        or use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic.
        """
        return pulumi.get(self, "partner_topic_routing_mode")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the partner namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PartnerNamespaceProperties.InboundIpRules" />
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to Partner Namespace resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

