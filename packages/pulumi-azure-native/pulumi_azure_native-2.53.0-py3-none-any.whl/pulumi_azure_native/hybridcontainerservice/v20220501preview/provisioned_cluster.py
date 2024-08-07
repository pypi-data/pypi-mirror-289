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

__all__ = ['ProvisionedClusterArgs', 'ProvisionedCluster']

@pulumi.input_type
class ProvisionedClusterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 extended_location: Optional[pulumi.Input['ProvisionedClustersExtendedLocationArgs']] = None,
                 identity: Optional[pulumi.Input['ProvisionedClusterIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['ProvisionedClustersAllPropertiesArgs']] = None,
                 provisioned_clusters_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ProvisionedCluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ProvisionedClusterIdentityArgs'] identity: Identity for the Provisioned cluster.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['ProvisionedClustersAllPropertiesArgs'] properties: All properties of the provisioned cluster
        :param pulumi.Input[str] provisioned_clusters_name: Parameter for the name of the provisioned cluster
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if provisioned_clusters_name is not None:
            pulumi.set(__self__, "provisioned_clusters_name", provisioned_clusters_name)
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
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ProvisionedClustersExtendedLocationArgs']]:
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ProvisionedClustersExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ProvisionedClusterIdentityArgs']]:
        """
        Identity for the Provisioned cluster.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ProvisionedClusterIdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    def properties(self) -> Optional[pulumi.Input['ProvisionedClustersAllPropertiesArgs']]:
        """
        All properties of the provisioned cluster
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ProvisionedClustersAllPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="provisionedClustersName")
    def provisioned_clusters_name(self) -> Optional[pulumi.Input[str]]:
        """
        Parameter for the name of the provisioned cluster
        """
        return pulumi.get(self, "provisioned_clusters_name")

    @provisioned_clusters_name.setter
    def provisioned_clusters_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioned_clusters_name", value)

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


class ProvisionedCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[Union['ProvisionedClustersExtendedLocationArgs', 'ProvisionedClustersExtendedLocationArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['ProvisionedClusterIdentityArgs', 'ProvisionedClusterIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['ProvisionedClustersAllPropertiesArgs', 'ProvisionedClustersAllPropertiesArgsDict']]] = None,
                 provisioned_clusters_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The provisionedClusters resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ProvisionedClusterIdentityArgs', 'ProvisionedClusterIdentityArgsDict']] identity: Identity for the Provisioned cluster.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union['ProvisionedClustersAllPropertiesArgs', 'ProvisionedClustersAllPropertiesArgsDict']] properties: All properties of the provisioned cluster
        :param pulumi.Input[str] provisioned_clusters_name: Parameter for the name of the provisioned cluster
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProvisionedClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provisionedClusters resource definition.

        :param str resource_name: The name of the resource.
        :param ProvisionedClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProvisionedClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[Union['ProvisionedClustersExtendedLocationArgs', 'ProvisionedClustersExtendedLocationArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['ProvisionedClusterIdentityArgs', 'ProvisionedClusterIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['ProvisionedClustersAllPropertiesArgs', 'ProvisionedClustersAllPropertiesArgsDict']]] = None,
                 provisioned_clusters_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProvisionedClusterArgs.__new__(ProvisionedClusterArgs)

            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            __props__.__dict__["provisioned_clusters_name"] = provisioned_clusters_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybridcontainerservice:ProvisionedCluster"), pulumi.Alias(type_="azure-native:hybridcontainerservice/v20220901preview:ProvisionedCluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ProvisionedCluster, __self__).__init__(
            'azure-native:hybridcontainerservice/v20220501preview:ProvisionedCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProvisionedCluster':
        """
        Get an existing ProvisionedCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProvisionedClusterArgs.__new__(ProvisionedClusterArgs)

        __props__.__dict__["extended_location"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ProvisionedCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ProvisionedClustersResponseResponseExtendedLocation']]:
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ProvisionedClusterIdentityResponse']]:
        """
        Identity for the Provisioned cluster.
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
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ProvisionedClustersResponsePropertiesResponse']:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
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

