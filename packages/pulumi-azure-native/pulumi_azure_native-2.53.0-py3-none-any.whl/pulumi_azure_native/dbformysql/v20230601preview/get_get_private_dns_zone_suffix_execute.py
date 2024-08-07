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
    'GetGetPrivateDnsZoneSuffixExecuteResult',
    'AwaitableGetGetPrivateDnsZoneSuffixExecuteResult',
    'get_get_private_dns_zone_suffix_execute',
    'get_get_private_dns_zone_suffix_execute_output',
]

@pulumi.output_type
class GetGetPrivateDnsZoneSuffixExecuteResult:
    """
    The response of get private dns zone suffix.
    """
    def __init__(__self__, private_dns_zone_suffix=None):
        if private_dns_zone_suffix and not isinstance(private_dns_zone_suffix, str):
            raise TypeError("Expected argument 'private_dns_zone_suffix' to be a str")
        pulumi.set(__self__, "private_dns_zone_suffix", private_dns_zone_suffix)

    @property
    @pulumi.getter(name="privateDnsZoneSuffix")
    def private_dns_zone_suffix(self) -> Optional[str]:
        """
        Represents the private DNS zone suffix.
        """
        return pulumi.get(self, "private_dns_zone_suffix")


class AwaitableGetGetPrivateDnsZoneSuffixExecuteResult(GetGetPrivateDnsZoneSuffixExecuteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGetPrivateDnsZoneSuffixExecuteResult(
            private_dns_zone_suffix=self.private_dns_zone_suffix)


def get_get_private_dns_zone_suffix_execute(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGetPrivateDnsZoneSuffixExecuteResult:
    """
    Get private DNS zone suffix in the cloud.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbformysql/v20230601preview:getGetPrivateDnsZoneSuffixExecute', __args__, opts=opts, typ=GetGetPrivateDnsZoneSuffixExecuteResult).value

    return AwaitableGetGetPrivateDnsZoneSuffixExecuteResult(
        private_dns_zone_suffix=pulumi.get(__ret__, 'private_dns_zone_suffix'))


@_utilities.lift_output_func(get_get_private_dns_zone_suffix_execute)
def get_get_private_dns_zone_suffix_execute_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGetPrivateDnsZoneSuffixExecuteResult]:
    """
    Get private DNS zone suffix in the cloud.
    """
    ...
