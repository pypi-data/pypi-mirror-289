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

__all__ = ['NotificationRecipientEmailArgs', 'NotificationRecipientEmail']

@pulumi.input_type
class NotificationRecipientEmailArgs:
    def __init__(__self__, *,
                 notification_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 email: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NotificationRecipientEmail resource.
        :param pulumi.Input[str] notification_name: Notification Name Identifier.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] email: Email identifier.
        """
        pulumi.set(__self__, "notification_name", notification_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if email is not None:
            pulumi.set(__self__, "email", email)

    @property
    @pulumi.getter(name="notificationName")
    def notification_name(self) -> pulumi.Input[str]:
        """
        Notification Name Identifier.
        """
        return pulumi.get(self, "notification_name")

    @notification_name.setter
    def notification_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "notification_name", value)

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
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email identifier.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)


class NotificationRecipientEmail(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 notification_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Recipient Email details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email: Email identifier.
        :param pulumi.Input[str] notification_name: Notification Name Identifier.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationRecipientEmailArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Recipient Email details.

        :param str resource_name: The name of the resource.
        :param NotificationRecipientEmailArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationRecipientEmailArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 notification_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NotificationRecipientEmailArgs.__new__(NotificationRecipientEmailArgs)

            __props__.__dict__["email"] = email
            if notification_name is None and not opts.urn:
                raise TypeError("Missing required property 'notification_name'")
            __props__.__dict__["notification_name"] = notification_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20220801:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:NotificationRecipientEmail"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:NotificationRecipientEmail")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NotificationRecipientEmail, __self__).__init__(
            'azure-native:apimanagement/v20230501preview:NotificationRecipientEmail',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NotificationRecipientEmail':
        """
        Get an existing NotificationRecipientEmail resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NotificationRecipientEmailArgs.__new__(NotificationRecipientEmailArgs)

        __props__.__dict__["email"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return NotificationRecipientEmail(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[Optional[str]]:
        """
        User Email subscribed to notification.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

