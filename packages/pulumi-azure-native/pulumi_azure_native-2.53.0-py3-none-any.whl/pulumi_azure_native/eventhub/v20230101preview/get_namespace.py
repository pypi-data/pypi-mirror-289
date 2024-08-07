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
    'GetNamespaceResult',
    'AwaitableGetNamespaceResult',
    'get_namespace',
    'get_namespace_output',
]

@pulumi.output_type
class GetNamespaceResult:
    """
    Single Namespace item in List or Get Operation
    """
    def __init__(__self__, alternate_name=None, cluster_arm_id=None, created_at=None, disable_local_auth=None, encryption=None, geo_data_replication=None, id=None, identity=None, is_auto_inflate_enabled=None, kafka_enabled=None, location=None, maximum_throughput_units=None, metric_id=None, minimum_tls_version=None, name=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, service_bus_endpoint=None, sku=None, status=None, system_data=None, tags=None, type=None, updated_at=None, zone_redundant=None):
        if alternate_name and not isinstance(alternate_name, str):
            raise TypeError("Expected argument 'alternate_name' to be a str")
        pulumi.set(__self__, "alternate_name", alternate_name)
        if cluster_arm_id and not isinstance(cluster_arm_id, str):
            raise TypeError("Expected argument 'cluster_arm_id' to be a str")
        pulumi.set(__self__, "cluster_arm_id", cluster_arm_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if disable_local_auth and not isinstance(disable_local_auth, bool):
            raise TypeError("Expected argument 'disable_local_auth' to be a bool")
        pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if geo_data_replication and not isinstance(geo_data_replication, dict):
            raise TypeError("Expected argument 'geo_data_replication' to be a dict")
        pulumi.set(__self__, "geo_data_replication", geo_data_replication)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if is_auto_inflate_enabled and not isinstance(is_auto_inflate_enabled, bool):
            raise TypeError("Expected argument 'is_auto_inflate_enabled' to be a bool")
        pulumi.set(__self__, "is_auto_inflate_enabled", is_auto_inflate_enabled)
        if kafka_enabled and not isinstance(kafka_enabled, bool):
            raise TypeError("Expected argument 'kafka_enabled' to be a bool")
        pulumi.set(__self__, "kafka_enabled", kafka_enabled)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maximum_throughput_units and not isinstance(maximum_throughput_units, int):
            raise TypeError("Expected argument 'maximum_throughput_units' to be a int")
        pulumi.set(__self__, "maximum_throughput_units", maximum_throughput_units)
        if metric_id and not isinstance(metric_id, str):
            raise TypeError("Expected argument 'metric_id' to be a str")
        pulumi.set(__self__, "metric_id", metric_id)
        if minimum_tls_version and not isinstance(minimum_tls_version, str):
            raise TypeError("Expected argument 'minimum_tls_version' to be a str")
        pulumi.set(__self__, "minimum_tls_version", minimum_tls_version)
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
        if service_bus_endpoint and not isinstance(service_bus_endpoint, str):
            raise TypeError("Expected argument 'service_bus_endpoint' to be a str")
        pulumi.set(__self__, "service_bus_endpoint", service_bus_endpoint)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if zone_redundant and not isinstance(zone_redundant, bool):
            raise TypeError("Expected argument 'zone_redundant' to be a bool")
        pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> Optional[str]:
        """
        Alternate name specified when alias and namespace names are same.
        """
        return pulumi.get(self, "alternate_name")

    @property
    @pulumi.getter(name="clusterArmId")
    def cluster_arm_id(self) -> Optional[str]:
        """
        Cluster ARM ID of the Namespace.
        """
        return pulumi.get(self, "cluster_arm_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time the Namespace was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[bool]:
        """
        This property disables SAS authentication for the Event Hubs namespace.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EncryptionResponse']:
        """
        Properties of BYOK Encryption description
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="geoDataReplication")
    def geo_data_replication(self) -> Optional['outputs.GeoDataReplicationPropertiesResponse']:
        """
        Geo Data Replication settings for the namespace
        """
        return pulumi.get(self, "geo_data_replication")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        Properties of BYOK Identity description
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="isAutoInflateEnabled")
    def is_auto_inflate_enabled(self) -> Optional[bool]:
        """
        Value that indicates whether AutoInflate is enabled for eventhub namespace.
        """
        return pulumi.get(self, "is_auto_inflate_enabled")

    @property
    @pulumi.getter(name="kafkaEnabled")
    def kafka_enabled(self) -> Optional[bool]:
        """
        Value that indicates whether Kafka is enabled for eventhub namespace.
        """
        return pulumi.get(self, "kafka_enabled")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maximumThroughputUnits")
    def maximum_throughput_units(self) -> Optional[int]:
        """
        Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)
        """
        return pulumi.get(self, "maximum_throughput_units")

    @property
    @pulumi.getter(name="metricId")
    def metric_id(self) -> str:
        """
        Identifier for Azure Insights metrics.
        """
        return pulumi.get(self, "metric_id")

    @property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[str]:
        """
        The minimum TLS version for the cluster to support, e.g. '1.2'
        """
        return pulumi.get(self, "minimum_tls_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        List of private endpoint connections.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the Namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="serviceBusEndpoint")
    def service_bus_endpoint(self) -> str:
        """
        Endpoint you can use to perform Service Bus operations.
        """
        return pulumi.get(self, "service_bus_endpoint")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        Properties of sku resource
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the Namespace.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The time the Namespace was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[bool]:
        """
        Enabling this property creates a Standard Event Hubs Namespace in regions supported availability zones.
        """
        return pulumi.get(self, "zone_redundant")


class AwaitableGetNamespaceResult(GetNamespaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceResult(
            alternate_name=self.alternate_name,
            cluster_arm_id=self.cluster_arm_id,
            created_at=self.created_at,
            disable_local_auth=self.disable_local_auth,
            encryption=self.encryption,
            geo_data_replication=self.geo_data_replication,
            id=self.id,
            identity=self.identity,
            is_auto_inflate_enabled=self.is_auto_inflate_enabled,
            kafka_enabled=self.kafka_enabled,
            location=self.location,
            maximum_throughput_units=self.maximum_throughput_units,
            metric_id=self.metric_id,
            minimum_tls_version=self.minimum_tls_version,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            service_bus_endpoint=self.service_bus_endpoint,
            sku=self.sku,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            updated_at=self.updated_at,
            zone_redundant=self.zone_redundant)


def get_namespace(namespace_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceResult:
    """
    Gets the description of the specified namespace.


    :param str namespace_name: The Namespace name
    :param str resource_group_name: Name of the resource group within the azure subscription.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventhub/v20230101preview:getNamespace', __args__, opts=opts, typ=GetNamespaceResult).value

    return AwaitableGetNamespaceResult(
        alternate_name=pulumi.get(__ret__, 'alternate_name'),
        cluster_arm_id=pulumi.get(__ret__, 'cluster_arm_id'),
        created_at=pulumi.get(__ret__, 'created_at'),
        disable_local_auth=pulumi.get(__ret__, 'disable_local_auth'),
        encryption=pulumi.get(__ret__, 'encryption'),
        geo_data_replication=pulumi.get(__ret__, 'geo_data_replication'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        is_auto_inflate_enabled=pulumi.get(__ret__, 'is_auto_inflate_enabled'),
        kafka_enabled=pulumi.get(__ret__, 'kafka_enabled'),
        location=pulumi.get(__ret__, 'location'),
        maximum_throughput_units=pulumi.get(__ret__, 'maximum_throughput_units'),
        metric_id=pulumi.get(__ret__, 'metric_id'),
        minimum_tls_version=pulumi.get(__ret__, 'minimum_tls_version'),
        name=pulumi.get(__ret__, 'name'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        service_bus_endpoint=pulumi.get(__ret__, 'service_bus_endpoint'),
        sku=pulumi.get(__ret__, 'sku'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        zone_redundant=pulumi.get(__ret__, 'zone_redundant'))


@_utilities.lift_output_func(get_namespace)
def get_namespace_output(namespace_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceResult]:
    """
    Gets the description of the specified namespace.


    :param str namespace_name: The Namespace name
    :param str resource_group_name: Name of the resource group within the azure subscription.
    """
    ...
