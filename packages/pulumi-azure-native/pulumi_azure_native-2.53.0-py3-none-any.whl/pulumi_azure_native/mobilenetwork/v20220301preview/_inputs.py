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
from ._enums import *

__all__ = [
    'AttachedDataNetworkResourceIdArgs',
    'AttachedDataNetworkResourceIdArgsDict',
    'CustomLocationResourceIdArgs',
    'CustomLocationResourceIdArgsDict',
    'InterfacePropertiesArgs',
    'InterfacePropertiesArgsDict',
    'MobileNetworkResourceIdArgs',
    'MobileNetworkResourceIdArgsDict',
    'SimPolicyResourceIdArgs',
    'SimPolicyResourceIdArgsDict',
    'SimStaticIpPropertiesStaticIpArgs',
    'SimStaticIpPropertiesStaticIpArgsDict',
    'SimStaticIpPropertiesArgs',
    'SimStaticIpPropertiesArgsDict',
    'SliceResourceIdArgs',
    'SliceResourceIdArgsDict',
]

MYPY = False

if not MYPY:
    class AttachedDataNetworkResourceIdArgsDict(TypedDict):
        """
        Reference to an Attached Data Network resource.
        """
        id: pulumi.Input[str]
        """
        Attached Data Network resource ID.
        """
elif False:
    AttachedDataNetworkResourceIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AttachedDataNetworkResourceIdArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        Reference to an Attached Data Network resource.
        :param pulumi.Input[str] id: Attached Data Network resource ID.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Attached Data Network resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


if not MYPY:
    class CustomLocationResourceIdArgsDict(TypedDict):
        """
        Reference to an Azure ARC custom location resource.
        """
        id: pulumi.Input[str]
        """
        Azure ARC custom location resource ID.
        """
elif False:
    CustomLocationResourceIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CustomLocationResourceIdArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        Reference to an Azure ARC custom location resource.
        :param pulumi.Input[str] id: Azure ARC custom location resource ID.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Azure ARC custom location resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


if not MYPY:
    class InterfacePropertiesArgsDict(TypedDict):
        """
        Interface properties
        """
        name: pulumi.Input[str]
        """
        The logical name for this interface. This should match one of the interfaces configured on your Azure Stack Edge machine.
        """
        ipv4_address: NotRequired[pulumi.Input[str]]
        """
        The IPv4 address.
        """
        ipv4_gateway: NotRequired[pulumi.Input[str]]
        """
        The default IPv4 gateway (router).
        """
        ipv4_subnet: NotRequired[pulumi.Input[str]]
        """
        The IPv4 subnet.
        """
elif False:
    InterfacePropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class InterfacePropertiesArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 ipv4_address: Optional[pulumi.Input[str]] = None,
                 ipv4_gateway: Optional[pulumi.Input[str]] = None,
                 ipv4_subnet: Optional[pulumi.Input[str]] = None):
        """
        Interface properties
        :param pulumi.Input[str] name: The logical name for this interface. This should match one of the interfaces configured on your Azure Stack Edge machine.
        :param pulumi.Input[str] ipv4_address: The IPv4 address.
        :param pulumi.Input[str] ipv4_gateway: The default IPv4 gateway (router).
        :param pulumi.Input[str] ipv4_subnet: The IPv4 subnet.
        """
        pulumi.set(__self__, "name", name)
        if ipv4_address is not None:
            pulumi.set(__self__, "ipv4_address", ipv4_address)
        if ipv4_gateway is not None:
            pulumi.set(__self__, "ipv4_gateway", ipv4_gateway)
        if ipv4_subnet is not None:
            pulumi.set(__self__, "ipv4_subnet", ipv4_subnet)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The logical name for this interface. This should match one of the interfaces configured on your Azure Stack Edge machine.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address.
        """
        return pulumi.get(self, "ipv4_address")

    @ipv4_address.setter
    def ipv4_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_address", value)

    @property
    @pulumi.getter(name="ipv4Gateway")
    def ipv4_gateway(self) -> Optional[pulumi.Input[str]]:
        """
        The default IPv4 gateway (router).
        """
        return pulumi.get(self, "ipv4_gateway")

    @ipv4_gateway.setter
    def ipv4_gateway(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_gateway", value)

    @property
    @pulumi.getter(name="ipv4Subnet")
    def ipv4_subnet(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 subnet.
        """
        return pulumi.get(self, "ipv4_subnet")

    @ipv4_subnet.setter
    def ipv4_subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_subnet", value)


if not MYPY:
    class MobileNetworkResourceIdArgsDict(TypedDict):
        """
        Reference to a Mobile Network resource.
        """
        id: pulumi.Input[str]
        """
        Mobile Network resource ID.
        """
elif False:
    MobileNetworkResourceIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MobileNetworkResourceIdArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        Reference to a Mobile Network resource.
        :param pulumi.Input[str] id: Mobile Network resource ID.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Mobile Network resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


if not MYPY:
    class SimPolicyResourceIdArgsDict(TypedDict):
        """
        Reference to a SIM Policy resource.
        """
        id: pulumi.Input[str]
        """
        SIM Policy resource ID.
        """
elif False:
    SimPolicyResourceIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SimPolicyResourceIdArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        Reference to a SIM Policy resource.
        :param pulumi.Input[str] id: SIM Policy resource ID.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        SIM Policy resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


if not MYPY:
    class SimStaticIpPropertiesStaticIpArgsDict(TypedDict):
        """
        The static IP configuration for the sim to use at the defined network scope.
        """
        ipv4_address: NotRequired[pulumi.Input[str]]
        """
        The IPv4 address assigned to the sim at this network scope. This address must be in the userEquipmentStaticAddressPoolPrefix defined in the attachedDataNetwork.
        """
elif False:
    SimStaticIpPropertiesStaticIpArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SimStaticIpPropertiesStaticIpArgs:
    def __init__(__self__, *,
                 ipv4_address: Optional[pulumi.Input[str]] = None):
        """
        The static IP configuration for the sim to use at the defined network scope.
        :param pulumi.Input[str] ipv4_address: The IPv4 address assigned to the sim at this network scope. This address must be in the userEquipmentStaticAddressPoolPrefix defined in the attachedDataNetwork.
        """
        if ipv4_address is not None:
            pulumi.set(__self__, "ipv4_address", ipv4_address)

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address assigned to the sim at this network scope. This address must be in the userEquipmentStaticAddressPoolPrefix defined in the attachedDataNetwork.
        """
        return pulumi.get(self, "ipv4_address")

    @ipv4_address.setter
    def ipv4_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_address", value)


if not MYPY:
    class SimStaticIpPropertiesArgsDict(TypedDict):
        """
        Static IP configuration for a sim, scoped to a particular attached data network and slice.
        """
        attached_data_network: NotRequired[pulumi.Input['AttachedDataNetworkResourceIdArgsDict']]
        """
        The attached data network on which the static IP address will be used. The combination of attachedDataNetwork and slice defines the network scope of the IP address.
        """
        slice: NotRequired[pulumi.Input['SliceResourceIdArgsDict']]
        """
        The network slice on which the static IP address will be used. The combination of attachedDataNetwork and slice defines the network scope of the IP address.
        """
        static_ip: NotRequired[pulumi.Input['SimStaticIpPropertiesStaticIpArgsDict']]
        """
        The static IP configuration for the sim to use at the defined network scope.
        """
elif False:
    SimStaticIpPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SimStaticIpPropertiesArgs:
    def __init__(__self__, *,
                 attached_data_network: Optional[pulumi.Input['AttachedDataNetworkResourceIdArgs']] = None,
                 slice: Optional[pulumi.Input['SliceResourceIdArgs']] = None,
                 static_ip: Optional[pulumi.Input['SimStaticIpPropertiesStaticIpArgs']] = None):
        """
        Static IP configuration for a sim, scoped to a particular attached data network and slice.
        :param pulumi.Input['AttachedDataNetworkResourceIdArgs'] attached_data_network: The attached data network on which the static IP address will be used. The combination of attachedDataNetwork and slice defines the network scope of the IP address.
        :param pulumi.Input['SliceResourceIdArgs'] slice: The network slice on which the static IP address will be used. The combination of attachedDataNetwork and slice defines the network scope of the IP address.
        :param pulumi.Input['SimStaticIpPropertiesStaticIpArgs'] static_ip: The static IP configuration for the sim to use at the defined network scope.
        """
        if attached_data_network is not None:
            pulumi.set(__self__, "attached_data_network", attached_data_network)
        if slice is not None:
            pulumi.set(__self__, "slice", slice)
        if static_ip is not None:
            pulumi.set(__self__, "static_ip", static_ip)

    @property
    @pulumi.getter(name="attachedDataNetwork")
    def attached_data_network(self) -> Optional[pulumi.Input['AttachedDataNetworkResourceIdArgs']]:
        """
        The attached data network on which the static IP address will be used. The combination of attachedDataNetwork and slice defines the network scope of the IP address.
        """
        return pulumi.get(self, "attached_data_network")

    @attached_data_network.setter
    def attached_data_network(self, value: Optional[pulumi.Input['AttachedDataNetworkResourceIdArgs']]):
        pulumi.set(self, "attached_data_network", value)

    @property
    @pulumi.getter
    def slice(self) -> Optional[pulumi.Input['SliceResourceIdArgs']]:
        """
        The network slice on which the static IP address will be used. The combination of attachedDataNetwork and slice defines the network scope of the IP address.
        """
        return pulumi.get(self, "slice")

    @slice.setter
    def slice(self, value: Optional[pulumi.Input['SliceResourceIdArgs']]):
        pulumi.set(self, "slice", value)

    @property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> Optional[pulumi.Input['SimStaticIpPropertiesStaticIpArgs']]:
        """
        The static IP configuration for the sim to use at the defined network scope.
        """
        return pulumi.get(self, "static_ip")

    @static_ip.setter
    def static_ip(self, value: Optional[pulumi.Input['SimStaticIpPropertiesStaticIpArgs']]):
        pulumi.set(self, "static_ip", value)


if not MYPY:
    class SliceResourceIdArgsDict(TypedDict):
        """
        Reference to a Slice resource.
        """
        id: pulumi.Input[str]
        """
        Slice resource ID.
        """
elif False:
    SliceResourceIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SliceResourceIdArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        Reference to a Slice resource.
        :param pulumi.Input[str] id: Slice resource ID.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Slice resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


