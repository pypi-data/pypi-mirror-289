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
    'SubscriptionFeatureRegistrationPropertiesArgs',
    'SubscriptionFeatureRegistrationPropertiesArgsDict',
]

MYPY = False

if not MYPY:
    class SubscriptionFeatureRegistrationPropertiesArgsDict(TypedDict):
        description: NotRequired[pulumi.Input[str]]
        """
        The feature description.
        """
        metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[str]]]]
        """
        Key-value pairs for meta data.
        """
        should_feature_display_in_portal: NotRequired[pulumi.Input[bool]]
        """
        Indicates whether feature should be displayed in Portal.
        """
        state: NotRequired[pulumi.Input[Union[str, 'SubscriptionFeatureRegistrationState']]]
        """
        The state.
        """
elif False:
    SubscriptionFeatureRegistrationPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SubscriptionFeatureRegistrationPropertiesArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 should_feature_display_in_portal: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input[Union[str, 'SubscriptionFeatureRegistrationState']]] = None):
        """
        :param pulumi.Input[str] description: The feature description.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Key-value pairs for meta data.
        :param pulumi.Input[bool] should_feature_display_in_portal: Indicates whether feature should be displayed in Portal.
        :param pulumi.Input[Union[str, 'SubscriptionFeatureRegistrationState']] state: The state.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if should_feature_display_in_portal is None:
            should_feature_display_in_portal = False
        if should_feature_display_in_portal is not None:
            pulumi.set(__self__, "should_feature_display_in_portal", should_feature_display_in_portal)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The feature description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value pairs for meta data.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="shouldFeatureDisplayInPortal")
    def should_feature_display_in_portal(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether feature should be displayed in Portal.
        """
        return pulumi.get(self, "should_feature_display_in_portal")

    @should_feature_display_in_portal.setter
    def should_feature_display_in_portal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "should_feature_display_in_portal", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'SubscriptionFeatureRegistrationState']]]:
        """
        The state.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'SubscriptionFeatureRegistrationState']]]):
        pulumi.set(self, "state", value)


