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
    'ListServerlessEndpointKeysResult',
    'AwaitableListServerlessEndpointKeysResult',
    'list_serverless_endpoint_keys',
    'list_serverless_endpoint_keys_output',
]

@pulumi.output_type
class ListServerlessEndpointKeysResult:
    """
    Keys for endpoint authentication.
    """
    def __init__(__self__, primary_key=None, secondary_key=None):
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[str]:
        """
        The primary key.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[str]:
        """
        The secondary key.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListServerlessEndpointKeysResult(ListServerlessEndpointKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListServerlessEndpointKeysResult(
            primary_key=self.primary_key,
            secondary_key=self.secondary_key)


def list_serverless_endpoint_keys(name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  workspace_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListServerlessEndpointKeysResult:
    """
    Keys for endpoint authentication.
    Azure REST API version: 2023-08-01-preview.

    Other available API versions: 2024-01-01-preview, 2024-04-01, 2024-04-01-preview, 2024-07-01-preview.


    :param str name: Serverless Endpoint name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices:listServerlessEndpointKeys', __args__, opts=opts, typ=ListServerlessEndpointKeysResult).value

    return AwaitableListServerlessEndpointKeysResult(
        primary_key=pulumi.get(__ret__, 'primary_key'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))


@_utilities.lift_output_func(list_serverless_endpoint_keys)
def list_serverless_endpoint_keys_output(name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         workspace_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListServerlessEndpointKeysResult]:
    """
    Keys for endpoint authentication.
    Azure REST API version: 2023-08-01-preview.

    Other available API versions: 2024-01-01-preview, 2024-04-01, 2024-04-01-preview, 2024-07-01-preview.


    :param str name: Serverless Endpoint name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
