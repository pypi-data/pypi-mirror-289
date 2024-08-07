# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AdvertiseToFabric',
    'AgentPoolMode',
    'BareMetalMachineKeySetPrivilegeLevel',
    'BfdEnabled',
    'BgpMultiHop',
    'BmcKeySetPrivilegeLevel',
    'CloudServicesNetworkEnableDefaultEgressEndpoints',
    'ClusterSecretArchiveEnabled',
    'ClusterType',
    'ClusterUpdateStrategyType',
    'ConsoleEnabled',
    'DefaultGateway',
    'FabricPeeringEnabled',
    'HugepagesSize',
    'HybridAksIpamEnabled',
    'HybridAksPluginType',
    'IpAllocationType',
    'KubernetesPluginType',
    'L3NetworkConfigurationIpamEnabled',
    'OsDiskCreateOption',
    'OsDiskDeleteOption',
    'RuntimeProtectionEnforcementLevel',
    'ValidationThresholdGrouping',
    'ValidationThresholdType',
    'VirtualMachineBootMethod',
    'VirtualMachineDeviceModelType',
    'VirtualMachineIPAllocationMethod',
    'VirtualMachineIsolateEmulatorThread',
    'VirtualMachinePlacementHintPodAffinityScope',
    'VirtualMachinePlacementHintType',
    'VirtualMachineSchedulingExecution',
    'VirtualMachineVirtioInterfaceType',
]


class AdvertiseToFabric(str, Enum):
    """
    The indicator of if this advertisement is also made to the network fabric associated with the Network Cloud Cluster. This field is ignored if fabricPeeringEnabled is set to False.
    """
    TRUE = "True"
    FALSE = "False"


class AgentPoolMode(str, Enum):
    """
    The selection of how this agent pool is utilized, either as a system pool or a user pool. System pools run the features and critical services for the Kubernetes Cluster, while user pools are dedicated to user workloads. Every Kubernetes cluster must contain at least one system node pool with at least one node.
    """
    SYSTEM = "System"
    USER = "User"
    NOT_APPLICABLE = "NotApplicable"


class BareMetalMachineKeySetPrivilegeLevel(str, Enum):
    """
    The access level allowed for the users in this key set.
    """
    STANDARD = "Standard"
    SUPERUSER = "Superuser"


class BfdEnabled(str, Enum):
    """
    The indicator to prevent the use of IP addresses ending with .0 and .255 for this pool. Enabling this option will only use IP addresses between .1 and .254 inclusive.
    """
    TRUE = "True"
    FALSE = "False"


class BgpMultiHop(str, Enum):
    """
    The indicator to enable multi-hop peering support.
    """
    TRUE = "True"
    FALSE = "False"


class BmcKeySetPrivilegeLevel(str, Enum):
    """
    The access level allowed for the users in this key set.
    """
    READ_ONLY = "ReadOnly"
    ADMINISTRATOR = "Administrator"


class CloudServicesNetworkEnableDefaultEgressEndpoints(str, Enum):
    """
    The indicator of whether the platform default endpoints are allowed for the egress traffic.
    """
    TRUE = "True"
    FALSE = "False"


class ClusterSecretArchiveEnabled(str, Enum):
    """
    The indicator if the specified key vault should be used to archive the secrets of the cluster.
    """
    TRUE = "True"
    FALSE = "False"


class ClusterType(str, Enum):
    """
    The type of rack configuration for the cluster.
    """
    SINGLE_RACK = "SingleRack"
    MULTI_RACK = "MultiRack"


class ClusterUpdateStrategyType(str, Enum):
    """
    The mode of operation for runtime protection.
    """
    RACK = "Rack"


class ConsoleEnabled(str, Enum):
    """
    The indicator of whether the console access is enabled.
    """
    TRUE = "True"
    FALSE = "False"


class DefaultGateway(str, Enum):
    """
    The indicator of whether this is the default gateway.
    Only one of the attached networks (including the CloudServicesNetwork attachment) for a single machine may be specified as True.
    """
    TRUE = "True"
    FALSE = "False"


class FabricPeeringEnabled(str, Enum):
    """
    The indicator to specify if the load balancer peers with the network fabric.
    """
    TRUE = "True"
    FALSE = "False"


class HugepagesSize(str, Enum):
    """
    The size of the hugepages to allocate.
    """
    HUGEPAGES_SIZE_2_M = "2M"
    HUGEPAGES_SIZE_1_G = "1G"


class HybridAksIpamEnabled(str, Enum):
    """
    Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The indicator of whether or not to disable IPAM allocation on the network attachment definition injected into the Hybrid AKS Cluster.
    """
    TRUE = "True"
    FALSE = "False"


class HybridAksPluginType(str, Enum):
    """
    Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The network plugin type for Hybrid AKS.
    """
    DPDK = "DPDK"
    SRIOV = "SRIOV"
    OS_DEVICE = "OSDevice"


class IpAllocationType(str, Enum):
    """
    The type of the IP address allocation, defaulted to "DualStack".
    """
    IPV4 = "IPV4"
    IPV6 = "IPV6"
    DUAL_STACK = "DualStack"


class KubernetesPluginType(str, Enum):
    """
    The indicator of how this network will be utilized by the Kubernetes cluster.
    """
    DPDK = "DPDK"
    SRIOV = "SRIOV"
    OS_DEVICE = "OSDevice"
    MACVLAN = "MACVLAN"
    IPVLAN = "IPVLAN"


class L3NetworkConfigurationIpamEnabled(str, Enum):
    """
    The indication of whether this network will or will not perform IP address management and allocate IP addresses when attached.
    """
    TRUE = "True"
    FALSE = "False"


class OsDiskCreateOption(str, Enum):
    """
    The strategy for creating the OS disk.
    """
    EPHEMERAL = "Ephemeral"


class OsDiskDeleteOption(str, Enum):
    """
    The strategy for deleting the OS disk.
    """
    DELETE = "Delete"


class RuntimeProtectionEnforcementLevel(str, Enum):
    """
    The mode of operation for runtime protection.
    """
    AUDIT = "Audit"
    DISABLED = "Disabled"
    ON_DEMAND = "OnDemand"
    PASSIVE = "Passive"
    REAL_TIME = "RealTime"


class ValidationThresholdGrouping(str, Enum):
    """
    Selection of how the type evaluation is applied to the cluster calculation.
    """
    PER_CLUSTER = "PerCluster"
    PER_RACK = "PerRack"


class ValidationThresholdType(str, Enum):
    """
    Selection of how the threshold should be evaluated.
    """
    COUNT_SUCCESS = "CountSuccess"
    PERCENT_SUCCESS = "PercentSuccess"


class VirtualMachineBootMethod(str, Enum):
    """
    Selects the boot method for the virtual machine.
    """
    UEFI = "UEFI"
    BIOS = "BIOS"


class VirtualMachineDeviceModelType(str, Enum):
    """
    The type of the device model to use.
    """
    T1 = "T1"
    T2 = "T2"


class VirtualMachineIPAllocationMethod(str, Enum):
    """
    The IP allocation mechanism for the virtual machine.
    Dynamic and Static are only valid for l3Network which may also specify Disabled.
    Otherwise, Disabled is the only permitted value.
    """
    DYNAMIC = "Dynamic"
    STATIC = "Static"
    DISABLED = "Disabled"


class VirtualMachineIsolateEmulatorThread(str, Enum):
    """
    Field Deprecated, the value will be ignored if provided. The indicator of whether one of the specified CPU cores is isolated to run the emulator thread for this virtual machine.
    """
    TRUE = "True"
    FALSE = "False"


class VirtualMachinePlacementHintPodAffinityScope(str, Enum):
    """
    The scope for the virtual machine affinity or anti-affinity placement hint. It should always be "Machine" in the case of node affinity.
    """
    RACK = "Rack"
    MACHINE = "Machine"


class VirtualMachinePlacementHintType(str, Enum):
    """
    The specification of whether this hint supports affinity or anti-affinity with the referenced resources.
    """
    AFFINITY = "Affinity"
    ANTI_AFFINITY = "AntiAffinity"


class VirtualMachineSchedulingExecution(str, Enum):
    """
    The indicator of whether the hint is a hard or soft requirement during scheduling.
    """
    HARD = "Hard"
    SOFT = "Soft"


class VirtualMachineVirtioInterfaceType(str, Enum):
    """
    Field Deprecated, use virtualizationModel instead. The type of the virtio interface.
    """
    MODERN = "Modern"
    TRANSITIONAL = "Transitional"
