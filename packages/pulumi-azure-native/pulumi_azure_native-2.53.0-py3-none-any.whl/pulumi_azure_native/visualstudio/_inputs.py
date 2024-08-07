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
    'ExtensionResourcePlanArgs',
    'ExtensionResourcePlanArgsDict',
]

MYPY = False

if not MYPY:
    class ExtensionResourcePlanArgsDict(TypedDict):
        """
        Plan data for an extension resource.
        """
        name: NotRequired[pulumi.Input[str]]
        """
        Name of the plan.
        """
        product: NotRequired[pulumi.Input[str]]
        """
        Product name.
        """
        promotion_code: NotRequired[pulumi.Input[str]]
        """
        Optional: the promotion code associated with the plan.
        """
        publisher: NotRequired[pulumi.Input[str]]
        """
        Name of the extension publisher.
        """
        version: NotRequired[pulumi.Input[str]]
        """
        A string that uniquely identifies the plan version.
        """
elif False:
    ExtensionResourcePlanArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ExtensionResourcePlanArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 product: Optional[pulumi.Input[str]] = None,
                 promotion_code: Optional[pulumi.Input[str]] = None,
                 publisher: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Plan data for an extension resource.
        :param pulumi.Input[str] name: Name of the plan.
        :param pulumi.Input[str] product: Product name.
        :param pulumi.Input[str] promotion_code: Optional: the promotion code associated with the plan.
        :param pulumi.Input[str] publisher: Name of the extension publisher.
        :param pulumi.Input[str] version: A string that uniquely identifies the plan version.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if product is not None:
            pulumi.set(__self__, "product", product)
        if promotion_code is not None:
            pulumi.set(__self__, "promotion_code", promotion_code)
        if publisher is not None:
            pulumi.set(__self__, "publisher", publisher)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the plan.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def product(self) -> Optional[pulumi.Input[str]]:
        """
        Product name.
        """
        return pulumi.get(self, "product")

    @product.setter
    def product(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product", value)

    @property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[str]]:
        """
        Optional: the promotion code associated with the plan.
        """
        return pulumi.get(self, "promotion_code")

    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "promotion_code", value)

    @property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the extension publisher.
        """
        return pulumi.get(self, "publisher")

    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "publisher", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        A string that uniquely identifies the plan version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


