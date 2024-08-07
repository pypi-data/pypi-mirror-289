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
    'ListRegistryCredentialsResult',
    'AwaitableListRegistryCredentialsResult',
    'list_registry_credentials',
    'list_registry_credentials_output',
]

@pulumi.output_type
class ListRegistryCredentialsResult:
    """
    The response from the ListCredentials operation.
    """
    def __init__(__self__, passwords=None, username=None):
        if passwords and not isinstance(passwords, list):
            raise TypeError("Expected argument 'passwords' to be a list")
        pulumi.set(__self__, "passwords", passwords)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def passwords(self) -> Optional[Sequence['outputs.RegistryPasswordResponse']]:
        """
        The list of passwords for a container registry.
        """
        return pulumi.get(self, "passwords")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        """
        The username for a container registry.
        """
        return pulumi.get(self, "username")


class AwaitableListRegistryCredentialsResult(ListRegistryCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListRegistryCredentialsResult(
            passwords=self.passwords,
            username=self.username)


def list_registry_credentials(registry_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListRegistryCredentialsResult:
    """
    Lists the login credentials for the specified container registry.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20231101preview:listRegistryCredentials', __args__, opts=opts, typ=ListRegistryCredentialsResult).value

    return AwaitableListRegistryCredentialsResult(
        passwords=pulumi.get(__ret__, 'passwords'),
        username=pulumi.get(__ret__, 'username'))


@_utilities.lift_output_func(list_registry_credentials)
def list_registry_credentials_output(registry_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListRegistryCredentialsResult]:
    """
    Lists the login credentials for the specified container registry.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
