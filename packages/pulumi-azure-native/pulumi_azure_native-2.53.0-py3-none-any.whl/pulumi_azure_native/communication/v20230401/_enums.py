# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DomainManagement',
    'ManagedServiceIdentityType',
    'UserEngagementTracking',
]


class DomainManagement(str, Enum):
    """
    Describes how a Domains resource is being managed.
    """
    AZURE_MANAGED = "AzureManaged"
    CUSTOMER_MANAGED = "CustomerManaged"
    CUSTOMER_MANAGED_IN_EXCHANGE_ONLINE = "CustomerManagedInExchangeOnline"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class UserEngagementTracking(str, Enum):
    """
    Describes whether user engagement tracking is enabled or disabled.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"
