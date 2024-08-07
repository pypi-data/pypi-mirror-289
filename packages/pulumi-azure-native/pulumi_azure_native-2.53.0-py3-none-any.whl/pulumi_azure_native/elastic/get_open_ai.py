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
    'GetOpenAIResult',
    'AwaitableGetOpenAIResult',
    'get_open_ai',
    'get_open_ai_output',
]

@pulumi.output_type
class GetOpenAIResult:
    """
    Capture properties of Open AI resource Integration.
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the integration.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the integration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.OpenAIIntegrationPropertiesResponse':
        """
        Open AI Integration details.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the integration.
        """
        return pulumi.get(self, "type")


class AwaitableGetOpenAIResult(GetOpenAIResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOpenAIResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_open_ai(integration_name: Optional[str] = None,
                monitor_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOpenAIResult:
    """
    Capture properties of Open AI resource Integration.
    Azure REST API version: 2024-03-01.

    Other available API versions: 2024-01-01-preview, 2024-05-01-preview, 2024-06-15-preview.


    :param str integration_name: OpenAI Integration name
    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['integrationName'] = integration_name
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic:getOpenAI', __args__, opts=opts, typ=GetOpenAIResult).value

    return AwaitableGetOpenAIResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_open_ai)
def get_open_ai_output(integration_name: Optional[pulumi.Input[str]] = None,
                       monitor_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOpenAIResult]:
    """
    Capture properties of Open AI resource Integration.
    Azure REST API version: 2024-03-01.

    Other available API versions: 2024-01-01-preview, 2024-05-01-preview, 2024-06-15-preview.


    :param str integration_name: OpenAI Integration name
    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
