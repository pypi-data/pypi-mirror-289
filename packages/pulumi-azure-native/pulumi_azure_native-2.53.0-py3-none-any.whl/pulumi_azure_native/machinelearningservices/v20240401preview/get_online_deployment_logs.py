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
from ._enums import *

__all__ = [
    'GetOnlineDeploymentLogsResult',
    'AwaitableGetOnlineDeploymentLogsResult',
    'get_online_deployment_logs',
    'get_online_deployment_logs_output',
]

@pulumi.output_type
class GetOnlineDeploymentLogsResult:
    def __init__(__self__, content=None):
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        """
        The retrieved online deployment logs.
        """
        return pulumi.get(self, "content")


class AwaitableGetOnlineDeploymentLogsResult(GetOnlineDeploymentLogsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOnlineDeploymentLogsResult(
            content=self.content)


def get_online_deployment_logs(container_type: Optional[Union[str, 'ContainerType']] = None,
                               deployment_name: Optional[str] = None,
                               endpoint_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               tail: Optional[int] = None,
                               workspace_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOnlineDeploymentLogsResult:
    """
    Use this data source to access information about an existing resource.

    :param Union[str, 'ContainerType'] container_type: The type of container to retrieve logs from.
    :param str deployment_name: The name and identifier for the endpoint.
    :param str endpoint_name: Inference endpoint name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param int tail: The maximum number of lines to tail.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['containerType'] = container_type
    __args__['deploymentName'] = deployment_name
    __args__['endpointName'] = endpoint_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['tail'] = tail
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20240401preview:getOnlineDeploymentLogs', __args__, opts=opts, typ=GetOnlineDeploymentLogsResult).value

    return AwaitableGetOnlineDeploymentLogsResult(
        content=pulumi.get(__ret__, 'content'))


@_utilities.lift_output_func(get_online_deployment_logs)
def get_online_deployment_logs_output(container_type: Optional[pulumi.Input[Optional[Union[str, 'ContainerType']]]] = None,
                                      deployment_name: Optional[pulumi.Input[str]] = None,
                                      endpoint_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      tail: Optional[pulumi.Input[Optional[int]]] = None,
                                      workspace_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOnlineDeploymentLogsResult]:
    """
    Use this data source to access information about an existing resource.

    :param Union[str, 'ContainerType'] container_type: The type of container to retrieve logs from.
    :param str deployment_name: The name and identifier for the endpoint.
    :param str endpoint_name: Inference endpoint name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param int tail: The maximum number of lines to tail.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
