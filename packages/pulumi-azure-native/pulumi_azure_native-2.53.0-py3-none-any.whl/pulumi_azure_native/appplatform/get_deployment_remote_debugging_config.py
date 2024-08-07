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

__all__ = [
    'GetDeploymentRemoteDebuggingConfigResult',
    'AwaitableGetDeploymentRemoteDebuggingConfigResult',
    'get_deployment_remote_debugging_config',
    'get_deployment_remote_debugging_config_output',
]

@pulumi.output_type
class GetDeploymentRemoteDebuggingConfigResult:
    """
    Remote debugging config.
    """
    def __init__(__self__, enabled=None, port=None):
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Indicate if remote debugging is enabled
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        Application debugging port
        """
        return pulumi.get(self, "port")


class AwaitableGetDeploymentRemoteDebuggingConfigResult(GetDeploymentRemoteDebuggingConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentRemoteDebuggingConfigResult(
            enabled=self.enabled,
            port=self.port)


def get_deployment_remote_debugging_config(app_name: Optional[str] = None,
                                           deployment_name: Optional[str] = None,
                                           resource_group_name: Optional[str] = None,
                                           service_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentRemoteDebuggingConfigResult:
    """
    Get remote debugging config.
    Azure REST API version: 2023-05-01-preview.

    Other available API versions: 2023-07-01-preview, 2023-09-01-preview, 2023-11-01-preview, 2023-12-01, 2024-01-01-preview, 2024-05-01-preview.


    :param str app_name: The name of the App resource.
    :param str deployment_name: The name of the Deployment resource.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    __args__ = dict()
    __args__['appName'] = app_name
    __args__['deploymentName'] = deployment_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appplatform:getDeploymentRemoteDebuggingConfig', __args__, opts=opts, typ=GetDeploymentRemoteDebuggingConfigResult).value

    return AwaitableGetDeploymentRemoteDebuggingConfigResult(
        enabled=pulumi.get(__ret__, 'enabled'),
        port=pulumi.get(__ret__, 'port'))


@_utilities.lift_output_func(get_deployment_remote_debugging_config)
def get_deployment_remote_debugging_config_output(app_name: Optional[pulumi.Input[str]] = None,
                                                  deployment_name: Optional[pulumi.Input[str]] = None,
                                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  service_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentRemoteDebuggingConfigResult]:
    """
    Get remote debugging config.
    Azure REST API version: 2023-05-01-preview.

    Other available API versions: 2023-07-01-preview, 2023-09-01-preview, 2023-11-01-preview, 2023-12-01, 2024-01-01-preview, 2024-05-01-preview.


    :param str app_name: The name of the App resource.
    :param str deployment_name: The name of the Deployment resource.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    ...
