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
    'GetReplicationProtectionClusterResult',
    'AwaitableGetReplicationProtectionClusterResult',
    'get_replication_protection_cluster',
    'get_replication_protection_cluster_output',
]

@pulumi.output_type
class GetReplicationProtectionClusterResult:
    """
    Replication protection Cluster.
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The protection cluster Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the protection cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ReplicationProtectionClusterPropertiesResponse':
        """
        The custom data.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The Type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetReplicationProtectionClusterResult(GetReplicationProtectionClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationProtectionClusterResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_replication_protection_cluster(fabric_name: Optional[str] = None,
                                       protection_container_name: Optional[str] = None,
                                       replication_protection_cluster_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       resource_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationProtectionClusterResult:
    """
    Gets the details of an ASR replication protection cluster.


    :param str fabric_name: Fabric name.
    :param str protection_container_name: Protection container name.
    :param str replication_protection_cluster_name: Replication protection cluster name.
    :param str resource_group_name: The name of the resource group where the recovery services vault is present.
    :param str resource_name: The name of the recovery services vault.
    """
    __args__ = dict()
    __args__['fabricName'] = fabric_name
    __args__['protectionContainerName'] = protection_container_name
    __args__['replicationProtectionClusterName'] = replication_protection_cluster_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:recoveryservices/v20240401:getReplicationProtectionCluster', __args__, opts=opts, typ=GetReplicationProtectionClusterResult).value

    return AwaitableGetReplicationProtectionClusterResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_replication_protection_cluster)
def get_replication_protection_cluster_output(fabric_name: Optional[pulumi.Input[str]] = None,
                                              protection_container_name: Optional[pulumi.Input[str]] = None,
                                              replication_protection_cluster_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              resource_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationProtectionClusterResult]:
    """
    Gets the details of an ASR replication protection cluster.


    :param str fabric_name: Fabric name.
    :param str protection_container_name: Protection container name.
    :param str replication_protection_cluster_name: Replication protection cluster name.
    :param str resource_group_name: The name of the resource group where the recovery services vault is present.
    :param str resource_name: The name of the recovery services vault.
    """
    ...
