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
from ._enums import *

__all__ = [
    'PutAliasRequestAdditionalPropertiesArgs',
    'PutAliasRequestAdditionalPropertiesArgsDict',
    'PutAliasRequestPropertiesArgs',
    'PutAliasRequestPropertiesArgsDict',
]

MYPY = False

if not MYPY:
    class PutAliasRequestAdditionalPropertiesArgsDict(TypedDict):
        """
        Put subscription additional properties.
        """
        management_group_id: NotRequired[pulumi.Input[str]]
        """
        Management group Id for the subscription.
        """
        subscription_owner_id: NotRequired[pulumi.Input[str]]
        """
        Owner Id of the subscription
        """
        subscription_tenant_id: NotRequired[pulumi.Input[str]]
        """
        Tenant Id of the subscription
        """
        tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[str]]]]
        """
        Tags for the subscription
        """
elif False:
    PutAliasRequestAdditionalPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PutAliasRequestAdditionalPropertiesArgs:
    def __init__(__self__, *,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 subscription_owner_id: Optional[pulumi.Input[str]] = None,
                 subscription_tenant_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Put subscription additional properties.
        :param pulumi.Input[str] management_group_id: Management group Id for the subscription.
        :param pulumi.Input[str] subscription_owner_id: Owner Id of the subscription
        :param pulumi.Input[str] subscription_tenant_id: Tenant Id of the subscription
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags for the subscription
        """
        if management_group_id is not None:
            pulumi.set(__self__, "management_group_id", management_group_id)
        if subscription_owner_id is not None:
            pulumi.set(__self__, "subscription_owner_id", subscription_owner_id)
        if subscription_tenant_id is not None:
            pulumi.set(__self__, "subscription_tenant_id", subscription_tenant_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Management group Id for the subscription.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_group_id", value)

    @property
    @pulumi.getter(name="subscriptionOwnerId")
    def subscription_owner_id(self) -> Optional[pulumi.Input[str]]:
        """
        Owner Id of the subscription
        """
        return pulumi.get(self, "subscription_owner_id")

    @subscription_owner_id.setter
    def subscription_owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_owner_id", value)

    @property
    @pulumi.getter(name="subscriptionTenantId")
    def subscription_tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Tenant Id of the subscription
        """
        return pulumi.get(self, "subscription_tenant_id")

    @subscription_tenant_id.setter
    def subscription_tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_tenant_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags for the subscription
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


if not MYPY:
    class PutAliasRequestPropertiesArgsDict(TypedDict):
        """
        Put subscription properties.
        """
        additional_properties: NotRequired[pulumi.Input['PutAliasRequestAdditionalPropertiesArgsDict']]
        """
        Put alias request additional properties.
        """
        billing_scope: NotRequired[pulumi.Input[str]]
        """
        Billing scope of the subscription.
        For CustomerLed and FieldLed - /billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}
        For PartnerLed - /billingAccounts/{billingAccountName}/customers/{customerName}
        For Legacy EA - /billingAccounts/{billingAccountName}/enrollmentAccounts/{enrollmentAccountName}
        """
        display_name: NotRequired[pulumi.Input[str]]
        """
        The friendly name of the subscription.
        """
        reseller_id: NotRequired[pulumi.Input[str]]
        """
        Reseller Id
        """
        subscription_id: NotRequired[pulumi.Input[str]]
        """
        This parameter can be used to create alias for existing subscription Id
        """
        workload: NotRequired[pulumi.Input[Union[str, 'Workload']]]
        """
        The workload type of the subscription. It can be either Production or DevTest.
        """
elif False:
    PutAliasRequestPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PutAliasRequestPropertiesArgs:
    def __init__(__self__, *,
                 additional_properties: Optional[pulumi.Input['PutAliasRequestAdditionalPropertiesArgs']] = None,
                 billing_scope: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 reseller_id: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 workload: Optional[pulumi.Input[Union[str, 'Workload']]] = None):
        """
        Put subscription properties.
        :param pulumi.Input['PutAliasRequestAdditionalPropertiesArgs'] additional_properties: Put alias request additional properties.
        :param pulumi.Input[str] billing_scope: Billing scope of the subscription.
               For CustomerLed and FieldLed - /billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}
               For PartnerLed - /billingAccounts/{billingAccountName}/customers/{customerName}
               For Legacy EA - /billingAccounts/{billingAccountName}/enrollmentAccounts/{enrollmentAccountName}
        :param pulumi.Input[str] display_name: The friendly name of the subscription.
        :param pulumi.Input[str] reseller_id: Reseller Id
        :param pulumi.Input[str] subscription_id: This parameter can be used to create alias for existing subscription Id
        :param pulumi.Input[Union[str, 'Workload']] workload: The workload type of the subscription. It can be either Production or DevTest.
        """
        if additional_properties is not None:
            pulumi.set(__self__, "additional_properties", additional_properties)
        if billing_scope is not None:
            pulumi.set(__self__, "billing_scope", billing_scope)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if reseller_id is not None:
            pulumi.set(__self__, "reseller_id", reseller_id)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if workload is not None:
            pulumi.set(__self__, "workload", workload)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input['PutAliasRequestAdditionalPropertiesArgs']]:
        """
        Put alias request additional properties.
        """
        return pulumi.get(self, "additional_properties")

    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input['PutAliasRequestAdditionalPropertiesArgs']]):
        pulumi.set(self, "additional_properties", value)

    @property
    @pulumi.getter(name="billingScope")
    def billing_scope(self) -> Optional[pulumi.Input[str]]:
        """
        Billing scope of the subscription.
        For CustomerLed and FieldLed - /billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}
        For PartnerLed - /billingAccounts/{billingAccountName}/customers/{customerName}
        For Legacy EA - /billingAccounts/{billingAccountName}/enrollmentAccounts/{enrollmentAccountName}
        """
        return pulumi.get(self, "billing_scope")

    @billing_scope.setter
    def billing_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_scope", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The friendly name of the subscription.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="resellerId")
    def reseller_id(self) -> Optional[pulumi.Input[str]]:
        """
        Reseller Id
        """
        return pulumi.get(self, "reseller_id")

    @reseller_id.setter
    def reseller_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reseller_id", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        This parameter can be used to create alias for existing subscription Id
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter
    def workload(self) -> Optional[pulumi.Input[Union[str, 'Workload']]]:
        """
        The workload type of the subscription. It can be either Production or DevTest.
        """
        return pulumi.get(self, "workload")

    @workload.setter
    def workload(self, value: Optional[pulumi.Input[Union[str, 'Workload']]]):
        pulumi.set(self, "workload", value)


