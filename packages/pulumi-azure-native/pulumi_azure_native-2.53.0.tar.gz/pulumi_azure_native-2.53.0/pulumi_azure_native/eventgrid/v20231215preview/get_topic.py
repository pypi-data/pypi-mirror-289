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
    'GetTopicResult',
    'AwaitableGetTopicResult',
    'get_topic',
    'get_topic_output',
]

@pulumi.output_type
class GetTopicResult:
    """
    EventGrid Topic
    """
    def __init__(__self__, data_residency_boundary=None, disable_local_auth=None, endpoint=None, event_type_info=None, extended_location=None, id=None, identity=None, inbound_ip_rules=None, input_schema=None, input_schema_mapping=None, kind=None, location=None, metric_resource_id=None, minimum_tls_version_allowed=None, name=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, sku=None, system_data=None, tags=None, type=None):
        if data_residency_boundary and not isinstance(data_residency_boundary, str):
            raise TypeError("Expected argument 'data_residency_boundary' to be a str")
        pulumi.set(__self__, "data_residency_boundary", data_residency_boundary)
        if disable_local_auth and not isinstance(disable_local_auth, bool):
            raise TypeError("Expected argument 'disable_local_auth' to be a bool")
        pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if event_type_info and not isinstance(event_type_info, dict):
            raise TypeError("Expected argument 'event_type_info' to be a dict")
        pulumi.set(__self__, "event_type_info", event_type_info)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if inbound_ip_rules and not isinstance(inbound_ip_rules, list):
            raise TypeError("Expected argument 'inbound_ip_rules' to be a list")
        pulumi.set(__self__, "inbound_ip_rules", inbound_ip_rules)
        if input_schema and not isinstance(input_schema, str):
            raise TypeError("Expected argument 'input_schema' to be a str")
        pulumi.set(__self__, "input_schema", input_schema)
        if input_schema_mapping and not isinstance(input_schema_mapping, dict):
            raise TypeError("Expected argument 'input_schema_mapping' to be a dict")
        pulumi.set(__self__, "input_schema_mapping", input_schema_mapping)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if metric_resource_id and not isinstance(metric_resource_id, str):
            raise TypeError("Expected argument 'metric_resource_id' to be a str")
        pulumi.set(__self__, "metric_resource_id", metric_resource_id)
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
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataResidencyBoundary")
    def data_residency_boundary(self) -> Optional[str]:
        """
        Data Residency Boundary of the resource.
        """
        return pulumi.get(self, "data_residency_boundary")

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[bool]:
        """
        This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the topic.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        Endpoint for the topic.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="eventTypeInfo")
    def event_type_info(self) -> Optional['outputs.EventTypeInfoResponse']:
        """
        Event Type Information for the user topic. This information is provided by the publisher and can be used by the 
        subscriber to view different types of events that are published.
        """
        return pulumi.get(self, "event_type_info")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        Extended location of the resource.
        """
        return pulumi.get(self, "extended_location")

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
        Identity information for the resource.
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
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[str]:
        """
        This determines the format that Event Grid should expect for incoming events published to the topic.
        """
        return pulumi.get(self, "input_schema")

    @property
    @pulumi.getter(name="inputSchemaMapping")
    def input_schema_mapping(self) -> Optional['outputs.JsonInputSchemaMappingResponse']:
        """
        This enables publishing using custom event schemas. An InputSchemaMapping can be specified to map various properties of a source schema to various required properties of the EventGridEvent schema.
        """
        return pulumi.get(self, "input_schema_mapping")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="metricResourceId")
    def metric_resource_id(self) -> str:
        """
        Metric resource id for the topic.
        """
        return pulumi.get(self, "metric_resource_id")

    @property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> Optional[str]:
        """
        Minimum TLS version of the publisher allowed to publish to this topic
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
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the topic.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        This determines if traffic is allowed over public network. By default it is enabled. 
        You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.TopicProperties.InboundIpRules" />
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.ResourceSkuResponse']:
        """
        The Sku pricing tier for the topic.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to Topic resource.
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
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetTopicResult(GetTopicResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicResult(
            data_residency_boundary=self.data_residency_boundary,
            disable_local_auth=self.disable_local_auth,
            endpoint=self.endpoint,
            event_type_info=self.event_type_info,
            extended_location=self.extended_location,
            id=self.id,
            identity=self.identity,
            inbound_ip_rules=self.inbound_ip_rules,
            input_schema=self.input_schema,
            input_schema_mapping=self.input_schema_mapping,
            kind=self.kind,
            location=self.location,
            metric_resource_id=self.metric_resource_id,
            minimum_tls_version_allowed=self.minimum_tls_version_allowed,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_topic(resource_group_name: Optional[str] = None,
              topic_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTopicResult:
    """
    Get properties of a topic.


    :param str resource_group_name: The name of the resource group within the user's subscription.
    :param str topic_name: Name of the topic.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['topicName'] = topic_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20231215preview:getTopic', __args__, opts=opts, typ=GetTopicResult).value

    return AwaitableGetTopicResult(
        data_residency_boundary=pulumi.get(__ret__, 'data_residency_boundary'),
        disable_local_auth=pulumi.get(__ret__, 'disable_local_auth'),
        endpoint=pulumi.get(__ret__, 'endpoint'),
        event_type_info=pulumi.get(__ret__, 'event_type_info'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        inbound_ip_rules=pulumi.get(__ret__, 'inbound_ip_rules'),
        input_schema=pulumi.get(__ret__, 'input_schema'),
        input_schema_mapping=pulumi.get(__ret__, 'input_schema_mapping'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        metric_resource_id=pulumi.get(__ret__, 'metric_resource_id'),
        minimum_tls_version_allowed=pulumi.get(__ret__, 'minimum_tls_version_allowed'),
        name=pulumi.get(__ret__, 'name'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_topic)
def get_topic_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                     topic_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTopicResult]:
    """
    Get properties of a topic.


    :param str resource_group_name: The name of the resource group within the user's subscription.
    :param str topic_name: Name of the topic.
    """
    ...
