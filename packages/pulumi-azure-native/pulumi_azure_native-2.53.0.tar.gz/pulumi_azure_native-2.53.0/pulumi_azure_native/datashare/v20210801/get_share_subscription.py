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

__all__ = [
    'GetShareSubscriptionResult',
    'AwaitableGetShareSubscriptionResult',
    'get_share_subscription',
    'get_share_subscription_output',
]

@pulumi.output_type
class GetShareSubscriptionResult:
    """
    A share subscription data transfer object.
    """
    def __init__(__self__, created_at=None, expiration_date=None, id=None, invitation_id=None, name=None, provider_email=None, provider_name=None, provider_tenant_name=None, provisioning_state=None, share_description=None, share_kind=None, share_name=None, share_subscription_status=None, share_terms=None, source_share_location=None, system_data=None, type=None, user_email=None, user_name=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if expiration_date and not isinstance(expiration_date, str):
            raise TypeError("Expected argument 'expiration_date' to be a str")
        pulumi.set(__self__, "expiration_date", expiration_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if invitation_id and not isinstance(invitation_id, str):
            raise TypeError("Expected argument 'invitation_id' to be a str")
        pulumi.set(__self__, "invitation_id", invitation_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provider_email and not isinstance(provider_email, str):
            raise TypeError("Expected argument 'provider_email' to be a str")
        pulumi.set(__self__, "provider_email", provider_email)
        if provider_name and not isinstance(provider_name, str):
            raise TypeError("Expected argument 'provider_name' to be a str")
        pulumi.set(__self__, "provider_name", provider_name)
        if provider_tenant_name and not isinstance(provider_tenant_name, str):
            raise TypeError("Expected argument 'provider_tenant_name' to be a str")
        pulumi.set(__self__, "provider_tenant_name", provider_tenant_name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if share_description and not isinstance(share_description, str):
            raise TypeError("Expected argument 'share_description' to be a str")
        pulumi.set(__self__, "share_description", share_description)
        if share_kind and not isinstance(share_kind, str):
            raise TypeError("Expected argument 'share_kind' to be a str")
        pulumi.set(__self__, "share_kind", share_kind)
        if share_name and not isinstance(share_name, str):
            raise TypeError("Expected argument 'share_name' to be a str")
        pulumi.set(__self__, "share_name", share_name)
        if share_subscription_status and not isinstance(share_subscription_status, str):
            raise TypeError("Expected argument 'share_subscription_status' to be a str")
        pulumi.set(__self__, "share_subscription_status", share_subscription_status)
        if share_terms and not isinstance(share_terms, str):
            raise TypeError("Expected argument 'share_terms' to be a str")
        pulumi.set(__self__, "share_terms", share_terms)
        if source_share_location and not isinstance(source_share_location, str):
            raise TypeError("Expected argument 'source_share_location' to be a str")
        pulumi.set(__self__, "source_share_location", source_share_location)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_email and not isinstance(user_email, str):
            raise TypeError("Expected argument 'user_email' to be a str")
        pulumi.set(__self__, "user_email", user_email)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Time at which the share subscription was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[str]:
        """
        The expiration date of the share subscription.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="invitationId")
    def invitation_id(self) -> str:
        """
        The invitation id.
        """
        return pulumi.get(self, "invitation_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerEmail")
    def provider_email(self) -> str:
        """
        Email of the provider who created the resource
        """
        return pulumi.get(self, "provider_email")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> str:
        """
        Name of the provider who created the resource
        """
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter(name="providerTenantName")
    def provider_tenant_name(self) -> str:
        """
        Tenant name of the provider who created the resource
        """
        return pulumi.get(self, "provider_tenant_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the share subscription
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="shareDescription")
    def share_description(self) -> str:
        """
        Description of share
        """
        return pulumi.get(self, "share_description")

    @property
    @pulumi.getter(name="shareKind")
    def share_kind(self) -> str:
        """
        Kind of share
        """
        return pulumi.get(self, "share_kind")

    @property
    @pulumi.getter(name="shareName")
    def share_name(self) -> str:
        """
        Name of the share
        """
        return pulumi.get(self, "share_name")

    @property
    @pulumi.getter(name="shareSubscriptionStatus")
    def share_subscription_status(self) -> str:
        """
        Gets the current status of share subscription.
        """
        return pulumi.get(self, "share_subscription_status")

    @property
    @pulumi.getter(name="shareTerms")
    def share_terms(self) -> str:
        """
        Terms of a share
        """
        return pulumi.get(self, "share_terms")

    @property
    @pulumi.getter(name="sourceShareLocation")
    def source_share_location(self) -> str:
        """
        Source share location.
        """
        return pulumi.get(self, "source_share_location")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> str:
        """
        Email of the user who created the resource
        """
        return pulumi.get(self, "user_email")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        """
        Name of the user who created the resource
        """
        return pulumi.get(self, "user_name")


class AwaitableGetShareSubscriptionResult(GetShareSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetShareSubscriptionResult(
            created_at=self.created_at,
            expiration_date=self.expiration_date,
            id=self.id,
            invitation_id=self.invitation_id,
            name=self.name,
            provider_email=self.provider_email,
            provider_name=self.provider_name,
            provider_tenant_name=self.provider_tenant_name,
            provisioning_state=self.provisioning_state,
            share_description=self.share_description,
            share_kind=self.share_kind,
            share_name=self.share_name,
            share_subscription_status=self.share_subscription_status,
            share_terms=self.share_terms,
            source_share_location=self.source_share_location,
            system_data=self.system_data,
            type=self.type,
            user_email=self.user_email,
            user_name=self.user_name)


def get_share_subscription(account_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           share_subscription_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetShareSubscriptionResult:
    """
    Get a shareSubscription in an account


    :param str account_name: The name of the share account.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the shareSubscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareSubscriptionName'] = share_subscription_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datashare/v20210801:getShareSubscription', __args__, opts=opts, typ=GetShareSubscriptionResult).value

    return AwaitableGetShareSubscriptionResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        expiration_date=pulumi.get(__ret__, 'expiration_date'),
        id=pulumi.get(__ret__, 'id'),
        invitation_id=pulumi.get(__ret__, 'invitation_id'),
        name=pulumi.get(__ret__, 'name'),
        provider_email=pulumi.get(__ret__, 'provider_email'),
        provider_name=pulumi.get(__ret__, 'provider_name'),
        provider_tenant_name=pulumi.get(__ret__, 'provider_tenant_name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        share_description=pulumi.get(__ret__, 'share_description'),
        share_kind=pulumi.get(__ret__, 'share_kind'),
        share_name=pulumi.get(__ret__, 'share_name'),
        share_subscription_status=pulumi.get(__ret__, 'share_subscription_status'),
        share_terms=pulumi.get(__ret__, 'share_terms'),
        source_share_location=pulumi.get(__ret__, 'source_share_location'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        user_email=pulumi.get(__ret__, 'user_email'),
        user_name=pulumi.get(__ret__, 'user_name'))


@_utilities.lift_output_func(get_share_subscription)
def get_share_subscription_output(account_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  share_subscription_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetShareSubscriptionResult]:
    """
    Get a shareSubscription in an account


    :param str account_name: The name of the share account.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the shareSubscription.
    """
    ...
