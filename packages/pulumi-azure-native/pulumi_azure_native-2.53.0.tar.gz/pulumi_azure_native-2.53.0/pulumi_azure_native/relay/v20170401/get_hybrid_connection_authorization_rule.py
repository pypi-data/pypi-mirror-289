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
    'GetHybridConnectionAuthorizationRuleResult',
    'AwaitableGetHybridConnectionAuthorizationRuleResult',
    'get_hybrid_connection_authorization_rule',
    'get_hybrid_connection_authorization_rule_output',
]

@pulumi.output_type
class GetHybridConnectionAuthorizationRuleResult:
    """
    Description of a namespace authorization rule.
    """
    def __init__(__self__, id=None, name=None, rights=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rights and not isinstance(rights, list):
            raise TypeError("Expected argument 'rights' to be a list")
        pulumi.set(__self__, "rights", rights)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rights(self) -> Sequence[str]:
        """
        The rights associated with the rule.
        """
        return pulumi.get(self, "rights")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetHybridConnectionAuthorizationRuleResult(GetHybridConnectionAuthorizationRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHybridConnectionAuthorizationRuleResult(
            id=self.id,
            name=self.name,
            rights=self.rights,
            type=self.type)


def get_hybrid_connection_authorization_rule(authorization_rule_name: Optional[str] = None,
                                             hybrid_connection_name: Optional[str] = None,
                                             namespace_name: Optional[str] = None,
                                             resource_group_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHybridConnectionAuthorizationRuleResult:
    """
    Hybrid connection authorization rule for a hybrid connection by name.


    :param str authorization_rule_name: The authorization rule name.
    :param str hybrid_connection_name: The hybrid connection name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['authorizationRuleName'] = authorization_rule_name
    __args__['hybridConnectionName'] = hybrid_connection_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:relay/v20170401:getHybridConnectionAuthorizationRule', __args__, opts=opts, typ=GetHybridConnectionAuthorizationRuleResult).value

    return AwaitableGetHybridConnectionAuthorizationRuleResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        rights=pulumi.get(__ret__, 'rights'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_hybrid_connection_authorization_rule)
def get_hybrid_connection_authorization_rule_output(authorization_rule_name: Optional[pulumi.Input[str]] = None,
                                                    hybrid_connection_name: Optional[pulumi.Input[str]] = None,
                                                    namespace_name: Optional[pulumi.Input[str]] = None,
                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHybridConnectionAuthorizationRuleResult]:
    """
    Hybrid connection authorization rule for a hybrid connection by name.


    :param str authorization_rule_name: The authorization rule name.
    :param str hybrid_connection_name: The hybrid connection name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
