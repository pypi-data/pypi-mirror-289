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

__all__ = ['NamespaceArgs', 'Namespace']

@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 alternate_name: Optional[pulumi.Input[str]] = None,
                 cluster_arm_id: Optional[pulumi.Input[str]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input['EncryptionArgs']] = None,
                 geo_data_replication: Optional[pulumi.Input['GeoDataReplicationPropertiesArgs']] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 is_auto_inflate_enabled: Optional[pulumi.Input[bool]] = None,
                 kafka_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_throughput_units: Optional[pulumi.Input[int]] = None,
                 minimum_tls_version: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Namespace resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        :param pulumi.Input[str] alternate_name: Alternate name specified when alias and namespace names are same.
        :param pulumi.Input[str] cluster_arm_id: Cluster ARM ID of the Namespace.
        :param pulumi.Input[bool] disable_local_auth: This property disables SAS authentication for the Event Hubs namespace.
        :param pulumi.Input['EncryptionArgs'] encryption: Properties of BYOK Encryption description
        :param pulumi.Input['GeoDataReplicationPropertiesArgs'] geo_data_replication: Geo Data Replication settings for the namespace
        :param pulumi.Input['IdentityArgs'] identity: Properties of BYOK Identity description
        :param pulumi.Input[bool] is_auto_inflate_enabled: Value that indicates whether AutoInflate is enabled for eventhub namespace.
        :param pulumi.Input[bool] kafka_enabled: Value that indicates whether Kafka is enabled for eventhub namespace.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[int] maximum_throughput_units: Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)
        :param pulumi.Input[Union[str, 'TlsVersion']] minimum_tls_version: The minimum TLS version for the cluster to support, e.g. '1.2'
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]] private_endpoint_connections: List of private endpoint connections.
               These are also available as standalone resources. Do not mix inline and standalone resource as they will conflict with each other, leading to resources deletion.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled.
        :param pulumi.Input['SkuArgs'] sku: Properties of sku resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] zone_redundant: Enabling this property creates a Standard Event Hubs Namespace in regions supported availability zones.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if alternate_name is not None:
            pulumi.set(__self__, "alternate_name", alternate_name)
        if cluster_arm_id is not None:
            pulumi.set(__self__, "cluster_arm_id", cluster_arm_id)
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if geo_data_replication is not None:
            pulumi.set(__self__, "geo_data_replication", geo_data_replication)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if is_auto_inflate_enabled is not None:
            pulumi.set(__self__, "is_auto_inflate_enabled", is_auto_inflate_enabled)
        if kafka_enabled is not None:
            pulumi.set(__self__, "kafka_enabled", kafka_enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if maximum_throughput_units is not None:
            pulumi.set(__self__, "maximum_throughput_units", maximum_throughput_units)
        if minimum_tls_version is not None:
            pulumi.set(__self__, "minimum_tls_version", minimum_tls_version)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if private_endpoint_connections is not None:
            pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access is None:
            public_network_access = 'Enabled'
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone_redundant is not None:
            pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group within the azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> Optional[pulumi.Input[str]]:
        """
        Alternate name specified when alias and namespace names are same.
        """
        return pulumi.get(self, "alternate_name")

    @alternate_name.setter
    def alternate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alternate_name", value)

    @property
    @pulumi.getter(name="clusterArmId")
    def cluster_arm_id(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster ARM ID of the Namespace.
        """
        return pulumi.get(self, "cluster_arm_id")

    @cluster_arm_id.setter
    def cluster_arm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_arm_id", value)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        This property disables SAS authentication for the Event Hubs namespace.
        """
        return pulumi.get(self, "disable_local_auth")

    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_local_auth", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['EncryptionArgs']]:
        """
        Properties of BYOK Encryption description
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['EncryptionArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter(name="geoDataReplication")
    def geo_data_replication(self) -> Optional[pulumi.Input['GeoDataReplicationPropertiesArgs']]:
        """
        Geo Data Replication settings for the namespace
        """
        return pulumi.get(self, "geo_data_replication")

    @geo_data_replication.setter
    def geo_data_replication(self, value: Optional[pulumi.Input['GeoDataReplicationPropertiesArgs']]):
        pulumi.set(self, "geo_data_replication", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        Properties of BYOK Identity description
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="isAutoInflateEnabled")
    def is_auto_inflate_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Value that indicates whether AutoInflate is enabled for eventhub namespace.
        """
        return pulumi.get(self, "is_auto_inflate_enabled")

    @is_auto_inflate_enabled.setter
    def is_auto_inflate_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_auto_inflate_enabled", value)

    @property
    @pulumi.getter(name="kafkaEnabled")
    def kafka_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Value that indicates whether Kafka is enabled for eventhub namespace.
        """
        return pulumi.get(self, "kafka_enabled")

    @kafka_enabled.setter
    def kafka_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "kafka_enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="maximumThroughputUnits")
    def maximum_throughput_units(self) -> Optional[pulumi.Input[int]]:
        """
        Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)
        """
        return pulumi.get(self, "maximum_throughput_units")

    @maximum_throughput_units.setter
    def maximum_throughput_units(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_throughput_units", value)

    @property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[pulumi.Input[Union[str, 'TlsVersion']]]:
        """
        The minimum TLS version for the cluster to support, e.g. '1.2'
        """
        return pulumi.get(self, "minimum_tls_version")

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: Optional[pulumi.Input[Union[str, 'TlsVersion']]]):
        pulumi.set(self, "minimum_tls_version", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]:
        """
        List of private endpoint connections.
        These are also available as standalone resources. Do not mix inline and standalone resource as they will conflict with each other, leading to resources deletion.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @private_endpoint_connections.setter
    def private_endpoint_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]):
        pulumi.set(self, "private_endpoint_connections", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        Properties of sku resource
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

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

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[pulumi.Input[bool]]:
        """
        Enabling this property creates a Standard Event Hubs Namespace in regions supported availability zones.
        """
        return pulumi.get(self, "zone_redundant")

    @zone_redundant.setter
    def zone_redundant(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "zone_redundant", value)


class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alternate_name: Optional[pulumi.Input[str]] = None,
                 cluster_arm_id: Optional[pulumi.Input[str]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[Union['EncryptionArgs', 'EncryptionArgsDict']]] = None,
                 geo_data_replication: Optional[pulumi.Input[Union['GeoDataReplicationPropertiesArgs', 'GeoDataReplicationPropertiesArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['IdentityArgs', 'IdentityArgsDict']]] = None,
                 is_auto_inflate_enabled: Optional[pulumi.Input[bool]] = None,
                 kafka_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_throughput_units: Optional[pulumi.Input[int]] = None,
                 minimum_tls_version: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrivateEndpointConnectionArgs', 'PrivateEndpointConnectionArgsDict']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Single Namespace item in List or Get Operation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alternate_name: Alternate name specified when alias and namespace names are same.
        :param pulumi.Input[str] cluster_arm_id: Cluster ARM ID of the Namespace.
        :param pulumi.Input[bool] disable_local_auth: This property disables SAS authentication for the Event Hubs namespace.
        :param pulumi.Input[Union['EncryptionArgs', 'EncryptionArgsDict']] encryption: Properties of BYOK Encryption description
        :param pulumi.Input[Union['GeoDataReplicationPropertiesArgs', 'GeoDataReplicationPropertiesArgsDict']] geo_data_replication: Geo Data Replication settings for the namespace
        :param pulumi.Input[Union['IdentityArgs', 'IdentityArgsDict']] identity: Properties of BYOK Identity description
        :param pulumi.Input[bool] is_auto_inflate_enabled: Value that indicates whether AutoInflate is enabled for eventhub namespace.
        :param pulumi.Input[bool] kafka_enabled: Value that indicates whether Kafka is enabled for eventhub namespace.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[int] maximum_throughput_units: Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)
        :param pulumi.Input[Union[str, 'TlsVersion']] minimum_tls_version: The minimum TLS version for the cluster to support, e.g. '1.2'
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input[Sequence[pulumi.Input[Union['PrivateEndpointConnectionArgs', 'PrivateEndpointConnectionArgsDict']]]] private_endpoint_connections: List of private endpoint connections.
               These are also available as standalone resources. Do not mix inline and standalone resource as they will conflict with each other, leading to resources deletion.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        :param pulumi.Input[Union['SkuArgs', 'SkuArgsDict']] sku: Properties of sku resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] zone_redundant: Enabling this property creates a Standard Event Hubs Namespace in regions supported availability zones.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Single Namespace item in List or Get Operation

        :param str resource_name: The name of the resource.
        :param NamespaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alternate_name: Optional[pulumi.Input[str]] = None,
                 cluster_arm_id: Optional[pulumi.Input[str]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[Union['EncryptionArgs', 'EncryptionArgsDict']]] = None,
                 geo_data_replication: Optional[pulumi.Input[Union['GeoDataReplicationPropertiesArgs', 'GeoDataReplicationPropertiesArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['IdentityArgs', 'IdentityArgsDict']]] = None,
                 is_auto_inflate_enabled: Optional[pulumi.Input[bool]] = None,
                 kafka_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_throughput_units: Optional[pulumi.Input[int]] = None,
                 minimum_tls_version: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrivateEndpointConnectionArgs', 'PrivateEndpointConnectionArgsDict']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceArgs.__new__(NamespaceArgs)

            __props__.__dict__["alternate_name"] = alternate_name
            __props__.__dict__["cluster_arm_id"] = cluster_arm_id
            __props__.__dict__["disable_local_auth"] = disable_local_auth
            __props__.__dict__["encryption"] = encryption
            __props__.__dict__["geo_data_replication"] = geo_data_replication
            __props__.__dict__["identity"] = identity
            __props__.__dict__["is_auto_inflate_enabled"] = is_auto_inflate_enabled
            __props__.__dict__["kafka_enabled"] = kafka_enabled
            __props__.__dict__["location"] = location
            __props__.__dict__["maximum_throughput_units"] = maximum_throughput_units
            __props__.__dict__["minimum_tls_version"] = minimum_tls_version
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["private_endpoint_connections"] = private_endpoint_connections
            if public_network_access is None:
                public_network_access = 'Enabled'
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone_redundant"] = zone_redundant
            __props__.__dict__["created_at"] = None
            __props__.__dict__["metric_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["service_bus_endpoint"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_at"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventhub:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20140901:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20150801:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20170401:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20180101preview:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20210101preview:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20210601preview:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20211101:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20220101preview:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20221001preview:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20240101:Namespace"), pulumi.Alias(type_="azure-native:eventhub/v20240501preview:Namespace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Namespace, __self__).__init__(
            'azure-native:eventhub/v20230101preview:Namespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Namespace':
        """
        Get an existing Namespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceArgs.__new__(NamespaceArgs)

        __props__.__dict__["alternate_name"] = None
        __props__.__dict__["cluster_arm_id"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["disable_local_auth"] = None
        __props__.__dict__["encryption"] = None
        __props__.__dict__["geo_data_replication"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["is_auto_inflate_enabled"] = None
        __props__.__dict__["kafka_enabled"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["maximum_throughput_units"] = None
        __props__.__dict__["metric_id"] = None
        __props__.__dict__["minimum_tls_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["service_bus_endpoint"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_at"] = None
        __props__.__dict__["zone_redundant"] = None
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> pulumi.Output[Optional[str]]:
        """
        Alternate name specified when alias and namespace names are same.
        """
        return pulumi.get(self, "alternate_name")

    @property
    @pulumi.getter(name="clusterArmId")
    def cluster_arm_id(self) -> pulumi.Output[Optional[str]]:
        """
        Cluster ARM ID of the Namespace.
        """
        return pulumi.get(self, "cluster_arm_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time the Namespace was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        This property disables SAS authentication for the Event Hubs namespace.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional['outputs.EncryptionResponse']]:
        """
        Properties of BYOK Encryption description
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="geoDataReplication")
    def geo_data_replication(self) -> pulumi.Output[Optional['outputs.GeoDataReplicationPropertiesResponse']]:
        """
        Geo Data Replication settings for the namespace
        """
        return pulumi.get(self, "geo_data_replication")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        Properties of BYOK Identity description
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="isAutoInflateEnabled")
    def is_auto_inflate_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Value that indicates whether AutoInflate is enabled for eventhub namespace.
        """
        return pulumi.get(self, "is_auto_inflate_enabled")

    @property
    @pulumi.getter(name="kafkaEnabled")
    def kafka_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Value that indicates whether Kafka is enabled for eventhub namespace.
        """
        return pulumi.get(self, "kafka_enabled")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maximumThroughputUnits")
    def maximum_throughput_units(self) -> pulumi.Output[Optional[int]]:
        """
        Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)
        """
        return pulumi.get(self, "maximum_throughput_units")

    @property
    @pulumi.getter(name="metricId")
    def metric_id(self) -> pulumi.Output[str]:
        """
        Identifier for Azure Insights metrics.
        """
        return pulumi.get(self, "metric_id")

    @property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> pulumi.Output[Optional[str]]:
        """
        The minimum TLS version for the cluster to support, e.g. '1.2'
        """
        return pulumi.get(self, "minimum_tls_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]]:
        """
        List of private endpoint connections.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the Namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="serviceBusEndpoint")
    def service_bus_endpoint(self) -> pulumi.Output[str]:
        """
        Endpoint you can use to perform Service Bus operations.
        """
        return pulumi.get(self, "service_bus_endpoint")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        Properties of sku resource
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the Namespace.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system meta data relating to this resource.
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

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The time the Namespace was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[bool]]:
        """
        Enabling this property creates a Standard Event Hubs Namespace in regions supported availability zones.
        """
        return pulumi.get(self, "zone_redundant")

