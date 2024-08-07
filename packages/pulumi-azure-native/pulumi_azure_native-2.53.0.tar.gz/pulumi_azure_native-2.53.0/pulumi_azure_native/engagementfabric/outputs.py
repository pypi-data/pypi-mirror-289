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

__all__ = [
    'ChannelTypeDescriptionResponse',
    'KeyDescriptionResponse',
    'SKUResponse',
]

@pulumi.output_type
class ChannelTypeDescriptionResponse(dict):
    """
    EngagementFabric channel description
    """
    def __init__(__self__, *,
                 channel_description: Optional[str] = None,
                 channel_functions: Optional[Sequence[str]] = None,
                 channel_type: Optional[str] = None):
        """
        EngagementFabric channel description
        :param str channel_description: Text description for the channel
        :param Sequence[str] channel_functions: All the available functions for the channel
        :param str channel_type: Channel type
        """
        if channel_description is not None:
            pulumi.set(__self__, "channel_description", channel_description)
        if channel_functions is not None:
            pulumi.set(__self__, "channel_functions", channel_functions)
        if channel_type is not None:
            pulumi.set(__self__, "channel_type", channel_type)

    @property
    @pulumi.getter(name="channelDescription")
    def channel_description(self) -> Optional[str]:
        """
        Text description for the channel
        """
        return pulumi.get(self, "channel_description")

    @property
    @pulumi.getter(name="channelFunctions")
    def channel_functions(self) -> Optional[Sequence[str]]:
        """
        All the available functions for the channel
        """
        return pulumi.get(self, "channel_functions")

    @property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[str]:
        """
        Channel type
        """
        return pulumi.get(self, "channel_type")


@pulumi.output_type
class KeyDescriptionResponse(dict):
    """
    The description of the EngagementFabric account key
    """
    def __init__(__self__, *,
                 name: str,
                 rank: str,
                 value: str):
        """
        The description of the EngagementFabric account key
        :param str name: The name of the key
        :param str rank: The rank of the key
        :param str value: The value of the key
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "rank", rank)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the key
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rank(self) -> str:
        """
        The rank of the key
        """
        return pulumi.get(self, "rank")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the key
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class SKUResponse(dict):
    """
    The EngagementFabric SKU
    """
    def __init__(__self__, *,
                 name: str,
                 tier: Optional[str] = None):
        """
        The EngagementFabric SKU
        :param str name: The name of the SKU
        :param str tier: The price tier of the SKU
        """
        pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        The price tier of the SKU
        """
        return pulumi.get(self, "tier")


