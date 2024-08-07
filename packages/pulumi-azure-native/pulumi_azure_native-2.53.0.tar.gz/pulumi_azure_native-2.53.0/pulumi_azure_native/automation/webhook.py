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

__all__ = ['WebhookArgs', 'Webhook']

@pulumi.input_type
class WebhookArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 run_on: Optional[pulumi.Input[str]] = None,
                 runbook: Optional[pulumi.Input['RunbookAssociationPropertyArgs']] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 webhook_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Webhook resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] name: Gets or sets the name of the webhook.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[str] expiry_time: Gets or sets the expiry time.
        :param pulumi.Input[bool] is_enabled: Gets or sets the value of the enabled flag of webhook.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Gets or sets the parameters of the job.
        :param pulumi.Input[str] run_on: Gets or sets the name of the hybrid worker group the webhook job will run on.
        :param pulumi.Input['RunbookAssociationPropertyArgs'] runbook: Gets or sets the runbook.
        :param pulumi.Input[str] uri: Gets or sets the uri.
        :param pulumi.Input[str] webhook_name: The webhook name.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if expiry_time is not None:
            pulumi.set(__self__, "expiry_time", expiry_time)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if run_on is not None:
            pulumi.set(__self__, "run_on", run_on)
        if runbook is not None:
            pulumi.set(__self__, "runbook", runbook)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)
        if webhook_name is not None:
            pulumi.set(__self__, "webhook_name", webhook_name)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Gets or sets the name of the webhook.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the expiry time.
        """
        return pulumi.get(self, "expiry_time")

    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry_time", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Gets or sets the value of the enabled flag of webhook.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets the parameters of the job.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="runOn")
    def run_on(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the name of the hybrid worker group the webhook job will run on.
        """
        return pulumi.get(self, "run_on")

    @run_on.setter
    def run_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_on", value)

    @property
    @pulumi.getter
    def runbook(self) -> Optional[pulumi.Input['RunbookAssociationPropertyArgs']]:
        """
        Gets or sets the runbook.
        """
        return pulumi.get(self, "runbook")

    @runbook.setter
    def runbook(self, value: Optional[pulumi.Input['RunbookAssociationPropertyArgs']]):
        pulumi.set(self, "runbook", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the uri.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter(name="webhookName")
    def webhook_name(self) -> Optional[pulumi.Input[str]]:
        """
        The webhook name.
        """
        return pulumi.get(self, "webhook_name")

    @webhook_name.setter
    def webhook_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "webhook_name", value)


class Webhook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_on: Optional[pulumi.Input[str]] = None,
                 runbook: Optional[pulumi.Input[Union['RunbookAssociationPropertyArgs', 'RunbookAssociationPropertyArgsDict']]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 webhook_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of the webhook type.
        Azure REST API version: 2015-10-31. Prior API version in Azure Native 1.x: 2015-10-31.

        Other available API versions: 2023-05-15-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] expiry_time: Gets or sets the expiry time.
        :param pulumi.Input[bool] is_enabled: Gets or sets the value of the enabled flag of webhook.
        :param pulumi.Input[str] name: Gets or sets the name of the webhook.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Gets or sets the parameters of the job.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[str] run_on: Gets or sets the name of the hybrid worker group the webhook job will run on.
        :param pulumi.Input[Union['RunbookAssociationPropertyArgs', 'RunbookAssociationPropertyArgsDict']] runbook: Gets or sets the runbook.
        :param pulumi.Input[str] uri: Gets or sets the uri.
        :param pulumi.Input[str] webhook_name: The webhook name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebhookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the webhook type.
        Azure REST API version: 2015-10-31. Prior API version in Azure Native 1.x: 2015-10-31.

        Other available API versions: 2023-05-15-preview.

        :param str resource_name: The name of the resource.
        :param WebhookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebhookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_on: Optional[pulumi.Input[str]] = None,
                 runbook: Optional[pulumi.Input[Union['RunbookAssociationPropertyArgs', 'RunbookAssociationPropertyArgsDict']]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 webhook_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebhookArgs.__new__(WebhookArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            __props__.__dict__["expiry_time"] = expiry_time
            __props__.__dict__["is_enabled"] = is_enabled
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["run_on"] = run_on
            __props__.__dict__["runbook"] = runbook
            __props__.__dict__["uri"] = uri
            __props__.__dict__["webhook_name"] = webhook_name
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["last_invoked_time"] = None
            __props__.__dict__["last_modified_by"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:automation/v20151031:Webhook"), pulumi.Alias(type_="azure-native:automation/v20230515preview:Webhook")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Webhook, __self__).__init__(
            'azure-native:automation:Webhook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Webhook':
        """
        Get an existing Webhook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebhookArgs.__new__(WebhookArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["expiry_time"] = None
        __props__.__dict__["is_enabled"] = None
        __props__.__dict__["last_invoked_time"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["run_on"] = None
        __props__.__dict__["runbook"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uri"] = None
        return Webhook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the expiry time.
        """
        return pulumi.get(self, "expiry_time")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets or sets the value of the enabled flag of the webhook.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="lastInvokedTime")
    def last_invoked_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the last invoked time.
        """
        return pulumi.get(self, "last_invoked_time")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[str]]:
        """
        Details of the user who last modified the Webhook
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Gets or sets the parameters of the job that is created when the webhook calls the runbook it is associated with.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="runOn")
    def run_on(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the name of the hybrid worker group the webhook job will run on.
        """
        return pulumi.get(self, "run_on")

    @property
    @pulumi.getter
    def runbook(self) -> pulumi.Output[Optional['outputs.RunbookAssociationPropertyResponse']]:
        """
        Gets or sets the runbook the webhook is associated with.
        """
        return pulumi.get(self, "runbook")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the webhook uri.
        """
        return pulumi.get(self, "uri")

