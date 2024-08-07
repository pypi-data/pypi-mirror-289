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

__all__ = [
    'AuthorizationProfileResponse',
    'SubscriptionFeatureRegistrationResponseProperties',
]

@pulumi.output_type
class AuthorizationProfileResponse(dict):
    """
    Authorization Profile
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "approvedTime":
            suggest = "approved_time"
        elif key == "requestedTime":
            suggest = "requested_time"
        elif key == "requesterObjectId":
            suggest = "requester_object_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AuthorizationProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AuthorizationProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AuthorizationProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 approved_time: str,
                 approver: str,
                 requested_time: str,
                 requester: str,
                 requester_object_id: str):
        """
        Authorization Profile
        :param str approved_time: The approved time
        :param str approver: The approver
        :param str requested_time: The requested time
        :param str requester: The requester
        :param str requester_object_id: The requester object id
        """
        pulumi.set(__self__, "approved_time", approved_time)
        pulumi.set(__self__, "approver", approver)
        pulumi.set(__self__, "requested_time", requested_time)
        pulumi.set(__self__, "requester", requester)
        pulumi.set(__self__, "requester_object_id", requester_object_id)

    @property
    @pulumi.getter(name="approvedTime")
    def approved_time(self) -> str:
        """
        The approved time
        """
        return pulumi.get(self, "approved_time")

    @property
    @pulumi.getter
    def approver(self) -> str:
        """
        The approver
        """
        return pulumi.get(self, "approver")

    @property
    @pulumi.getter(name="requestedTime")
    def requested_time(self) -> str:
        """
        The requested time
        """
        return pulumi.get(self, "requested_time")

    @property
    @pulumi.getter
    def requester(self) -> str:
        """
        The requester
        """
        return pulumi.get(self, "requester")

    @property
    @pulumi.getter(name="requesterObjectId")
    def requester_object_id(self) -> str:
        """
        The requester object id
        """
        return pulumi.get(self, "requester_object_id")


@pulumi.output_type
class SubscriptionFeatureRegistrationResponseProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "approvalType":
            suggest = "approval_type"
        elif key == "displayName":
            suggest = "display_name"
        elif key == "documentationLink":
            suggest = "documentation_link"
        elif key == "featureName":
            suggest = "feature_name"
        elif key == "providerNamespace":
            suggest = "provider_namespace"
        elif key == "registrationDate":
            suggest = "registration_date"
        elif key == "releaseDate":
            suggest = "release_date"
        elif key == "subscriptionId":
            suggest = "subscription_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "authorizationProfile":
            suggest = "authorization_profile"
        elif key == "shouldFeatureDisplayInPortal":
            suggest = "should_feature_display_in_portal"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SubscriptionFeatureRegistrationResponseProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SubscriptionFeatureRegistrationResponseProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SubscriptionFeatureRegistrationResponseProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 approval_type: str,
                 display_name: str,
                 documentation_link: str,
                 feature_name: str,
                 provider_namespace: str,
                 registration_date: str,
                 release_date: str,
                 subscription_id: str,
                 tenant_id: str,
                 authorization_profile: Optional['outputs.AuthorizationProfileResponse'] = None,
                 description: Optional[str] = None,
                 metadata: Optional[Mapping[str, str]] = None,
                 should_feature_display_in_portal: Optional[bool] = None,
                 state: Optional[str] = None):
        """
        :param str approval_type: The feature approval type.
        :param str display_name: The featureDisplayName.
        :param str documentation_link: The feature documentation link.
        :param str feature_name: The featureName.
        :param str provider_namespace: The providerNamespace.
        :param str registration_date: The feature registration date.
        :param str release_date: The feature release date.
        :param str subscription_id: The subscriptionId.
        :param str tenant_id: The tenantId.
        :param 'AuthorizationProfileResponse' authorization_profile: Authorization Profile
        :param str description: The feature description.
        :param Mapping[str, str] metadata: Key-value pairs for meta data.
        :param bool should_feature_display_in_portal: Indicates whether feature should be displayed in Portal.
        :param str state: The state.
        """
        pulumi.set(__self__, "approval_type", approval_type)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "documentation_link", documentation_link)
        pulumi.set(__self__, "feature_name", feature_name)
        pulumi.set(__self__, "provider_namespace", provider_namespace)
        pulumi.set(__self__, "registration_date", registration_date)
        pulumi.set(__self__, "release_date", release_date)
        pulumi.set(__self__, "subscription_id", subscription_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if authorization_profile is not None:
            pulumi.set(__self__, "authorization_profile", authorization_profile)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if should_feature_display_in_portal is None:
            should_feature_display_in_portal = False
        if should_feature_display_in_portal is not None:
            pulumi.set(__self__, "should_feature_display_in_portal", should_feature_display_in_portal)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="approvalType")
    def approval_type(self) -> str:
        """
        The feature approval type.
        """
        return pulumi.get(self, "approval_type")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The featureDisplayName.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="documentationLink")
    def documentation_link(self) -> str:
        """
        The feature documentation link.
        """
        return pulumi.get(self, "documentation_link")

    @property
    @pulumi.getter(name="featureName")
    def feature_name(self) -> str:
        """
        The featureName.
        """
        return pulumi.get(self, "feature_name")

    @property
    @pulumi.getter(name="providerNamespace")
    def provider_namespace(self) -> str:
        """
        The providerNamespace.
        """
        return pulumi.get(self, "provider_namespace")

    @property
    @pulumi.getter(name="registrationDate")
    def registration_date(self) -> str:
        """
        The feature registration date.
        """
        return pulumi.get(self, "registration_date")

    @property
    @pulumi.getter(name="releaseDate")
    def release_date(self) -> str:
        """
        The feature release date.
        """
        return pulumi.get(self, "release_date")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        The subscriptionId.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenantId.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="authorizationProfile")
    def authorization_profile(self) -> Optional['outputs.AuthorizationProfileResponse']:
        """
        Authorization Profile
        """
        return pulumi.get(self, "authorization_profile")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The feature description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, str]]:
        """
        Key-value pairs for meta data.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="shouldFeatureDisplayInPortal")
    def should_feature_display_in_portal(self) -> Optional[bool]:
        """
        Indicates whether feature should be displayed in Portal.
        """
        return pulumi.get(self, "should_feature_display_in_portal")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state.
        """
        return pulumi.get(self, "state")


