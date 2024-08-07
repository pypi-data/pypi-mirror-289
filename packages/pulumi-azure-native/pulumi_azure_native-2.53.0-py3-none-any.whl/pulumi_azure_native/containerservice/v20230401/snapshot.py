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

__all__ = ['SnapshotArgs', 'Snapshot']

@pulumi.input_type
class SnapshotArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 creation_data: Optional[pulumi.Input['CreationDataArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 snapshot_type: Optional[pulumi.Input[Union[str, 'SnapshotType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Snapshot resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['CreationDataArgs'] creation_data: CreationData to be used to specify the source agent pool resource ID to create this snapshot.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_name: The name of the managed cluster resource.
        :param pulumi.Input[Union[str, 'SnapshotType']] snapshot_type: The type of a snapshot. The default is NodePool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if creation_data is not None:
            pulumi.set(__self__, "creation_data", creation_data)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if snapshot_type is not None:
            pulumi.set(__self__, "snapshot_type", snapshot_type)
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
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional[pulumi.Input['CreationDataArgs']]:
        """
        CreationData to be used to specify the source agent pool resource ID to create this snapshot.
        """
        return pulumi.get(self, "creation_data")

    @creation_data.setter
    def creation_data(self, value: Optional[pulumi.Input['CreationDataArgs']]):
        pulumi.set(self, "creation_data", value)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the managed cluster resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[pulumi.Input[Union[str, 'SnapshotType']]]:
        """
        The type of a snapshot. The default is NodePool.
        """
        return pulumi.get(self, "snapshot_type")

    @snapshot_type.setter
    def snapshot_type(self, value: Optional[pulumi.Input[Union[str, 'SnapshotType']]]):
        pulumi.set(self, "snapshot_type", value)

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


class Snapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_data: Optional[pulumi.Input[Union['CreationDataArgs', 'CreationDataArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 snapshot_type: Optional[pulumi.Input[Union[str, 'SnapshotType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A node pool snapshot resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['CreationDataArgs', 'CreationDataArgsDict']] creation_data: CreationData to be used to specify the source agent pool resource ID to create this snapshot.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the managed cluster resource.
        :param pulumi.Input[Union[str, 'SnapshotType']] snapshot_type: The type of a snapshot. The default is NodePool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SnapshotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A node pool snapshot resource.

        :param str resource_name: The name of the resource.
        :param SnapshotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SnapshotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_data: Optional[pulumi.Input[Union['CreationDataArgs', 'CreationDataArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 snapshot_type: Optional[pulumi.Input[Union[str, 'SnapshotType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SnapshotArgs.__new__(SnapshotArgs)

            __props__.__dict__["creation_data"] = creation_data
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["snapshot_type"] = snapshot_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["enable_fips"] = None
            __props__.__dict__["kubernetes_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["node_image_version"] = None
            __props__.__dict__["os_sku"] = None
            __props__.__dict__["os_type"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["vm_size"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerservice:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20210801:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20210901:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20211001:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20211101preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220101:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220102preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220201:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220202preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220301:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220302preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220401:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220402preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220502preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220601:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220602preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220701:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220702preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220802preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220803preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220901:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20220902preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20221002preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20221101:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20221102preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230101:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230102preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230201:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230202preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230301:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230302preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230402preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230501:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230502preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230601:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230602preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230701:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230702preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230801:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230802preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230901:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20230902preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20231001:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20231002preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20231101:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20231102preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20240101:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20240102preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20240201:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20240202preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20240302preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20240402preview:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20240501:Snapshot"), pulumi.Alias(type_="azure-native:containerservice/v20240502preview:Snapshot")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Snapshot, __self__).__init__(
            'azure-native:containerservice/v20230401:Snapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Snapshot':
        """
        Get an existing Snapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SnapshotArgs.__new__(SnapshotArgs)

        __props__.__dict__["creation_data"] = None
        __props__.__dict__["enable_fips"] = None
        __props__.__dict__["kubernetes_version"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["node_image_version"] = None
        __props__.__dict__["os_sku"] = None
        __props__.__dict__["os_type"] = None
        __props__.__dict__["snapshot_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vm_size"] = None
        return Snapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Output[Optional['outputs.CreationDataResponse']]:
        """
        CreationData to be used to specify the source agent pool resource ID to create this snapshot.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter(name="enableFIPS")
    def enable_fips(self) -> pulumi.Output[bool]:
        """
        Whether to use a FIPS-enabled OS.
        """
        return pulumi.get(self, "enable_fips")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[str]:
        """
        The version of Kubernetes.
        """
        return pulumi.get(self, "kubernetes_version")

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
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> pulumi.Output[str]:
        """
        The version of node image.
        """
        return pulumi.get(self, "node_image_version")

    @property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> pulumi.Output[str]:
        """
        Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The default is Windows2019 when Kubernetes <= 1.24 or Windows2022 when Kubernetes >= 1.25 if OSType is Windows.
        """
        return pulumi.get(self, "os_sku")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[str]:
        """
        The operating system type. The default is Linux.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of a snapshot. The default is NodePool.
        """
        return pulumi.get(self, "snapshot_type")

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

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> pulumi.Output[str]:
        """
        The size of the VM.
        """
        return pulumi.get(self, "vm_size")

