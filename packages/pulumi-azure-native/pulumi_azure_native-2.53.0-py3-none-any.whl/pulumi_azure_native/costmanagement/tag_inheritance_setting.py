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
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['TagInheritanceSettingArgs', 'TagInheritanceSetting']

@pulumi.input_type
class TagInheritanceSettingArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 scope: pulumi.Input[str],
                 e_tag: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['TagInheritancePropertiesArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TagInheritanceSetting resource.
        :param pulumi.Input[str] kind: Specifies the kind of settings.
               Expected value is 'taginheritance'.
        :param pulumi.Input[str] scope: The scope associated with this setting. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billing profile scope.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input['TagInheritancePropertiesArgs'] properties: The properties of the tag inheritance setting.
        :param pulumi.Input[str] type: Setting type.
        """
        pulumi.set(__self__, "kind", 'taginheritance')
        pulumi.set(__self__, "scope", scope)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Specifies the kind of settings.
        Expected value is 'taginheritance'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope associated with this setting. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billing profile scope.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['TagInheritancePropertiesArgs']]:
        """
        The properties of the tag inheritance setting.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['TagInheritancePropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Setting type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class TagInheritanceSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['TagInheritancePropertiesArgs', 'TagInheritancePropertiesArgsDict']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Tag Inheritance Setting definition.
        Azure REST API version: 2022-10-05-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input[str] kind: Specifies the kind of settings.
               Expected value is 'taginheritance'.
        :param pulumi.Input[Union['TagInheritancePropertiesArgs', 'TagInheritancePropertiesArgsDict']] properties: The properties of the tag inheritance setting.
        :param pulumi.Input[str] scope: The scope associated with this setting. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billing profile scope.
        :param pulumi.Input[str] type: Setting type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagInheritanceSettingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Tag Inheritance Setting definition.
        Azure REST API version: 2022-10-05-preview.

        :param str resource_name: The name of the resource.
        :param TagInheritanceSettingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagInheritanceSettingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['TagInheritancePropertiesArgs', 'TagInheritancePropertiesArgsDict']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagInheritanceSettingArgs.__new__(TagInheritanceSettingArgs)

            __props__.__dict__["e_tag"] = e_tag
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'taginheritance'
            __props__.__dict__["properties"] = properties
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["type"] = type
            __props__.__dict__["name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:costmanagement/v20221001preview:TagInheritanceSetting"), pulumi.Alias(type_="azure-native:costmanagement/v20221005preview:TagInheritanceSetting"), pulumi.Alias(type_="azure-native:costmanagement/v20230801:TagInheritanceSetting"), pulumi.Alias(type_="azure-native:costmanagement/v20230901:TagInheritanceSetting"), pulumi.Alias(type_="azure-native:costmanagement/v20231101:TagInheritanceSetting")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(TagInheritanceSetting, __self__).__init__(
            'azure-native:costmanagement:TagInheritanceSetting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TagInheritanceSetting':
        """
        Get an existing TagInheritanceSetting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TagInheritanceSettingArgs.__new__(TagInheritanceSettingArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return TagInheritanceSetting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Specifies the kind of settings.
        Expected value is 'taginheritance'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.TagInheritancePropertiesResponse']:
        """
        The properties of the tag inheritance setting.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

