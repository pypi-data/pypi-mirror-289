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
from ._enums import *

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


def list_source_control_repositories(client_id: Optional[str] = None,
                                     code: Optional[str] = None,
                                     installation_id: Optional[str] = None,
                                     kind: Optional[Union[str, 'RepositoryAccessKind']] = None,
                                     resource_group_name: Optional[str] = None,
                                     state: Optional[str] = None,
                                     token: Optional[str] = None,
                                     workspace_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSourceControlRepositoriesResult:
    """
    Gets a list of repositories metadata.


    :param str client_id: OAuth ClientId. Required when `kind` is `OAuth`
    :param str code: OAuth Code. Required when `kind` is `OAuth`
    :param str installation_id: Application installation ID. Required when `kind` is `App`. Supported by `GitHub` only.
    :param Union[str, 'RepositoryAccessKind'] kind: The kind of repository access credentials
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str state: OAuth State. Required when `kind` is `OAuth`
    :param str token: Personal Access Token. Required when `kind` is `PAT`
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['clientId'] = client_id
    __args__['code'] = code
    __args__['installationId'] = installation_id
    __args__['kind'] = kind
    __args__['resourceGroupName'] = resource_group_name
    __args__['state'] = state
    __args__['token'] = token
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20231001preview:listSourceControlRepositories', __args__, opts=opts, typ=ListSourceControlRepositoriesResult).value

    return AwaitableListSourceControlRepositoriesResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_source_control_repositories)
def list_source_control_repositories_output(client_id: Optional[pulumi.Input[Optional[str]]] = None,
                                            code: Optional[pulumi.Input[Optional[str]]] = None,
                                            installation_id: Optional[pulumi.Input[Optional[str]]] = None,
                                            kind: Optional[pulumi.Input[Union[str, 'RepositoryAccessKind']]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            state: Optional[pulumi.Input[Optional[str]]] = None,
                                            token: Optional[pulumi.Input[Optional[str]]] = None,
                                            workspace_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListSourceControlRepositoriesResult]:
    """
    Gets a list of repositories metadata.


    :param str client_id: OAuth ClientId. Required when `kind` is `OAuth`
    :param str code: OAuth Code. Required when `kind` is `OAuth`
    :param str installation_id: Application installation ID. Required when `kind` is `App`. Supported by `GitHub` only.
    :param Union[str, 'RepositoryAccessKind'] kind: The kind of repository access credentials
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str state: OAuth State. Required when `kind` is `OAuth`
    :param str token: Personal Access Token. Required when `kind` is `PAT`
    :param str workspace_name: The name of the workspace.
    """
    ...
