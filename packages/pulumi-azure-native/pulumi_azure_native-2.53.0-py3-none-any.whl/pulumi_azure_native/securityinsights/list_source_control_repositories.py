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
    'ListSourceControlRepositoriesResult',
    'AwaitableListSourceControlRepositoriesResult',
    'list_source_control_repositories',
    'list_source_control_repositories_output',
]

@pulumi.output_type
class ListSourceControlRepositoriesResult:
    """
    List all the source controls.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        URL to fetch the next set of repositories.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.RepoResponse']:
        """
        Array of repositories.
        """
        return pulumi.get(self, "value")


class AwaitableListSourceControlRepositoriesResult(ListSourceControlRepositoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSourceControlRepositoriesResult(
            next_link=self.next_link,
            value=self.value)


def list_source_control_repositories(resource_group_name: Optional[str] = None,
                                     workspace_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSourceControlRepositoriesResult:
    """
    Gets a list of repositories metadata.
    Azure REST API version: 2023-06-01-preview.

    Other available API versions: 2021-03-01-preview, 2021-09-01-preview, 2021-10-01-preview, 2022-01-01-preview, 2022-04-01-preview, 2022-05-01-preview, 2022-06-01-preview, 2022-07-01-preview, 2022-08-01-preview, 2022-09-01-preview, 2022-10-01-preview, 2022-11-01-preview, 2022-12-01-preview, 2023-02-01-preview, 2023-03-01-preview, 2023-04-01-preview, 2023-05-01-preview, 2023-07-01-preview, 2023-08-01-preview, 2023-09-01-preview, 2023-10-01-preview, 2023-11-01, 2023-12-01-preview, 2024-01-01-preview, 2024-03-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights:listSourceControlRepositories', __args__, opts=opts, typ=ListSourceControlRepositoriesResult).value

    return AwaitableListSourceControlRepositoriesResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_source_control_repositories)
def list_source_control_repositories_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                            workspace_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListSourceControlRepositoriesResult]:
    """
    Gets a list of repositories metadata.
    Azure REST API version: 2023-06-01-preview.

    Other available API versions: 2021-03-01-preview, 2021-09-01-preview, 2021-10-01-preview, 2022-01-01-preview, 2022-04-01-preview, 2022-05-01-preview, 2022-06-01-preview, 2022-07-01-preview, 2022-08-01-preview, 2022-09-01-preview, 2022-10-01-preview, 2022-11-01-preview, 2022-12-01-preview, 2023-02-01-preview, 2023-03-01-preview, 2023-04-01-preview, 2023-05-01-preview, 2023-07-01-preview, 2023-08-01-preview, 2023-09-01-preview, 2023-10-01-preview, 2023-11-01, 2023-12-01-preview, 2024-01-01-preview, 2024-03-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
