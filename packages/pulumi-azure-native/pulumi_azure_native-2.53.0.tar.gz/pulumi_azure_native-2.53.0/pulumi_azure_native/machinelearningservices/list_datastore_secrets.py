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
    'ListDatastoreSecretsResult',
    'AwaitableListDatastoreSecretsResult',
    'list_datastore_secrets',
    'list_datastore_secrets_output',
]

@pulumi.output_type
class ListDatastoreSecretsResult:
    """
    Base definition for datastore secrets.
    """
    def __init__(__self__, secrets_type=None):
        if secrets_type and not isinstance(secrets_type, str):
            raise TypeError("Expected argument 'secrets_type' to be a str")
        pulumi.set(__self__, "secrets_type", secrets_type)

    @property
    @pulumi.getter(name="secretsType")
    def secrets_type(self) -> str:
        """
        [Required] Credential type used to authentication with storage.
        """
        return pulumi.get(self, "secrets_type")


class AwaitableListDatastoreSecretsResult(ListDatastoreSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDatastoreSecretsResult(
            secrets_type=self.secrets_type)


def list_datastore_secrets(name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           workspace_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDatastoreSecretsResult:
    """
    Base definition for datastore secrets.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-04-01-preview, 2023-06-01-preview, 2023-08-01-preview, 2023-10-01, 2024-01-01-preview, 2024-04-01, 2024-04-01-preview, 2024-07-01-preview.


    :param str name: Datastore name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices:listDatastoreSecrets', __args__, opts=opts, typ=ListDatastoreSecretsResult).value

    return AwaitableListDatastoreSecretsResult(
        secrets_type=pulumi.get(__ret__, 'secrets_type'))


@_utilities.lift_output_func(list_datastore_secrets)
def list_datastore_secrets_output(name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  workspace_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDatastoreSecretsResult]:
    """
    Base definition for datastore secrets.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-04-01-preview, 2023-06-01-preview, 2023-08-01-preview, 2023-10-01, 2024-01-01-preview, 2024-04-01, 2024-04-01-preview, 2024-07-01-preview.


    :param str name: Datastore name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
