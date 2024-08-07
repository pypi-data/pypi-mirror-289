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
    'ListListTenantConfigurationViolationResult',
    'AwaitableListListTenantConfigurationViolationResult',
    'list_list_tenant_configuration_violation',
    'list_list_tenant_configuration_violation_output',
]

@pulumi.output_type
class ListListTenantConfigurationViolationResult:
    """
    List of list of items that violate tenant's configuration.
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
    def value(self) -> Optional[Sequence['outputs.ViolationResponse']]:
        """
        The array of violations.
        """
        return pulumi.get(self, "value")


class AwaitableListListTenantConfigurationViolationResult(ListListTenantConfigurationViolationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListListTenantConfigurationViolationResult(
            next_link=self.next_link,
            value=self.value)


def list_list_tenant_configuration_violation(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListListTenantConfigurationViolationResult:
    """
    Gets list of items that violate tenant's configuration.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:portal/v20200901preview:listListTenantConfigurationViolation', __args__, opts=opts, typ=ListListTenantConfigurationViolationResult).value

    return AwaitableListListTenantConfigurationViolationResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_list_tenant_configuration_violation)
def list_list_tenant_configuration_violation_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListListTenantConfigurationViolationResult]:
    """
    Gets list of items that violate tenant's configuration.
    """
    ...
