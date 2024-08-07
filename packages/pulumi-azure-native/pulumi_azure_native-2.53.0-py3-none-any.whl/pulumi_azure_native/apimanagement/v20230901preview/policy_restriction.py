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
from ._enums import *

__all__ = ['PolicyRestrictionArgs', 'PolicyRestriction']

@pulumi.input_type
class PolicyRestrictionArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 policy_restriction_id: Optional[pulumi.Input[str]] = None,
                 require_base: Optional[pulumi.Input[Union[str, 'PolicyRestrictionRequireBase']]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PolicyRestriction resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] policy_restriction_id: Policy restrictions after an entity level
        :param pulumi.Input[Union[str, 'PolicyRestrictionRequireBase']] require_base: Indicates if base policy should be enforced for the policy document.
        :param pulumi.Input[str] scope: Path to the policy document.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if policy_restriction_id is not None:
            pulumi.set(__self__, "policy_restriction_id", policy_restriction_id)
        if require_base is None:
            require_base = 'false'
        if require_base is not None:
            pulumi.set(__self__, "require_base", require_base)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="policyRestrictionId")
    def policy_restriction_id(self) -> Optional[pulumi.Input[str]]:
        """
        Policy restrictions after an entity level
        """
        return pulumi.get(self, "policy_restriction_id")

    @policy_restriction_id.setter
    def policy_restriction_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_restriction_id", value)

    @property
    @pulumi.getter(name="requireBase")
    def require_base(self) -> Optional[pulumi.Input[Union[str, 'PolicyRestrictionRequireBase']]]:
        """
        Indicates if base policy should be enforced for the policy document.
        """
        return pulumi.get(self, "require_base")

    @require_base.setter
    def require_base(self, value: Optional[pulumi.Input[Union[str, 'PolicyRestrictionRequireBase']]]):
        pulumi.set(self, "require_base", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        Path to the policy document.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


class PolicyRestriction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_restriction_id: Optional[pulumi.Input[str]] = None,
                 require_base: Optional[pulumi.Input[Union[str, 'PolicyRestrictionRequireBase']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Policy restriction contract details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] policy_restriction_id: Policy restrictions after an entity level
        :param pulumi.Input[Union[str, 'PolicyRestrictionRequireBase']] require_base: Indicates if base policy should be enforced for the policy document.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] scope: Path to the policy document.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyRestrictionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Policy restriction contract details.

        :param str resource_name: The name of the resource.
        :param PolicyRestrictionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyRestrictionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_restriction_id: Optional[pulumi.Input[str]] = None,
                 require_base: Optional[pulumi.Input[Union[str, 'PolicyRestrictionRequireBase']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyRestrictionArgs.__new__(PolicyRestrictionArgs)

            __props__.__dict__["policy_restriction_id"] = policy_restriction_id
            if require_base is None:
                require_base = 'false'
            __props__.__dict__["require_base"] = require_base
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scope"] = scope
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:PolicyRestriction"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:PolicyRestriction")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PolicyRestriction, __self__).__init__(
            'azure-native:apimanagement/v20230901preview:PolicyRestriction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PolicyRestriction':
        """
        Get an existing PolicyRestriction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyRestrictionArgs.__new__(PolicyRestrictionArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["require_base"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["type"] = None
        return PolicyRestriction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requireBase")
    def require_base(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates if base policy should be enforced for the policy document.
        """
        return pulumi.get(self, "require_base")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        Path to the policy document.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

