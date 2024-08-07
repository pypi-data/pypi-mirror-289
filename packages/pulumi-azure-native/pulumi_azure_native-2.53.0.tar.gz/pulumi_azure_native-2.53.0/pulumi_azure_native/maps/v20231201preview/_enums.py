# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'InfrastructureEncryption',
    'Kind',
    'ManagedServiceIdentityType',
    'Name',
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccess',
    'SigningKey',
]


class InfrastructureEncryption(str, Enum):
    """
    (Optional) Discouraged to include in resource definition. Only needed where it is possible to disable platform (AKA infrastructure) encryption. Azure SQL TDE is an example of this. Values are enabled and disabled.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class Kind(str, Enum):
    """
    Get or Set Kind property.
    """
    GEN2 = "Gen2"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class Name(str, Enum):
    """
    The name of the SKU, in standard format (such as G2).
    """
    G2 = "G2"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccess(str, Enum):
    """
    Property to specify whether the Maps Account will accept traffic from public internet. If set to 'disabled' all traffic except private endpoint traffic and that that originates from trusted services will be blocked.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class SigningKey(str, Enum):
    """
    The Maps account key to use for signing. Picking `primaryKey` or `secondaryKey` will use the Maps account Shared Keys, and using `managedIdentity` will use the auto-renewed private key to sign the SAS.
    """
    PRIMARY_KEY = "primaryKey"
    SECONDARY_KEY = "secondaryKey"
    MANAGED_IDENTITY = "managedIdentity"
