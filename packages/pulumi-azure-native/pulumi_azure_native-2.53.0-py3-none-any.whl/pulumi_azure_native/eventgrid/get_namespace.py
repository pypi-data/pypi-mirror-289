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

__all__ = [
    'GetNamespaceResult',
    'AwaitableGetNamespaceResult',
    'get_namespace',
    'get_namespace_output',
]

@pulumi.output_type
class GetNamespaceResult:
    """
    Namespace resource.
    """
    def __init__(__self__, id=None, identity=None, inbound_ip_rules=None, is_zone_redundant=None, location=None, minimum_tls_version_allowed=None, name=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, sku=None, system_data=None, tags=None, topic_spaces_configuration=None, topics_configuration=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if inbound_ip_rules and not isinstance(inbound_ip_rules, list):
            raise TypeError("Expected argument 'inbound_ip_rules' to be a list")
        pulumi.set(__self__, "inbound_ip_rules", inbound_ip_rules)
        if is_zone_redundant and not isinstance(is_zone_redundant, bool):
            raise TypeError("Expected argument 'is_zone_redundant' to be a bool")
        pulumi.set(__self__, "is_zone_redundant", is_zone_redundant)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if minimum_tls_version_allowed and not isinstance(minimum_tls_version_allowed, str):
            raise TypeError("Expected argument 'minimum_tls_version_allowed' to be a str")
        pulumi.set(__self__, "minimum_tls_version_allowed", minimum_tls_version_allowed)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if topic_spaces_configuration and not isinstance(topic_spaces_configuration, dict):
            raise TypeError("Expected argument 'topic_spaces_configuration' to be a dict")
        pulumi.set(__self__, "topic_spaces_configuration", topic_spaces_configuration)
        if topics_configuration and not isinstance(topics_configuration, dict):
            raise TypeError("Expected argument 'topics_configuration' to be a dict")
        pulumi.set(__self__, "topics_configuration", topics_configuration)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityInfoResponse']:
        """
        Identity information for the Namespace resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> Optional[Sequence['outputs.InboundIpRuleResponse']]:
        """
        This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        """
        return pulumi.get(self, "inbound_ip_rules")

    @property
    @pulumi.getter(name="isZoneRedundant")
    def is_zone_redundant(self) -> Optional[bool]:
        """
        Allows the user to specify if the service is zone-redundant. This is a required property and user needs to specify this value explicitly.
        Once specified, this property cannot be updated.
        """
        return pulumi.get(self, "is_zone_redundant")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> Optional[str]:
        """
        Minimum TLS version of the publisher allowed to publish to this namespace. Only TLS version 1.2 is supported.
        """
        return pulumi.get(self, "minimum_tls_version_allowed")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the namespace resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PubSub.NamespaceProperties.InboundIpRules" />
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.NamespaceSkuResponse']:
        """
        Represents available Sku pricing tiers.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to the namespace resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="topicSpacesConfiguration")
    def topic_spaces_configuration(self) -> Optional['outputs.TopicSpacesConfigurationResponse']:
        """
        Topic spaces configuration information for the namespace resource
        """
        return pulumi.get(self, "topic_spaces_configuration")

    @property
    @pulumi.getter(name="topicsConfiguration")
    def topics_configuration(self) -> Optional['outputs.TopicsConfigurationResponse']:
        """
        Topics configuration information for the namespace resource
        """
        return pulumi.get(self, "topics_configuration")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetNamespaceResult(GetNamespaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceResult(
            id=self.id,
            identity=self.identity,
            inbound_ip_rules=self.inbound_ip_rules,
            is_zone_redundant=self.is_zone_redundant,
            location=self.location,
            minimum_tls_version_allowed=self.minimum_tls_version_allowed,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            topic_spaces_configuration=self.topic_spaces_configuration,
            topics_configuration=self.topics_configuration,
            type=self.type)


def get_namespace(namespace_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceResult:
    """
    Get properties of a namespace.
    Azure REST API version: 2023-06-01-preview.

    Other available API versions: 2023-12-15-preview, 2024-06-01-preview.


    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid:getNamespace', __args__, opts=opts, typ=GetNamespaceResult).value

    return AwaitableGetNamespaceResult(
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        inbound_ip_rules=pulumi.get(__ret__, 'inbound_ip_rules'),
        is_zone_redundant=pulumi.get(__ret__, 'is_zone_redundant'),
        location=pulumi.get(__ret__, 'location'),
        minimum_tls_version_allowed=pulumi.get(__ret__, 'minimum_tls_version_allowed'),
        name=pulumi.get(__ret__, 'name'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        topic_spaces_configuration=pulumi.get(__ret__, 'topic_spaces_configuration'),
        topics_configuration=pulumi.get(__ret__, 'topics_configuration'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_namespace)
def get_namespace_output(namespace_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceResult]:
    """
    Get properties of a namespace.
    Azure REST API version: 2023-06-01-preview.

    Other available API versions: 2023-12-15-preview, 2024-06-01-preview.


    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    ...
