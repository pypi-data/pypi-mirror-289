# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EntityTimelineKind',
    'SettingKind',
    'SourceType',
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


class SettingKind(str, Enum):
    """
    The kind of the setting
    """
    ANOMALIES = "Anomalies"
    EYES_ON = "EyesOn"
    ENTITY_ANALYTICS = "EntityAnalytics"
    UEBA = "Ueba"


class SourceType(str, Enum):
    """
    The sourceType of the watchlist
    """
    LOCAL_FILE = "Local file"
    REMOTE_STORAGE = "Remote storage"
