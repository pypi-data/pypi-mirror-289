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
    'B2CResourceSKUResponse',
    'B2CTenantResourcePropertiesResponseBillingConfig',
]

@pulumi.output_type
class B2CResourceSKUResponse(dict):
    """
    SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling).
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling).
        :param str name: The name of the SKU for the tenant.
        :param str tier: The tier of the tenant.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the SKU for the tenant.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        The tier of the tenant.
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class B2CTenantResourcePropertiesResponseBillingConfig(dict):
    """
    The billing configuration for the tenant.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "effectiveStartDateUtc":
            suggest = "effective_start_date_utc"
        elif key == "billingType":
            suggest = "billing_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in B2CTenantResourcePropertiesResponseBillingConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        B2CTenantResourcePropertiesResponseBillingConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        B2CTenantResourcePropertiesResponseBillingConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 effective_start_date_utc: str,
                 billing_type: Optional[str] = None):
        """
        The billing configuration for the tenant.
        :param str effective_start_date_utc: The data from which the billing type took effect
        :param str billing_type: The type of billing. Will be MAU for all new customers. If 'Auths', it can be updated to 'MAU'. Cannot be changed if value is 'MAU'. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cbilling).
        """
        pulumi.set(__self__, "effective_start_date_utc", effective_start_date_utc)
        if billing_type is not None:
            pulumi.set(__self__, "billing_type", billing_type)

    @property
    @pulumi.getter(name="effectiveStartDateUtc")
    def effective_start_date_utc(self) -> str:
        """
        The data from which the billing type took effect
        """
        return pulumi.get(self, "effective_start_date_utc")

    @property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> Optional[str]:
        """
        The type of billing. Will be MAU for all new customers. If 'Auths', it can be updated to 'MAU'. Cannot be changed if value is 'MAU'. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cbilling).
        """
        return pulumi.get(self, "billing_type")


