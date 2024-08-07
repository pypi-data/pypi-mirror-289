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
    'GetL2ConnectionResult',
    'AwaitableGetL2ConnectionResult',
    'get_l2_connection',
    'get_l2_connection_output',
]

@pulumi.output_type
class GetL2ConnectionResult:
    """
    Connects an edge site to an orbital gateway and describes what layer 2 traffic to forward between them.
    """
    def __init__(__self__, circuit_id=None, edge_site=None, ground_station=None, id=None, location=None, name=None, system_data=None, tags=None, type=None, vlan_id=None):
        if circuit_id and not isinstance(circuit_id, str):
            raise TypeError("Expected argument 'circuit_id' to be a str")
        pulumi.set(__self__, "circuit_id", circuit_id)
        if edge_site and not isinstance(edge_site, dict):
            raise TypeError("Expected argument 'edge_site' to be a dict")
        pulumi.set(__self__, "edge_site", edge_site)
        if ground_station and not isinstance(ground_station, dict):
            raise TypeError("Expected argument 'ground_station' to be a dict")
        pulumi.set(__self__, "ground_station", ground_station)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vlan_id and not isinstance(vlan_id, int):
            raise TypeError("Expected argument 'vlan_id' to be a int")
        pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter(name="circuitId")
    def circuit_id(self) -> str:
        """
        Globally-unique identifier for this connection that is to be used as a circuit ID.
        """
        return pulumi.get(self, "circuit_id")

    @property
    @pulumi.getter(name="edgeSite")
    def edge_site(self) -> 'outputs.L2ConnectionsPropertiesResponseEdgeSite':
        """
        A reference to an Microsoft.Orbital/edgeSites resource to route traffic for.
        """
        return pulumi.get(self, "edge_site")

    @property
    @pulumi.getter(name="groundStation")
    def ground_station(self) -> 'outputs.L2ConnectionsPropertiesResponseGroundStation':
        """
        A reference to an Microsoft.Orbital/groundStations resource to route traffic for.
        """
        return pulumi.get(self, "ground_station")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> int:
        """
        The VLAN ID for the L2 connection.
        """
        return pulumi.get(self, "vlan_id")


class AwaitableGetL2ConnectionResult(GetL2ConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetL2ConnectionResult(
            circuit_id=self.circuit_id,
            edge_site=self.edge_site,
            ground_station=self.ground_station,
            id=self.id,
            location=self.location,
            name=self.name,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vlan_id=self.vlan_id)


def get_l2_connection(l2_connection_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetL2ConnectionResult:
    """
    Gets the specified L2 connection in a specified resource group.


    :param str l2_connection_name: L2 Connection name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['l2ConnectionName'] = l2_connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:orbital/v20240301preview:getL2Connection', __args__, opts=opts, typ=GetL2ConnectionResult).value

    return AwaitableGetL2ConnectionResult(
        circuit_id=pulumi.get(__ret__, 'circuit_id'),
        edge_site=pulumi.get(__ret__, 'edge_site'),
        ground_station=pulumi.get(__ret__, 'ground_station'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vlan_id=pulumi.get(__ret__, 'vlan_id'))


@_utilities.lift_output_func(get_l2_connection)
def get_l2_connection_output(l2_connection_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetL2ConnectionResult]:
    """
    Gets the specified L2 connection in a specified resource group.


    :param str l2_connection_name: L2 Connection name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
