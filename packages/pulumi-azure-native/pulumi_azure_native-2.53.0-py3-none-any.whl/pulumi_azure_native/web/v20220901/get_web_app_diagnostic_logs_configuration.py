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
    'GetWebAppDiagnosticLogsConfigurationResult',
    'AwaitableGetWebAppDiagnosticLogsConfigurationResult',
    'get_web_app_diagnostic_logs_configuration',
    'get_web_app_diagnostic_logs_configuration_output',
]

@pulumi.output_type
class GetWebAppDiagnosticLogsConfigurationResult:
    """
    Configuration of App Service site logs.
    """
    def __init__(__self__, application_logs=None, detailed_error_messages=None, failed_requests_tracing=None, http_logs=None, id=None, kind=None, name=None, type=None):
        if application_logs and not isinstance(application_logs, dict):
            raise TypeError("Expected argument 'application_logs' to be a dict")
        pulumi.set(__self__, "application_logs", application_logs)
        if detailed_error_messages and not isinstance(detailed_error_messages, dict):
            raise TypeError("Expected argument 'detailed_error_messages' to be a dict")
        pulumi.set(__self__, "detailed_error_messages", detailed_error_messages)
        if failed_requests_tracing and not isinstance(failed_requests_tracing, dict):
            raise TypeError("Expected argument 'failed_requests_tracing' to be a dict")
        pulumi.set(__self__, "failed_requests_tracing", failed_requests_tracing)
        if http_logs and not isinstance(http_logs, dict):
            raise TypeError("Expected argument 'http_logs' to be a dict")
        pulumi.set(__self__, "http_logs", http_logs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="applicationLogs")
    def application_logs(self) -> Optional['outputs.ApplicationLogsConfigResponse']:
        """
        Application logs configuration.
        """
        return pulumi.get(self, "application_logs")

    @property
    @pulumi.getter(name="detailedErrorMessages")
    def detailed_error_messages(self) -> Optional['outputs.EnabledConfigResponse']:
        """
        Detailed error messages configuration.
        """
        return pulumi.get(self, "detailed_error_messages")

    @property
    @pulumi.getter(name="failedRequestsTracing")
    def failed_requests_tracing(self) -> Optional['outputs.EnabledConfigResponse']:
        """
        Failed requests tracing configuration.
        """
        return pulumi.get(self, "failed_requests_tracing")

    @property
    @pulumi.getter(name="httpLogs")
    def http_logs(self) -> Optional['outputs.HttpLogsConfigResponse']:
        """
        HTTP logs configuration.
        """
        return pulumi.get(self, "http_logs")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetWebAppDiagnosticLogsConfigurationResult(GetWebAppDiagnosticLogsConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAppDiagnosticLogsConfigurationResult(
            application_logs=self.application_logs,
            detailed_error_messages=self.detailed_error_messages,
            failed_requests_tracing=self.failed_requests_tracing,
            http_logs=self.http_logs,
            id=self.id,
            kind=self.kind,
            name=self.name,
            type=self.type)


def get_web_app_diagnostic_logs_configuration(name: Optional[str] = None,
                                              resource_group_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAppDiagnosticLogsConfigurationResult:
    """
    Description for Gets the logging configuration of an app.


    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20220901:getWebAppDiagnosticLogsConfiguration', __args__, opts=opts, typ=GetWebAppDiagnosticLogsConfigurationResult).value

    return AwaitableGetWebAppDiagnosticLogsConfigurationResult(
        application_logs=pulumi.get(__ret__, 'application_logs'),
        detailed_error_messages=pulumi.get(__ret__, 'detailed_error_messages'),
        failed_requests_tracing=pulumi.get(__ret__, 'failed_requests_tracing'),
        http_logs=pulumi.get(__ret__, 'http_logs'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_web_app_diagnostic_logs_configuration)
def get_web_app_diagnostic_logs_configuration_output(name: Optional[pulumi.Input[str]] = None,
                                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAppDiagnosticLogsConfigurationResult]:
    """
    Description for Gets the logging configuration of an app.


    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
