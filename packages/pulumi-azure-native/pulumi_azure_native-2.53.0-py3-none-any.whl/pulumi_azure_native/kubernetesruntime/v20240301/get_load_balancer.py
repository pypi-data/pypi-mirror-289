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
    'GetLoadBalancerResult',
    'AwaitableGetLoadBalancerResult',
    'get_load_balancer',
    'get_load_balancer_output',
]

@pulumi.output_type
class GetLoadBalancerResult:
    """
    A LoadBalancer resource for an Arc connected cluster (Microsoft.Kubernetes/connectedClusters)
    """
    def __init__(__self__, addresses=None, advertise_mode=None, bgp_peers=None, id=None, name=None, provisioning_state=None, service_selector=None, system_data=None, type=None):
        if addresses and not isinstance(addresses, list):
            raise TypeError("Expected argument 'addresses' to be a list")
        pulumi.set(__self__, "addresses", addresses)
        if advertise_mode and not isinstance(advertise_mode, str):
            raise TypeError("Expected argument 'advertise_mode' to be a str")
        pulumi.set(__self__, "advertise_mode", advertise_mode)
        if bgp_peers and not isinstance(bgp_peers, list):
            raise TypeError("Expected argument 'bgp_peers' to be a list")
        pulumi.set(__self__, "bgp_peers", bgp_peers)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_selector and not isinstance(service_selector, dict):
            raise TypeError("Expected argument 'service_selector' to be a dict")
        pulumi.set(__self__, "service_selector", service_selector)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def addresses(self) -> Sequence[str]:
        """
        IP Range
        """
        return pulumi.get(self, "addresses")

    @property
    @pulumi.getter(name="advertiseMode")
    def advertise_mode(self) -> str:
        """
        Advertise Mode
        """
        return pulumi.get(self, "advertise_mode")

    @property
    @pulumi.getter(name="bgpPeers")
    def bgp_peers(self) -> Optional[Sequence[str]]:
        """
        The list of BGP peers it should advertise to. Null or empty means to advertise to all peers.
        """
        return pulumi.get(self, "bgp_peers")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Resource provision state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceSelector")
    def service_selector(self) -> Optional[Mapping[str, str]]:
        """
        A dynamic label mapping to select related services. For instance, if you want to create a load balancer only for services with label "a=b", then please specify {"a": "b"} in the field.
        """
        return pulumi.get(self, "service_selector")

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


class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerResult(
            addresses=self.addresses,
            advertise_mode=self.advertise_mode,
            bgp_peers=self.bgp_peers,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            service_selector=self.service_selector,
            system_data=self.system_data,
            type=self.type)


def get_load_balancer(load_balancer_name: Optional[str] = None,
                      resource_uri: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoadBalancerResult:
    """
    Get a LoadBalancer


    :param str load_balancer_name: The name of the LoadBalancer
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource.
    """
    __args__ = dict()
    __args__['loadBalancerName'] = load_balancer_name
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kubernetesruntime/v20240301:getLoadBalancer', __args__, opts=opts, typ=GetLoadBalancerResult).value

    return AwaitableGetLoadBalancerResult(
        addresses=pulumi.get(__ret__, 'addresses'),
        advertise_mode=pulumi.get(__ret__, 'advertise_mode'),
        bgp_peers=pulumi.get(__ret__, 'bgp_peers'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        service_selector=pulumi.get(__ret__, 'service_selector'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_load_balancer)
def get_load_balancer_output(load_balancer_name: Optional[pulumi.Input[str]] = None,
                             resource_uri: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLoadBalancerResult]:
    """
    Get a LoadBalancer


    :param str load_balancer_name: The name of the LoadBalancer
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource.
    """
    ...
