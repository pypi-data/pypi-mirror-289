# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApiBridgeActivationState',
    'AutoGeneratedDomainNameLabelScope',
    'CommunicationsPlatform',
    'Connectivity',
    'E911Type',
    'ManagedServiceIdentityType',
    'SkuTier',
    'TeamsCodecs',
    'TestLinePurpose',
]


class ApiBridgeActivationState(str, Enum):
    """
    The activation state of the API Bridge for this Communications Gateway
    """
    ENABLED = "enabled"
    """
    API Bridge is enabled
    """
    DISABLED = "disabled"
    """
    API Bridge is disabled
    """


class AutoGeneratedDomainNameLabelScope(str, Enum):
    """
    The scope at which the auto-generated domain name can be re-used
    """
    TENANT_REUSE = "TenantReuse"
    """
    Generated domain name label depends on resource name and tenant ID.
    """
    SUBSCRIPTION_REUSE = "SubscriptionReuse"
    """
    Generated domain name label depends on resource name, tenant ID and subscription ID.
    """
    RESOURCE_GROUP_REUSE = "ResourceGroupReuse"
    """
    Generated domain name label depends on resource name, tenant ID, subscription ID and resource group name.
    """
    NO_REUSE = "NoReuse"
    """
    Generated domain name label is always unique.
    """


class CommunicationsPlatform(str, Enum):
    """
    Available platform types.
    """
    OPERATOR_CONNECT = "OperatorConnect"
    """
    Operator Connect
    """
    TEAMS_PHONE_MOBILE = "TeamsPhoneMobile"
    """
    Teams Phone Mobile
    """
    TEAMS_DIRECT_ROUTING = "TeamsDirectRouting"
    """
    Teams Direct Routing
    """


class Connectivity(str, Enum):
    """
    How to connect back to the operator network, e.g. MAPS
    """
    PUBLIC_ADDRESS = "PublicAddress"
    """
    This deployment connects to the operator network using a Public IP address, e.g. when using MAPS
    """


class E911Type(str, Enum):
    """
    How to handle 911 calls
    """
    STANDARD = "Standard"
    """
    Emergency calls are not handled different from other calls
    """
    DIRECT_TO_ESRP = "DirectToEsrp"
    """
    Emergency calls are routed directly to the ESRP
    """


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class SkuTier(str, Enum):
    """
    This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
    """
    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class TeamsCodecs(str, Enum):
    """
    The voice codecs expected for communication with Teams.
    """
    PCMA = "PCMA"
    """
    Pulse code modulation(PCM) U-law narrowband audio codec(G.711u)
    """
    PCMU = "PCMU"
    """
    Pulse code modulation(PCM) U-law narrowband audio codec(G.711u)
    """
    G722 = "G722"
    """
    G.722 wideband audio codec
    """
    G722_2 = "G722_2"
    """
    G.722.2 wideband audio codec
    """
    SIL_K_8 = "SILK_8"
    """
    SILK/8000 narrowband audio codec
    """
    SIL_K_16 = "SILK_16"
    """
    SILK/16000 wideband audio codec
    """


class TestLinePurpose(str, Enum):
    """
    Purpose of this test line, e.g. automated or manual testing
    """
    MANUAL = "Manual"
    """
    The test line is used for manual testing
    """
    AUTOMATED = "Automated"
    """
    The test line is used for automated testing
    """
