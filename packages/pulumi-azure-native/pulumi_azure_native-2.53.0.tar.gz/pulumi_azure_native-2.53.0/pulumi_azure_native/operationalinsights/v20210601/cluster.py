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

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 billing_type: Optional[pulumi.Input[Union[str, 'BillingType']]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 is_availability_zones_enabled: Optional[pulumi.Input[bool]] = None,
                 is_double_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 key_vault_properties: Optional[pulumi.Input['KeyVaultPropertiesArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['ClusterSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'BillingType']] billing_type: The cluster's billing type.
        :param pulumi.Input[str] cluster_name: The name of the Log Analytics cluster.
        :param pulumi.Input['IdentityArgs'] identity: The identity of the resource.
        :param pulumi.Input[bool] is_availability_zones_enabled: Sets whether the cluster will support availability zones. This can be set as true only in regions where Azure Data Explorer support Availability Zones. This Property can not be modified after cluster creation. Default value is 'true' if region supports Availability Zones.
        :param pulumi.Input[bool] is_double_encryption_enabled: Configures whether cluster will use double encryption. This Property can not be modified after cluster creation. Default value is 'true'
        :param pulumi.Input['KeyVaultPropertiesArgs'] key_vault_properties: The associated key properties.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['ClusterSkuArgs'] sku: The sku properties.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if billing_type is not None:
            pulumi.set(__self__, "billing_type", billing_type)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if is_availability_zones_enabled is not None:
            pulumi.set(__self__, "is_availability_zones_enabled", is_availability_zones_enabled)
        if is_double_encryption_enabled is not None:
            pulumi.set(__self__, "is_double_encryption_enabled", is_double_encryption_enabled)
        if key_vault_properties is not None:
            pulumi.set(__self__, "key_vault_properties", key_vault_properties)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
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
    @pulumi.getter(name="billingType")
    def billing_type(self) -> Optional[pulumi.Input[Union[str, 'BillingType']]]:
        """
        The cluster's billing type.
        """
        return pulumi.get(self, "billing_type")

    @billing_type.setter
    def billing_type(self, value: Optional[pulumi.Input[Union[str, 'BillingType']]]):
        pulumi.set(self, "billing_type", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Log Analytics cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="isAvailabilityZonesEnabled")
    def is_availability_zones_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Sets whether the cluster will support availability zones. This can be set as true only in regions where Azure Data Explorer support Availability Zones. This Property can not be modified after cluster creation. Default value is 'true' if region supports Availability Zones.
        """
        return pulumi.get(self, "is_availability_zones_enabled")

    @is_availability_zones_enabled.setter
    def is_availability_zones_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_availability_zones_enabled", value)

    @property
    @pulumi.getter(name="isDoubleEncryptionEnabled")
    def is_double_encryption_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Configures whether cluster will use double encryption. This Property can not be modified after cluster creation. Default value is 'true'
        """
        return pulumi.get(self, "is_double_encryption_enabled")

    @is_double_encryption_enabled.setter
    def is_double_encryption_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_double_encryption_enabled", value)

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[pulumi.Input['KeyVaultPropertiesArgs']]:
        """
        The associated key properties.
        """
        return pulumi.get(self, "key_vault_properties")

    @key_vault_properties.setter
    def key_vault_properties(self, value: Optional[pulumi.Input['KeyVaultPropertiesArgs']]):
        pulumi.set(self, "key_vault_properties", value)

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
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['ClusterSkuArgs']]:
        """
        The sku properties.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['ClusterSkuArgs']]):
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


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_type: Optional[pulumi.Input[Union[str, 'BillingType']]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['IdentityArgs', 'IdentityArgsDict']]] = None,
                 is_availability_zones_enabled: Optional[pulumi.Input[bool]] = None,
                 is_double_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 key_vault_properties: Optional[pulumi.Input[Union['KeyVaultPropertiesArgs', 'KeyVaultPropertiesArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['ClusterSkuArgs', 'ClusterSkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The top level Log Analytics cluster resource container.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'BillingType']] billing_type: The cluster's billing type.
        :param pulumi.Input[str] cluster_name: The name of the Log Analytics cluster.
        :param pulumi.Input[Union['IdentityArgs', 'IdentityArgsDict']] identity: The identity of the resource.
        :param pulumi.Input[bool] is_availability_zones_enabled: Sets whether the cluster will support availability zones. This can be set as true only in regions where Azure Data Explorer support Availability Zones. This Property can not be modified after cluster creation. Default value is 'true' if region supports Availability Zones.
        :param pulumi.Input[bool] is_double_encryption_enabled: Configures whether cluster will use double encryption. This Property can not be modified after cluster creation. Default value is 'true'
        :param pulumi.Input[Union['KeyVaultPropertiesArgs', 'KeyVaultPropertiesArgsDict']] key_vault_properties: The associated key properties.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['ClusterSkuArgs', 'ClusterSkuArgsDict']] sku: The sku properties.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The top level Log Analytics cluster resource container.

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_type: Optional[pulumi.Input[Union[str, 'BillingType']]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['IdentityArgs', 'IdentityArgsDict']]] = None,
                 is_availability_zones_enabled: Optional[pulumi.Input[bool]] = None,
                 is_double_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 key_vault_properties: Optional[pulumi.Input[Union['KeyVaultPropertiesArgs', 'KeyVaultPropertiesArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['ClusterSkuArgs', 'ClusterSkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["billing_type"] = billing_type
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["is_availability_zones_enabled"] = is_availability_zones_enabled
            __props__.__dict__["is_double_encryption_enabled"] = is_double_encryption_enabled
            __props__.__dict__["key_vault_properties"] = key_vault_properties
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["associated_workspaces"] = None
            __props__.__dict__["capacity_reservation_properties"] = None
            __props__.__dict__["cluster_id"] = None
            __props__.__dict__["created_date"] = None
            __props__.__dict__["last_modified_date"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:operationalinsights:Cluster"), pulumi.Alias(type_="azure-native:operationalinsights/v20190801preview:Cluster"), pulumi.Alias(type_="azure-native:operationalinsights/v20200301preview:Cluster"), pulumi.Alias(type_="azure-native:operationalinsights/v20200801:Cluster"), pulumi.Alias(type_="azure-native:operationalinsights/v20201001:Cluster"), pulumi.Alias(type_="azure-native:operationalinsights/v20221001:Cluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Cluster, __self__).__init__(
            'azure-native:operationalinsights/v20210601:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["associated_workspaces"] = None
        __props__.__dict__["billing_type"] = None
        __props__.__dict__["capacity_reservation_properties"] = None
        __props__.__dict__["cluster_id"] = None
        __props__.__dict__["created_date"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["is_availability_zones_enabled"] = None
        __props__.__dict__["is_double_encryption_enabled"] = None
        __props__.__dict__["key_vault_properties"] = None
        __props__.__dict__["last_modified_date"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedWorkspaces")
    def associated_workspaces(self) -> pulumi.Output[Optional[Sequence['outputs.AssociatedWorkspaceResponse']]]:
        """
        The list of Log Analytics workspaces associated with the cluster
        """
        return pulumi.get(self, "associated_workspaces")

    @property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> pulumi.Output[Optional[str]]:
        """
        The cluster's billing type.
        """
        return pulumi.get(self, "billing_type")

    @property
    @pulumi.getter(name="capacityReservationProperties")
    def capacity_reservation_properties(self) -> pulumi.Output[Optional['outputs.CapacityReservationPropertiesResponse']]:
        """
        Additional properties for capacity reservation
        """
        return pulumi.get(self, "capacity_reservation_properties")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID associated with the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        The cluster creation time
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="isAvailabilityZonesEnabled")
    def is_availability_zones_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Sets whether the cluster will support availability zones. This can be set as true only in regions where Azure Data Explorer support Availability Zones. This Property can not be modified after cluster creation. Default value is 'true' if region supports Availability Zones.
        """
        return pulumi.get(self, "is_availability_zones_enabled")

    @property
    @pulumi.getter(name="isDoubleEncryptionEnabled")
    def is_double_encryption_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Configures whether cluster will use double encryption. This Property can not be modified after cluster creation. Default value is 'true'
        """
        return pulumi.get(self, "is_double_encryption_enabled")

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> pulumi.Output[Optional['outputs.KeyVaultPropertiesResponse']]:
        """
        The associated key properties.
        """
        return pulumi.get(self, "key_vault_properties")

    @property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> pulumi.Output[str]:
        """
        The last time the cluster was updated.
        """
        return pulumi.get(self, "last_modified_date")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the cluster.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.ClusterSkuResponse']]:
        """
        The sku properties.
        """
        return pulumi.get(self, "sku")

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

