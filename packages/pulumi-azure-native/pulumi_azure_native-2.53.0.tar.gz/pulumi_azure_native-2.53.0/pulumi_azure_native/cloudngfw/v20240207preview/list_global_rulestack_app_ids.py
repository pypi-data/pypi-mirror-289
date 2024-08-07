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
    'ListGlobalRulestackAppIdsResult',
    'AwaitableListGlobalRulestackAppIdsResult',
    'list_global_rulestack_app_ids',
    'list_global_rulestack_app_ids_output',
]

@pulumi.output_type
class ListGlobalRulestackAppIdsResult:
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
        next Link
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence[str]:
        """
        List of AppIds
        """
        return pulumi.get(self, "value")


class AwaitableListGlobalRulestackAppIdsResult(ListGlobalRulestackAppIdsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListGlobalRulestackAppIdsResult(
            next_link=self.next_link,
            value=self.value)


def list_global_rulestack_app_ids(app_id_version: Optional[str] = None,
                                  app_prefix: Optional[str] = None,
                                  global_rulestack_name: Optional[str] = None,
                                  skip: Optional[str] = None,
                                  top: Optional[int] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListGlobalRulestackAppIdsResult:
    """
    List of AppIds for GlobalRulestack ApiVersion


    :param str global_rulestack_name: GlobalRulestack resource name
    """
    __args__ = dict()
    __args__['appIdVersion'] = app_id_version
    __args__['appPrefix'] = app_prefix
    __args__['globalRulestackName'] = global_rulestack_name
    __args__['skip'] = skip
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20240207preview:listGlobalRulestackAppIds', __args__, opts=opts, typ=ListGlobalRulestackAppIdsResult).value

    return AwaitableListGlobalRulestackAppIdsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_global_rulestack_app_ids)
def list_global_rulestack_app_ids_output(app_id_version: Optional[pulumi.Input[Optional[str]]] = None,
                                         app_prefix: Optional[pulumi.Input[Optional[str]]] = None,
                                         global_rulestack_name: Optional[pulumi.Input[str]] = None,
                                         skip: Optional[pulumi.Input[Optional[str]]] = None,
                                         top: Optional[pulumi.Input[Optional[int]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListGlobalRulestackAppIdsResult]:
    """
    List of AppIds for GlobalRulestack ApiVersion


    :param str global_rulestack_name: GlobalRulestack resource name
    """
    ...
