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

__all__ = [
    'GuestOSCustomizationResponse',
    'GuestOSNICCustomizationResponse',
    'ResourcePoolResponse',
    'SkuResponse',
    'VirtualDiskControllerResponse',
    'VirtualDiskResponse',
    'VirtualNetworkResponse',
    'VirtualNicResponse',
]

@pulumi.output_type
class GuestOSCustomizationResponse(dict):
    """
    Guest OS Customization properties
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dnsServers":
            suggest = "dns_servers"
        elif key == "hostName":
            suggest = "host_name"
        elif key == "policyId":
            suggest = "policy_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GuestOSCustomizationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GuestOSCustomizationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GuestOSCustomizationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 dns_servers: Optional[Sequence[str]] = None,
                 host_name: Optional[str] = None,
                 password: Optional[str] = None,
                 policy_id: Optional[str] = None,
                 username: Optional[str] = None):
        """
        Guest OS Customization properties
        :param Sequence[str] dns_servers: List of dns servers to use
        :param str host_name: Virtual Machine hostname
        :param str password: Password for login
        :param str policy_id: id of customization policy
        :param str username: Username for login
        """
        if dns_servers is not None:
            pulumi.set(__self__, "dns_servers", dns_servers)
        if host_name is not None:
            pulumi.set(__self__, "host_name", host_name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[str]]:
        """
        List of dns servers to use
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[str]:
        """
        Virtual Machine hostname
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        Password for login
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[str]:
        """
        id of customization policy
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        """
        Username for login
        """
        return pulumi.get(self, "username")


@pulumi.output_type
class GuestOSNICCustomizationResponse(dict):
    """
    Guest OS nic customization
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dnsServers":
            suggest = "dns_servers"
        elif key == "ipAddress":
            suggest = "ip_address"
        elif key == "primaryWinsServer":
            suggest = "primary_wins_server"
        elif key == "secondaryWinsServer":
            suggest = "secondary_wins_server"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GuestOSNICCustomizationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GuestOSNICCustomizationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GuestOSNICCustomizationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allocation: Optional[str] = None,
                 dns_servers: Optional[Sequence[str]] = None,
                 gateway: Optional[Sequence[str]] = None,
                 ip_address: Optional[str] = None,
                 mask: Optional[str] = None,
                 primary_wins_server: Optional[str] = None,
                 secondary_wins_server: Optional[str] = None):
        """
        Guest OS nic customization
        :param str allocation: IP address allocation method
        :param Sequence[str] dns_servers: List of dns servers to use
        :param Sequence[str] gateway: Gateway addresses assigned to nic
        :param str ip_address: Static ip address for nic
        :param str mask: Network mask for nic
        :param str primary_wins_server: primary WINS server for Windows
        :param str secondary_wins_server: secondary WINS server for Windows
        """
        if allocation is not None:
            pulumi.set(__self__, "allocation", allocation)
        if dns_servers is not None:
            pulumi.set(__self__, "dns_servers", dns_servers)
        if gateway is not None:
            pulumi.set(__self__, "gateway", gateway)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if mask is not None:
            pulumi.set(__self__, "mask", mask)
        if primary_wins_server is not None:
            pulumi.set(__self__, "primary_wins_server", primary_wins_server)
        if secondary_wins_server is not None:
            pulumi.set(__self__, "secondary_wins_server", secondary_wins_server)

    @property
    @pulumi.getter
    def allocation(self) -> Optional[str]:
        """
        IP address allocation method
        """
        return pulumi.get(self, "allocation")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[str]]:
        """
        List of dns servers to use
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter
    def gateway(self) -> Optional[Sequence[str]]:
        """
        Gateway addresses assigned to nic
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[str]:
        """
        Static ip address for nic
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def mask(self) -> Optional[str]:
        """
        Network mask for nic
        """
        return pulumi.get(self, "mask")

    @property
    @pulumi.getter(name="primaryWinsServer")
    def primary_wins_server(self) -> Optional[str]:
        """
        primary WINS server for Windows
        """
        return pulumi.get(self, "primary_wins_server")

    @property
    @pulumi.getter(name="secondaryWinsServer")
    def secondary_wins_server(self) -> Optional[str]:
        """
        secondary WINS server for Windows
        """
        return pulumi.get(self, "secondary_wins_server")


@pulumi.output_type
class ResourcePoolResponse(dict):
    """
    Resource pool model
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fullName":
            suggest = "full_name"
        elif key == "privateCloudId":
            suggest = "private_cloud_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourcePoolResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourcePoolResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourcePoolResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 full_name: str,
                 id: str,
                 location: str,
                 name: str,
                 private_cloud_id: str,
                 type: str):
        """
        Resource pool model
        :param str full_name: Hierarchical resource pool name
        :param str id: resource pool id (privateCloudId:vsphereId)
        :param str location: Azure region
        :param str name: {ResourcePoolName}
        :param str private_cloud_id: The Private Cloud Id
        :param str type: {resourceProviderNamespace}/{resourceType}
        """
        pulumi.set(__self__, "full_name", full_name)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "private_cloud_id", private_cloud_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="fullName")
    def full_name(self) -> str:
        """
        Hierarchical resource pool name
        """
        return pulumi.get(self, "full_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        resource pool id (privateCloudId:vsphereId)
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Azure region
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        {ResourcePoolName}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateCloudId")
    def private_cloud_id(self) -> str:
        """
        The Private Cloud Id
        """
        return pulumi.get(self, "private_cloud_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        {resourceProviderNamespace}/{resourceType}
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class SkuResponse(dict):
    """
    The purchase SKU for CloudSimple paid resources
    """
    def __init__(__self__, *,
                 name: str,
                 capacity: Optional[str] = None,
                 description: Optional[str] = None,
                 family: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        The purchase SKU for CloudSimple paid resources
        :param str name: The name of the SKU for VMWare CloudSimple Node
        :param str capacity: The capacity of the SKU
        :param str description: dedicatedCloudNode example: 8 x Ten-Core Intel® Xeon® Processor E5-2640 v4 2.40GHz 25MB Cache (90W); 12 x 64GB PC4-19200 2400MHz DDR4 ECC Registered DIMM, ...
        :param str family: If the service has different generations of hardware, for the same SKU, then that can be captured here
        :param str tier: The tier of the SKU
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU for VMWare CloudSimple Node
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[str]:
        """
        The capacity of the SKU
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        dedicatedCloudNode example: 8 x Ten-Core Intel® Xeon® Processor E5-2640 v4 2.40GHz 25MB Cache (90W); 12 x 64GB PC4-19200 2400MHz DDR4 ECC Registered DIMM, ...
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def family(self) -> Optional[str]:
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        The tier of the SKU
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class VirtualDiskControllerResponse(dict):
    """
    Virtual disk controller model
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subType":
            suggest = "sub_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VirtualDiskControllerResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VirtualDiskControllerResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VirtualDiskControllerResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 name: str,
                 sub_type: str,
                 type: str):
        """
        Virtual disk controller model
        :param str id: Controller's id
        :param str name: The display name of Controller
        :param str sub_type: dik controller subtype (VMWARE_PARAVIRTUAL, BUS_PARALLEL, LSI_PARALLEL, LSI_SAS)
        :param str type: disk controller type (SCSI)
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "sub_type", sub_type)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Controller's id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The display name of Controller
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subType")
    def sub_type(self) -> str:
        """
        dik controller subtype (VMWARE_PARAVIRTUAL, BUS_PARALLEL, LSI_PARALLEL, LSI_SAS)
        """
        return pulumi.get(self, "sub_type")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        disk controller type (SCSI)
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class VirtualDiskResponse(dict):
    """
    Virtual disk model
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "controllerId":
            suggest = "controller_id"
        elif key == "independenceMode":
            suggest = "independence_mode"
        elif key == "totalSize":
            suggest = "total_size"
        elif key == "virtualDiskName":
            suggest = "virtual_disk_name"
        elif key == "virtualDiskId":
            suggest = "virtual_disk_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VirtualDiskResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VirtualDiskResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VirtualDiskResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 controller_id: str,
                 independence_mode: str,
                 total_size: int,
                 virtual_disk_name: str,
                 virtual_disk_id: Optional[str] = None):
        """
        Virtual disk model
        :param str controller_id: Disk's Controller id
        :param str independence_mode: Disk's independence mode type
        :param int total_size: Disk's total size
        :param str virtual_disk_name: Disk's display name
        :param str virtual_disk_id: Disk's id
        """
        pulumi.set(__self__, "controller_id", controller_id)
        pulumi.set(__self__, "independence_mode", independence_mode)
        pulumi.set(__self__, "total_size", total_size)
        pulumi.set(__self__, "virtual_disk_name", virtual_disk_name)
        if virtual_disk_id is not None:
            pulumi.set(__self__, "virtual_disk_id", virtual_disk_id)

    @property
    @pulumi.getter(name="controllerId")
    def controller_id(self) -> str:
        """
        Disk's Controller id
        """
        return pulumi.get(self, "controller_id")

    @property
    @pulumi.getter(name="independenceMode")
    def independence_mode(self) -> str:
        """
        Disk's independence mode type
        """
        return pulumi.get(self, "independence_mode")

    @property
    @pulumi.getter(name="totalSize")
    def total_size(self) -> int:
        """
        Disk's total size
        """
        return pulumi.get(self, "total_size")

    @property
    @pulumi.getter(name="virtualDiskName")
    def virtual_disk_name(self) -> str:
        """
        Disk's display name
        """
        return pulumi.get(self, "virtual_disk_name")

    @property
    @pulumi.getter(name="virtualDiskId")
    def virtual_disk_id(self) -> Optional[str]:
        """
        Disk's id
        """
        return pulumi.get(self, "virtual_disk_id")


@pulumi.output_type
class VirtualNetworkResponse(dict):
    """
    Virtual network model
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateCloudId":
            suggest = "private_cloud_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VirtualNetworkResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VirtualNetworkResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VirtualNetworkResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 assignable: bool,
                 id: str,
                 location: str,
                 name: str,
                 private_cloud_id: str,
                 type: str):
        """
        Virtual network model
        :param bool assignable: can be used in vm creation/deletion
        :param str id: virtual network id (privateCloudId:vsphereId)
        :param str location: Azure region
        :param str name: {VirtualNetworkName}
        :param str private_cloud_id: The Private Cloud id
        :param str type: {resourceProviderNamespace}/{resourceType}
        """
        pulumi.set(__self__, "assignable", assignable)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "private_cloud_id", private_cloud_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def assignable(self) -> bool:
        """
        can be used in vm creation/deletion
        """
        return pulumi.get(self, "assignable")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        virtual network id (privateCloudId:vsphereId)
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Azure region
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        {VirtualNetworkName}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateCloudId")
    def private_cloud_id(self) -> str:
        """
        The Private Cloud id
        """
        return pulumi.get(self, "private_cloud_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        {resourceProviderNamespace}/{resourceType}
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class VirtualNicResponse(dict):
    """
    Virtual NIC model
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nicType":
            suggest = "nic_type"
        elif key == "virtualNicName":
            suggest = "virtual_nic_name"
        elif key == "ipAddresses":
            suggest = "ip_addresses"
        elif key == "macAddress":
            suggest = "mac_address"
        elif key == "powerOnBoot":
            suggest = "power_on_boot"
        elif key == "virtualNicId":
            suggest = "virtual_nic_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VirtualNicResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VirtualNicResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VirtualNicResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 network: 'outputs.VirtualNetworkResponse',
                 nic_type: str,
                 virtual_nic_name: str,
                 customization: Optional['outputs.GuestOSNICCustomizationResponse'] = None,
                 ip_addresses: Optional[Sequence[str]] = None,
                 mac_address: Optional[str] = None,
                 power_on_boot: Optional[bool] = None,
                 virtual_nic_id: Optional[str] = None):
        """
        Virtual NIC model
        :param 'VirtualNetworkResponse' network: Virtual Network
        :param str nic_type: NIC type
        :param str virtual_nic_name: NIC name
        :param 'GuestOSNICCustomizationResponse' customization: guest OS customization for nic
        :param Sequence[str] ip_addresses: NIC ip address
        :param str mac_address: NIC MAC address
        :param bool power_on_boot: Is NIC powered on/off on boot
        :param str virtual_nic_id: NIC id
        """
        pulumi.set(__self__, "network", network)
        pulumi.set(__self__, "nic_type", nic_type)
        pulumi.set(__self__, "virtual_nic_name", virtual_nic_name)
        if customization is not None:
            pulumi.set(__self__, "customization", customization)
        if ip_addresses is not None:
            pulumi.set(__self__, "ip_addresses", ip_addresses)
        if mac_address is not None:
            pulumi.set(__self__, "mac_address", mac_address)
        if power_on_boot is not None:
            pulumi.set(__self__, "power_on_boot", power_on_boot)
        if virtual_nic_id is not None:
            pulumi.set(__self__, "virtual_nic_id", virtual_nic_id)

    @property
    @pulumi.getter
    def network(self) -> 'outputs.VirtualNetworkResponse':
        """
        Virtual Network
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> str:
        """
        NIC type
        """
        return pulumi.get(self, "nic_type")

    @property
    @pulumi.getter(name="virtualNicName")
    def virtual_nic_name(self) -> str:
        """
        NIC name
        """
        return pulumi.get(self, "virtual_nic_name")

    @property
    @pulumi.getter
    def customization(self) -> Optional['outputs.GuestOSNICCustomizationResponse']:
        """
        guest OS customization for nic
        """
        return pulumi.get(self, "customization")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[str]]:
        """
        NIC ip address
        """
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[str]:
        """
        NIC MAC address
        """
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter(name="powerOnBoot")
    def power_on_boot(self) -> Optional[bool]:
        """
        Is NIC powered on/off on boot
        """
        return pulumi.get(self, "power_on_boot")

    @property
    @pulumi.getter(name="virtualNicId")
    def virtual_nic_id(self) -> Optional[str]:
        """
        NIC id
        """
        return pulumi.get(self, "virtual_nic_id")


