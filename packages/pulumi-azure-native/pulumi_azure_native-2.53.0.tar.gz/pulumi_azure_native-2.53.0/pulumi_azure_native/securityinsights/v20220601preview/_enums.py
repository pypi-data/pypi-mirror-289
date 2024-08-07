# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EntityTimelineKind',
]


class EntityTimelineKind(str, Enum):
    """
    The entity query kind
    """
    ACTIVITY = "Activity"
    """
    activity
    """
    BOOKMARK = "Bookmark"
    """
    bookmarks
    """
    SECURITY_ALERT = "SecurityAlert"
    """
    security alerts
    """
    ANOMALY = "Anomaly"
    """
    anomaly
    """
