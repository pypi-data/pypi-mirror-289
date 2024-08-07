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

__all__ = [
    'GetVirtualNetworkRuleResult',
    'AwaitableGetVirtualNetworkRuleResult',
    'get_virtual_network_rule',
    'get_virtual_network_rule_output',
]

@pulumi.output_type
class GetVirtualNetworkRuleResult:
    """
    A virtual network rule.
    """
    def __init__(__self__, id=None, ignore_missing_vnet_service_endpoint=None, name=None, state=None, type=None, virtual_network_subnet_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ignore_missing_vnet_service_endpoint and not isinstance(ignore_missing_vnet_service_endpoint, bool):
            raise TypeError("Expected argument 'ignore_missing_vnet_service_endpoint' to be a bool")
        pulumi.set(__self__, "ignore_missing_vnet_service_endpoint", ignore_missing_vnet_service_endpoint)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_network_subnet_id and not isinstance(virtual_network_subnet_id, str):
            raise TypeError("Expected argument 'virtual_network_subnet_id' to be a str")
        pulumi.set(__self__, "virtual_network_subnet_id", virtual_network_subnet_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[bool]:
        """
        Create firewall rule before the virtual network has vnet service endpoint enabled.
        """
        return pulumi.get(self, "ignore_missing_vnet_service_endpoint")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Virtual Network Rule State
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> str:
        """
        The ARM resource id of the virtual network subnet.
        """
        return pulumi.get(self, "virtual_network_subnet_id")


class AwaitableGetVirtualNetworkRuleResult(GetVirtualNetworkRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkRuleResult(
            id=self.id,
            ignore_missing_vnet_service_endpoint=self.ignore_missing_vnet_service_endpoint,
            name=self.name,
            state=self.state,
            type=self.type,
            virtual_network_subnet_id=self.virtual_network_subnet_id)


def get_virtual_network_rule(resource_group_name: Optional[str] = None,
                             server_name: Optional[str] = None,
                             virtual_network_rule_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkRuleResult:
    """
    Gets a virtual network rule.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    :param str virtual_network_rule_name: The name of the virtual network rule.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    __args__['virtualNetworkRuleName'] = virtual_network_rule_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbforpostgresql/v20171201preview:getVirtualNetworkRule', __args__, opts=opts, typ=GetVirtualNetworkRuleResult).value

    return AwaitableGetVirtualNetworkRuleResult(
        id=pulumi.get(__ret__, 'id'),
        ignore_missing_vnet_service_endpoint=pulumi.get(__ret__, 'ignore_missing_vnet_service_endpoint'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        type=pulumi.get(__ret__, 'type'),
        virtual_network_subnet_id=pulumi.get(__ret__, 'virtual_network_subnet_id'))


@_utilities.lift_output_func(get_virtual_network_rule)
def get_virtual_network_rule_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                    server_name: Optional[pulumi.Input[str]] = None,
                                    virtual_network_rule_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNetworkRuleResult]:
    """
    Gets a virtual network rule.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    :param str virtual_network_rule_name: The name of the virtual network rule.
    """
    ...
