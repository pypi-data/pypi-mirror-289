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
    'GetTagInheritanceSettingResult',
    'AwaitableGetTagInheritanceSettingResult',
    'get_tag_inheritance_setting',
    'get_tag_inheritance_setting_output',
]

@pulumi.output_type
class GetTagInheritanceSettingResult:
    """
    Tag Inheritance Setting definition.
    """
    def __init__(__self__, id=None, kind=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Specifies the kind of settings.
        Expected value is 'taginheritance'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.TagInheritancePropertiesResponse':
        """
        The properties of the tag inheritance setting.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetTagInheritanceSettingResult(GetTagInheritanceSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagInheritanceSettingResult(
            id=self.id,
            kind=self.kind,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_tag_inheritance_setting(scope: Optional[str] = None,
                                type: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagInheritanceSettingResult:
    """
    Get the setting from the given scope by name.


    :param str scope: The scope associated with this setting. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billing profile scope.
    :param str type: Setting type.
    """
    __args__ = dict()
    __args__['scope'] = scope
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:costmanagement/v20230901:getTagInheritanceSetting', __args__, opts=opts, typ=GetTagInheritanceSettingResult).value

    return AwaitableGetTagInheritanceSettingResult(
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_tag_inheritance_setting)
def get_tag_inheritance_setting_output(scope: Optional[pulumi.Input[str]] = None,
                                       type: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagInheritanceSettingResult]:
    """
    Get the setting from the given scope by name.


    :param str scope: The scope associated with this setting. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billing profile scope.
    :param str type: Setting type.
    """
    ...
