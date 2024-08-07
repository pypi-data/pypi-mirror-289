# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ManagedIdentityTypes',
    'MonitoringStatus',
]


class ManagedIdentityTypes(str, Enum):
    """
    Specifies the identity type of the Datadog Monitor. At this time the only allowed value is 'SystemAssigned'.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class MonitoringStatus(str, Enum):
    """
    Flag specifying if the resource monitoring is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
