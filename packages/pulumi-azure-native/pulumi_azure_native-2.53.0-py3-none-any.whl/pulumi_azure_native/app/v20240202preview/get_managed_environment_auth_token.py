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
    'GetManagedEnvironmentAuthTokenResult',
    'AwaitableGetManagedEnvironmentAuthTokenResult',
    'get_managed_environment_auth_token',
    'get_managed_environment_auth_token_output',
]

@pulumi.output_type
class GetManagedEnvironmentAuthTokenResult:
    """
    Environment Auth Token.
    """
    def __init__(__self__, expires=None, id=None, location=None, name=None, system_data=None, tags=None, token=None, type=None):
        if expires and not isinstance(expires, str):
            raise TypeError("Expected argument 'expires' to be a str")
        pulumi.set(__self__, "expires", expires)
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
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def expires(self) -> str:
        """
        Token expiration date.
        """
        return pulumi.get(self, "expires")

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
    def token(self) -> str:
        """
        Auth token value.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedEnvironmentAuthTokenResult(GetManagedEnvironmentAuthTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedEnvironmentAuthTokenResult(
            expires=self.expires,
            id=self.id,
            location=self.location,
            name=self.name,
            system_data=self.system_data,
            tags=self.tags,
            token=self.token,
            type=self.type)


def get_managed_environment_auth_token(environment_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedEnvironmentAuthTokenResult:
    """
    Checks if resource name is available.


    :param str environment_name: Name of the Managed Environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20240202preview:getManagedEnvironmentAuthToken', __args__, opts=opts, typ=GetManagedEnvironmentAuthTokenResult).value

    return AwaitableGetManagedEnvironmentAuthTokenResult(
        expires=pulumi.get(__ret__, 'expires'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        token=pulumi.get(__ret__, 'token'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_managed_environment_auth_token)
def get_managed_environment_auth_token_output(environment_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedEnvironmentAuthTokenResult]:
    """
    Checks if resource name is available.


    :param str environment_name: Name of the Managed Environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
