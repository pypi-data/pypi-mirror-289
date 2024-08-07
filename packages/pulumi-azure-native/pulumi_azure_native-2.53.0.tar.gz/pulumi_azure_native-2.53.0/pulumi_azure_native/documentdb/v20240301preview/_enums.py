# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CreateMode',
    'NodeKind',
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccess',
]


class CreateMode(str, Enum):
    """
    The mode to create a mongo cluster.
    """
    DEFAULT = "Default"
    """
    Create a new mongo cluster.
    """
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    """
    Create a mongo cluster from a restore point-in-time.
    """


class NodeKind(str, Enum):
    """
    The node type deployed in the node group.
    """
    SHARD = "Shard"
    """
    The node is a shard kind.
    """


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccess(str, Enum):
    """
    Whether or not public endpoint access is allowed for this mongo cluster.
    """
    ENABLED = "Enabled"
    """
    If set, mongo cluster can be accessed through private and public methods.
    """
    DISABLED = "Disabled"
    """
    If set, the private endpoints are the exclusive access method.
    """
