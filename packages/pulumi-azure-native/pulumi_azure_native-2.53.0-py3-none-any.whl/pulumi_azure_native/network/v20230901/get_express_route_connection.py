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
    'GetExpressRouteConnectionResult',
    'AwaitableGetExpressRouteConnectionResult',
    'get_express_route_connection',
    'get_express_route_connection_output',
]

@pulumi.output_type
class GetExpressRouteConnectionResult:
    """
    ExpressRouteConnection resource.
    """
    def __init__(__self__, authorization_key=None, enable_internet_security=None, enable_private_link_fast_path=None, express_route_circuit_peering=None, express_route_gateway_bypass=None, id=None, name=None, provisioning_state=None, routing_configuration=None, routing_weight=None):
        if authorization_key and not isinstance(authorization_key, str):
            raise TypeError("Expected argument 'authorization_key' to be a str")
        pulumi.set(__self__, "authorization_key", authorization_key)
        if enable_internet_security and not isinstance(enable_internet_security, bool):
            raise TypeError("Expected argument 'enable_internet_security' to be a bool")
        pulumi.set(__self__, "enable_internet_security", enable_internet_security)
        if enable_private_link_fast_path and not isinstance(enable_private_link_fast_path, bool):
            raise TypeError("Expected argument 'enable_private_link_fast_path' to be a bool")
        pulumi.set(__self__, "enable_private_link_fast_path", enable_private_link_fast_path)
        if express_route_circuit_peering and not isinstance(express_route_circuit_peering, dict):
            raise TypeError("Expected argument 'express_route_circuit_peering' to be a dict")
        pulumi.set(__self__, "express_route_circuit_peering", express_route_circuit_peering)
        if express_route_gateway_bypass and not isinstance(express_route_gateway_bypass, bool):
            raise TypeError("Expected argument 'express_route_gateway_bypass' to be a bool")
        pulumi.set(__self__, "express_route_gateway_bypass", express_route_gateway_bypass)
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
        if routing_weight and not isinstance(routing_weight, int):
            raise TypeError("Expected argument 'routing_weight' to be a int")
        pulumi.set(__self__, "routing_weight", routing_weight)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[str]:
        """
        Authorization key to establish the connection.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> Optional[bool]:
        """
        Enable internet security.
        """
        return pulumi.get(self, "enable_internet_security")

    @property
    @pulumi.getter(name="enablePrivateLinkFastPath")
    def enable_private_link_fast_path(self) -> Optional[bool]:
        """
        Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.
        """
        return pulumi.get(self, "enable_private_link_fast_path")

    @property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> 'outputs.ExpressRouteCircuitPeeringIdResponse':
        """
        The ExpressRoute circuit peering.
        """
        return pulumi.get(self, "express_route_circuit_peering")

    @property
    @pulumi.getter(name="expressRouteGatewayBypass")
    def express_route_gateway_bypass(self) -> Optional[bool]:
        """
        Enable FastPath to vWan Firewall hub.
        """
        return pulumi.get(self, "express_route_gateway_bypass")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the express route connection resource.
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
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> Optional[int]:
        """
        The routing weight associated to the connection.
        """
        return pulumi.get(self, "routing_weight")


class AwaitableGetExpressRouteConnectionResult(GetExpressRouteConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExpressRouteConnectionResult(
            authorization_key=self.authorization_key,
            enable_internet_security=self.enable_internet_security,
            enable_private_link_fast_path=self.enable_private_link_fast_path,
            express_route_circuit_peering=self.express_route_circuit_peering,
            express_route_gateway_bypass=self.express_route_gateway_bypass,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            routing_configuration=self.routing_configuration,
            routing_weight=self.routing_weight)


def get_express_route_connection(connection_name: Optional[str] = None,
                                 express_route_gateway_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExpressRouteConnectionResult:
    """
    Gets the specified ExpressRouteConnection.


    :param str connection_name: The name of the ExpressRoute connection.
    :param str express_route_gateway_name: The name of the ExpressRoute gateway.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['connectionName'] = connection_name
    __args__['expressRouteGatewayName'] = express_route_gateway_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230901:getExpressRouteConnection', __args__, opts=opts, typ=GetExpressRouteConnectionResult).value

    return AwaitableGetExpressRouteConnectionResult(
        authorization_key=pulumi.get(__ret__, 'authorization_key'),
        enable_internet_security=pulumi.get(__ret__, 'enable_internet_security'),
        enable_private_link_fast_path=pulumi.get(__ret__, 'enable_private_link_fast_path'),
        express_route_circuit_peering=pulumi.get(__ret__, 'express_route_circuit_peering'),
        express_route_gateway_bypass=pulumi.get(__ret__, 'express_route_gateway_bypass'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        routing_configuration=pulumi.get(__ret__, 'routing_configuration'),
        routing_weight=pulumi.get(__ret__, 'routing_weight'))


@_utilities.lift_output_func(get_express_route_connection)
def get_express_route_connection_output(connection_name: Optional[pulumi.Input[str]] = None,
                                        express_route_gateway_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExpressRouteConnectionResult]:
    """
    Gets the specified ExpressRouteConnection.


    :param str connection_name: The name of the ExpressRoute connection.
    :param str express_route_gateway_name: The name of the ExpressRoute gateway.
    :param str resource_group_name: The name of the resource group.
    """
    ...
