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
    'ListGlobalRulestackSecurityServicesResult',
    'AwaitableListGlobalRulestackSecurityServicesResult',
    'list_global_rulestack_security_services',
    'list_global_rulestack_security_services_output',
]

@pulumi.output_type
class ListGlobalRulestackSecurityServicesResult:
    """
    Security services list response
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, dict):
            raise TypeError("Expected argument 'value' to be a dict")
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
    def value(self) -> 'outputs.SecurityServicesTypeListResponse':
        """
        response value
        """
        return pulumi.get(self, "value")


class AwaitableListGlobalRulestackSecurityServicesResult(ListGlobalRulestackSecurityServicesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListGlobalRulestackSecurityServicesResult(
            next_link=self.next_link,
            value=self.value)


def list_global_rulestack_security_services(global_rulestack_name: Optional[str] = None,
                                            skip: Optional[str] = None,
                                            top: Optional[int] = None,
                                            type: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListGlobalRulestackSecurityServicesResult:
    """
    List the security services for rulestack


    :param str global_rulestack_name: GlobalRulestack resource name
    """
    __args__ = dict()
    __args__['globalRulestackName'] = global_rulestack_name
    __args__['skip'] = skip
    __args__['top'] = top
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20231010preview:listGlobalRulestackSecurityServices', __args__, opts=opts, typ=ListGlobalRulestackSecurityServicesResult).value

    return AwaitableListGlobalRulestackSecurityServicesResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_global_rulestack_security_services)
def list_global_rulestack_security_services_output(global_rulestack_name: Optional[pulumi.Input[str]] = None,
                                                   skip: Optional[pulumi.Input[Optional[str]]] = None,
                                                   top: Optional[pulumi.Input[Optional[int]]] = None,
                                                   type: Optional[pulumi.Input[str]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListGlobalRulestackSecurityServicesResult]:
    """
    List the security services for rulestack


    :param str global_rulestack_name: GlobalRulestack resource name
    """
    ...
