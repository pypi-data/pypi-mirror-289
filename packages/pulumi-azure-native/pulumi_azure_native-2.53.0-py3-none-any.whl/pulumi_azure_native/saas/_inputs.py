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
from ._enums import *

__all__ = [
    'SaasCreationPropertiesArgs',
    'SaasCreationPropertiesArgsDict',
]

MYPY = False

if not MYPY:
    class SaasCreationPropertiesArgsDict(TypedDict):
        """
        properties for creation saas
        """
        auto_renew: NotRequired[pulumi.Input[bool]]
        """
        Whether the SaaS subscription will auto renew upon term end.
        """
        offer_id: NotRequired[pulumi.Input[str]]
        """
        The offer id.
        """
        payment_channel_metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[str]]]]
        """
        The metadata about the SaaS subscription such as the AzureSubscriptionId and ResourceUri.
        """
        payment_channel_type: NotRequired[pulumi.Input[Union[str, 'PaymentChannelType']]]
        """
        The Payment channel for the SaasSubscription.
        """
        publisher_id: NotRequired[pulumi.Input[str]]
        """
        The publisher id.
        """
        publisher_test_environment: NotRequired[pulumi.Input[str]]
        """
        The environment in the publisher side for this resource.
        """
        quantity: NotRequired[pulumi.Input[float]]
        """
        The seat count.
        """
        saas_resource_name: NotRequired[pulumi.Input[str]]
        """
        The SaaS resource name.
        """
        saas_session_id: NotRequired[pulumi.Input[str]]
        """
        The saas session id used for dev service migration request.
        """
        saas_subscription_id: NotRequired[pulumi.Input[str]]
        """
        The saas subscription id used for tenant to subscription level migration request.
        """
        sku_id: NotRequired[pulumi.Input[str]]
        """
        The plan id.
        """
        term_id: NotRequired[pulumi.Input[str]]
        """
        The current Term id.
        """
elif False:
    SaasCreationPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SaasCreationPropertiesArgs:
    def __init__(__self__, *,
                 auto_renew: Optional[pulumi.Input[bool]] = None,
                 offer_id: Optional[pulumi.Input[str]] = None,
                 payment_channel_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 payment_channel_type: Optional[pulumi.Input[Union[str, 'PaymentChannelType']]] = None,
                 publisher_id: Optional[pulumi.Input[str]] = None,
                 publisher_test_environment: Optional[pulumi.Input[str]] = None,
                 quantity: Optional[pulumi.Input[float]] = None,
                 saas_resource_name: Optional[pulumi.Input[str]] = None,
                 saas_session_id: Optional[pulumi.Input[str]] = None,
                 saas_subscription_id: Optional[pulumi.Input[str]] = None,
                 sku_id: Optional[pulumi.Input[str]] = None,
                 term_id: Optional[pulumi.Input[str]] = None):
        """
        properties for creation saas
        :param pulumi.Input[bool] auto_renew: Whether the SaaS subscription will auto renew upon term end.
        :param pulumi.Input[str] offer_id: The offer id.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] payment_channel_metadata: The metadata about the SaaS subscription such as the AzureSubscriptionId and ResourceUri.
        :param pulumi.Input[Union[str, 'PaymentChannelType']] payment_channel_type: The Payment channel for the SaasSubscription.
        :param pulumi.Input[str] publisher_id: The publisher id.
        :param pulumi.Input[str] publisher_test_environment: The environment in the publisher side for this resource.
        :param pulumi.Input[float] quantity: The seat count.
        :param pulumi.Input[str] saas_resource_name: The SaaS resource name.
        :param pulumi.Input[str] saas_session_id: The saas session id used for dev service migration request.
        :param pulumi.Input[str] saas_subscription_id: The saas subscription id used for tenant to subscription level migration request.
        :param pulumi.Input[str] sku_id: The plan id.
        :param pulumi.Input[str] term_id: The current Term id.
        """
        if auto_renew is not None:
            pulumi.set(__self__, "auto_renew", auto_renew)
        if offer_id is not None:
            pulumi.set(__self__, "offer_id", offer_id)
        if payment_channel_metadata is not None:
            pulumi.set(__self__, "payment_channel_metadata", payment_channel_metadata)
        if payment_channel_type is not None:
            pulumi.set(__self__, "payment_channel_type", payment_channel_type)
        if publisher_id is not None:
            pulumi.set(__self__, "publisher_id", publisher_id)
        if publisher_test_environment is not None:
            pulumi.set(__self__, "publisher_test_environment", publisher_test_environment)
        if quantity is not None:
            pulumi.set(__self__, "quantity", quantity)
        if saas_resource_name is not None:
            pulumi.set(__self__, "saas_resource_name", saas_resource_name)
        if saas_session_id is not None:
            pulumi.set(__self__, "saas_session_id", saas_session_id)
        if saas_subscription_id is not None:
            pulumi.set(__self__, "saas_subscription_id", saas_subscription_id)
        if sku_id is not None:
            pulumi.set(__self__, "sku_id", sku_id)
        if term_id is not None:
            pulumi.set(__self__, "term_id", term_id)

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the SaaS subscription will auto renew upon term end.
        """
        return pulumi.get(self, "auto_renew")

    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_renew", value)

    @property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> Optional[pulumi.Input[str]]:
        """
        The offer id.
        """
        return pulumi.get(self, "offer_id")

    @offer_id.setter
    def offer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "offer_id", value)

    @property
    @pulumi.getter(name="paymentChannelMetadata")
    def payment_channel_metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The metadata about the SaaS subscription such as the AzureSubscriptionId and ResourceUri.
        """
        return pulumi.get(self, "payment_channel_metadata")

    @payment_channel_metadata.setter
    def payment_channel_metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "payment_channel_metadata", value)

    @property
    @pulumi.getter(name="paymentChannelType")
    def payment_channel_type(self) -> Optional[pulumi.Input[Union[str, 'PaymentChannelType']]]:
        """
        The Payment channel for the SaasSubscription.
        """
        return pulumi.get(self, "payment_channel_type")

    @payment_channel_type.setter
    def payment_channel_type(self, value: Optional[pulumi.Input[Union[str, 'PaymentChannelType']]]):
        pulumi.set(self, "payment_channel_type", value)

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> Optional[pulumi.Input[str]]:
        """
        The publisher id.
        """
        return pulumi.get(self, "publisher_id")

    @publisher_id.setter
    def publisher_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "publisher_id", value)

    @property
    @pulumi.getter(name="publisherTestEnvironment")
    def publisher_test_environment(self) -> Optional[pulumi.Input[str]]:
        """
        The environment in the publisher side for this resource.
        """
        return pulumi.get(self, "publisher_test_environment")

    @publisher_test_environment.setter
    def publisher_test_environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "publisher_test_environment", value)

    @property
    @pulumi.getter
    def quantity(self) -> Optional[pulumi.Input[float]]:
        """
        The seat count.
        """
        return pulumi.get(self, "quantity")

    @quantity.setter
    def quantity(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "quantity", value)

    @property
    @pulumi.getter(name="saasResourceName")
    def saas_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The SaaS resource name.
        """
        return pulumi.get(self, "saas_resource_name")

    @saas_resource_name.setter
    def saas_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "saas_resource_name", value)

    @property
    @pulumi.getter(name="saasSessionId")
    def saas_session_id(self) -> Optional[pulumi.Input[str]]:
        """
        The saas session id used for dev service migration request.
        """
        return pulumi.get(self, "saas_session_id")

    @saas_session_id.setter
    def saas_session_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "saas_session_id", value)

    @property
    @pulumi.getter(name="saasSubscriptionId")
    def saas_subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The saas subscription id used for tenant to subscription level migration request.
        """
        return pulumi.get(self, "saas_subscription_id")

    @saas_subscription_id.setter
    def saas_subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "saas_subscription_id", value)

    @property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[pulumi.Input[str]]:
        """
        The plan id.
        """
        return pulumi.get(self, "sku_id")

    @sku_id.setter
    def sku_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku_id", value)

    @property
    @pulumi.getter(name="termId")
    def term_id(self) -> Optional[pulumi.Input[str]]:
        """
        The current Term id.
        """
        return pulumi.get(self, "term_id")

    @term_id.setter
    def term_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "term_id", value)


