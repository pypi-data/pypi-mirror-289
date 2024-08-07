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
    'GetDiagnosticServiceTokenReadWriteResult',
    'AwaitableGetDiagnosticServiceTokenReadWriteResult',
    'get_diagnostic_service_token_read_write',
    'get_diagnostic_service_token_read_write_output',
]

@pulumi.output_type
class GetDiagnosticServiceTokenReadWriteResult:
    """
    The response to a diagnostic services token query.
    """
    def __init__(__self__, token=None):
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        """
        JWT token for accessing application insights diagnostic service data.
        """
        return pulumi.get(self, "token")


class AwaitableGetDiagnosticServiceTokenReadWriteResult(GetDiagnosticServiceTokenReadWriteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiagnosticServiceTokenReadWriteResult(
            token=self.token)


def get_diagnostic_service_token_read_write(resource_uri: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiagnosticServiceTokenReadWriteResult:
    """
    Gets an read-write access token for application insights diagnostic service data.


    :param str resource_uri: The identifier of the resource.
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20210303preview:getDiagnosticServiceTokenReadWrite', __args__, opts=opts, typ=GetDiagnosticServiceTokenReadWriteResult).value

    return AwaitableGetDiagnosticServiceTokenReadWriteResult(
        token=pulumi.get(__ret__, 'token'))


@_utilities.lift_output_func(get_diagnostic_service_token_read_write)
def get_diagnostic_service_token_read_write_output(resource_uri: Optional[pulumi.Input[str]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDiagnosticServiceTokenReadWriteResult]:
    """
    Gets an read-write access token for application insights diagnostic service data.


    :param str resource_uri: The identifier of the resource.
    """
    ...
