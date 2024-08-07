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
    'GetVirtualNetworkGatewayBgpPeerStatusResult',
    'AwaitableGetVirtualNetworkGatewayBgpPeerStatusResult',
    'get_virtual_network_gateway_bgp_peer_status',
    'get_virtual_network_gateway_bgp_peer_status_output',
]

@pulumi.output_type
class GetVirtualNetworkGatewayBgpPeerStatusResult:
    """
    Response for list BGP peer status API service call.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.BgpPeerStatusResponse']]:
        """
        List of BGP peers.
        """
        return pulumi.get(self, "value")


class AwaitableGetVirtualNetworkGatewayBgpPeerStatusResult(GetVirtualNetworkGatewayBgpPeerStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkGatewayBgpPeerStatusResult(
            value=self.value)


def get_virtual_network_gateway_bgp_peer_status(peer: Optional[str] = None,
                                                resource_group_name: Optional[str] = None,
                                                virtual_network_gateway_name: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkGatewayBgpPeerStatusResult:
    """
    The GetBgpPeerStatus operation retrieves the status of all BGP peers.


    :param str peer: The IP address of the peer to retrieve the status of.
    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_gateway_name: The name of the virtual network gateway.
    """
    __args__ = dict()
    __args__['peer'] = peer
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkGatewayName'] = virtual_network_gateway_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230201:getVirtualNetworkGatewayBgpPeerStatus', __args__, opts=opts, typ=GetVirtualNetworkGatewayBgpPeerStatusResult).value

    return AwaitableGetVirtualNetworkGatewayBgpPeerStatusResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_virtual_network_gateway_bgp_peer_status)
def get_virtual_network_gateway_bgp_peer_status_output(peer: Optional[pulumi.Input[Optional[str]]] = None,
                                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                                       virtual_network_gateway_name: Optional[pulumi.Input[str]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNetworkGatewayBgpPeerStatusResult]:
    """
    The GetBgpPeerStatus operation retrieves the status of all BGP peers.


    :param str peer: The IP address of the peer to retrieve the status of.
    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_gateway_name: The name of the virtual network gateway.
    """
    ...
