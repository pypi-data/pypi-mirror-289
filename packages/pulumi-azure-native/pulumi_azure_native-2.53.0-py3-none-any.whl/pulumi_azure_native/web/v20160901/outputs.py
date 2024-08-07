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

__all__ = [
    'CapabilityResponse',
    'HostingEnvironmentProfileResponse',
    'SkuCapacityResponse',
    'SkuDescriptionResponse',
]

@pulumi.output_type
class CapabilityResponse(dict):
    """
    Describes the capabilities/features allowed for a specific SKU.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 reason: Optional[str] = None,
                 value: Optional[str] = None):
        """
        Describes the capabilities/features allowed for a specific SKU.
        :param str name: Name of the SKU capability.
        :param str reason: Reason of the SKU capability.
        :param str value: Value of the SKU capability.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if reason is not None:
            pulumi.set(__self__, "reason", reason)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the SKU capability.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def reason(self) -> Optional[str]:
        """
        Reason of the SKU capability.
        """
        return pulumi.get(self, "reason")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Value of the SKU capability.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class HostingEnvironmentProfileResponse(dict):
    """
    Specification for an App Service Environment to use for this resource.
    """
    def __init__(__self__, *,
                 name: str,
                 type: str,
                 id: Optional[str] = None):
        """
        Specification for an App Service Environment to use for this resource.
        :param str name: Name of the App Service Environment.
        :param str type: Resource type of the App Service Environment.
        :param str id: Resource ID of the App Service Environment.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the App Service Environment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type of the App Service Environment.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID of the App Service Environment.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class SkuCapacityResponse(dict):
    """
    Description of the App Service plan scale options.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "scaleType":
            suggest = "scale_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SkuCapacityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SkuCapacityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SkuCapacityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 default: Optional[int] = None,
                 maximum: Optional[int] = None,
                 minimum: Optional[int] = None,
                 scale_type: Optional[str] = None):
        """
        Description of the App Service plan scale options.
        :param int default: Default number of workers for this App Service plan SKU.
        :param int maximum: Maximum number of workers for this App Service plan SKU.
        :param int minimum: Minimum number of workers for this App Service plan SKU.
        :param str scale_type: Available scale configurations for an App Service plan.
        """
        if default is not None:
            pulumi.set(__self__, "default", default)
        if maximum is not None:
            pulumi.set(__self__, "maximum", maximum)
        if minimum is not None:
            pulumi.set(__self__, "minimum", minimum)
        if scale_type is not None:
            pulumi.set(__self__, "scale_type", scale_type)

    @property
    @pulumi.getter
    def default(self) -> Optional[int]:
        """
        Default number of workers for this App Service plan SKU.
        """
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def maximum(self) -> Optional[int]:
        """
        Maximum number of workers for this App Service plan SKU.
        """
        return pulumi.get(self, "maximum")

    @property
    @pulumi.getter
    def minimum(self) -> Optional[int]:
        """
        Minimum number of workers for this App Service plan SKU.
        """
        return pulumi.get(self, "minimum")

    @property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> Optional[str]:
        """
        Available scale configurations for an App Service plan.
        """
        return pulumi.get(self, "scale_type")


@pulumi.output_type
class SkuDescriptionResponse(dict):
    """
    Description of a SKU for a scalable resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "skuCapacity":
            suggest = "sku_capacity"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SkuDescriptionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SkuDescriptionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SkuDescriptionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 capabilities: Optional[Sequence['outputs.CapabilityResponse']] = None,
                 capacity: Optional[int] = None,
                 family: Optional[str] = None,
                 locations: Optional[Sequence[str]] = None,
                 name: Optional[str] = None,
                 size: Optional[str] = None,
                 sku_capacity: Optional['outputs.SkuCapacityResponse'] = None,
                 tier: Optional[str] = None):
        """
        Description of a SKU for a scalable resource.
        :param Sequence['CapabilityResponse'] capabilities: Capabilities of the SKU, e.g., is traffic manager enabled?
        :param int capacity: Current number of instances assigned to the resource.
        :param str family: Family code of the resource SKU.
        :param Sequence[str] locations: Locations of the SKU.
        :param str name: Name of the resource SKU.
        :param str size: Size specifier of the resource SKU.
        :param 'SkuCapacityResponse' sku_capacity: Min, max, and default scale values of the SKU.
        :param str tier: Service tier of the resource SKU.
        """
        if capabilities is not None:
            pulumi.set(__self__, "capabilities", capabilities)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if locations is not None:
            pulumi.set(__self__, "locations", locations)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if sku_capacity is not None:
            pulumi.set(__self__, "sku_capacity", sku_capacity)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence['outputs.CapabilityResponse']]:
        """
        Capabilities of the SKU, e.g., is traffic manager enabled?
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        Current number of instances assigned to the resource.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def family(self) -> Optional[str]:
        """
        Family code of the resource SKU.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[str]]:
        """
        Locations of the SKU.
        """
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the resource SKU.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        Size specifier of the resource SKU.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="skuCapacity")
    def sku_capacity(self) -> Optional['outputs.SkuCapacityResponse']:
        """
        Min, max, and default scale values of the SKU.
        """
        return pulumi.get(self, "sku_capacity")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        Service tier of the resource SKU.
        """
        return pulumi.get(self, "tier")


