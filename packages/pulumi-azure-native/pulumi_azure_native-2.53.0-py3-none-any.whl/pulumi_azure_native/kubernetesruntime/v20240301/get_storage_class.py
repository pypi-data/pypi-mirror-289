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
    'GetStorageClassResult',
    'AwaitableGetStorageClassResult',
    'get_storage_class',
    'get_storage_class_output',
]

@pulumi.output_type
class GetStorageClassResult:
    """
    A StorageClass resource for an Arc connected cluster (Microsoft.Kubernetes/connectedClusters)
    """
    def __init__(__self__, access_modes=None, allow_volume_expansion=None, data_resilience=None, failover_speed=None, id=None, limitations=None, mount_options=None, name=None, performance=None, priority=None, provisioner=None, provisioning_state=None, system_data=None, type=None, type_properties=None, volume_binding_mode=None):
        if access_modes and not isinstance(access_modes, list):
            raise TypeError("Expected argument 'access_modes' to be a list")
        pulumi.set(__self__, "access_modes", access_modes)
        if allow_volume_expansion and not isinstance(allow_volume_expansion, str):
            raise TypeError("Expected argument 'allow_volume_expansion' to be a str")
        pulumi.set(__self__, "allow_volume_expansion", allow_volume_expansion)
        if data_resilience and not isinstance(data_resilience, str):
            raise TypeError("Expected argument 'data_resilience' to be a str")
        pulumi.set(__self__, "data_resilience", data_resilience)
        if failover_speed and not isinstance(failover_speed, str):
            raise TypeError("Expected argument 'failover_speed' to be a str")
        pulumi.set(__self__, "failover_speed", failover_speed)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if limitations and not isinstance(limitations, list):
            raise TypeError("Expected argument 'limitations' to be a list")
        pulumi.set(__self__, "limitations", limitations)
        if mount_options and not isinstance(mount_options, list):
            raise TypeError("Expected argument 'mount_options' to be a list")
        pulumi.set(__self__, "mount_options", mount_options)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if performance and not isinstance(performance, str):
            raise TypeError("Expected argument 'performance' to be a str")
        pulumi.set(__self__, "performance", performance)
        if priority and not isinstance(priority, float):
            raise TypeError("Expected argument 'priority' to be a float")
        pulumi.set(__self__, "priority", priority)
        if provisioner and not isinstance(provisioner, str):
            raise TypeError("Expected argument 'provisioner' to be a str")
        pulumi.set(__self__, "provisioner", provisioner)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if type_properties and not isinstance(type_properties, dict):
            raise TypeError("Expected argument 'type_properties' to be a dict")
        pulumi.set(__self__, "type_properties", type_properties)
        if volume_binding_mode and not isinstance(volume_binding_mode, str):
            raise TypeError("Expected argument 'volume_binding_mode' to be a str")
        pulumi.set(__self__, "volume_binding_mode", volume_binding_mode)

    @property
    @pulumi.getter(name="accessModes")
    def access_modes(self) -> Optional[Sequence[str]]:
        """
        The access mode: [ReadWriteOnce, ReadWriteMany] or [ReadWriteOnce]
        """
        return pulumi.get(self, "access_modes")

    @property
    @pulumi.getter(name="allowVolumeExpansion")
    def allow_volume_expansion(self) -> Optional[str]:
        """
        Volume can be expanded or not
        """
        return pulumi.get(self, "allow_volume_expansion")

    @property
    @pulumi.getter(name="dataResilience")
    def data_resilience(self) -> Optional[str]:
        """
        Allow single data node failure
        """
        return pulumi.get(self, "data_resilience")

    @property
    @pulumi.getter(name="failoverSpeed")
    def failover_speed(self) -> Optional[str]:
        """
        Failover speed: NA, Slow, Fast
        """
        return pulumi.get(self, "failover_speed")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def limitations(self) -> Optional[Sequence[str]]:
        """
        Limitations of the storage class
        """
        return pulumi.get(self, "limitations")

    @property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[Sequence[str]]:
        """
        Additional mount options
        """
        return pulumi.get(self, "mount_options")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def performance(self) -> Optional[str]:
        """
        Performance tier
        """
        return pulumi.get(self, "performance")

    @property
    @pulumi.getter
    def priority(self) -> Optional[float]:
        """
        Selection priority when multiple storage classes meet the criteria. 0: Highest, -1: Never use
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def provisioner(self) -> Optional[str]:
        """
        Provisioner name
        """
        return pulumi.get(self, "provisioner")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Resource provision state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="typeProperties")
    def type_properties(self) -> Any:
        """
        Properties of the StorageClass
        """
        return pulumi.get(self, "type_properties")

    @property
    @pulumi.getter(name="volumeBindingMode")
    def volume_binding_mode(self) -> Optional[str]:
        """
        Binding mode of volumes: Immediate, WaitForFirstConsumer
        """
        return pulumi.get(self, "volume_binding_mode")


class AwaitableGetStorageClassResult(GetStorageClassResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStorageClassResult(
            access_modes=self.access_modes,
            allow_volume_expansion=self.allow_volume_expansion,
            data_resilience=self.data_resilience,
            failover_speed=self.failover_speed,
            id=self.id,
            limitations=self.limitations,
            mount_options=self.mount_options,
            name=self.name,
            performance=self.performance,
            priority=self.priority,
            provisioner=self.provisioner,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type,
            type_properties=self.type_properties,
            volume_binding_mode=self.volume_binding_mode)


def get_storage_class(resource_uri: Optional[str] = None,
                      storage_class_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStorageClassResult:
    """
    Get a StorageClassResource


    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource.
    :param str storage_class_name: The name of the the storage class
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    __args__['storageClassName'] = storage_class_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kubernetesruntime/v20240301:getStorageClass', __args__, opts=opts, typ=GetStorageClassResult).value

    return AwaitableGetStorageClassResult(
        access_modes=pulumi.get(__ret__, 'access_modes'),
        allow_volume_expansion=pulumi.get(__ret__, 'allow_volume_expansion'),
        data_resilience=pulumi.get(__ret__, 'data_resilience'),
        failover_speed=pulumi.get(__ret__, 'failover_speed'),
        id=pulumi.get(__ret__, 'id'),
        limitations=pulumi.get(__ret__, 'limitations'),
        mount_options=pulumi.get(__ret__, 'mount_options'),
        name=pulumi.get(__ret__, 'name'),
        performance=pulumi.get(__ret__, 'performance'),
        priority=pulumi.get(__ret__, 'priority'),
        provisioner=pulumi.get(__ret__, 'provisioner'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        type_properties=pulumi.get(__ret__, 'type_properties'),
        volume_binding_mode=pulumi.get(__ret__, 'volume_binding_mode'))


@_utilities.lift_output_func(get_storage_class)
def get_storage_class_output(resource_uri: Optional[pulumi.Input[str]] = None,
                             storage_class_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStorageClassResult]:
    """
    Get a StorageClassResource


    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource.
    :param str storage_class_name: The name of the the storage class
    """
    ...
