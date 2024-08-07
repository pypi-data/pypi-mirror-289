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
    'ListWorkspaceStorageAccountKeysResult',
    'AwaitableListWorkspaceStorageAccountKeysResult',
    'list_workspace_storage_account_keys',
    'list_workspace_storage_account_keys_output',
]

@pulumi.output_type
class ListWorkspaceStorageAccountKeysResult:
    def __init__(__self__, user_storage_key=None):
        if user_storage_key and not isinstance(user_storage_key, str):
            raise TypeError("Expected argument 'user_storage_key' to be a str")
        pulumi.set(__self__, "user_storage_key", user_storage_key)

    @property
    @pulumi.getter(name="userStorageKey")
    def user_storage_key(self) -> str:
        return pulumi.get(self, "user_storage_key")


class AwaitableListWorkspaceStorageAccountKeysResult(ListWorkspaceStorageAccountKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWorkspaceStorageAccountKeysResult(
            user_storage_key=self.user_storage_key)


def list_workspace_storage_account_keys(resource_group_name: Optional[str] = None,
                                        workspace_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWorkspaceStorageAccountKeysResult:
    """
    List storage account keys of a workspace.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20220101preview:listWorkspaceStorageAccountKeys', __args__, opts=opts, typ=ListWorkspaceStorageAccountKeysResult).value

    return AwaitableListWorkspaceStorageAccountKeysResult(
        user_storage_key=pulumi.get(__ret__, 'user_storage_key'))


@_utilities.lift_output_func(list_workspace_storage_account_keys)
def list_workspace_storage_account_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                               workspace_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWorkspaceStorageAccountKeysResult]:
    """
    List storage account keys of a workspace.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
