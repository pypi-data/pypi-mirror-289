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
from .. import _utilities
from . import outputs

__all__ = [
    'GetBareMetalMachineResult',
    'AwaitableGetBareMetalMachineResult',
    'get_bare_metal_machine',
    'get_bare_metal_machine_output',
]

@pulumi.output_type
class GetBareMetalMachineResult:
    def __init__(__self__, associated_resource_ids=None, bmc_connection_string=None, bmc_credentials=None, bmc_mac_address=None, boot_mac_address=None, cluster_id=None, cordon_status=None, detailed_status=None, detailed_status_message=None, extended_location=None, hardware_inventory=None, hardware_validation_status=None, hybrid_aks_clusters_associated_ids=None, id=None, kubernetes_node_name=None, kubernetes_version=None, location=None, machine_details=None, machine_name=None, machine_roles=None, machine_sku_id=None, name=None, oam_ipv4_address=None, oam_ipv6_address=None, os_image=None, power_state=None, provisioning_state=None, rack_id=None, rack_slot=None, ready_state=None, runtime_protection_status=None, serial_number=None, service_tag=None, system_data=None, tags=None, type=None, virtual_machines_associated_ids=None):
        if associated_resource_ids and not isinstance(associated_resource_ids, list):
            raise TypeError("Expected argument 'associated_resource_ids' to be a list")
        pulumi.set(__self__, "associated_resource_ids", associated_resource_ids)
        if bmc_connection_string and not isinstance(bmc_connection_string, str):
            raise TypeError("Expected argument 'bmc_connection_string' to be a str")
        pulumi.set(__self__, "bmc_connection_string", bmc_connection_string)
        if bmc_credentials and not isinstance(bmc_credentials, dict):
            raise TypeError("Expected argument 'bmc_credentials' to be a dict")
        pulumi.set(__self__, "bmc_credentials", bmc_credentials)
        if bmc_mac_address and not isinstance(bmc_mac_address, str):
            raise TypeError("Expected argument 'bmc_mac_address' to be a str")
        pulumi.set(__self__, "bmc_mac_address", bmc_mac_address)
        if boot_mac_address and not isinstance(boot_mac_address, str):
            raise TypeError("Expected argument 'boot_mac_address' to be a str")
        pulumi.set(__self__, "boot_mac_address", boot_mac_address)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if cordon_status and not isinstance(cordon_status, str):
            raise TypeError("Expected argument 'cordon_status' to be a str")
        pulumi.set(__self__, "cordon_status", cordon_status)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if detailed_status_message and not isinstance(detailed_status_message, str):
            raise TypeError("Expected argument 'detailed_status_message' to be a str")
        pulumi.set(__self__, "detailed_status_message", detailed_status_message)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if hardware_inventory and not isinstance(hardware_inventory, dict):
            raise TypeError("Expected argument 'hardware_inventory' to be a dict")
        pulumi.set(__self__, "hardware_inventory", hardware_inventory)
        if hardware_validation_status and not isinstance(hardware_validation_status, dict):
            raise TypeError("Expected argument 'hardware_validation_status' to be a dict")
        pulumi.set(__self__, "hardware_validation_status", hardware_validation_status)
        if hybrid_aks_clusters_associated_ids and not isinstance(hybrid_aks_clusters_associated_ids, list):
            raise TypeError("Expected argument 'hybrid_aks_clusters_associated_ids' to be a list")
        pulumi.set(__self__, "hybrid_aks_clusters_associated_ids", hybrid_aks_clusters_associated_ids)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubernetes_node_name and not isinstance(kubernetes_node_name, str):
            raise TypeError("Expected argument 'kubernetes_node_name' to be a str")
        pulumi.set(__self__, "kubernetes_node_name", kubernetes_node_name)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if machine_details and not isinstance(machine_details, str):
            raise TypeError("Expected argument 'machine_details' to be a str")
        pulumi.set(__self__, "machine_details", machine_details)
        if machine_name and not isinstance(machine_name, str):
            raise TypeError("Expected argument 'machine_name' to be a str")
        pulumi.set(__self__, "machine_name", machine_name)
        if machine_roles and not isinstance(machine_roles, list):
            raise TypeError("Expected argument 'machine_roles' to be a list")
        pulumi.set(__self__, "machine_roles", machine_roles)
        if machine_sku_id and not isinstance(machine_sku_id, str):
            raise TypeError("Expected argument 'machine_sku_id' to be a str")
        pulumi.set(__self__, "machine_sku_id", machine_sku_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if oam_ipv4_address and not isinstance(oam_ipv4_address, str):
            raise TypeError("Expected argument 'oam_ipv4_address' to be a str")
        pulumi.set(__self__, "oam_ipv4_address", oam_ipv4_address)
        if oam_ipv6_address and not isinstance(oam_ipv6_address, str):
            raise TypeError("Expected argument 'oam_ipv6_address' to be a str")
        pulumi.set(__self__, "oam_ipv6_address", oam_ipv6_address)
        if os_image and not isinstance(os_image, str):
            raise TypeError("Expected argument 'os_image' to be a str")
        pulumi.set(__self__, "os_image", os_image)
        if power_state and not isinstance(power_state, str):
            raise TypeError("Expected argument 'power_state' to be a str")
        pulumi.set(__self__, "power_state", power_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rack_id and not isinstance(rack_id, str):
            raise TypeError("Expected argument 'rack_id' to be a str")
        pulumi.set(__self__, "rack_id", rack_id)
        if rack_slot and not isinstance(rack_slot, float):
            raise TypeError("Expected argument 'rack_slot' to be a float")
        pulumi.set(__self__, "rack_slot", rack_slot)
        if ready_state and not isinstance(ready_state, str):
            raise TypeError("Expected argument 'ready_state' to be a str")
        pulumi.set(__self__, "ready_state", ready_state)
        if runtime_protection_status and not isinstance(runtime_protection_status, dict):
            raise TypeError("Expected argument 'runtime_protection_status' to be a dict")
        pulumi.set(__self__, "runtime_protection_status", runtime_protection_status)
        if serial_number and not isinstance(serial_number, str):
            raise TypeError("Expected argument 'serial_number' to be a str")
        pulumi.set(__self__, "serial_number", serial_number)
        if service_tag and not isinstance(service_tag, str):
            raise TypeError("Expected argument 'service_tag' to be a str")
        pulumi.set(__self__, "service_tag", service_tag)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_machines_associated_ids and not isinstance(virtual_machines_associated_ids, list):
            raise TypeError("Expected argument 'virtual_machines_associated_ids' to be a list")
        pulumi.set(__self__, "virtual_machines_associated_ids", virtual_machines_associated_ids)

    @property
    @pulumi.getter(name="associatedResourceIds")
    def associated_resource_ids(self) -> Sequence[str]:
        """
        The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.
        """
        return pulumi.get(self, "associated_resource_ids")

    @property
    @pulumi.getter(name="bmcConnectionString")
    def bmc_connection_string(self) -> str:
        """
        The connection string for the baseboard management controller including IP address and protocol.
        """
        return pulumi.get(self, "bmc_connection_string")

    @property
    @pulumi.getter(name="bmcCredentials")
    def bmc_credentials(self) -> 'outputs.AdministrativeCredentialsResponse':
        """
        The credentials of the baseboard management controller on this bare metal machine.
        """
        return pulumi.get(self, "bmc_credentials")

    @property
    @pulumi.getter(name="bmcMacAddress")
    def bmc_mac_address(self) -> str:
        """
        The MAC address of the BMC device.
        """
        return pulumi.get(self, "bmc_mac_address")

    @property
    @pulumi.getter(name="bootMacAddress")
    def boot_mac_address(self) -> str:
        """
        The MAC address of a NIC connected to the PXE network.
        """
        return pulumi.get(self, "boot_mac_address")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The resource ID of the cluster this bare metal machine is associated with.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="cordonStatus")
    def cordon_status(self) -> str:
        """
        The cordon status of the bare metal machine.
        """
        return pulumi.get(self, "cordon_status")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        The more detailed status of the bare metal machine.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> str:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hardwareInventory")
    def hardware_inventory(self) -> 'outputs.HardwareInventoryResponse':
        """
        The hardware inventory, including information acquired from the model/sku information and from the ironic inspector.
        """
        return pulumi.get(self, "hardware_inventory")

    @property
    @pulumi.getter(name="hardwareValidationStatus")
    def hardware_validation_status(self) -> 'outputs.HardwareValidationStatusResponse':
        """
        The details of the latest hardware validation performed for this bare metal machine.
        """
        return pulumi.get(self, "hardware_validation_status")

    @property
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> Sequence[str]:
        """
        Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the HybridAksClusters that have nodes hosted on this bare metal machine.
        """
        return pulumi.get(self, "hybrid_aks_clusters_associated_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubernetesNodeName")
    def kubernetes_node_name(self) -> str:
        """
        The name of this machine represented by the host object in the Cluster's Kubernetes control plane.
        """
        return pulumi.get(self, "kubernetes_node_name")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> str:
        """
        The version of Kubernetes running on this machine.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="machineDetails")
    def machine_details(self) -> str:
        """
        The custom details provided by the customer.
        """
        return pulumi.get(self, "machine_details")

    @property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> str:
        """
        The OS-level hostname assigned to this machine.
        """
        return pulumi.get(self, "machine_name")

    @property
    @pulumi.getter(name="machineRoles")
    def machine_roles(self) -> Sequence[str]:
        """
        The list of roles that are assigned to the cluster node running on this machine.
        """
        return pulumi.get(self, "machine_roles")

    @property
    @pulumi.getter(name="machineSkuId")
    def machine_sku_id(self) -> str:
        """
        The unique internal identifier of the bare metal machine SKU.
        """
        return pulumi.get(self, "machine_sku_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oamIpv4Address")
    def oam_ipv4_address(self) -> str:
        """
        The IPv4 address that is assigned to the bare metal machine during the cluster deployment.
        """
        return pulumi.get(self, "oam_ipv4_address")

    @property
    @pulumi.getter(name="oamIpv6Address")
    def oam_ipv6_address(self) -> str:
        """
        The IPv6 address that is assigned to the bare metal machine during the cluster deployment.
        """
        return pulumi.get(self, "oam_ipv6_address")

    @property
    @pulumi.getter(name="osImage")
    def os_image(self) -> str:
        """
        The image that is currently provisioned to the OS disk.
        """
        return pulumi.get(self, "os_image")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> str:
        """
        The power state derived from the baseboard management controller.
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the bare metal machine.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rackId")
    def rack_id(self) -> str:
        """
        The resource ID of the rack where this bare metal machine resides.
        """
        return pulumi.get(self, "rack_id")

    @property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> float:
        """
        The rack slot in which this bare metal machine is located, ordered from the bottom up i.e. the lowest slot is 1.
        """
        return pulumi.get(self, "rack_slot")

    @property
    @pulumi.getter(name="readyState")
    def ready_state(self) -> str:
        """
        The indicator of whether the bare metal machine is ready to receive workloads.
        """
        return pulumi.get(self, "ready_state")

    @property
    @pulumi.getter(name="runtimeProtectionStatus")
    def runtime_protection_status(self) -> 'outputs.RuntimeProtectionStatusResponse':
        """
        The runtime protection status of the bare metal machine.
        """
        return pulumi.get(self, "runtime_protection_status")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> str:
        """
        The serial number of the bare metal machine.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="serviceTag")
    def service_tag(self) -> str:
        """
        The discovered value of the machine's service tag.
        """
        return pulumi.get(self, "service_tag")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachinesAssociatedIds")
    def virtual_machines_associated_ids(self) -> Sequence[str]:
        """
        Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the VirtualMachines that are hosted on this bare metal machine.
        """
        return pulumi.get(self, "virtual_machines_associated_ids")


class AwaitableGetBareMetalMachineResult(GetBareMetalMachineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBareMetalMachineResult(
            associated_resource_ids=self.associated_resource_ids,
            bmc_connection_string=self.bmc_connection_string,
            bmc_credentials=self.bmc_credentials,
            bmc_mac_address=self.bmc_mac_address,
            boot_mac_address=self.boot_mac_address,
            cluster_id=self.cluster_id,
            cordon_status=self.cordon_status,
            detailed_status=self.detailed_status,
            detailed_status_message=self.detailed_status_message,
            extended_location=self.extended_location,
            hardware_inventory=self.hardware_inventory,
            hardware_validation_status=self.hardware_validation_status,
            hybrid_aks_clusters_associated_ids=self.hybrid_aks_clusters_associated_ids,
            id=self.id,
            kubernetes_node_name=self.kubernetes_node_name,
            kubernetes_version=self.kubernetes_version,
            location=self.location,
            machine_details=self.machine_details,
            machine_name=self.machine_name,
            machine_roles=self.machine_roles,
            machine_sku_id=self.machine_sku_id,
            name=self.name,
            oam_ipv4_address=self.oam_ipv4_address,
            oam_ipv6_address=self.oam_ipv6_address,
            os_image=self.os_image,
            power_state=self.power_state,
            provisioning_state=self.provisioning_state,
            rack_id=self.rack_id,
            rack_slot=self.rack_slot,
            ready_state=self.ready_state,
            runtime_protection_status=self.runtime_protection_status,
            serial_number=self.serial_number,
            service_tag=self.service_tag,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            virtual_machines_associated_ids=self.virtual_machines_associated_ids)


def get_bare_metal_machine(bare_metal_machine_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBareMetalMachineResult:
    """
    Get properties of the provided bare metal machine.
    Azure REST API version: 2023-10-01-preview.

    Other available API versions: 2023-07-01.


    :param str bare_metal_machine_name: The name of the bare metal machine.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['bareMetalMachineName'] = bare_metal_machine_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkcloud:getBareMetalMachine', __args__, opts=opts, typ=GetBareMetalMachineResult).value

    return AwaitableGetBareMetalMachineResult(
        associated_resource_ids=pulumi.get(__ret__, 'associated_resource_ids'),
        bmc_connection_string=pulumi.get(__ret__, 'bmc_connection_string'),
        bmc_credentials=pulumi.get(__ret__, 'bmc_credentials'),
        bmc_mac_address=pulumi.get(__ret__, 'bmc_mac_address'),
        boot_mac_address=pulumi.get(__ret__, 'boot_mac_address'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        cordon_status=pulumi.get(__ret__, 'cordon_status'),
        detailed_status=pulumi.get(__ret__, 'detailed_status'),
        detailed_status_message=pulumi.get(__ret__, 'detailed_status_message'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        hardware_inventory=pulumi.get(__ret__, 'hardware_inventory'),
        hardware_validation_status=pulumi.get(__ret__, 'hardware_validation_status'),
        hybrid_aks_clusters_associated_ids=pulumi.get(__ret__, 'hybrid_aks_clusters_associated_ids'),
        id=pulumi.get(__ret__, 'id'),
        kubernetes_node_name=pulumi.get(__ret__, 'kubernetes_node_name'),
        kubernetes_version=pulumi.get(__ret__, 'kubernetes_version'),
        location=pulumi.get(__ret__, 'location'),
        machine_details=pulumi.get(__ret__, 'machine_details'),
        machine_name=pulumi.get(__ret__, 'machine_name'),
        machine_roles=pulumi.get(__ret__, 'machine_roles'),
        machine_sku_id=pulumi.get(__ret__, 'machine_sku_id'),
        name=pulumi.get(__ret__, 'name'),
        oam_ipv4_address=pulumi.get(__ret__, 'oam_ipv4_address'),
        oam_ipv6_address=pulumi.get(__ret__, 'oam_ipv6_address'),
        os_image=pulumi.get(__ret__, 'os_image'),
        power_state=pulumi.get(__ret__, 'power_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rack_id=pulumi.get(__ret__, 'rack_id'),
        rack_slot=pulumi.get(__ret__, 'rack_slot'),
        ready_state=pulumi.get(__ret__, 'ready_state'),
        runtime_protection_status=pulumi.get(__ret__, 'runtime_protection_status'),
        serial_number=pulumi.get(__ret__, 'serial_number'),
        service_tag=pulumi.get(__ret__, 'service_tag'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_machines_associated_ids=pulumi.get(__ret__, 'virtual_machines_associated_ids'))


@_utilities.lift_output_func(get_bare_metal_machine)
def get_bare_metal_machine_output(bare_metal_machine_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBareMetalMachineResult]:
    """
    Get properties of the provided bare metal machine.
    Azure REST API version: 2023-10-01-preview.

    Other available API versions: 2023-07-01.


    :param str bare_metal_machine_name: The name of the bare metal machine.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
