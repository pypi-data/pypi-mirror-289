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
    'GetBuildServiceBuildResultLogResult',
    'AwaitableGetBuildServiceBuildResultLogResult',
    'get_build_service_build_result_log',
    'get_build_service_build_result_log_output',
]

@pulumi.output_type
class GetBuildServiceBuildResultLogResult:
    """
    Build result log resource properties payload
    """
    def __init__(__self__, blob_url=None):
        if blob_url and not isinstance(blob_url, str):
            raise TypeError("Expected argument 'blob_url' to be a str")
        pulumi.set(__self__, "blob_url", blob_url)

    @property
    @pulumi.getter(name="blobUrl")
    def blob_url(self) -> Optional[str]:
        """
        The public download URL of this build result log
        """
        return pulumi.get(self, "blob_url")


class AwaitableGetBuildServiceBuildResultLogResult(GetBuildServiceBuildResultLogResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBuildServiceBuildResultLogResult(
            blob_url=self.blob_url)


def get_build_service_build_result_log(build_name: Optional[str] = None,
                                       build_result_name: Optional[str] = None,
                                       build_service_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       service_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBuildServiceBuildResultLogResult:
    """
    Get a KPack build result log download URL.


    :param str build_name: The name of the build resource.
    :param str build_result_name: The name of the build result resource.
    :param str build_service_name: The name of the build service resource.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    __args__ = dict()
    __args__['buildName'] = build_name
    __args__['buildResultName'] = build_result_name
    __args__['buildServiceName'] = build_service_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appplatform/v20231201:getBuildServiceBuildResultLog', __args__, opts=opts, typ=GetBuildServiceBuildResultLogResult).value

    return AwaitableGetBuildServiceBuildResultLogResult(
        blob_url=pulumi.get(__ret__, 'blob_url'))


@_utilities.lift_output_func(get_build_service_build_result_log)
def get_build_service_build_result_log_output(build_name: Optional[pulumi.Input[str]] = None,
                                              build_result_name: Optional[pulumi.Input[str]] = None,
                                              build_service_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              service_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBuildServiceBuildResultLogResult]:
    """
    Get a KPack build result log download URL.


    :param str build_name: The name of the build resource.
    :param str build_result_name: The name of the build result resource.
    :param str build_service_name: The name of the build service resource.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    ...
