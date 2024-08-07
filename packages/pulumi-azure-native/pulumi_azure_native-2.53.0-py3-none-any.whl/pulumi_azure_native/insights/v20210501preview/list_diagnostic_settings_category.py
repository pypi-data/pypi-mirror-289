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
    'ListDiagnosticSettingsCategoryResult',
    'AwaitableListDiagnosticSettingsCategoryResult',
    'list_diagnostic_settings_category',
    'list_diagnostic_settings_category_output',
]

@pulumi.output_type
class ListDiagnosticSettingsCategoryResult:
    """
    Represents a collection of diagnostic setting category resources.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.DiagnosticSettingsCategoryResourceResponse']]:
        """
        The collection of diagnostic settings category resources.
        """
        return pulumi.get(self, "value")


class AwaitableListDiagnosticSettingsCategoryResult(ListDiagnosticSettingsCategoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDiagnosticSettingsCategoryResult(
            value=self.value)


def list_diagnostic_settings_category(resource_uri: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDiagnosticSettingsCategoryResult:
    """
    Lists the diagnostic settings categories for the specified resource.


    :param str resource_uri: The identifier of the resource.
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20210501preview:listDiagnosticSettingsCategory', __args__, opts=opts, typ=ListDiagnosticSettingsCategoryResult).value

    return AwaitableListDiagnosticSettingsCategoryResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_diagnostic_settings_category)
def list_diagnostic_settings_category_output(resource_uri: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDiagnosticSettingsCategoryResult]:
    """
    Lists the diagnostic settings categories for the specified resource.


    :param str resource_uri: The identifier of the resource.
    """
    ...
