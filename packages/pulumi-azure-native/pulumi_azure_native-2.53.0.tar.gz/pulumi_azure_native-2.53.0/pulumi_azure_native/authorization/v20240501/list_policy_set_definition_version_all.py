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
    'ListPolicySetDefinitionVersionAllResult',
    'AwaitableListPolicySetDefinitionVersionAllResult',
    'list_policy_set_definition_version_all',
    'list_policy_set_definition_version_all_output',
]

@pulumi.output_type
class ListPolicySetDefinitionVersionAllResult:
    """
    List of policy set definition versions.
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
        The URL to use for getting the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.PolicySetDefinitionVersionResponse']]:
        """
        An array of policy set definition versions.
        """
        return pulumi.get(self, "value")


class AwaitableListPolicySetDefinitionVersionAllResult(ListPolicySetDefinitionVersionAllResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListPolicySetDefinitionVersionAllResult(
            next_link=self.next_link,
            value=self.value)


def list_policy_set_definition_version_all(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListPolicySetDefinitionVersionAllResult:
    """
    This operation lists all the policy set definition versions for all policy set definitions within a subscription.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization/v20240501:listPolicySetDefinitionVersionAll', __args__, opts=opts, typ=ListPolicySetDefinitionVersionAllResult).value

    return AwaitableListPolicySetDefinitionVersionAllResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_policy_set_definition_version_all)
def list_policy_set_definition_version_all_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListPolicySetDefinitionVersionAllResult]:
    """
    This operation lists all the policy set definition versions for all policy set definitions within a subscription.
    """
    ...
