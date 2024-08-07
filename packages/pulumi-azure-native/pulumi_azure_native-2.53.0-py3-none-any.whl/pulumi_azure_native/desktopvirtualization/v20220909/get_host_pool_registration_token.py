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
    'GetHostPoolRegistrationTokenResult',
    'AwaitableGetHostPoolRegistrationTokenResult',
    'get_host_pool_registration_token',
    'get_host_pool_registration_token_output',
]

@pulumi.output_type
class GetHostPoolRegistrationTokenResult:
    """
    Represents a RegistrationInfo definition.
    """
    def __init__(__self__, expiration_time=None, registration_token_operation=None, token=None):
        if expiration_time and not isinstance(expiration_time, str):
            raise TypeError("Expected argument 'expiration_time' to be a str")
        pulumi.set(__self__, "expiration_time", expiration_time)
        if registration_token_operation and not isinstance(registration_token_operation, str):
            raise TypeError("Expected argument 'registration_token_operation' to be a str")
        pulumi.set(__self__, "registration_token_operation", registration_token_operation)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[str]:
        """
        Expiration time of registration token.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter(name="registrationTokenOperation")
    def registration_token_operation(self) -> Optional[str]:
        """
        The type of resetting the token.
        """
        return pulumi.get(self, "registration_token_operation")

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        """
        The registration token base64 encoded string.
        """
        return pulumi.get(self, "token")


class AwaitableGetHostPoolRegistrationTokenResult(GetHostPoolRegistrationTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHostPoolRegistrationTokenResult(
            expiration_time=self.expiration_time,
            registration_token_operation=self.registration_token_operation,
            token=self.token)


def get_host_pool_registration_token(host_pool_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHostPoolRegistrationTokenResult:
    """
    Registration token of the host pool.


    :param str host_pool_name: The name of the host pool within the specified resource group
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['hostPoolName'] = host_pool_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:desktopvirtualization/v20220909:getHostPoolRegistrationToken', __args__, opts=opts, typ=GetHostPoolRegistrationTokenResult).value

    return AwaitableGetHostPoolRegistrationTokenResult(
        expiration_time=pulumi.get(__ret__, 'expiration_time'),
        registration_token_operation=pulumi.get(__ret__, 'registration_token_operation'),
        token=pulumi.get(__ret__, 'token'))


@_utilities.lift_output_func(get_host_pool_registration_token)
def get_host_pool_registration_token_output(host_pool_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHostPoolRegistrationTokenResult]:
    """
    Registration token of the host pool.


    :param str host_pool_name: The name of the host pool within the specified resource group
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
