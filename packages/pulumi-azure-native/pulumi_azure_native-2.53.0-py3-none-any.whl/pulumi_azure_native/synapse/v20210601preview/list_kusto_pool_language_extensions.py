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
    'ListKustoPoolLanguageExtensionsResult',
    'AwaitableListKustoPoolLanguageExtensionsResult',
    'list_kusto_pool_language_extensions',
    'list_kusto_pool_language_extensions_output',
]

@pulumi.output_type
class ListKustoPoolLanguageExtensionsResult:
    """
    The list of language extension objects.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.LanguageExtensionResponse']]:
        """
        The list of language extensions.
        """
        return pulumi.get(self, "value")


class AwaitableListKustoPoolLanguageExtensionsResult(ListKustoPoolLanguageExtensionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListKustoPoolLanguageExtensionsResult(
            value=self.value)


def list_kusto_pool_language_extensions(kusto_pool_name: Optional[str] = None,
                                        resource_group_name: Optional[str] = None,
                                        workspace_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListKustoPoolLanguageExtensionsResult:
    """
    Returns a list of language extensions that can run within KQL queries.


    :param str kusto_pool_name: The name of the Kusto pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['kustoPoolName'] = kusto_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:synapse/v20210601preview:listKustoPoolLanguageExtensions', __args__, opts=opts, typ=ListKustoPoolLanguageExtensionsResult).value

    return AwaitableListKustoPoolLanguageExtensionsResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_kusto_pool_language_extensions)
def list_kusto_pool_language_extensions_output(kusto_pool_name: Optional[pulumi.Input[str]] = None,
                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                               workspace_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListKustoPoolLanguageExtensionsResult]:
    """
    Returns a list of language extensions that can run within KQL queries.


    :param str kusto_pool_name: The name of the Kusto pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
