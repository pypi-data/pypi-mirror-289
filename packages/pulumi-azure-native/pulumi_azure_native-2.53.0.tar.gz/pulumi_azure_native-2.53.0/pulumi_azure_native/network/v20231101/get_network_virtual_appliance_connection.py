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
    'GetNetworkVirtualApplianceConnectionResult',
    'AwaitableGetNetworkVirtualApplianceConnectionResult',
    'get_network_virtual_appliance_connection',
    'get_network_virtual_appliance_connection_output',
]

@pulumi.output_type
class GetNetworkVirtualApplianceConnectionResult:
    """
    NetworkVirtualApplianceConnection resource.
    """
    def __init__(__self__, asn=None, bgp_peer_address=None, enable_internet_security=None, id=None, name=None, provisioning_state=None, routing_configuration=None, tunnel_identifier=None):
        if asn and not isinstance(asn, float):
            raise TypeError("Expected argument 'asn' to be a float")
        pulumi.set(__self__, "asn", asn)
        if bgp_peer_address and not isinstance(bgp_peer_address, list):
            raise TypeError("Expected argument 'bgp_peer_address' to be a list")
        pulumi.set(__self__, "bgp_peer_address", bgp_peer_address)
        if enable_internet_security and not isinstance(enable_internet_security, bool):
            raise TypeError("Expected argument 'enable_internet_security' to be a bool")
        pulumi.set(__self__, "enable_internet_security", enable_internet_security)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if routing_configuration and not isinstance(routing_configuration, dict):
            raise TypeError("Expected argument 'routing_configuration' to be a dict")
        pulumi.set(__self__, "routing_configuration", routing_configuration)
        if tunnel_identifier and not isinstance(tunnel_identifier, float):
            raise TypeError("Expected argument 'tunnel_identifier' to be a float")
        pulumi.set(__self__, "tunnel_identifier", tunnel_identifier)

    @property
    @pulumi.getter
    def asn(self) -> Optional[float]:
        """
        Network Virtual Appliance ASN.
        """
        return pulumi.get(self, "asn")

    @property
    @pulumi.getter(name="bgpPeerAddress")
    def bgp_peer_address(self) -> Optional[Sequence[str]]:
        """
        List of bgpPeerAddresses for the NVA instances
        """
        return pulumi.get(self, "bgp_peer_address")

    @property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> Optional[bool]:
        """
        Enable internet security.
        """
        return pulumi.get(self, "enable_internet_security")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the NetworkVirtualApplianceConnection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> Optional['outputs.RoutingConfigurationResponse']:
        """
        The Routing Configuration indicating the associated and propagated route tables on this connection.
        """
        return pulumi.get(self, "routing_configuration")

    @property
    @pulumi.getter(name="tunnelIdentifier")
    def tunnel_identifier(self) -> Optional[float]:
        """
        Unique identifier for the connection.
        """
        return pulumi.get(self, "tunnel_identifier")


class AwaitableGetNetworkVirtualApplianceConnectionResult(GetNetworkVirtualApplianceConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkVirtualApplianceConnectionResult(
            asn=self.asn,
            bgp_peer_address=self.bgp_peer_address,
            enable_internet_security=self.enable_internet_security,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            routing_configuration=self.routing_configuration,
            tunnel_identifier=self.tunnel_identifier)


def get_network_virtual_appliance_connection(connection_name: Optional[str] = None,
                                             network_virtual_appliance_name: Optional[str] = None,
                                             resource_group_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkVirtualApplianceConnectionResult:
    """
    Retrieves the details of specified NVA connection.


    :param str connection_name: The name of the NVA connection.
    :param str network_virtual_appliance_name: The name of the Network Virtual Appliance.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['connectionName'] = connection_name
    __args__['networkVirtualApplianceName'] = network_virtual_appliance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20231101:getNetworkVirtualApplianceConnection', __args__, opts=opts, typ=GetNetworkVirtualApplianceConnectionResult).value

    return AwaitableGetNetworkVirtualApplianceConnectionResult(
        asn=pulumi.get(__ret__, 'asn'),
        bgp_peer_address=pulumi.get(__ret__, 'bgp_peer_address'),
        enable_internet_security=pulumi.get(__ret__, 'enable_internet_security'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        routing_configuration=pulumi.get(__ret__, 'routing_configuration'),
        tunnel_identifier=pulumi.get(__ret__, 'tunnel_identifier'))


@_utilities.lift_output_func(get_network_virtual_appliance_connection)
def get_network_virtual_appliance_connection_output(connection_name: Optional[pulumi.Input[str]] = None,
                                                    network_virtual_appliance_name: Optional[pulumi.Input[str]] = None,
                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkVirtualApplianceConnectionResult]:
    """
    Retrieves the details of specified NVA connection.


    :param str connection_name: The name of the NVA connection.
    :param str network_virtual_appliance_name: The name of the Network Virtual Appliance.
    :param str resource_group_name: The name of the resource group.
    """
    ...
