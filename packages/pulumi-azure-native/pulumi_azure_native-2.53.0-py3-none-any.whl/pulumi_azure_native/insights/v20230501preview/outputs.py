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

__all__ = [
    'AzureAppPushReceiverResponse',
    'EmailReceiverResponse',
    'SmsReceiverResponse',
    'VoiceReceiverResponse',
    'WebhookReceiverResponse',
]

@pulumi.output_type
class AzureAppPushReceiverResponse(dict):
    """
    The Azure mobile App push notification receiver.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "emailAddress":
            suggest = "email_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AzureAppPushReceiverResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AzureAppPushReceiverResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AzureAppPushReceiverResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 email_address: str,
                 name: str):
        """
        The Azure mobile App push notification receiver.
        :param str email_address: The email address registered for the Azure mobile app.
        :param str name: The name of the Azure mobile app push receiver. Names must be unique across all receivers within a tenant action group.
        """
        pulumi.set(__self__, "email_address", email_address)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> str:
        """
        The email address registered for the Azure mobile app.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Azure mobile app push receiver. Names must be unique across all receivers within a tenant action group.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class EmailReceiverResponse(dict):
    """
    An email receiver.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "emailAddress":
            suggest = "email_address"
        elif key == "useCommonAlertSchema":
            suggest = "use_common_alert_schema"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EmailReceiverResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EmailReceiverResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EmailReceiverResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 email_address: str,
                 name: str,
                 status: str,
                 use_common_alert_schema: Optional[bool] = None):
        """
        An email receiver.
        :param str email_address: The email address of this receiver.
        :param str name: The name of the email receiver. Names must be unique across all receivers within a tenant action group.
        :param str status: The receiver status of the e-mail.
        :param bool use_common_alert_schema: Indicates whether to use common alert schema.
        """
        pulumi.set(__self__, "email_address", email_address)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)
        if use_common_alert_schema is None:
            use_common_alert_schema = False
        if use_common_alert_schema is not None:
            pulumi.set(__self__, "use_common_alert_schema", use_common_alert_schema)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> str:
        """
        The email address of this receiver.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the email receiver. Names must be unique across all receivers within a tenant action group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The receiver status of the e-mail.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[bool]:
        """
        Indicates whether to use common alert schema.
        """
        return pulumi.get(self, "use_common_alert_schema")


@pulumi.output_type
class SmsReceiverResponse(dict):
    """
    An SMS receiver.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "countryCode":
            suggest = "country_code"
        elif key == "phoneNumber":
            suggest = "phone_number"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SmsReceiverResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SmsReceiverResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SmsReceiverResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 country_code: str,
                 name: str,
                 phone_number: str,
                 status: str):
        """
        An SMS receiver.
        :param str country_code: The country code of the SMS receiver.
        :param str name: The name of the SMS receiver. Names must be unique across all receivers within a tenant action group.
        :param str phone_number: The phone number of the SMS receiver.
        :param str status: The status of the receiver.
        """
        pulumi.set(__self__, "country_code", country_code)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "phone_number", phone_number)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> str:
        """
        The country code of the SMS receiver.
        """
        return pulumi.get(self, "country_code")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SMS receiver. Names must be unique across all receivers within a tenant action group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> str:
        """
        The phone number of the SMS receiver.
        """
        return pulumi.get(self, "phone_number")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the receiver.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class VoiceReceiverResponse(dict):
    """
    A voice receiver.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "countryCode":
            suggest = "country_code"
        elif key == "phoneNumber":
            suggest = "phone_number"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VoiceReceiverResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VoiceReceiverResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VoiceReceiverResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 country_code: str,
                 name: str,
                 phone_number: str):
        """
        A voice receiver.
        :param str country_code: The country code of the voice receiver.
        :param str name: The name of the voice receiver. Names must be unique across all receivers within a tenant action group.
        :param str phone_number: The phone number of the voice receiver.
        """
        pulumi.set(__self__, "country_code", country_code)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "phone_number", phone_number)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> str:
        """
        The country code of the voice receiver.
        """
        return pulumi.get(self, "country_code")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the voice receiver. Names must be unique across all receivers within a tenant action group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> str:
        """
        The phone number of the voice receiver.
        """
        return pulumi.get(self, "phone_number")


@pulumi.output_type
class WebhookReceiverResponse(dict):
    """
    A webhook receiver.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "serviceUri":
            suggest = "service_uri"
        elif key == "identifierUri":
            suggest = "identifier_uri"
        elif key == "objectId":
            suggest = "object_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "useAadAuth":
            suggest = "use_aad_auth"
        elif key == "useCommonAlertSchema":
            suggest = "use_common_alert_schema"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WebhookReceiverResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WebhookReceiverResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WebhookReceiverResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 service_uri: str,
                 identifier_uri: Optional[str] = None,
                 object_id: Optional[str] = None,
                 tenant_id: Optional[str] = None,
                 use_aad_auth: Optional[bool] = None,
                 use_common_alert_schema: Optional[bool] = None):
        """
        A webhook receiver.
        :param str name: The name of the webhook receiver. Names must be unique across all receivers within a tenant action group.
        :param str service_uri: The URI where webhooks should be sent.
        :param str identifier_uri: Indicates the identifier uri for aad auth.
        :param str object_id: Indicates the webhook app object Id for aad auth.
        :param str tenant_id: Indicates the tenant id for aad auth.
        :param bool use_aad_auth: Indicates whether or not use AAD authentication.
        :param bool use_common_alert_schema: Indicates whether to use common alert schema.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "service_uri", service_uri)
        if identifier_uri is not None:
            pulumi.set(__self__, "identifier_uri", identifier_uri)
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if use_aad_auth is None:
            use_aad_auth = False
        if use_aad_auth is not None:
            pulumi.set(__self__, "use_aad_auth", use_aad_auth)
        if use_common_alert_schema is None:
            use_common_alert_schema = False
        if use_common_alert_schema is not None:
            pulumi.set(__self__, "use_common_alert_schema", use_common_alert_schema)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the webhook receiver. Names must be unique across all receivers within a tenant action group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> str:
        """
        The URI where webhooks should be sent.
        """
        return pulumi.get(self, "service_uri")

    @property
    @pulumi.getter(name="identifierUri")
    def identifier_uri(self) -> Optional[str]:
        """
        Indicates the identifier uri for aad auth.
        """
        return pulumi.get(self, "identifier_uri")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[str]:
        """
        Indicates the webhook app object Id for aad auth.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        Indicates the tenant id for aad auth.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="useAadAuth")
    def use_aad_auth(self) -> Optional[bool]:
        """
        Indicates whether or not use AAD authentication.
        """
        return pulumi.get(self, "use_aad_auth")

    @property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[bool]:
        """
        Indicates whether to use common alert schema.
        """
        return pulumi.get(self, "use_common_alert_schema")


