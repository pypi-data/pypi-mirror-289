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
    'GetDatastoreResult',
    'AwaitableGetDatastoreResult',
    'get_datastore',
    'get_datastore_output',
]

@pulumi.output_type
class GetDatastoreResult:
    """
    A datastore resource
    """
    def __init__(__self__, disk_pool_volume=None, id=None, name=None, net_app_volume=None, provisioning_state=None, status=None, type=None):
        if disk_pool_volume and not isinstance(disk_pool_volume, dict):
            raise TypeError("Expected argument 'disk_pool_volume' to be a dict")
        pulumi.set(__self__, "disk_pool_volume", disk_pool_volume)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if net_app_volume and not isinstance(net_app_volume, dict):
            raise TypeError("Expected argument 'net_app_volume' to be a dict")
        pulumi.set(__self__, "net_app_volume", net_app_volume)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="diskPoolVolume")
    def disk_pool_volume(self) -> Optional['outputs.DiskPoolVolumeResponse']:
        """
        An iSCSI volume
        """
        return pulumi.get(self, "disk_pool_volume")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="netAppVolume")
    def net_app_volume(self) -> Optional['outputs.NetAppVolumeResponse']:
        """
        An Azure NetApp Files volume
        """
        return pulumi.get(self, "net_app_volume")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The state of the datastore provisioning
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The operational status of the datastore
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetDatastoreResult(GetDatastoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatastoreResult(
            disk_pool_volume=self.disk_pool_volume,
            id=self.id,
            name=self.name,
            net_app_volume=self.net_app_volume,
            provisioning_state=self.provisioning_state,
            status=self.status,
            type=self.type)


def get_datastore(cluster_name: Optional[str] = None,
                  datastore_name: Optional[str] = None,
                  private_cloud_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatastoreResult:
    """
    A datastore resource


    :param str cluster_name: Name of the cluster in the private cloud
    :param str datastore_name: Name of the datastore in the private cloud cluster
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['datastoreName'] = datastore_name
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20220501:getDatastore', __args__, opts=opts, typ=GetDatastoreResult).value

    return AwaitableGetDatastoreResult(
        disk_pool_volume=pulumi.get(__ret__, 'disk_pool_volume'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        net_app_volume=pulumi.get(__ret__, 'net_app_volume'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_datastore)
def get_datastore_output(cluster_name: Optional[pulumi.Input[str]] = None,
                         datastore_name: Optional[pulumi.Input[str]] = None,
                         private_cloud_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatastoreResult]:
    """
    A datastore resource


    :param str cluster_name: Name of the cluster in the private cloud
    :param str datastore_name: Name of the datastore in the private cloud cluster
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
