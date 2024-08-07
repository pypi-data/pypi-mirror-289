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

__all__ = ['AttachedDataNetworkArgs', 'AttachedDataNetwork']

@pulumi.input_type
class AttachedDataNetworkArgs:
    def __init__(__self__, *,
                 dns_addresses: pulumi.Input[Sequence[pulumi.Input[str]]],
                 packet_core_control_plane_name: pulumi.Input[str],
                 packet_core_data_plane_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 user_plane_data_interface: pulumi.Input['InterfacePropertiesArgs'],
                 attached_data_network_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 napt_configuration: Optional[pulumi.Input['NaptConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_equipment_address_pool_prefix: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_equipment_static_address_pool_prefix: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AttachedDataNetwork resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_addresses: The DNS servers to signal to UEs to use for this attached data network. This configuration is mandatory - if you don't want DNS servers, you must provide an empty array.
        :param pulumi.Input[str] packet_core_control_plane_name: The name of the packet core control plane.
        :param pulumi.Input[str] packet_core_data_plane_name: The name of the packet core data plane.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['InterfacePropertiesArgs'] user_plane_data_interface: The user plane interface on the data network. For 5G networks, this is the N6 interface. For 4G networks, this is the SGi interface.
        :param pulumi.Input[str] attached_data_network_name: The name of the attached data network.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['NaptConfigurationArgs'] napt_configuration: The network address and port translation (NAPT) configuration.
               If this is not specified, the attached data network will use a default NAPT configuration with NAPT enabled.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_equipment_address_pool_prefix: The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will dynamically assign IP addresses to UEs.
               The packet core instance assigns an IP address to a UE when the UE sets up a PDU session.
                You must define at least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix. If you define both, they must be of the same size.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_equipment_static_address_pool_prefix: The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will assign static IP addresses to UEs.
               The packet core instance assigns an IP address to a UE when the UE sets up a PDU session. The static IP address for a specific UE is set in StaticIPConfiguration on the corresponding SIM resource.
               At least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix must be defined. If both are defined, they must be of the same size.
        """
        pulumi.set(__self__, "dns_addresses", dns_addresses)
        pulumi.set(__self__, "packet_core_control_plane_name", packet_core_control_plane_name)
        pulumi.set(__self__, "packet_core_data_plane_name", packet_core_data_plane_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "user_plane_data_interface", user_plane_data_interface)
        if attached_data_network_name is not None:
            pulumi.set(__self__, "attached_data_network_name", attached_data_network_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if napt_configuration is not None:
            pulumi.set(__self__, "napt_configuration", napt_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_equipment_address_pool_prefix is not None:
            pulumi.set(__self__, "user_equipment_address_pool_prefix", user_equipment_address_pool_prefix)
        if user_equipment_static_address_pool_prefix is not None:
            pulumi.set(__self__, "user_equipment_static_address_pool_prefix", user_equipment_static_address_pool_prefix)

    @property
    @pulumi.getter(name="dnsAddresses")
    def dns_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The DNS servers to signal to UEs to use for this attached data network. This configuration is mandatory - if you don't want DNS servers, you must provide an empty array.
        """
        return pulumi.get(self, "dns_addresses")

    @dns_addresses.setter
    def dns_addresses(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "dns_addresses", value)

    @property
    @pulumi.getter(name="packetCoreControlPlaneName")
    def packet_core_control_plane_name(self) -> pulumi.Input[str]:
        """
        The name of the packet core control plane.
        """
        return pulumi.get(self, "packet_core_control_plane_name")

    @packet_core_control_plane_name.setter
    def packet_core_control_plane_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "packet_core_control_plane_name", value)

    @property
    @pulumi.getter(name="packetCoreDataPlaneName")
    def packet_core_data_plane_name(self) -> pulumi.Input[str]:
        """
        The name of the packet core data plane.
        """
        return pulumi.get(self, "packet_core_data_plane_name")

    @packet_core_data_plane_name.setter
    def packet_core_data_plane_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "packet_core_data_plane_name", value)

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
    @pulumi.getter(name="userPlaneDataInterface")
    def user_plane_data_interface(self) -> pulumi.Input['InterfacePropertiesArgs']:
        """
        The user plane interface on the data network. For 5G networks, this is the N6 interface. For 4G networks, this is the SGi interface.
        """
        return pulumi.get(self, "user_plane_data_interface")

    @user_plane_data_interface.setter
    def user_plane_data_interface(self, value: pulumi.Input['InterfacePropertiesArgs']):
        pulumi.set(self, "user_plane_data_interface", value)

    @property
    @pulumi.getter(name="attachedDataNetworkName")
    def attached_data_network_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the attached data network.
        """
        return pulumi.get(self, "attached_data_network_name")

    @attached_data_network_name.setter
    def attached_data_network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attached_data_network_name", value)

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
    @pulumi.getter(name="naptConfiguration")
    def napt_configuration(self) -> Optional[pulumi.Input['NaptConfigurationArgs']]:
        """
        The network address and port translation (NAPT) configuration.
        If this is not specified, the attached data network will use a default NAPT configuration with NAPT enabled.
        """
        return pulumi.get(self, "napt_configuration")

    @napt_configuration.setter
    def napt_configuration(self, value: Optional[pulumi.Input['NaptConfigurationArgs']]):
        pulumi.set(self, "napt_configuration", value)

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
    @pulumi.getter(name="userEquipmentAddressPoolPrefix")
    def user_equipment_address_pool_prefix(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will dynamically assign IP addresses to UEs.
        The packet core instance assigns an IP address to a UE when the UE sets up a PDU session.
         You must define at least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix. If you define both, they must be of the same size.
        """
        return pulumi.get(self, "user_equipment_address_pool_prefix")

    @user_equipment_address_pool_prefix.setter
    def user_equipment_address_pool_prefix(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_equipment_address_pool_prefix", value)

    @property
    @pulumi.getter(name="userEquipmentStaticAddressPoolPrefix")
    def user_equipment_static_address_pool_prefix(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will assign static IP addresses to UEs.
        The packet core instance assigns an IP address to a UE when the UE sets up a PDU session. The static IP address for a specific UE is set in StaticIPConfiguration on the corresponding SIM resource.
        At least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix must be defined. If both are defined, they must be of the same size.
        """
        return pulumi.get(self, "user_equipment_static_address_pool_prefix")

    @user_equipment_static_address_pool_prefix.setter
    def user_equipment_static_address_pool_prefix(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_equipment_static_address_pool_prefix", value)


class AttachedDataNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_data_network_name: Optional[pulumi.Input[str]] = None,
                 dns_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 napt_configuration: Optional[pulumi.Input[Union['NaptConfigurationArgs', 'NaptConfigurationArgsDict']]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 packet_core_data_plane_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_equipment_address_pool_prefix: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_equipment_static_address_pool_prefix: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_plane_data_interface: Optional[pulumi.Input[Union['InterfacePropertiesArgs', 'InterfacePropertiesArgsDict']]] = None,
                 __props__=None):
        """
        Attached data network resource. Must be created in the same location as its parent packet core data plane.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] attached_data_network_name: The name of the attached data network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_addresses: The DNS servers to signal to UEs to use for this attached data network. This configuration is mandatory - if you don't want DNS servers, you must provide an empty array.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union['NaptConfigurationArgs', 'NaptConfigurationArgsDict']] napt_configuration: The network address and port translation (NAPT) configuration.
               If this is not specified, the attached data network will use a default NAPT configuration with NAPT enabled.
        :param pulumi.Input[str] packet_core_control_plane_name: The name of the packet core control plane.
        :param pulumi.Input[str] packet_core_data_plane_name: The name of the packet core data plane.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_equipment_address_pool_prefix: The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will dynamically assign IP addresses to UEs.
               The packet core instance assigns an IP address to a UE when the UE sets up a PDU session.
                You must define at least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix. If you define both, they must be of the same size.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_equipment_static_address_pool_prefix: The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will assign static IP addresses to UEs.
               The packet core instance assigns an IP address to a UE when the UE sets up a PDU session. The static IP address for a specific UE is set in StaticIPConfiguration on the corresponding SIM resource.
               At least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix must be defined. If both are defined, they must be of the same size.
        :param pulumi.Input[Union['InterfacePropertiesArgs', 'InterfacePropertiesArgsDict']] user_plane_data_interface: The user plane interface on the data network. For 5G networks, this is the N6 interface. For 4G networks, this is the SGi interface.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AttachedDataNetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Attached data network resource. Must be created in the same location as its parent packet core data plane.

        :param str resource_name: The name of the resource.
        :param AttachedDataNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AttachedDataNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_data_network_name: Optional[pulumi.Input[str]] = None,
                 dns_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 napt_configuration: Optional[pulumi.Input[Union['NaptConfigurationArgs', 'NaptConfigurationArgsDict']]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 packet_core_data_plane_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_equipment_address_pool_prefix: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_equipment_static_address_pool_prefix: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_plane_data_interface: Optional[pulumi.Input[Union['InterfacePropertiesArgs', 'InterfacePropertiesArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AttachedDataNetworkArgs.__new__(AttachedDataNetworkArgs)

            __props__.__dict__["attached_data_network_name"] = attached_data_network_name
            if dns_addresses is None and not opts.urn:
                raise TypeError("Missing required property 'dns_addresses'")
            __props__.__dict__["dns_addresses"] = dns_addresses
            __props__.__dict__["location"] = location
            __props__.__dict__["napt_configuration"] = napt_configuration
            if packet_core_control_plane_name is None and not opts.urn:
                raise TypeError("Missing required property 'packet_core_control_plane_name'")
            __props__.__dict__["packet_core_control_plane_name"] = packet_core_control_plane_name
            if packet_core_data_plane_name is None and not opts.urn:
                raise TypeError("Missing required property 'packet_core_data_plane_name'")
            __props__.__dict__["packet_core_data_plane_name"] = packet_core_data_plane_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["user_equipment_address_pool_prefix"] = user_equipment_address_pool_prefix
            __props__.__dict__["user_equipment_static_address_pool_prefix"] = user_equipment_static_address_pool_prefix
            if user_plane_data_interface is None and not opts.urn:
                raise TypeError("Missing required property 'user_plane_data_interface'")
            __props__.__dict__["user_plane_data_interface"] = user_plane_data_interface
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:mobilenetwork:AttachedDataNetwork"), pulumi.Alias(type_="azure-native:mobilenetwork/v20220301preview:AttachedDataNetwork"), pulumi.Alias(type_="azure-native:mobilenetwork/v20220401preview:AttachedDataNetwork"), pulumi.Alias(type_="azure-native:mobilenetwork/v20221101:AttachedDataNetwork"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230601:AttachedDataNetwork"), pulumi.Alias(type_="azure-native:mobilenetwork/v20240201:AttachedDataNetwork"), pulumi.Alias(type_="azure-native:mobilenetwork/v20240401:AttachedDataNetwork")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AttachedDataNetwork, __self__).__init__(
            'azure-native:mobilenetwork/v20230901:AttachedDataNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AttachedDataNetwork':
        """
        Get an existing AttachedDataNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AttachedDataNetworkArgs.__new__(AttachedDataNetworkArgs)

        __props__.__dict__["dns_addresses"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["napt_configuration"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_equipment_address_pool_prefix"] = None
        __props__.__dict__["user_equipment_static_address_pool_prefix"] = None
        __props__.__dict__["user_plane_data_interface"] = None
        return AttachedDataNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dnsAddresses")
    def dns_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        The DNS servers to signal to UEs to use for this attached data network. This configuration is mandatory - if you don't want DNS servers, you must provide an empty array.
        """
        return pulumi.get(self, "dns_addresses")

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
    @pulumi.getter(name="naptConfiguration")
    def napt_configuration(self) -> pulumi.Output[Optional['outputs.NaptConfigurationResponse']]:
        """
        The network address and port translation (NAPT) configuration.
        If this is not specified, the attached data network will use a default NAPT configuration with NAPT enabled.
        """
        return pulumi.get(self, "napt_configuration")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the attached data network resource.
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
    @pulumi.getter(name="userEquipmentAddressPoolPrefix")
    def user_equipment_address_pool_prefix(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will dynamically assign IP addresses to UEs.
        The packet core instance assigns an IP address to a UE when the UE sets up a PDU session.
         You must define at least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix. If you define both, they must be of the same size.
        """
        return pulumi.get(self, "user_equipment_address_pool_prefix")

    @property
    @pulumi.getter(name="userEquipmentStaticAddressPoolPrefix")
    def user_equipment_static_address_pool_prefix(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will assign static IP addresses to UEs.
        The packet core instance assigns an IP address to a UE when the UE sets up a PDU session. The static IP address for a specific UE is set in StaticIPConfiguration on the corresponding SIM resource.
        At least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix must be defined. If both are defined, they must be of the same size.
        """
        return pulumi.get(self, "user_equipment_static_address_pool_prefix")

    @property
    @pulumi.getter(name="userPlaneDataInterface")
    def user_plane_data_interface(self) -> pulumi.Output['outputs.InterfacePropertiesResponse']:
        """
        The user plane interface on the data network. For 5G networks, this is the N6 interface. For 4G networks, this is the SGi interface.
        """
        return pulumi.get(self, "user_plane_data_interface")

