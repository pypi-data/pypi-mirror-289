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

__all__ = ['SecurityOperatorArgs', 'SecurityOperator']

@pulumi.input_type
class SecurityOperatorArgs:
    def __init__(__self__, *,
                 pricing_name: pulumi.Input[str],
                 security_operator_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityOperator resource.
        :param pulumi.Input[str] pricing_name: name of the pricing configuration
        :param pulumi.Input[str] security_operator_name: name of the securityOperator
        """
        pulumi.set(__self__, "pricing_name", pricing_name)
        if security_operator_name is not None:
            pulumi.set(__self__, "security_operator_name", security_operator_name)

    @property
    @pulumi.getter(name="pricingName")
    def pricing_name(self) -> pulumi.Input[str]:
        """
        name of the pricing configuration
        """
        return pulumi.get(self, "pricing_name")

    @pricing_name.setter
    def pricing_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "pricing_name", value)

    @property
    @pulumi.getter(name="securityOperatorName")
    def security_operator_name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the securityOperator
        """
        return pulumi.get(self, "security_operator_name")

    @security_operator_name.setter
    def security_operator_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_operator_name", value)


class SecurityOperator(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pricing_name: Optional[pulumi.Input[str]] = None,
                 security_operator_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Security operator under a given subscription and pricing

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] pricing_name: name of the pricing configuration
        :param pulumi.Input[str] security_operator_name: name of the securityOperator
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityOperatorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Security operator under a given subscription and pricing

        :param str resource_name: The name of the resource.
        :param SecurityOperatorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityOperatorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pricing_name: Optional[pulumi.Input[str]] = None,
                 security_operator_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityOperatorArgs.__new__(SecurityOperatorArgs)

            if pricing_name is None and not opts.urn:
                raise TypeError("Missing required property 'pricing_name'")
            __props__.__dict__["pricing_name"] = pricing_name
            __props__.__dict__["security_operator_name"] = security_operator_name
            __props__.__dict__["identity"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:SecurityOperator")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SecurityOperator, __self__).__init__(
            'azure-native:security/v20230101preview:SecurityOperator',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityOperator':
        """
        Get an existing SecurityOperator resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityOperatorArgs.__new__(SecurityOperatorArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return SecurityOperator(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

