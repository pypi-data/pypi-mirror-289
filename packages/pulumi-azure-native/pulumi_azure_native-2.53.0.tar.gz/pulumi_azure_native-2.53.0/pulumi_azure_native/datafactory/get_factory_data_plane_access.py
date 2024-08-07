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
    'GetFactoryDataPlaneAccessResult',
    'AwaitableGetFactoryDataPlaneAccessResult',
    'get_factory_data_plane_access',
    'get_factory_data_plane_access_output',
]

@pulumi.output_type
class GetFactoryDataPlaneAccessResult:
    """
    Get Data Plane read only token response definition.
    """
    def __init__(__self__, access_token=None, data_plane_url=None, policy=None):
        if access_token and not isinstance(access_token, str):
            raise TypeError("Expected argument 'access_token' to be a str")
        pulumi.set(__self__, "access_token", access_token)
        if data_plane_url and not isinstance(data_plane_url, str):
            raise TypeError("Expected argument 'data_plane_url' to be a str")
        pulumi.set(__self__, "data_plane_url", data_plane_url)
        if policy and not isinstance(policy, dict):
            raise TypeError("Expected argument 'policy' to be a dict")
        pulumi.set(__self__, "policy", policy)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[str]:
        """
        Data Plane read only access token.
        """
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter(name="dataPlaneUrl")
    def data_plane_url(self) -> Optional[str]:
        """
        Data Plane service base URL.
        """
        return pulumi.get(self, "data_plane_url")

    @property
    @pulumi.getter
    def policy(self) -> Optional['outputs.UserAccessPolicyResponse']:
        """
        The user access policy.
        """
        return pulumi.get(self, "policy")


class AwaitableGetFactoryDataPlaneAccessResult(GetFactoryDataPlaneAccessResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFactoryDataPlaneAccessResult(
            access_token=self.access_token,
            data_plane_url=self.data_plane_url,
            policy=self.policy)


def get_factory_data_plane_access(access_resource_path: Optional[str] = None,
                                  expire_time: Optional[str] = None,
                                  factory_name: Optional[str] = None,
                                  permissions: Optional[str] = None,
                                  profile_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  start_time: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFactoryDataPlaneAccessResult:
    """
    Get Data Plane access.
    Azure REST API version: 2018-06-01.


    :param str access_resource_path: The resource path to get access relative to factory. Currently only empty string is supported which corresponds to the factory resource.
    :param str expire_time: Expiration time for the token. Maximum duration for the token is eight hours and by default the token will expire in eight hours.
    :param str factory_name: The factory name.
    :param str permissions: The string with permissions for Data Plane access. Currently only 'r' is supported which grants read only access.
    :param str profile_name: The name of the profile. Currently only the default is supported. The default value is DefaultProfile.
    :param str resource_group_name: The resource group name.
    :param str start_time: Start time for the token. If not specified the current time will be used.
    """
    __args__ = dict()
    __args__['accessResourcePath'] = access_resource_path
    __args__['expireTime'] = expire_time
    __args__['factoryName'] = factory_name
    __args__['permissions'] = permissions
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['startTime'] = start_time
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory:getFactoryDataPlaneAccess', __args__, opts=opts, typ=GetFactoryDataPlaneAccessResult).value

    return AwaitableGetFactoryDataPlaneAccessResult(
        access_token=pulumi.get(__ret__, 'access_token'),
        data_plane_url=pulumi.get(__ret__, 'data_plane_url'),
        policy=pulumi.get(__ret__, 'policy'))


@_utilities.lift_output_func(get_factory_data_plane_access)
def get_factory_data_plane_access_output(access_resource_path: Optional[pulumi.Input[Optional[str]]] = None,
                                         expire_time: Optional[pulumi.Input[Optional[str]]] = None,
                                         factory_name: Optional[pulumi.Input[str]] = None,
                                         permissions: Optional[pulumi.Input[Optional[str]]] = None,
                                         profile_name: Optional[pulumi.Input[Optional[str]]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         start_time: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFactoryDataPlaneAccessResult]:
    """
    Get Data Plane access.
    Azure REST API version: 2018-06-01.


    :param str access_resource_path: The resource path to get access relative to factory. Currently only empty string is supported which corresponds to the factory resource.
    :param str expire_time: Expiration time for the token. Maximum duration for the token is eight hours and by default the token will expire in eight hours.
    :param str factory_name: The factory name.
    :param str permissions: The string with permissions for Data Plane access. Currently only 'r' is supported which grants read only access.
    :param str profile_name: The name of the profile. Currently only the default is supported. The default value is DefaultProfile.
    :param str resource_group_name: The resource group name.
    :param str start_time: Start time for the token. If not specified the current time will be used.
    """
    ...
