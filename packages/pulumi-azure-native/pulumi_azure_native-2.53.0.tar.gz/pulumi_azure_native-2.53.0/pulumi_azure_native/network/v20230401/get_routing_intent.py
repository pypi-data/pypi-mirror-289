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
    'GetRoutingIntentResult',
    'AwaitableGetRoutingIntentResult',
    'get_routing_intent',
    'get_routing_intent_output',
]

@pulumi.output_type
class GetRoutingIntentResult:
    """
    The routing intent child resource of a Virtual hub.
    """
    def __init__(__self__, etag=None, id=None, name=None, provisioning_state=None, routing_policies=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if routing_policies and not isinstance(routing_policies, list):
            raise TypeError("Expected argument 'routing_policies' to be a list")
        pulumi.set(__self__, "routing_policies", routing_policies)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

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
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the RoutingIntent resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="routingPolicies")
    def routing_policies(self) -> Optional[Sequence['outputs.RoutingPolicyResponse']]:
        """
        List of routing policies.
        """
        return pulumi.get(self, "routing_policies")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetRoutingIntentResult(GetRoutingIntentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoutingIntentResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            routing_policies=self.routing_policies,
            type=self.type)


def get_routing_intent(resource_group_name: Optional[str] = None,
                       routing_intent_name: Optional[str] = None,
                       virtual_hub_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoutingIntentResult:
    """
    Retrieves the details of a RoutingIntent.


    :param str resource_group_name: The resource group name of the RoutingIntent.
    :param str routing_intent_name: The name of the RoutingIntent.
    :param str virtual_hub_name: The name of the VirtualHub.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['routingIntentName'] = routing_intent_name
    __args__['virtualHubName'] = virtual_hub_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230401:getRoutingIntent', __args__, opts=opts, typ=GetRoutingIntentResult).value

    return AwaitableGetRoutingIntentResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        routing_policies=pulumi.get(__ret__, 'routing_policies'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_routing_intent)
def get_routing_intent_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                              routing_intent_name: Optional[pulumi.Input[str]] = None,
                              virtual_hub_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoutingIntentResult]:
    """
    Retrieves the details of a RoutingIntent.


    :param str resource_group_name: The resource group name of the RoutingIntent.
    :param str routing_intent_name: The name of the RoutingIntent.
    :param str virtual_hub_name: The name of the VirtualHub.
    """
    ...
