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
    'GetVirtualMachineResult',
    'AwaitableGetVirtualMachineResult',
    'get_virtual_machine',
    'get_virtual_machine_output',
]

@pulumi.output_type
class GetVirtualMachineResult:
    def __init__(__self__, admin_username=None, availability_zone=None, bare_metal_machine_id=None, boot_method=None, cloud_services_network_attachment=None, cluster_id=None, cpu_cores=None, detailed_status=None, detailed_status_message=None, extended_location=None, id=None, isolate_emulator_thread=None, location=None, memory_size_gb=None, name=None, network_attachments=None, network_data=None, placement_hints=None, power_state=None, provisioning_state=None, ssh_public_keys=None, storage_profile=None, system_data=None, tags=None, type=None, user_data=None, virtio_interface=None, vm_device_model=None, vm_image=None, vm_image_repository_credentials=None, volumes=None):
        if admin_username and not isinstance(admin_username, str):
            raise TypeError("Expected argument 'admin_username' to be a str")
        pulumi.set(__self__, "admin_username", admin_username)
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if bare_metal_machine_id and not isinstance(bare_metal_machine_id, str):
            raise TypeError("Expected argument 'bare_metal_machine_id' to be a str")
        pulumi.set(__self__, "bare_metal_machine_id", bare_metal_machine_id)
        if boot_method and not isinstance(boot_method, str):
            raise TypeError("Expected argument 'boot_method' to be a str")
        pulumi.set(__self__, "boot_method", boot_method)
        if cloud_services_network_attachment and not isinstance(cloud_services_network_attachment, dict):
            raise TypeError("Expected argument 'cloud_services_network_attachment' to be a dict")
        pulumi.set(__self__, "cloud_services_network_attachment", cloud_services_network_attachment)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if cpu_cores and not isinstance(cpu_cores, float):
            raise TypeError("Expected argument 'cpu_cores' to be a float")
        pulumi.set(__self__, "cpu_cores", cpu_cores)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if detailed_status_message and not isinstance(detailed_status_message, str):
            raise TypeError("Expected argument 'detailed_status_message' to be a str")
        pulumi.set(__self__, "detailed_status_message", detailed_status_message)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if isolate_emulator_thread and not isinstance(isolate_emulator_thread, str):
            raise TypeError("Expected argument 'isolate_emulator_thread' to be a str")
        pulumi.set(__self__, "isolate_emulator_thread", isolate_emulator_thread)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if memory_size_gb and not isinstance(memory_size_gb, float):
            raise TypeError("Expected argument 'memory_size_gb' to be a float")
        pulumi.set(__self__, "memory_size_gb", memory_size_gb)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_attachments and not isinstance(network_attachments, list):
            raise TypeError("Expected argument 'network_attachments' to be a list")
        pulumi.set(__self__, "network_attachments", network_attachments)
        if network_data and not isinstance(network_data, str):
            raise TypeError("Expected argument 'network_data' to be a str")
        pulumi.set(__self__, "network_data", network_data)
        if placement_hints and not isinstance(placement_hints, list):
            raise TypeError("Expected argument 'placement_hints' to be a list")
        pulumi.set(__self__, "placement_hints", placement_hints)
        if power_state and not isinstance(power_state, str):
            raise TypeError("Expected argument 'power_state' to be a str")
        pulumi.set(__self__, "power_state", power_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if ssh_public_keys and not isinstance(ssh_public_keys, list):
            raise TypeError("Expected argument 'ssh_public_keys' to be a list")
        pulumi.set(__self__, "ssh_public_keys", ssh_public_keys)
        if storage_profile and not isinstance(storage_profile, dict):
            raise TypeError("Expected argument 'storage_profile' to be a dict")
        pulumi.set(__self__, "storage_profile", storage_profile)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_data and not isinstance(user_data, str):
            raise TypeError("Expected argument 'user_data' to be a str")
        pulumi.set(__self__, "user_data", user_data)
        if virtio_interface and not isinstance(virtio_interface, str):
            raise TypeError("Expected argument 'virtio_interface' to be a str")
        pulumi.set(__self__, "virtio_interface", virtio_interface)
        if vm_device_model and not isinstance(vm_device_model, str):
            raise TypeError("Expected argument 'vm_device_model' to be a str")
        pulumi.set(__self__, "vm_device_model", vm_device_model)
        if vm_image and not isinstance(vm_image, str):
            raise TypeError("Expected argument 'vm_image' to be a str")
        pulumi.set(__self__, "vm_image", vm_image)
        if vm_image_repository_credentials and not isinstance(vm_image_repository_credentials, dict):
            raise TypeError("Expected argument 'vm_image_repository_credentials' to be a dict")
        pulumi.set(__self__, "vm_image_repository_credentials", vm_image_repository_credentials)
        if volumes and not isinstance(volumes, list):
            raise TypeError("Expected argument 'volumes' to be a list")
        pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> str:
        """
        The name of the administrator to which the ssh public keys will be added into the authorized keys.
        """
        return pulumi.get(self, "admin_username")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        """
        The cluster availability zone containing this virtual machine.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="bareMetalMachineId")
    def bare_metal_machine_id(self) -> str:
        """
        The resource ID of the bare metal machine that hosts the virtual machine.
        """
        return pulumi.get(self, "bare_metal_machine_id")

    @property
    @pulumi.getter(name="bootMethod")
    def boot_method(self) -> Optional[str]:
        """
        Selects the boot method for the virtual machine.
        """
        return pulumi.get(self, "boot_method")

    @property
    @pulumi.getter(name="cloudServicesNetworkAttachment")
    def cloud_services_network_attachment(self) -> 'outputs.NetworkAttachmentResponse':
        """
        The cloud service network that provides platform-level services for the virtual machine.
        """
        return pulumi.get(self, "cloud_services_network_attachment")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The resource ID of the cluster the virtual machine is created for.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> float:
        """
        The number of CPU cores in the virtual machine.
        """
        return pulumi.get(self, "cpu_cores")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        The more detailed status of the virtual machine.
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
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isolateEmulatorThread")
    def isolate_emulator_thread(self) -> Optional[str]:
        """
        Field Deprecated, the value will be ignored if provided. The indicator of whether one of the specified CPU cores is isolated to run the emulator thread for this virtual machine.
        """
        return pulumi.get(self, "isolate_emulator_thread")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="memorySizeGB")
    def memory_size_gb(self) -> float:
        """
        The memory size of the virtual machine in GB.
        """
        return pulumi.get(self, "memory_size_gb")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAttachments")
    def network_attachments(self) -> Optional[Sequence['outputs.NetworkAttachmentResponse']]:
        """
        The list of network attachments to the virtual machine.
        """
        return pulumi.get(self, "network_attachments")

    @property
    @pulumi.getter(name="networkData")
    def network_data(self) -> Optional[str]:
        """
        The Base64 encoded cloud-init network data.
        """
        return pulumi.get(self, "network_data")

    @property
    @pulumi.getter(name="placementHints")
    def placement_hints(self) -> Optional[Sequence['outputs.VirtualMachinePlacementHintResponse']]:
        """
        The scheduling hints for the virtual machine.
        """
        return pulumi.get(self, "placement_hints")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> str:
        """
        The power state of the virtual machine.
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the virtual machine.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Optional[Sequence['outputs.SshPublicKeyResponse']]:
        """
        The list of ssh public keys. Each key will be added to the virtual machine using the cloud-init ssh_authorized_keys mechanism for the adminUsername.
        """
        return pulumi.get(self, "ssh_public_keys")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> 'outputs.StorageProfileResponse':
        """
        The storage profile that specifies size and other parameters about the disks related to the virtual machine.
        """
        return pulumi.get(self, "storage_profile")

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
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[str]:
        """
        The Base64 encoded cloud-init user data.
        """
        return pulumi.get(self, "user_data")

    @property
    @pulumi.getter(name="virtioInterface")
    def virtio_interface(self) -> Optional[str]:
        """
        Field Deprecated, use virtualizationModel instead. The type of the virtio interface.
        """
        return pulumi.get(self, "virtio_interface")

    @property
    @pulumi.getter(name="vmDeviceModel")
    def vm_device_model(self) -> Optional[str]:
        """
        The type of the device model to use.
        """
        return pulumi.get(self, "vm_device_model")

    @property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> str:
        """
        The virtual machine image that is currently provisioned to the OS disk, using the full url and tag notation used to pull the image.
        """
        return pulumi.get(self, "vm_image")

    @property
    @pulumi.getter(name="vmImageRepositoryCredentials")
    def vm_image_repository_credentials(self) -> Optional['outputs.ImageRepositoryCredentialsResponse']:
        """
        The credentials used to login to the image repository that has access to the specified image.
        """
        return pulumi.get(self, "vm_image_repository_credentials")

    @property
    @pulumi.getter
    def volumes(self) -> Sequence[str]:
        """
        The resource IDs of volumes that are attached to the virtual machine.
        """
        return pulumi.get(self, "volumes")


class AwaitableGetVirtualMachineResult(GetVirtualMachineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineResult(
            admin_username=self.admin_username,
            availability_zone=self.availability_zone,
            bare_metal_machine_id=self.bare_metal_machine_id,
            boot_method=self.boot_method,
            cloud_services_network_attachment=self.cloud_services_network_attachment,
            cluster_id=self.cluster_id,
            cpu_cores=self.cpu_cores,
            detailed_status=self.detailed_status,
            detailed_status_message=self.detailed_status_message,
            extended_location=self.extended_location,
            id=self.id,
            isolate_emulator_thread=self.isolate_emulator_thread,
            location=self.location,
            memory_size_gb=self.memory_size_gb,
            name=self.name,
            network_attachments=self.network_attachments,
            network_data=self.network_data,
            placement_hints=self.placement_hints,
            power_state=self.power_state,
            provisioning_state=self.provisioning_state,
            ssh_public_keys=self.ssh_public_keys,
            storage_profile=self.storage_profile,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            user_data=self.user_data,
            virtio_interface=self.virtio_interface,
            vm_device_model=self.vm_device_model,
            vm_image=self.vm_image,
            vm_image_repository_credentials=self.vm_image_repository_credentials,
            volumes=self.volumes)


def get_virtual_machine(resource_group_name: Optional[str] = None,
                        virtual_machine_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineResult:
    """
    Get properties of the provided virtual machine.
    Azure REST API version: 2023-10-01-preview.

    Other available API versions: 2023-07-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str virtual_machine_name: The name of the virtual machine.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualMachineName'] = virtual_machine_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkcloud:getVirtualMachine', __args__, opts=opts, typ=GetVirtualMachineResult).value

    return AwaitableGetVirtualMachineResult(
        admin_username=pulumi.get(__ret__, 'admin_username'),
        availability_zone=pulumi.get(__ret__, 'availability_zone'),
        bare_metal_machine_id=pulumi.get(__ret__, 'bare_metal_machine_id'),
        boot_method=pulumi.get(__ret__, 'boot_method'),
        cloud_services_network_attachment=pulumi.get(__ret__, 'cloud_services_network_attachment'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        cpu_cores=pulumi.get(__ret__, 'cpu_cores'),
        detailed_status=pulumi.get(__ret__, 'detailed_status'),
        detailed_status_message=pulumi.get(__ret__, 'detailed_status_message'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        isolate_emulator_thread=pulumi.get(__ret__, 'isolate_emulator_thread'),
        location=pulumi.get(__ret__, 'location'),
        memory_size_gb=pulumi.get(__ret__, 'memory_size_gb'),
        name=pulumi.get(__ret__, 'name'),
        network_attachments=pulumi.get(__ret__, 'network_attachments'),
        network_data=pulumi.get(__ret__, 'network_data'),
        placement_hints=pulumi.get(__ret__, 'placement_hints'),
        power_state=pulumi.get(__ret__, 'power_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        ssh_public_keys=pulumi.get(__ret__, 'ssh_public_keys'),
        storage_profile=pulumi.get(__ret__, 'storage_profile'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        user_data=pulumi.get(__ret__, 'user_data'),
        virtio_interface=pulumi.get(__ret__, 'virtio_interface'),
        vm_device_model=pulumi.get(__ret__, 'vm_device_model'),
        vm_image=pulumi.get(__ret__, 'vm_image'),
        vm_image_repository_credentials=pulumi.get(__ret__, 'vm_image_repository_credentials'),
        volumes=pulumi.get(__ret__, 'volumes'))


@_utilities.lift_output_func(get_virtual_machine)
def get_virtual_machine_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                               virtual_machine_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineResult]:
    """
    Get properties of the provided virtual machine.
    Azure REST API version: 2023-10-01-preview.

    Other available API versions: 2023-07-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str virtual_machine_name: The name of the virtual machine.
    """
    ...
