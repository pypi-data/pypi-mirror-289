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
    'GetVirtualNetworkResult',
    'AwaitableGetVirtualNetworkResult',
    'get_virtual_network',
    'get_virtual_network_output',
]

@pulumi.output_type
class GetVirtualNetworkResult:
    """
    The VirtualNetworks resource definition.
    """
    def __init__(__self__, extended_location=None, id=None, inventory_item_id=None, location=None, name=None, network_name=None, provisioning_state=None, system_data=None, tags=None, type=None, uuid=None, vmm_server_id=None):
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inventory_item_id and not isinstance(inventory_item_id, str):
            raise TypeError("Expected argument 'inventory_item_id' to be a str")
        pulumi.set(__self__, "inventory_item_id", inventory_item_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_name and not isinstance(network_name, str):
            raise TypeError("Expected argument 'network_name' to be a str")
        pulumi.set(__self__, "network_name", network_name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if vmm_server_id and not isinstance(vmm_server_id, str):
            raise TypeError("Expected argument 'vmm_server_id' to be a str")
        pulumi.set(__self__, "vmm_server_id", vmm_server_id)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[str]:
        """
        Gets or sets the inventory Item ID for the resource.
        """
        return pulumi.get(self, "inventory_item_id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkName")
    def network_name(self) -> str:
        """
        Name of the virtual network in vmmServer.
        """
        return pulumi.get(self, "network_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> Optional[str]:
        """
        Unique ID of the virtual network.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[str]:
        """
        ARM Id of the vmmServer resource in which this resource resides.
        """
        return pulumi.get(self, "vmm_server_id")


class AwaitableGetVirtualNetworkResult(GetVirtualNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkResult(
            extended_location=self.extended_location,
            id=self.id,
            inventory_item_id=self.inventory_item_id,
            location=self.location,
            name=self.name,
            network_name=self.network_name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            uuid=self.uuid,
            vmm_server_id=self.vmm_server_id)


def get_virtual_network(resource_group_name: Optional[str] = None,
                        virtual_network_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkResult:
    """
    Implements VirtualNetwork GET method.
    Azure REST API version: 2022-05-21-preview.

    Other available API versions: 2023-04-01-preview, 2023-10-07, 2024-06-01.


    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_name: Name of the VirtualNetwork.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkName'] = virtual_network_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:scvmm:getVirtualNetwork', __args__, opts=opts, typ=GetVirtualNetworkResult).value

    return AwaitableGetVirtualNetworkResult(
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        inventory_item_id=pulumi.get(__ret__, 'inventory_item_id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_name=pulumi.get(__ret__, 'network_name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        uuid=pulumi.get(__ret__, 'uuid'),
        vmm_server_id=pulumi.get(__ret__, 'vmm_server_id'))


@_utilities.lift_output_func(get_virtual_network)
def get_virtual_network_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                               virtual_network_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNetworkResult]:
    """
    Implements VirtualNetwork GET method.
    Azure REST API version: 2022-05-21-preview.

    Other available API versions: 2023-04-01-preview, 2023-10-07, 2024-06-01.


    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_name: Name of the VirtualNetwork.
    """
    ...
