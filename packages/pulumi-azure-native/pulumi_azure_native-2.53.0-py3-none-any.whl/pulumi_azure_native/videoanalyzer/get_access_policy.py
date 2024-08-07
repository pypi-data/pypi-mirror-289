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
    'GetAccessPolicyResult',
    'AwaitableGetAccessPolicyResult',
    'get_access_policy',
    'get_access_policy_output',
]

@pulumi.output_type
class GetAccessPolicyResult:
    """
    Access policies help define the authentication rules, and control access to specific video resources.
    """
    def __init__(__self__, authentication=None, id=None, name=None, role=None, system_data=None, type=None):
        if authentication and not isinstance(authentication, dict):
            raise TypeError("Expected argument 'authentication' to be a dict")
        pulumi.set(__self__, "authentication", authentication)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def authentication(self) -> Optional['outputs.JwtAuthenticationResponse']:
        """
        Authentication method to be used when validating client API access.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
    @pulumi.getter
    def role(self) -> Optional[str]:
        """
        Defines the access level granted by this policy.
        """
        return pulumi.get(self, "role")

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


class AwaitableGetAccessPolicyResult(GetAccessPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessPolicyResult(
            authentication=self.authentication,
            id=self.id,
            name=self.name,
            role=self.role,
            system_data=self.system_data,
            type=self.type)


def get_access_policy(access_policy_name: Optional[str] = None,
                      account_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessPolicyResult:
    """
    Retrieves an existing access policy resource with the given name.
    Azure REST API version: 2021-11-01-preview.


    :param str access_policy_name: The Access Policy name.
    :param str account_name: The Azure Video Analyzer account name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accessPolicyName'] = access_policy_name
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:videoanalyzer:getAccessPolicy', __args__, opts=opts, typ=GetAccessPolicyResult).value

    return AwaitableGetAccessPolicyResult(
        authentication=pulumi.get(__ret__, 'authentication'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        role=pulumi.get(__ret__, 'role'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_access_policy)
def get_access_policy_output(access_policy_name: Optional[pulumi.Input[str]] = None,
                             account_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessPolicyResult]:
    """
    Retrieves an existing access policy resource with the given name.
    Azure REST API version: 2021-11-01-preview.


    :param str access_policy_name: The Access Policy name.
    :param str account_name: The Azure Video Analyzer account name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
