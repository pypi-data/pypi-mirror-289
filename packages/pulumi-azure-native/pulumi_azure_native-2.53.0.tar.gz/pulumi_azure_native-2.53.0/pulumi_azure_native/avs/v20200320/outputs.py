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
    'SkuResponse',
]

@pulumi.output_type
class SkuResponse(dict):
    """
    The resource model definition representing SKU
    """
    def __init__(__self__, *,
                 name: str):
        """
        The resource model definition representing SKU
        :param str name: The name of the SKU.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU.
        """
        return pulumi.get(self, "name")


