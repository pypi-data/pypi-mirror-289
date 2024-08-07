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
    'DatabaseStatisticsResponse',
]

@pulumi.output_type
class DatabaseStatisticsResponse(dict):
    """
    A class that contains database statistics information.
    """
    def __init__(__self__, *,
                 size: Optional[float] = None):
        """
        A class that contains database statistics information.
        :param float size: The database size - the total size of compressed data and index in bytes.
        """
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def size(self) -> Optional[float]:
        """
        The database size - the total size of compressed data and index in bytes.
        """
        return pulumi.get(self, "size")


