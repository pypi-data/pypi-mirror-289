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
from ._enums import *
from ._inputs import *

__all__ = ['AccessPolicyArgs', 'AccessPolicy']

@pulumi.input_type
class AccessPolicyArgs:
    def __init__(__self__, *,
                 policy: pulumi.Input['AccessPolicyEntryArgs'],
                 resource_group_name: pulumi.Input[str],
                 vault_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a AccessPolicy resource.
        :param pulumi.Input['AccessPolicyEntryArgs'] policy: The definition of the access policy.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the vault.
        :param pulumi.Input[str] vault_name: Name of the Key Vault.
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vault_name", vault_name)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input['AccessPolicyEntryArgs']:
        """
        The definition of the access policy.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input['AccessPolicyEntryArgs']):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group that contains the vault.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Input[str]:
        """
        Name of the Key Vault.
        """
        return pulumi.get(self, "vault_name")

    @vault_name.setter
    def vault_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vault_name", value)


class AccessPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy: Optional[pulumi.Input[Union['AccessPolicyEntryArgs', 'AccessPolicyEntryArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vault_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Key Vault Access Policy for managing policies on existing vaults.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['AccessPolicyEntryArgs', 'AccessPolicyEntryArgsDict']] policy: The definition of the access policy.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the vault.
        :param pulumi.Input[str] vault_name: Name of the Key Vault.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Key Vault Access Policy for managing policies on existing vaults.

        :param str resource_name: The name of the resource.
        :param AccessPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy: Optional[pulumi.Input[Union['AccessPolicyEntryArgs', 'AccessPolicyEntryArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vault_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessPolicyArgs.__new__(AccessPolicyArgs)

            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if vault_name is None and not opts.urn:
                raise TypeError("Missing required property 'vault_name'")
            __props__.__dict__["vault_name"] = vault_name
        super(AccessPolicy, __self__).__init__(
            'azure-native:keyvault:AccessPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccessPolicy':
        """
        Get an existing AccessPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccessPolicyArgs.__new__(AccessPolicyArgs)

        __props__.__dict__["policy"] = None
        __props__.__dict__["resource_group_name"] = None
        __props__.__dict__["vault_name"] = None
        return AccessPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional['outputs.AccessPolicyEntry']]:
        """
        The definition of the access policy.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the resource group that contains the vault.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the Key Vault.
        """
        return pulumi.get(self, "vault_name")

