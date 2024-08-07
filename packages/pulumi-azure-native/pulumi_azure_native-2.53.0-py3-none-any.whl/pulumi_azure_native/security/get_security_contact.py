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

__all__ = [
    'GetSecurityContactResult',
    'AwaitableGetSecurityContactResult',
    'get_security_contact',
    'get_security_contact_output',
]

@pulumi.output_type
class GetSecurityContactResult:
    """
    Contact details and configurations for notifications coming from Microsoft Defender for Cloud.
    """
    def __init__(__self__, alert_notifications=None, emails=None, id=None, name=None, notifications_by_role=None, phone=None, type=None):
        if alert_notifications and not isinstance(alert_notifications, dict):
            raise TypeError("Expected argument 'alert_notifications' to be a dict")
        pulumi.set(__self__, "alert_notifications", alert_notifications)
        if emails and not isinstance(emails, str):
            raise TypeError("Expected argument 'emails' to be a str")
        pulumi.set(__self__, "emails", emails)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notifications_by_role and not isinstance(notifications_by_role, dict):
            raise TypeError("Expected argument 'notifications_by_role' to be a dict")
        pulumi.set(__self__, "notifications_by_role", notifications_by_role)
        if phone and not isinstance(phone, str):
            raise TypeError("Expected argument 'phone' to be a str")
        pulumi.set(__self__, "phone", phone)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="alertNotifications")
    def alert_notifications(self) -> Optional['outputs.SecurityContactPropertiesResponseAlertNotifications']:
        """
        Defines whether to send email notifications about new security alerts
        """
        return pulumi.get(self, "alert_notifications")

    @property
    @pulumi.getter
    def emails(self) -> Optional[str]:
        """
        List of email addresses which will get notifications from Microsoft Defender for Cloud by the configurations defined in this security contact.
        """
        return pulumi.get(self, "emails")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationsByRole")
    def notifications_by_role(self) -> Optional['outputs.SecurityContactPropertiesResponseNotificationsByRole']:
        """
        Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        """
        return pulumi.get(self, "notifications_by_role")

    @property
    @pulumi.getter
    def phone(self) -> Optional[str]:
        """
        The security contact's phone number
        """
        return pulumi.get(self, "phone")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetSecurityContactResult(GetSecurityContactResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityContactResult(
            alert_notifications=self.alert_notifications,
            emails=self.emails,
            id=self.id,
            name=self.name,
            notifications_by_role=self.notifications_by_role,
            phone=self.phone,
            type=self.type)


def get_security_contact(security_contact_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityContactResult:
    """
    Get Default Security contact configurations for the subscription
    Azure REST API version: 2020-01-01-preview.

    Other available API versions: 2017-08-01-preview, 2023-12-01-preview.


    :param str security_contact_name: Name of the security contact object
    """
    __args__ = dict()
    __args__['securityContactName'] = security_contact_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security:getSecurityContact', __args__, opts=opts, typ=GetSecurityContactResult).value

    return AwaitableGetSecurityContactResult(
        alert_notifications=pulumi.get(__ret__, 'alert_notifications'),
        emails=pulumi.get(__ret__, 'emails'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        notifications_by_role=pulumi.get(__ret__, 'notifications_by_role'),
        phone=pulumi.get(__ret__, 'phone'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_security_contact)
def get_security_contact_output(security_contact_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityContactResult]:
    """
    Get Default Security contact configurations for the subscription
    Azure REST API version: 2020-01-01-preview.

    Other available API versions: 2017-08-01-preview, 2023-12-01-preview.


    :param str security_contact_name: Name of the security contact object
    """
    ...
