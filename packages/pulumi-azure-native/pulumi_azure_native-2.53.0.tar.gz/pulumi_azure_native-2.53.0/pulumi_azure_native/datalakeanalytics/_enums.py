# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AADObjectType',
    'FirewallAllowAzureIpsState',
    'FirewallState',
    'TierType',
]


class AADObjectType(str, Enum):
    """
    The type of AAD object the object identifier refers to.
    """
    USER = "User"
    GROUP = "Group"
    SERVICE_PRINCIPAL = "ServicePrincipal"


class FirewallAllowAzureIpsState(str, Enum):
    """
    The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FirewallState(str, Enum):
    """
    The current state of the IP address firewall for this account.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TierType(str, Enum):
    """
    The commitment tier for the next month.
    """
    CONSUMPTION = "Consumption"
    COMMITMENT_100_AU_HOURS = "Commitment_100AUHours"
    COMMITMENT_500_AU_HOURS = "Commitment_500AUHours"
    COMMITMENT_1000_AU_HOURS = "Commitment_1000AUHours"
    COMMITMENT_5000_AU_HOURS = "Commitment_5000AUHours"
    COMMITMENT_10000_AU_HOURS = "Commitment_10000AUHours"
    COMMITMENT_50000_AU_HOURS = "Commitment_50000AUHours"
    COMMITMENT_100000_AU_HOURS = "Commitment_100000AUHours"
    COMMITMENT_500000_AU_HOURS = "Commitment_500000AUHours"
