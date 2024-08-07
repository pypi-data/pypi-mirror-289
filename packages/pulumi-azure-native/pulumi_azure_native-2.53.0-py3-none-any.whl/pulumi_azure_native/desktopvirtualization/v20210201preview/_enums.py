# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'HostPoolType',
    'ResourceIdentityType',
    'SessionHostLoadBalancingAlgorithm',
    'SkuTier',
    'StopHostsWhen',
]


class HostPoolType(str, Enum):
    """
    HostPool type for desktop.
    """
    PERSONAL = "Personal"
    """
    Users will be assigned a SessionHost either by administrators (PersonalDesktopAssignmentType = Direct) or upon connecting to the pool (PersonalDesktopAssignmentType = Automatic). They will always be redirected to their assigned SessionHost.
    """
    POOLED = "Pooled"
    """
    Users get a new (random) SessionHost every time it connects to the HostPool.
    """
    BYO_DESKTOP = "BYODesktop"
    """
    Users assign their own machines, load balancing logic remains the same as Personal. PersonalDesktopAssignmentType must be Direct.
    """


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"


class SessionHostLoadBalancingAlgorithm(str, Enum):
    """
    Load balancing algorithm for ramp up period.
    """
    BREADTH_FIRST = "BreadthFirst"
    DEPTH_FIRST = "DepthFirst"


class SkuTier(str, Enum):
    """
    This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
    """
    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class StopHostsWhen(str, Enum):
    """
    Specifies when to stop hosts during ramp down period.
    """
    ZERO_SESSIONS = "ZeroSessions"
    ZERO_ACTIVE_SESSIONS = "ZeroActiveSessions"
