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
    'ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesResponseRuleDefinitions',
]

@pulumi.output_type
class ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesResponseRuleDefinitions(dict):
    """
    Static definitions of the ProactiveDetection configuration rule (same values for all components).
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "displayName":
            suggest = "display_name"
        elif key == "helpUrl":
            suggest = "help_url"
        elif key == "isEnabledByDefault":
            suggest = "is_enabled_by_default"
        elif key == "isHidden":
            suggest = "is_hidden"
        elif key == "isInPreview":
            suggest = "is_in_preview"
        elif key == "supportsEmailNotifications":
            suggest = "supports_email_notifications"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesResponseRuleDefinitions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesResponseRuleDefinitions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesResponseRuleDefinitions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: Optional[str] = None,
                 display_name: Optional[str] = None,
                 help_url: Optional[str] = None,
                 is_enabled_by_default: Optional[bool] = None,
                 is_hidden: Optional[bool] = None,
                 is_in_preview: Optional[bool] = None,
                 name: Optional[str] = None,
                 supports_email_notifications: Optional[bool] = None):
        """
        Static definitions of the ProactiveDetection configuration rule (same values for all components).
        :param str description: The rule description
        :param str display_name: The rule name as it is displayed in UI
        :param str help_url: URL which displays additional info about the proactive detection rule
        :param bool is_enabled_by_default: A flag indicating whether the rule is enabled by default
        :param bool is_hidden: A flag indicating whether the rule is hidden (from the UI)
        :param bool is_in_preview: A flag indicating whether the rule is in preview
        :param str name: The rule name
        :param bool supports_email_notifications: A flag indicating whether email notifications are supported for detections for this rule
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if help_url is not None:
            pulumi.set(__self__, "help_url", help_url)
        if is_enabled_by_default is not None:
            pulumi.set(__self__, "is_enabled_by_default", is_enabled_by_default)
        if is_hidden is not None:
            pulumi.set(__self__, "is_hidden", is_hidden)
        if is_in_preview is not None:
            pulumi.set(__self__, "is_in_preview", is_in_preview)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if supports_email_notifications is not None:
            pulumi.set(__self__, "supports_email_notifications", supports_email_notifications)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The rule description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The rule name as it is displayed in UI
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="helpUrl")
    def help_url(self) -> Optional[str]:
        """
        URL which displays additional info about the proactive detection rule
        """
        return pulumi.get(self, "help_url")

    @property
    @pulumi.getter(name="isEnabledByDefault")
    def is_enabled_by_default(self) -> Optional[bool]:
        """
        A flag indicating whether the rule is enabled by default
        """
        return pulumi.get(self, "is_enabled_by_default")

    @property
    @pulumi.getter(name="isHidden")
    def is_hidden(self) -> Optional[bool]:
        """
        A flag indicating whether the rule is hidden (from the UI)
        """
        return pulumi.get(self, "is_hidden")

    @property
    @pulumi.getter(name="isInPreview")
    def is_in_preview(self) -> Optional[bool]:
        """
        A flag indicating whether the rule is in preview
        """
        return pulumi.get(self, "is_in_preview")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The rule name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="supportsEmailNotifications")
    def supports_email_notifications(self) -> Optional[bool]:
        """
        A flag indicating whether email notifications are supported for detections for this rule
        """
        return pulumi.get(self, "supports_email_notifications")


