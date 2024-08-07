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
from ._inputs import *

__all__ = ['LocalRuleArgs', 'LocalRule']

@pulumi.input_type
class LocalRuleArgs:
    def __init__(__self__, *,
                 local_rulestack_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 rule_name: pulumi.Input[str],
                 action_type: Optional[pulumi.Input[Union[str, 'ActionEnum']]] = None,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input['CategoryArgs']] = None,
                 decryption_rule_type: Optional[pulumi.Input[Union[str, 'DecryptionRuleTypeEnum']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input['DestinationAddrArgs']] = None,
                 enable_logging: Optional[pulumi.Input[Union[str, 'StateEnum']]] = None,
                 inbound_inspection_certificate: Optional[pulumi.Input[str]] = None,
                 negate_destination: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 negate_source: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 protocol_port_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rule_state: Optional[pulumi.Input[Union[str, 'StateEnum']]] = None,
                 source: Optional[pulumi.Input['SourceAddrArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TagInfoArgs']]]] = None):
        """
        The set of arguments for constructing a LocalRule resource.
        :param pulumi.Input[str] local_rulestack_name: LocalRulestack resource name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] rule_name: rule name
        :param pulumi.Input[Union[str, 'ActionEnum']] action_type: rule action
        :param pulumi.Input[Sequence[pulumi.Input[str]]] applications: array of rule applications
        :param pulumi.Input[str] audit_comment: rule comment
        :param pulumi.Input['CategoryArgs'] category: rule category
        :param pulumi.Input[Union[str, 'DecryptionRuleTypeEnum']] decryption_rule_type: enable or disable decryption
        :param pulumi.Input[str] description: rule description
        :param pulumi.Input['DestinationAddrArgs'] destination: destination address
        :param pulumi.Input[Union[str, 'StateEnum']] enable_logging: enable or disable logging
        :param pulumi.Input[str] inbound_inspection_certificate: inbound Inspection Certificate
        :param pulumi.Input[Union[str, 'BooleanEnum']] negate_destination: cidr should not be 'any'
        :param pulumi.Input[Union[str, 'BooleanEnum']] negate_source: cidr should not be 'any'
        :param pulumi.Input[str] priority: Local Rule priority
        :param pulumi.Input[str] protocol: any, application-default, TCP:number, UDP:number
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocol_port_list: prot port list
        :param pulumi.Input[Union[str, 'StateEnum']] rule_state: state of this rule
        :param pulumi.Input['SourceAddrArgs'] source: source address
        :param pulumi.Input[Sequence[pulumi.Input['TagInfoArgs']]] tags: tag for rule
        """
        pulumi.set(__self__, "local_rulestack_name", local_rulestack_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "rule_name", rule_name)
        if action_type is not None:
            pulumi.set(__self__, "action_type", action_type)
        if applications is not None:
            pulumi.set(__self__, "applications", applications)
        if audit_comment is not None:
            pulumi.set(__self__, "audit_comment", audit_comment)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if decryption_rule_type is not None:
            pulumi.set(__self__, "decryption_rule_type", decryption_rule_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if enable_logging is not None:
            pulumi.set(__self__, "enable_logging", enable_logging)
        if inbound_inspection_certificate is not None:
            pulumi.set(__self__, "inbound_inspection_certificate", inbound_inspection_certificate)
        if negate_destination is not None:
            pulumi.set(__self__, "negate_destination", negate_destination)
        if negate_source is not None:
            pulumi.set(__self__, "negate_source", negate_source)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if protocol is None:
            protocol = 'application-default'
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if protocol_port_list is not None:
            pulumi.set(__self__, "protocol_port_list", protocol_port_list)
        if rule_state is not None:
            pulumi.set(__self__, "rule_state", rule_state)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="localRulestackName")
    def local_rulestack_name(self) -> pulumi.Input[str]:
        """
        LocalRulestack resource name
        """
        return pulumi.get(self, "local_rulestack_name")

    @local_rulestack_name.setter
    def local_rulestack_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "local_rulestack_name", value)

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
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[str]:
        """
        rule name
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_name", value)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> Optional[pulumi.Input[Union[str, 'ActionEnum']]]:
        """
        rule action
        """
        return pulumi.get(self, "action_type")

    @action_type.setter
    def action_type(self, value: Optional[pulumi.Input[Union[str, 'ActionEnum']]]):
        pulumi.set(self, "action_type", value)

    @property
    @pulumi.getter
    def applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        array of rule applications
        """
        return pulumi.get(self, "applications")

    @applications.setter
    def applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "applications", value)

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[pulumi.Input[str]]:
        """
        rule comment
        """
        return pulumi.get(self, "audit_comment")

    @audit_comment.setter
    def audit_comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audit_comment", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input['CategoryArgs']]:
        """
        rule category
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input['CategoryArgs']]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="decryptionRuleType")
    def decryption_rule_type(self) -> Optional[pulumi.Input[Union[str, 'DecryptionRuleTypeEnum']]]:
        """
        enable or disable decryption
        """
        return pulumi.get(self, "decryption_rule_type")

    @decryption_rule_type.setter
    def decryption_rule_type(self, value: Optional[pulumi.Input[Union[str, 'DecryptionRuleTypeEnum']]]):
        pulumi.set(self, "decryption_rule_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        rule description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input['DestinationAddrArgs']]:
        """
        destination address
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input['DestinationAddrArgs']]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[Union[str, 'StateEnum']]]:
        """
        enable or disable logging
        """
        return pulumi.get(self, "enable_logging")

    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[Union[str, 'StateEnum']]]):
        pulumi.set(self, "enable_logging", value)

    @property
    @pulumi.getter(name="inboundInspectionCertificate")
    def inbound_inspection_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        inbound Inspection Certificate
        """
        return pulumi.get(self, "inbound_inspection_certificate")

    @inbound_inspection_certificate.setter
    def inbound_inspection_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inbound_inspection_certificate", value)

    @property
    @pulumi.getter(name="negateDestination")
    def negate_destination(self) -> Optional[pulumi.Input[Union[str, 'BooleanEnum']]]:
        """
        cidr should not be 'any'
        """
        return pulumi.get(self, "negate_destination")

    @negate_destination.setter
    def negate_destination(self, value: Optional[pulumi.Input[Union[str, 'BooleanEnum']]]):
        pulumi.set(self, "negate_destination", value)

    @property
    @pulumi.getter(name="negateSource")
    def negate_source(self) -> Optional[pulumi.Input[Union[str, 'BooleanEnum']]]:
        """
        cidr should not be 'any'
        """
        return pulumi.get(self, "negate_source")

    @negate_source.setter
    def negate_source(self, value: Optional[pulumi.Input[Union[str, 'BooleanEnum']]]):
        pulumi.set(self, "negate_source", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[str]]:
        """
        Local Rule priority
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        any, application-default, TCP:number, UDP:number
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="protocolPortList")
    def protocol_port_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        prot port list
        """
        return pulumi.get(self, "protocol_port_list")

    @protocol_port_list.setter
    def protocol_port_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "protocol_port_list", value)

    @property
    @pulumi.getter(name="ruleState")
    def rule_state(self) -> Optional[pulumi.Input[Union[str, 'StateEnum']]]:
        """
        state of this rule
        """
        return pulumi.get(self, "rule_state")

    @rule_state.setter
    def rule_state(self, value: Optional[pulumi.Input[Union[str, 'StateEnum']]]):
        pulumi.set(self, "rule_state", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['SourceAddrArgs']]:
        """
        source address
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['SourceAddrArgs']]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TagInfoArgs']]]]:
        """
        tag for rule
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TagInfoArgs']]]]):
        pulumi.set(self, "tags", value)


class LocalRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_type: Optional[pulumi.Input[Union[str, 'ActionEnum']]] = None,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[Union['CategoryArgs', 'CategoryArgsDict']]] = None,
                 decryption_rule_type: Optional[pulumi.Input[Union[str, 'DecryptionRuleTypeEnum']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[Union['DestinationAddrArgs', 'DestinationAddrArgsDict']]] = None,
                 enable_logging: Optional[pulumi.Input[Union[str, 'StateEnum']]] = None,
                 inbound_inspection_certificate: Optional[pulumi.Input[str]] = None,
                 local_rulestack_name: Optional[pulumi.Input[str]] = None,
                 negate_destination: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 negate_source: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 protocol_port_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 rule_state: Optional[pulumi.Input[Union[str, 'StateEnum']]] = None,
                 source: Optional[pulumi.Input[Union['SourceAddrArgs', 'SourceAddrArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TagInfoArgs', 'TagInfoArgsDict']]]]] = None,
                 __props__=None):
        """
        LocalRulestack rule list

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'ActionEnum']] action_type: rule action
        :param pulumi.Input[Sequence[pulumi.Input[str]]] applications: array of rule applications
        :param pulumi.Input[str] audit_comment: rule comment
        :param pulumi.Input[Union['CategoryArgs', 'CategoryArgsDict']] category: rule category
        :param pulumi.Input[Union[str, 'DecryptionRuleTypeEnum']] decryption_rule_type: enable or disable decryption
        :param pulumi.Input[str] description: rule description
        :param pulumi.Input[Union['DestinationAddrArgs', 'DestinationAddrArgsDict']] destination: destination address
        :param pulumi.Input[Union[str, 'StateEnum']] enable_logging: enable or disable logging
        :param pulumi.Input[str] inbound_inspection_certificate: inbound Inspection Certificate
        :param pulumi.Input[str] local_rulestack_name: LocalRulestack resource name
        :param pulumi.Input[Union[str, 'BooleanEnum']] negate_destination: cidr should not be 'any'
        :param pulumi.Input[Union[str, 'BooleanEnum']] negate_source: cidr should not be 'any'
        :param pulumi.Input[str] priority: Local Rule priority
        :param pulumi.Input[str] protocol: any, application-default, TCP:number, UDP:number
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocol_port_list: prot port list
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] rule_name: rule name
        :param pulumi.Input[Union[str, 'StateEnum']] rule_state: state of this rule
        :param pulumi.Input[Union['SourceAddrArgs', 'SourceAddrArgsDict']] source: source address
        :param pulumi.Input[Sequence[pulumi.Input[Union['TagInfoArgs', 'TagInfoArgsDict']]]] tags: tag for rule
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocalRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        LocalRulestack rule list

        :param str resource_name: The name of the resource.
        :param LocalRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocalRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_type: Optional[pulumi.Input[Union[str, 'ActionEnum']]] = None,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[Union['CategoryArgs', 'CategoryArgsDict']]] = None,
                 decryption_rule_type: Optional[pulumi.Input[Union[str, 'DecryptionRuleTypeEnum']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[Union['DestinationAddrArgs', 'DestinationAddrArgsDict']]] = None,
                 enable_logging: Optional[pulumi.Input[Union[str, 'StateEnum']]] = None,
                 inbound_inspection_certificate: Optional[pulumi.Input[str]] = None,
                 local_rulestack_name: Optional[pulumi.Input[str]] = None,
                 negate_destination: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 negate_source: Optional[pulumi.Input[Union[str, 'BooleanEnum']]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 protocol_port_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 rule_state: Optional[pulumi.Input[Union[str, 'StateEnum']]] = None,
                 source: Optional[pulumi.Input[Union['SourceAddrArgs', 'SourceAddrArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TagInfoArgs', 'TagInfoArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocalRuleArgs.__new__(LocalRuleArgs)

            __props__.__dict__["action_type"] = action_type
            __props__.__dict__["applications"] = applications
            __props__.__dict__["audit_comment"] = audit_comment
            __props__.__dict__["category"] = category
            __props__.__dict__["decryption_rule_type"] = decryption_rule_type
            __props__.__dict__["description"] = description
            __props__.__dict__["destination"] = destination
            __props__.__dict__["enable_logging"] = enable_logging
            __props__.__dict__["inbound_inspection_certificate"] = inbound_inspection_certificate
            if local_rulestack_name is None and not opts.urn:
                raise TypeError("Missing required property 'local_rulestack_name'")
            __props__.__dict__["local_rulestack_name"] = local_rulestack_name
            __props__.__dict__["negate_destination"] = negate_destination
            __props__.__dict__["negate_source"] = negate_source
            __props__.__dict__["priority"] = priority
            if protocol is None:
                protocol = 'application-default'
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["protocol_port_list"] = protocol_port_list
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if rule_name is None and not opts.urn:
                raise TypeError("Missing required property 'rule_name'")
            __props__.__dict__["rule_name"] = rule_name
            __props__.__dict__["rule_state"] = rule_state
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cloudngfw:LocalRule"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829:LocalRule"), pulumi.Alias(type_="azure-native:cloudngfw/v20230901:LocalRule"), pulumi.Alias(type_="azure-native:cloudngfw/v20230901preview:LocalRule"), pulumi.Alias(type_="azure-native:cloudngfw/v20231010preview:LocalRule"), pulumi.Alias(type_="azure-native:cloudngfw/v20240119preview:LocalRule"), pulumi.Alias(type_="azure-native:cloudngfw/v20240207preview:LocalRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LocalRule, __self__).__init__(
            'azure-native:cloudngfw/v20220829preview:LocalRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocalRule':
        """
        Get an existing LocalRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocalRuleArgs.__new__(LocalRuleArgs)

        __props__.__dict__["action_type"] = None
        __props__.__dict__["applications"] = None
        __props__.__dict__["audit_comment"] = None
        __props__.__dict__["category"] = None
        __props__.__dict__["decryption_rule_type"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["destination"] = None
        __props__.__dict__["enable_logging"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["inbound_inspection_certificate"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["negate_destination"] = None
        __props__.__dict__["negate_source"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["protocol_port_list"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rule_name"] = None
        __props__.__dict__["rule_state"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return LocalRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Output[Optional[str]]:
        """
        rule action
        """
        return pulumi.get(self, "action_type")

    @property
    @pulumi.getter
    def applications(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        array of rule applications
        """
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> pulumi.Output[Optional[str]]:
        """
        rule comment
        """
        return pulumi.get(self, "audit_comment")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[Optional['outputs.CategoryResponse']]:
        """
        rule category
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="decryptionRuleType")
    def decryption_rule_type(self) -> pulumi.Output[Optional[str]]:
        """
        enable or disable decryption
        """
        return pulumi.get(self, "decryption_rule_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        rule description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional['outputs.DestinationAddrResponse']]:
        """
        destination address
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> pulumi.Output[Optional[str]]:
        """
        enable or disable logging
        """
        return pulumi.get(self, "enable_logging")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        etag info
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="inboundInspectionCertificate")
    def inbound_inspection_certificate(self) -> pulumi.Output[Optional[str]]:
        """
        inbound Inspection Certificate
        """
        return pulumi.get(self, "inbound_inspection_certificate")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="negateDestination")
    def negate_destination(self) -> pulumi.Output[Optional[str]]:
        """
        cidr should not be 'any'
        """
        return pulumi.get(self, "negate_destination")

    @property
    @pulumi.getter(name="negateSource")
    def negate_source(self) -> pulumi.Output[Optional[str]]:
        """
        cidr should not be 'any'
        """
        return pulumi.get(self, "negate_source")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[str]]:
        """
        any, application-default, TCP:number, UDP:number
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="protocolPortList")
    def protocol_port_list(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        prot port list
        """
        return pulumi.get(self, "protocol_port_list")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[str]:
        """
        rule name
        """
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter(name="ruleState")
    def rule_state(self) -> pulumi.Output[Optional[str]]:
        """
        state of this rule
        """
        return pulumi.get(self, "rule_state")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional['outputs.SourceAddrResponse']]:
        """
        source address
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TagInfoResponse']]]:
        """
        tag for rule
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

