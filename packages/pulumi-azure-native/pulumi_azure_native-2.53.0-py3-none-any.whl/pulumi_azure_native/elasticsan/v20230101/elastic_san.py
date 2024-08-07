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

__all__ = ['ElasticSanArgs', 'ElasticSan']

@pulumi.input_type
class ElasticSanArgs:
    def __init__(__self__, *,
                 base_size_ti_b: pulumi.Input[float],
                 extended_capacity_size_ti_b: pulumi.Input[float],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 elastic_san_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ElasticSan resource.
        :param pulumi.Input[float] base_size_ti_b: Base size of the Elastic San appliance in TiB.
        :param pulumi.Input[float] extended_capacity_size_ti_b: Extended size of the Elastic San appliance in TiB.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['SkuArgs'] sku: resource sku
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: Logical zone for Elastic San resource; example: ["1"].
        :param pulumi.Input[str] elastic_san_name: The name of the ElasticSan.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Allow or disallow public network access to ElasticSan. Value is optional but if passed in, must be 'Enabled' or 'Disabled'.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "base_size_ti_b", base_size_ti_b)
        pulumi.set(__self__, "extended_capacity_size_ti_b", extended_capacity_size_ti_b)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if elastic_san_name is not None:
            pulumi.set(__self__, "elastic_san_name", elastic_san_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="baseSizeTiB")
    def base_size_ti_b(self) -> pulumi.Input[float]:
        """
        Base size of the Elastic San appliance in TiB.
        """
        return pulumi.get(self, "base_size_ti_b")

    @base_size_ti_b.setter
    def base_size_ti_b(self, value: pulumi.Input[float]):
        pulumi.set(self, "base_size_ti_b", value)

    @property
    @pulumi.getter(name="extendedCapacitySizeTiB")
    def extended_capacity_size_ti_b(self) -> pulumi.Input[float]:
        """
        Extended size of the Elastic San appliance in TiB.
        """
        return pulumi.get(self, "extended_capacity_size_ti_b")

    @extended_capacity_size_ti_b.setter
    def extended_capacity_size_ti_b(self, value: pulumi.Input[float]):
        pulumi.set(self, "extended_capacity_size_ti_b", value)

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
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        resource sku
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Logical zone for Elastic San resource; example: ["1"].
        """
        return pulumi.get(self, "availability_zones")

    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "availability_zones", value)

    @property
    @pulumi.getter(name="elasticSanName")
    def elastic_san_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ElasticSan.
        """
        return pulumi.get(self, "elastic_san_name")

    @elastic_san_name.setter
    def elastic_san_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "elastic_san_name", value)

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
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        Allow or disallow public network access to ElasticSan. Value is optional but if passed in, must be 'Enabled' or 'Disabled'.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

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


class ElasticSan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 base_size_ti_b: Optional[pulumi.Input[float]] = None,
                 elastic_san_name: Optional[pulumi.Input[str]] = None,
                 extended_capacity_size_ti_b: Optional[pulumi.Input[float]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Response for ElasticSan request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: Logical zone for Elastic San resource; example: ["1"].
        :param pulumi.Input[float] base_size_ti_b: Base size of the Elastic San appliance in TiB.
        :param pulumi.Input[str] elastic_san_name: The name of the ElasticSan.
        :param pulumi.Input[float] extended_capacity_size_ti_b: Extended size of the Elastic San appliance in TiB.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Allow or disallow public network access to ElasticSan. Value is optional but if passed in, must be 'Enabled' or 'Disabled'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['SkuArgs', 'SkuArgsDict']] sku: resource sku
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ElasticSanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Response for ElasticSan request.

        :param str resource_name: The name of the resource.
        :param ElasticSanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ElasticSanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 base_size_ti_b: Optional[pulumi.Input[float]] = None,
                 elastic_san_name: Optional[pulumi.Input[str]] = None,
                 extended_capacity_size_ti_b: Optional[pulumi.Input[float]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ElasticSanArgs.__new__(ElasticSanArgs)

            __props__.__dict__["availability_zones"] = availability_zones
            if base_size_ti_b is None and not opts.urn:
                raise TypeError("Missing required property 'base_size_ti_b'")
            __props__.__dict__["base_size_ti_b"] = base_size_ti_b
            __props__.__dict__["elastic_san_name"] = elastic_san_name
            if extended_capacity_size_ti_b is None and not opts.urn:
                raise TypeError("Missing required property 'extended_capacity_size_ti_b'")
            __props__.__dict__["extended_capacity_size_ti_b"] = extended_capacity_size_ti_b
            __props__.__dict__["location"] = location
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["total_iops"] = None
            __props__.__dict__["total_m_bps"] = None
            __props__.__dict__["total_size_ti_b"] = None
            __props__.__dict__["total_volume_size_gi_b"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["volume_group_count"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:elasticsan:ElasticSan"), pulumi.Alias(type_="azure-native:elasticsan/v20211120preview:ElasticSan"), pulumi.Alias(type_="azure-native:elasticsan/v20221201preview:ElasticSan"), pulumi.Alias(type_="azure-native:elasticsan/v20240501:ElasticSan")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ElasticSan, __self__).__init__(
            'azure-native:elasticsan/v20230101:ElasticSan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ElasticSan':
        """
        Get an existing ElasticSan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ElasticSanArgs.__new__(ElasticSanArgs)

        __props__.__dict__["availability_zones"] = None
        __props__.__dict__["base_size_ti_b"] = None
        __props__.__dict__["extended_capacity_size_ti_b"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["total_iops"] = None
        __props__.__dict__["total_m_bps"] = None
        __props__.__dict__["total_size_ti_b"] = None
        __props__.__dict__["total_volume_size_gi_b"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["volume_group_count"] = None
        return ElasticSan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Logical zone for Elastic San resource; example: ["1"].
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="baseSizeTiB")
    def base_size_ti_b(self) -> pulumi.Output[float]:
        """
        Base size of the Elastic San appliance in TiB.
        """
        return pulumi.get(self, "base_size_ti_b")

    @property
    @pulumi.getter(name="extendedCapacitySizeTiB")
    def extended_capacity_size_ti_b(self) -> pulumi.Output[float]:
        """
        Extended size of the Elastic San appliance in TiB.
        """
        return pulumi.get(self, "extended_capacity_size_ti_b")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        The list of Private Endpoint Connections.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Allow or disallow public network access to ElasticSan. Value is optional but if passed in, must be 'Enabled' or 'Disabled'.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        resource sku
        """
        return pulumi.get(self, "sku")

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
    @pulumi.getter(name="totalIops")
    def total_iops(self) -> pulumi.Output[float]:
        """
        Total Provisioned IOPS of the Elastic San appliance.
        """
        return pulumi.get(self, "total_iops")

    @property
    @pulumi.getter(name="totalMBps")
    def total_m_bps(self) -> pulumi.Output[float]:
        """
        Total Provisioned MBps Elastic San appliance.
        """
        return pulumi.get(self, "total_m_bps")

    @property
    @pulumi.getter(name="totalSizeTiB")
    def total_size_ti_b(self) -> pulumi.Output[float]:
        """
        Total size of the Elastic San appliance in TB.
        """
        return pulumi.get(self, "total_size_ti_b")

    @property
    @pulumi.getter(name="totalVolumeSizeGiB")
    def total_volume_size_gi_b(self) -> pulumi.Output[float]:
        """
        Total size of the provisioned Volumes in GiB.
        """
        return pulumi.get(self, "total_volume_size_gi_b")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeGroupCount")
    def volume_group_count(self) -> pulumi.Output[float]:
        """
        Total number of volume groups in this Elastic San appliance.
        """
        return pulumi.get(self, "volume_group_count")

