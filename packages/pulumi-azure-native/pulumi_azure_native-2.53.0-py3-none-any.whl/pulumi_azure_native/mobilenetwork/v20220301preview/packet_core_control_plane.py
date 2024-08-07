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

__all__ = ['PacketCoreControlPlaneArgs', 'PacketCoreControlPlane']

@pulumi.input_type
class PacketCoreControlPlaneArgs:
    def __init__(__self__, *,
                 control_plane_access_interface: pulumi.Input['InterfacePropertiesArgs'],
                 mobile_network: pulumi.Input['MobileNetworkResourceIdArgs'],
                 resource_group_name: pulumi.Input[str],
                 core_network_technology: Optional[pulumi.Input[Union[str, 'CoreNetworkType']]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 custom_location: Optional[pulumi.Input['CustomLocationResourceIdArgs']] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PacketCoreControlPlane resource.
        :param pulumi.Input['InterfacePropertiesArgs'] control_plane_access_interface: The control plane interface on the access network. In 5G networks this is called as N2 interface whereas in 4G networks this is called as S1-MME interface.
        :param pulumi.Input['MobileNetworkResourceIdArgs'] mobile_network: Mobile network that this packet core control plane belongs to
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'CoreNetworkType']] core_network_technology: The core network technology generation.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input['CustomLocationResourceIdArgs'] custom_location: Azure ARC custom location where the packet core is deployed.
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] packet_core_control_plane_name: The name of the packet core control plane.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] version: The version of the packet core software that is deployed.
        """
        pulumi.set(__self__, "control_plane_access_interface", control_plane_access_interface)
        pulumi.set(__self__, "mobile_network", mobile_network)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if core_network_technology is not None:
            pulumi.set(__self__, "core_network_technology", core_network_technology)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if custom_location is not None:
            pulumi.set(__self__, "custom_location", custom_location)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if packet_core_control_plane_name is not None:
            pulumi.set(__self__, "packet_core_control_plane_name", packet_core_control_plane_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="controlPlaneAccessInterface")
    def control_plane_access_interface(self) -> pulumi.Input['InterfacePropertiesArgs']:
        """
        The control plane interface on the access network. In 5G networks this is called as N2 interface whereas in 4G networks this is called as S1-MME interface.
        """
        return pulumi.get(self, "control_plane_access_interface")

    @control_plane_access_interface.setter
    def control_plane_access_interface(self, value: pulumi.Input['InterfacePropertiesArgs']):
        pulumi.set(self, "control_plane_access_interface", value)

    @property
    @pulumi.getter(name="mobileNetwork")
    def mobile_network(self) -> pulumi.Input['MobileNetworkResourceIdArgs']:
        """
        Mobile network that this packet core control plane belongs to
        """
        return pulumi.get(self, "mobile_network")

    @mobile_network.setter
    def mobile_network(self, value: pulumi.Input['MobileNetworkResourceIdArgs']):
        pulumi.set(self, "mobile_network", value)

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
    @pulumi.getter(name="coreNetworkTechnology")
    def core_network_technology(self) -> Optional[pulumi.Input[Union[str, 'CoreNetworkType']]]:
        """
        The core network technology generation.
        """
        return pulumi.get(self, "core_network_technology")

    @core_network_technology.setter
    def core_network_technology(self, value: Optional[pulumi.Input[Union[str, 'CoreNetworkType']]]):
        pulumi.set(self, "core_network_technology", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @created_by_type.setter
    def created_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "created_by_type", value)

    @property
    @pulumi.getter(name="customLocation")
    def custom_location(self) -> Optional[pulumi.Input['CustomLocationResourceIdArgs']]:
        """
        Azure ARC custom location where the packet core is deployed.
        """
        return pulumi.get(self, "custom_location")

    @custom_location.setter
    def custom_location(self, value: Optional[pulumi.Input['CustomLocationResourceIdArgs']]):
        pulumi.set(self, "custom_location", value)

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_at", value)

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @last_modified_by.setter
    def last_modified_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_by", value)

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @last_modified_by_type.setter
    def last_modified_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "last_modified_by_type", value)

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
    @pulumi.getter(name="packetCoreControlPlaneName")
    def packet_core_control_plane_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the packet core control plane.
        """
        return pulumi.get(self, "packet_core_control_plane_name")

    @packet_core_control_plane_name.setter
    def packet_core_control_plane_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "packet_core_control_plane_name", value)

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
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the packet core software that is deployed.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class PacketCoreControlPlane(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_plane_access_interface: Optional[pulumi.Input[Union['InterfacePropertiesArgs', 'InterfacePropertiesArgsDict']]] = None,
                 core_network_technology: Optional[pulumi.Input[Union[str, 'CoreNetworkType']]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 custom_location: Optional[pulumi.Input[Union['CustomLocationResourceIdArgs', 'CustomLocationResourceIdArgsDict']]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network: Optional[pulumi.Input[Union['MobileNetworkResourceIdArgs', 'MobileNetworkResourceIdArgsDict']]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Packet core control plane resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['InterfacePropertiesArgs', 'InterfacePropertiesArgsDict']] control_plane_access_interface: The control plane interface on the access network. In 5G networks this is called as N2 interface whereas in 4G networks this is called as S1-MME interface.
        :param pulumi.Input[Union[str, 'CoreNetworkType']] core_network_technology: The core network technology generation.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input[Union['CustomLocationResourceIdArgs', 'CustomLocationResourceIdArgsDict']] custom_location: Azure ARC custom location where the packet core is deployed.
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union['MobileNetworkResourceIdArgs', 'MobileNetworkResourceIdArgsDict']] mobile_network: Mobile network that this packet core control plane belongs to
        :param pulumi.Input[str] packet_core_control_plane_name: The name of the packet core control plane.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] version: The version of the packet core software that is deployed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PacketCoreControlPlaneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Packet core control plane resource.

        :param str resource_name: The name of the resource.
        :param PacketCoreControlPlaneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PacketCoreControlPlaneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_plane_access_interface: Optional[pulumi.Input[Union['InterfacePropertiesArgs', 'InterfacePropertiesArgsDict']]] = None,
                 core_network_technology: Optional[pulumi.Input[Union[str, 'CoreNetworkType']]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 custom_location: Optional[pulumi.Input[Union['CustomLocationResourceIdArgs', 'CustomLocationResourceIdArgsDict']]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network: Optional[pulumi.Input[Union['MobileNetworkResourceIdArgs', 'MobileNetworkResourceIdArgsDict']]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PacketCoreControlPlaneArgs.__new__(PacketCoreControlPlaneArgs)

            if control_plane_access_interface is None and not opts.urn:
                raise TypeError("Missing required property 'control_plane_access_interface'")
            __props__.__dict__["control_plane_access_interface"] = control_plane_access_interface
            __props__.__dict__["core_network_technology"] = core_network_technology
            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["created_by_type"] = created_by_type
            __props__.__dict__["custom_location"] = custom_location
            __props__.__dict__["last_modified_at"] = last_modified_at
            __props__.__dict__["last_modified_by"] = last_modified_by
            __props__.__dict__["last_modified_by_type"] = last_modified_by_type
            __props__.__dict__["location"] = location
            if mobile_network is None and not opts.urn:
                raise TypeError("Missing required property 'mobile_network'")
            __props__.__dict__["mobile_network"] = mobile_network
            __props__.__dict__["packet_core_control_plane_name"] = packet_core_control_plane_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["version"] = version
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:mobilenetwork:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20220401preview:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20221101:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230601:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230901:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20240201:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20240401:PacketCoreControlPlane")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PacketCoreControlPlane, __self__).__init__(
            'azure-native:mobilenetwork/v20220301preview:PacketCoreControlPlane',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PacketCoreControlPlane':
        """
        Get an existing PacketCoreControlPlane resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PacketCoreControlPlaneArgs.__new__(PacketCoreControlPlaneArgs)

        __props__.__dict__["control_plane_access_interface"] = None
        __props__.__dict__["core_network_technology"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["created_by_type"] = None
        __props__.__dict__["custom_location"] = None
        __props__.__dict__["last_modified_at"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_by_type"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mobile_network"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return PacketCoreControlPlane(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="controlPlaneAccessInterface")
    def control_plane_access_interface(self) -> pulumi.Output['outputs.InterfacePropertiesResponse']:
        """
        The control plane interface on the access network. In 5G networks this is called as N2 interface whereas in 4G networks this is called as S1-MME interface.
        """
        return pulumi.get(self, "control_plane_access_interface")

    @property
    @pulumi.getter(name="coreNetworkTechnology")
    def core_network_technology(self) -> pulumi.Output[Optional[str]]:
        """
        The core network technology generation.
        """
        return pulumi.get(self, "core_network_technology")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="customLocation")
    def custom_location(self) -> pulumi.Output[Optional['outputs.CustomLocationResourceIdResponse']]:
        """
        Azure ARC custom location where the packet core is deployed.
        """
        return pulumi.get(self, "custom_location")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mobileNetwork")
    def mobile_network(self) -> pulumi.Output['outputs.MobileNetworkResourceIdResponse']:
        """
        Mobile network that this packet core control plane belongs to
        """
        return pulumi.get(self, "mobile_network")

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
        The provisioning state of the packet core control plane resource.
        """
        return pulumi.get(self, "provisioning_state")

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
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of the packet core software that is deployed.
        """
        return pulumi.get(self, "version")

