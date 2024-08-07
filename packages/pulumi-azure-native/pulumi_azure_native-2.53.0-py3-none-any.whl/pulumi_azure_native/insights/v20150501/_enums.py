# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'FavoriteType',
    'ItemScope',
    'ItemType',
    'SharedTypeKind',
]


class FavoriteType(str, Enum):
    """
    Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    """
    SHARED = "shared"
    USER = "user"


class ItemScope(str, Enum):
    """
    Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    """
    SHARED = "shared"
    USER = "user"


class ItemType(str, Enum):
    """
    Enum indicating the type of the Analytics item.
    """
    NONE = "none"
    QUERY = "query"
    RECENT = "recent"
    FUNCTION = "function"


class SharedTypeKind(str, Enum):
    """
    Enum indicating if this workbook definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    """
    SHARED = "shared"
    USER = "user"
