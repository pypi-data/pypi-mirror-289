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
from ._enums import *

__all__ = ['CertificateObjectGlobalRulestackArgs', 'CertificateObjectGlobalRulestack']

@pulumi.input_type
class CertificateObjectGlobalRulestackArgs:
    def __init__(__self__, *,
                 certificate_self_signed: pulumi.Input[Union[str, 'BooleanEnum']],
                 global_rulestack_name: pulumi.Input[str],
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 certificate_signer_resource_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CertificateObjectGlobalRulestack resource.
        :param pulumi.Input[Union[str, 'BooleanEnum']] certificate_self_signed: use certificate self signed
        :param pulumi.Input[str] global_rulestack_name: GlobalRulestack resource name
        :param pulumi.Input[str] audit_comment: comment for this object
        :param pulumi.Input[str] certificate_signer_resource_id: Resource Id of certificate signer, to be populated only when certificateSelfSigned is false
        :param pulumi.Input[str] description: user description for this object
        :param pulumi.Input[str] name: certificate name
        """
        pulumi.set(__self__, "certificate_self_signed", certificate_self_signed)
        pulumi.set(__self__, "global_rulestack_name", global_rulestack_name)
        if audit_comment is not None:
            pulumi.set(__self__, "audit_comment", audit_comment)
        if certificate_signer_resource_id is not None:
            pulumi.set(__self__, "certificate_signer_resource_id", certificate_signer_resource_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="certificateSelfSigned")
    def certificate_self_signed(self) -> pulumi.Input[Union[str, 'BooleanEnum']]:
        """
        use certificate self signed
        """
        return pulumi.get(self, "certificate_self_signed")

    @certificate_self_signed.setter
    def certificate_self_signed(self, value: pulumi.Input[Union[str, 'BooleanEnum']]):
        pulumi.set(self, "certificate_self_signed", value)

    @property
    @pulumi.getter(name="globalRulestackName")
    def global_rulestack_name(self) -> pulumi.Input[str]:
        """
        GlobalRulestack resource name
        """
        return pulumi.get(self, "global_rulestack_name")

    @global_rulestack_name.setter
    def global_rulestack_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "global_rulestack_name", value)

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[pulumi.Input[str]]:
        """
        comment for this object
        """
        return pulumi.get(self, "audit_comment")

    @audit_comment.setter
    def audit_comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audit_comment", value)

    @property
    @pulumi.getter(name="certificateSignerResourceId")
    def certificate_signer_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id of certificate signer, to be populated only when certificateSelfSigned is false
        """
        return pulumi.get(self, "certificate_signer_resource_id")

    @certificate_signer_resource_id.setter
    def certificate_signer_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_signer_resource_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        user description for this object
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        certificate name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class CertificateObjectGlobalRulestack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 certificate_self_signed: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 certificate_signer_resource_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_rulestack_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        GlobalRulestack Certificate Object

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] audit_comment: comment for this object
        :param pulumi.Input[Union[str, 'BooleanEnum']] certificate_self_signed: use certificate self signed
        :param pulumi.Input[str] certificate_signer_resource_id: Resource Id of certificate signer, to be populated only when certificateSelfSigned is false
        :param pulumi.Input[str] description: user description for this object
        :param pulumi.Input[str] global_rulestack_name: GlobalRulestack resource name
        :param pulumi.Input[str] name: certificate name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateObjectGlobalRulestackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        GlobalRulestack Certificate Object

        :param str resource_name: The name of the resource.
        :param CertificateObjectGlobalRulestackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateObjectGlobalRulestackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 certificate_self_signed: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 certificate_signer_resource_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_rulestack_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CertificateObjectGlobalRulestackArgs.__new__(CertificateObjectGlobalRulestackArgs)

            __props__.__dict__["audit_comment"] = audit_comment
            if certificate_self_signed is None and not opts.urn:
                raise TypeError("Missing required property 'certificate_self_signed'")
            __props__.__dict__["certificate_self_signed"] = certificate_self_signed
            __props__.__dict__["certificate_signer_resource_id"] = certificate_signer_resource_id
            __props__.__dict__["description"] = description
            if global_rulestack_name is None and not opts.urn:
                raise TypeError("Missing required property 'global_rulestack_name'")
            __props__.__dict__["global_rulestack_name"] = global_rulestack_name
            __props__.__dict__["name"] = name
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cloudngfw:CertificateObjectGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829:CertificateObjectGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829preview:CertificateObjectGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20230901preview:CertificateObjectGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20231010preview:CertificateObjectGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20240119preview:CertificateObjectGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20240207preview:CertificateObjectGlobalRulestack")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CertificateObjectGlobalRulestack, __self__).__init__(
            'azure-native:cloudngfw/v20230901:CertificateObjectGlobalRulestack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CertificateObjectGlobalRulestack':
        """
        Get an existing CertificateObjectGlobalRulestack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CertificateObjectGlobalRulestackArgs.__new__(CertificateObjectGlobalRulestackArgs)

        __props__.__dict__["audit_comment"] = None
        __props__.__dict__["certificate_self_signed"] = None
        __props__.__dict__["certificate_signer_resource_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CertificateObjectGlobalRulestack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> pulumi.Output[Optional[str]]:
        """
        comment for this object
        """
        return pulumi.get(self, "audit_comment")

    @property
    @pulumi.getter(name="certificateSelfSigned")
    def certificate_self_signed(self) -> pulumi.Output[str]:
        """
        use certificate self signed
        """
        return pulumi.get(self, "certificate_self_signed")

    @property
    @pulumi.getter(name="certificateSignerResourceId")
    def certificate_signer_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Id of certificate signer, to be populated only when certificateSelfSigned is false
        """
        return pulumi.get(self, "certificate_signer_resource_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        user description for this object
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        read only string representing last create or update
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

