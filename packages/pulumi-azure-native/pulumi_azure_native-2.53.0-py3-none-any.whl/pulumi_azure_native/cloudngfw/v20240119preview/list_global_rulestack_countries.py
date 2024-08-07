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
    'ListGlobalRulestackCountriesResult',
    'AwaitableListGlobalRulestackCountriesResult',
    'list_global_rulestack_countries',
    'list_global_rulestack_countries_output',
]

@pulumi.output_type
class ListGlobalRulestackCountriesResult:
    """
    Countries Response Object
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
        next link
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.CountryResponse']:
        """
        List of countries
        """
        return pulumi.get(self, "value")


class AwaitableListGlobalRulestackCountriesResult(ListGlobalRulestackCountriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListGlobalRulestackCountriesResult(
            next_link=self.next_link,
            value=self.value)


def list_global_rulestack_countries(global_rulestack_name: Optional[str] = None,
                                    skip: Optional[str] = None,
                                    top: Optional[int] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListGlobalRulestackCountriesResult:
    """
    List of countries for Rulestack


    :param str global_rulestack_name: GlobalRulestack resource name
    """
    __args__ = dict()
    __args__['globalRulestackName'] = global_rulestack_name
    __args__['skip'] = skip
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20240119preview:listGlobalRulestackCountries', __args__, opts=opts, typ=ListGlobalRulestackCountriesResult).value

    return AwaitableListGlobalRulestackCountriesResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_global_rulestack_countries)
def list_global_rulestack_countries_output(global_rulestack_name: Optional[pulumi.Input[str]] = None,
                                           skip: Optional[pulumi.Input[Optional[str]]] = None,
                                           top: Optional[pulumi.Input[Optional[int]]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListGlobalRulestackCountriesResult]:
    """
    List of countries for Rulestack


    :param str global_rulestack_name: GlobalRulestack resource name
    """
    ...
