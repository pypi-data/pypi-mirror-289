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

__all__ = [
    'GetSnapshotResult',
    'AwaitableGetSnapshotResult',
    'get_snapshot',
    'get_snapshot_output',
]

@pulumi.output_type
class GetSnapshotResult:
    """
    A node pool snapshot resource.
    """
    def __init__(__self__, creation_data=None, enable_fips=None, id=None, kubernetes_version=None, location=None, name=None, node_image_version=None, os_sku=None, os_type=None, snapshot_type=None, system_data=None, tags=None, type=None, vm_size=None):
        if creation_data and not isinstance(creation_data, dict):
            raise TypeError("Expected argument 'creation_data' to be a dict")
        pulumi.set(__self__, "creation_data", creation_data)
        if enable_fips and not isinstance(enable_fips, bool):
            raise TypeError("Expected argument 'enable_fips' to be a bool")
        pulumi.set(__self__, "enable_fips", enable_fips)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_image_version and not isinstance(node_image_version, str):
            raise TypeError("Expected argument 'node_image_version' to be a str")
        pulumi.set(__self__, "node_image_version", node_image_version)
        if os_sku and not isinstance(os_sku, str):
            raise TypeError("Expected argument 'os_sku' to be a str")
        pulumi.set(__self__, "os_sku", os_sku)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if snapshot_type and not isinstance(snapshot_type, str):
            raise TypeError("Expected argument 'snapshot_type' to be a str")
        pulumi.set(__self__, "snapshot_type", snapshot_type)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_size and not isinstance(vm_size, str):
            raise TypeError("Expected argument 'vm_size' to be a str")
        pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional['outputs.CreationDataResponse']:
        """
        CreationData to be used to specify the source agent pool resource ID to create this snapshot.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter(name="enableFIPS")
    def enable_fips(self) -> bool:
        """
        Whether to use a FIPS-enabled OS.
        """
        return pulumi.get(self, "enable_fips")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> str:
        """
        The version of Kubernetes.
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
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> str:
        """
        The version of node image.
        """
        return pulumi.get(self, "node_image_version")

    @property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> str:
        """
        Specifies the OS SKU used by the agent pool. If not specified, the default is Ubuntu if OSType=Linux or Windows2019 if OSType=Windows. And the default Windows OSSKU will be changed to Windows2022 after Windows2019 is deprecated.
        """
        return pulumi.get(self, "os_sku")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> str:
        """
        The operating system type. The default is Linux.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[str]:
        """
        The type of a snapshot. The default is NodePool.
        """
        return pulumi.get(self, "snapshot_type")

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
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> str:
        """
        The size of the VM.
        """
        return pulumi.get(self, "vm_size")


class AwaitableGetSnapshotResult(GetSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotResult(
            creation_data=self.creation_data,
            enable_fips=self.enable_fips,
            id=self.id,
            kubernetes_version=self.kubernetes_version,
            location=self.location,
            name=self.name,
            node_image_version=self.node_image_version,
            os_sku=self.os_sku,
            os_type=self.os_type,
            snapshot_type=self.snapshot_type,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vm_size=self.vm_size)


def get_snapshot(resource_group_name: Optional[str] = None,
                 resource_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotResult:
    """
    A node pool snapshot resource.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice/v20230702preview:getSnapshot', __args__, opts=opts, typ=GetSnapshotResult).value

    return AwaitableGetSnapshotResult(
        creation_data=pulumi.get(__ret__, 'creation_data'),
        enable_fips=pulumi.get(__ret__, 'enable_fips'),
        id=pulumi.get(__ret__, 'id'),
        kubernetes_version=pulumi.get(__ret__, 'kubernetes_version'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        node_image_version=pulumi.get(__ret__, 'node_image_version'),
        os_sku=pulumi.get(__ret__, 'os_sku'),
        os_type=pulumi.get(__ret__, 'os_type'),
        snapshot_type=pulumi.get(__ret__, 'snapshot_type'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vm_size=pulumi.get(__ret__, 'vm_size'))


@_utilities.lift_output_func(get_snapshot)
def get_snapshot_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                        resource_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSnapshotResult]:
    """
    A node pool snapshot resource.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    """
    ...
