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
    'ListClusterZonesResult',
    'AwaitableListClusterZonesResult',
    'list_cluster_zones',
    'list_cluster_zones_output',
]

@pulumi.output_type
class ListClusterZonesResult:
    """
    List of all zones and associated hosts for a cluster
    """
    def __init__(__self__, zones=None):
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence['outputs.ClusterZoneResponse']]:
        """
        Zone and associated hosts info
        """
        return pulumi.get(self, "zones")


class AwaitableListClusterZonesResult(ListClusterZonesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListClusterZonesResult(
            zones=self.zones)


def list_cluster_zones(cluster_name: Optional[str] = None,
                       private_cloud_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListClusterZonesResult:
    """
    List of all zones and associated hosts for a cluster


    :param str cluster_name: Name of the cluster in the private cloud
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20230301:listClusterZones', __args__, opts=opts, typ=ListClusterZonesResult).value

    return AwaitableListClusterZonesResult(
        zones=pulumi.get(__ret__, 'zones'))


@_utilities.lift_output_func(list_cluster_zones)
def list_cluster_zones_output(cluster_name: Optional[pulumi.Input[str]] = None,
                              private_cloud_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListClusterZonesResult]:
    """
    List of all zones and associated hosts for a cluster


    :param str cluster_name: Name of the cluster in the private cloud
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
