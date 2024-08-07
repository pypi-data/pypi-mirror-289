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
    'ListConfigurationStoreKeysResult',
    'AwaitableListConfigurationStoreKeysResult',
    'list_configuration_store_keys',
    'list_configuration_store_keys_output',
]

@pulumi.output_type
class ListConfigurationStoreKeysResult:
    """
    The result of a request to list API keys.
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
    def next_link(self) -> Optional[str]:
        """
        The URI that can be used to request the next set of paged results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.ApiKeyResponse']]:
        """
        The collection value.
        """
        return pulumi.get(self, "value")


class AwaitableListConfigurationStoreKeysResult(ListConfigurationStoreKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListConfigurationStoreKeysResult(
            next_link=self.next_link,
            value=self.value)


def list_configuration_store_keys(config_store_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  skip_token: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListConfigurationStoreKeysResult:
    """
    Lists the access key for the specified configuration store.


    :param str config_store_name: The name of the configuration store.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    :param str skip_token: A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    """
    __args__ = dict()
    __args__['configStoreName'] = config_store_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['skipToken'] = skip_token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appconfiguration/v20230801preview:listConfigurationStoreKeys', __args__, opts=opts, typ=ListConfigurationStoreKeysResult).value

    return AwaitableListConfigurationStoreKeysResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_configuration_store_keys)
def list_configuration_store_keys_output(config_store_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         skip_token: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListConfigurationStoreKeysResult]:
    """
    Lists the access key for the specified configuration store.


    :param str config_store_name: The name of the configuration store.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    :param str skip_token: A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    """
    ...
