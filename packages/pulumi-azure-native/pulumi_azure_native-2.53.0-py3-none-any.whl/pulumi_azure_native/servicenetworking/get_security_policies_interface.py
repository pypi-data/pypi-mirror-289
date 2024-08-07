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
    'GetSecurityPoliciesInterfaceResult',
    'AwaitableGetSecurityPoliciesInterfaceResult',
    'get_security_policies_interface',
    'get_security_policies_interface_output',
]

@pulumi.output_type
class GetSecurityPoliciesInterfaceResult:
    """
    SecurityPolicy Subresource of Traffic Controller.
    """
    def __init__(__self__, id=None, location=None, name=None, policy_type=None, provisioning_state=None, system_data=None, tags=None, type=None, waf_policy=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policy_type and not isinstance(policy_type, str):
            raise TypeError("Expected argument 'policy_type' to be a str")
        pulumi.set(__self__, "policy_type", policy_type)
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
        if waf_policy and not isinstance(waf_policy, dict):
            raise TypeError("Expected argument 'waf_policy' to be a dict")
        pulumi.set(__self__, "waf_policy", waf_policy)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
    @pulumi.getter(name="policyType")
    def policy_type(self) -> str:
        """
        Type of the Traffic Controller Security Policy
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning State of Traffic Controller SecurityPolicy Resource
        """
        return pulumi.get(self, "provisioning_state")

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
    @pulumi.getter(name="wafPolicy")
    def waf_policy(self) -> Optional['outputs.WafPolicyResponse']:
        """
        Web Application Firewall Policy of the Traffic Controller Security Policy
        """
        return pulumi.get(self, "waf_policy")


class AwaitableGetSecurityPoliciesInterfaceResult(GetSecurityPoliciesInterfaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityPoliciesInterfaceResult(
            id=self.id,
            location=self.location,
            name=self.name,
            policy_type=self.policy_type,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            waf_policy=self.waf_policy)


def get_security_policies_interface(resource_group_name: Optional[str] = None,
                                    security_policy_name: Optional[str] = None,
                                    traffic_controller_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityPoliciesInterfaceResult:
    """
    Get a SecurityPolicy
    Azure REST API version: 2024-05-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str security_policy_name: SecurityPolicy
    :param str traffic_controller_name: traffic controller name for path
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['securityPolicyName'] = security_policy_name
    __args__['trafficControllerName'] = traffic_controller_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicenetworking:getSecurityPoliciesInterface', __args__, opts=opts, typ=GetSecurityPoliciesInterfaceResult).value

    return AwaitableGetSecurityPoliciesInterfaceResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        policy_type=pulumi.get(__ret__, 'policy_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        waf_policy=pulumi.get(__ret__, 'waf_policy'))


@_utilities.lift_output_func(get_security_policies_interface)
def get_security_policies_interface_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                           security_policy_name: Optional[pulumi.Input[str]] = None,
                                           traffic_controller_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityPoliciesInterfaceResult]:
    """
    Get a SecurityPolicy
    Azure REST API version: 2024-05-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str security_policy_name: SecurityPolicy
    :param str traffic_controller_name: traffic controller name for path
    """
    ...
