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

__all__ = ['SecurityContactArgs', 'SecurityContact']

@pulumi.input_type
class SecurityContactArgs:
    def __init__(__self__, *,
                 alert_notifications: Optional[pulumi.Input['SecurityContactPropertiesAlertNotificationsArgs']] = None,
                 emails: Optional[pulumi.Input[str]] = None,
                 notifications_by_role: Optional[pulumi.Input['SecurityContactPropertiesNotificationsByRoleArgs']] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 security_contact_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityContact resource.
        :param pulumi.Input['SecurityContactPropertiesAlertNotificationsArgs'] alert_notifications: Defines whether to send email notifications about new security alerts
        :param pulumi.Input[str] emails: List of email addresses which will get notifications from Microsoft Defender for Cloud by the configurations defined in this security contact.
        :param pulumi.Input['SecurityContactPropertiesNotificationsByRoleArgs'] notifications_by_role: Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        :param pulumi.Input[str] phone: The security contact's phone number
        :param pulumi.Input[str] security_contact_name: Name of the security contact object
        """
        if alert_notifications is not None:
            pulumi.set(__self__, "alert_notifications", alert_notifications)
        if emails is not None:
            pulumi.set(__self__, "emails", emails)
        if notifications_by_role is not None:
            pulumi.set(__self__, "notifications_by_role", notifications_by_role)
        if phone is not None:
            pulumi.set(__self__, "phone", phone)
        if security_contact_name is not None:
            pulumi.set(__self__, "security_contact_name", security_contact_name)

    @property
    @pulumi.getter(name="alertNotifications")
    def alert_notifications(self) -> Optional[pulumi.Input['SecurityContactPropertiesAlertNotificationsArgs']]:
        """
        Defines whether to send email notifications about new security alerts
        """
        return pulumi.get(self, "alert_notifications")

    @alert_notifications.setter
    def alert_notifications(self, value: Optional[pulumi.Input['SecurityContactPropertiesAlertNotificationsArgs']]):
        pulumi.set(self, "alert_notifications", value)

    @property
    @pulumi.getter
    def emails(self) -> Optional[pulumi.Input[str]]:
        """
        List of email addresses which will get notifications from Microsoft Defender for Cloud by the configurations defined in this security contact.
        """
        return pulumi.get(self, "emails")

    @emails.setter
    def emails(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "emails", value)

    @property
    @pulumi.getter(name="notificationsByRole")
    def notifications_by_role(self) -> Optional[pulumi.Input['SecurityContactPropertiesNotificationsByRoleArgs']]:
        """
        Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        """
        return pulumi.get(self, "notifications_by_role")

    @notifications_by_role.setter
    def notifications_by_role(self, value: Optional[pulumi.Input['SecurityContactPropertiesNotificationsByRoleArgs']]):
        pulumi.set(self, "notifications_by_role", value)

    @property
    @pulumi.getter
    def phone(self) -> Optional[pulumi.Input[str]]:
        """
        The security contact's phone number
        """
        return pulumi.get(self, "phone")

    @phone.setter
    def phone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone", value)

    @property
    @pulumi.getter(name="securityContactName")
    def security_contact_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the security contact object
        """
        return pulumi.get(self, "security_contact_name")

    @security_contact_name.setter
    def security_contact_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_contact_name", value)


class SecurityContact(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_notifications: Optional[pulumi.Input[Union['SecurityContactPropertiesAlertNotificationsArgs', 'SecurityContactPropertiesAlertNotificationsArgsDict']]] = None,
                 emails: Optional[pulumi.Input[str]] = None,
                 notifications_by_role: Optional[pulumi.Input[Union['SecurityContactPropertiesNotificationsByRoleArgs', 'SecurityContactPropertiesNotificationsByRoleArgsDict']]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 security_contact_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Contact details and configurations for notifications coming from Microsoft Defender for Cloud.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['SecurityContactPropertiesAlertNotificationsArgs', 'SecurityContactPropertiesAlertNotificationsArgsDict']] alert_notifications: Defines whether to send email notifications about new security alerts
        :param pulumi.Input[str] emails: List of email addresses which will get notifications from Microsoft Defender for Cloud by the configurations defined in this security contact.
        :param pulumi.Input[Union['SecurityContactPropertiesNotificationsByRoleArgs', 'SecurityContactPropertiesNotificationsByRoleArgsDict']] notifications_by_role: Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        :param pulumi.Input[str] phone: The security contact's phone number
        :param pulumi.Input[str] security_contact_name: Name of the security contact object
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SecurityContactArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contact details and configurations for notifications coming from Microsoft Defender for Cloud.

        :param str resource_name: The name of the resource.
        :param SecurityContactArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityContactArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_notifications: Optional[pulumi.Input[Union['SecurityContactPropertiesAlertNotificationsArgs', 'SecurityContactPropertiesAlertNotificationsArgsDict']]] = None,
                 emails: Optional[pulumi.Input[str]] = None,
                 notifications_by_role: Optional[pulumi.Input[Union['SecurityContactPropertiesNotificationsByRoleArgs', 'SecurityContactPropertiesNotificationsByRoleArgsDict']]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 security_contact_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityContactArgs.__new__(SecurityContactArgs)

            __props__.__dict__["alert_notifications"] = alert_notifications
            __props__.__dict__["emails"] = emails
            __props__.__dict__["notifications_by_role"] = notifications_by_role
            __props__.__dict__["phone"] = phone
            __props__.__dict__["security_contact_name"] = security_contact_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:SecurityContact"), pulumi.Alias(type_="azure-native:security/v20170801preview:SecurityContact"), pulumi.Alias(type_="azure-native:security/v20231201preview:SecurityContact")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SecurityContact, __self__).__init__(
            'azure-native:security/v20200101preview:SecurityContact',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityContact':
        """
        Get an existing SecurityContact resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityContactArgs.__new__(SecurityContactArgs)

        __props__.__dict__["alert_notifications"] = None
        __props__.__dict__["emails"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notifications_by_role"] = None
        __props__.__dict__["phone"] = None
        __props__.__dict__["type"] = None
        return SecurityContact(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alertNotifications")
    def alert_notifications(self) -> pulumi.Output[Optional['outputs.SecurityContactPropertiesResponseAlertNotifications']]:
        """
        Defines whether to send email notifications about new security alerts
        """
        return pulumi.get(self, "alert_notifications")

    @property
    @pulumi.getter
    def emails(self) -> pulumi.Output[Optional[str]]:
        """
        List of email addresses which will get notifications from Microsoft Defender for Cloud by the configurations defined in this security contact.
        """
        return pulumi.get(self, "emails")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationsByRole")
    def notifications_by_role(self) -> pulumi.Output[Optional['outputs.SecurityContactPropertiesResponseNotificationsByRole']]:
        """
        Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        """
        return pulumi.get(self, "notifications_by_role")

    @property
    @pulumi.getter
    def phone(self) -> pulumi.Output[Optional[str]]:
        """
        The security contact's phone number
        """
        return pulumi.get(self, "phone")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

