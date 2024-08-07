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
    'GetLocalRulestackChangeLogResult',
    'AwaitableGetLocalRulestackChangeLogResult',
    'get_local_rulestack_change_log',
    'get_local_rulestack_change_log_output',
]

@pulumi.output_type
class GetLocalRulestackChangeLogResult:
    """
    Changelog list
    """
    def __init__(__self__, changes=None, last_committed=None, last_modified=None):
        if changes and not isinstance(changes, list):
            raise TypeError("Expected argument 'changes' to be a list")
        pulumi.set(__self__, "changes", changes)
        if last_committed and not isinstance(last_committed, str):
            raise TypeError("Expected argument 'last_committed' to be a str")
        pulumi.set(__self__, "last_committed", last_committed)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)

    @property
    @pulumi.getter
    def changes(self) -> Sequence[str]:
        """
        list of changes
        """
        return pulumi.get(self, "changes")

    @property
    @pulumi.getter(name="lastCommitted")
    def last_committed(self) -> Optional[str]:
        """
        lastCommitted timestamp
        """
        return pulumi.get(self, "last_committed")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[str]:
        """
        lastModified timestamp
        """
        return pulumi.get(self, "last_modified")


class AwaitableGetLocalRulestackChangeLogResult(GetLocalRulestackChangeLogResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalRulestackChangeLogResult(
            changes=self.changes,
            last_committed=self.last_committed,
            last_modified=self.last_modified)


def get_local_rulestack_change_log(local_rulestack_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalRulestackChangeLogResult:
    """
    Get changelog


    :param str local_rulestack_name: LocalRulestack resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['localRulestackName'] = local_rulestack_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20240207preview:getLocalRulestackChangeLog', __args__, opts=opts, typ=GetLocalRulestackChangeLogResult).value

    return AwaitableGetLocalRulestackChangeLogResult(
        changes=pulumi.get(__ret__, 'changes'),
        last_committed=pulumi.get(__ret__, 'last_committed'),
        last_modified=pulumi.get(__ret__, 'last_modified'))


@_utilities.lift_output_func(get_local_rulestack_change_log)
def get_local_rulestack_change_log_output(local_rulestack_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocalRulestackChangeLogResult]:
    """
    Get changelog


    :param str local_rulestack_name: LocalRulestack resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
