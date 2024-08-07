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
    'ExperimentEndpointResponse',
]

@pulumi.output_type
class ExperimentEndpointResponse(dict):
    """
    Defines the endpoint properties
    """
    def __init__(__self__, *,
                 endpoint: Optional[str] = None,
                 name: Optional[str] = None):
        """
        Defines the endpoint properties
        :param str endpoint: The endpoint URL
        :param str name: The name of the endpoint
        """
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[str]:
        """
        The endpoint URL
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the endpoint
        """
        return pulumi.get(self, "name")


