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
    'ListApplicationTokensResult',
    'AwaitableListApplicationTokensResult',
    'list_application_tokens',
    'list_application_tokens_output',
]

@pulumi.output_type
class ListApplicationTokensResult:
    """
    The array of managed identity tokens.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.ManagedIdentityTokenResponse']]:
        """
        The array of managed identity tokens.
        """
        return pulumi.get(self, "value")


class AwaitableListApplicationTokensResult(ListApplicationTokensResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListApplicationTokensResult(
            value=self.value)


def list_application_tokens(application_name: Optional[str] = None,
                            authorization_audience: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            user_assigned_identities: Optional[Sequence[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListApplicationTokensResult:
    """
    List tokens for application.
    Azure REST API version: 2021-07-01.

    Other available API versions: 2018-06-01, 2023-12-01-preview.


    :param str application_name: The name of the managed application.
    :param str authorization_audience: The authorization audience.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param Sequence[str] user_assigned_identities: The user assigned identities.
    """
    __args__ = dict()
    __args__['applicationName'] = application_name
    __args__['authorizationAudience'] = authorization_audience
    __args__['resourceGroupName'] = resource_group_name
    __args__['userAssignedIdentities'] = user_assigned_identities
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:solutions:listApplicationTokens', __args__, opts=opts, typ=ListApplicationTokensResult).value

    return AwaitableListApplicationTokensResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_application_tokens)
def list_application_tokens_output(application_name: Optional[pulumi.Input[str]] = None,
                                   authorization_audience: Optional[pulumi.Input[Optional[str]]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   user_assigned_identities: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListApplicationTokensResult]:
    """
    List tokens for application.
    Azure REST API version: 2021-07-01.

    Other available API versions: 2018-06-01, 2023-12-01-preview.


    :param str application_name: The name of the managed application.
    :param str authorization_audience: The authorization audience.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param Sequence[str] user_assigned_identities: The user assigned identities.
    """
    ...
