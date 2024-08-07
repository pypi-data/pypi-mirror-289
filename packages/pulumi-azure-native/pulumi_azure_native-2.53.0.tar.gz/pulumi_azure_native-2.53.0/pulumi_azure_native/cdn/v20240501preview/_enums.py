# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AFDEndpointProtocols',
    'AFDRouteGrpcState',
    'ActionType',
    'AfdCertificateType',
    'AfdCipherSuiteSetType',
    'AfdCustomizedCipherSuiteForTls10',
    'AfdCustomizedCipherSuiteForTls12',
    'AfdCustomizedCipherSuiteForTls13',
    'AfdMinimumTlsVersion',
    'AfdQueryStringCachingBehavior',
    'Algorithm',
    'AutoGeneratedDomainNameLabelScope',
    'CacheBehavior',
    'CacheType',
    'ClientPortOperator',
    'CookiesOperator',
    'CustomRuleEnabledState',
    'DeliveryRuleAction',
    'DestinationProtocol',
    'EnabledState',
    'ForwardingProtocol',
    'GeoFilterActions',
    'HeaderAction',
    'HealthProbeRequestType',
    'HostNameOperator',
    'HttpVersionOperator',
    'HttpsRedirect',
    'IsDeviceOperator',
    'LinkToDefaultDomain',
    'ManagedRuleEnabledState',
    'ManagedServiceIdentityType',
    'MatchProcessingBehavior',
    'MatchVariable',
    'Operator',
    'OptimizationType',
    'ParamIndicator',
    'PolicyEnabledState',
    'PolicyMode',
    'PostArgsOperator',
    'ProbeProtocol',
    'ProfileScrubbingState',
    'QueryStringBehavior',
    'QueryStringCachingBehavior',
    'QueryStringOperator',
    'RedirectType',
    'RemoteAddressOperator',
    'RequestBodyOperator',
    'RequestHeaderOperator',
    'RequestMethodOperator',
    'RequestUriOperator',
    'ResponseBasedDetectedErrorTypes',
    'RuleCacheBehavior',
    'RuleIsCompressionEnabled',
    'RuleQueryStringCachingBehavior',
    'ScrubbingRuleEntryMatchOperator',
    'ScrubbingRuleEntryMatchVariable',
    'ScrubbingRuleEntryState',
    'SecretType',
    'SecurityPolicyType',
    'ServerPortOperator',
    'SharedPrivateLinkResourceStatus',
    'SkuName',
    'SocketAddrOperator',
    'SslProtocol',
    'SslProtocolOperator',
    'Transform',
    'TransformType',
    'UrlFileExtensionOperator',
    'UrlFileNameOperator',
    'UrlPathOperator',
    'WafMatchVariable',
]


class AFDEndpointProtocols(str, Enum):
    """
    Supported protocols for the customer's endpoint.
    """
    HTTP = "Http"
    HTTPS = "Https"


class AFDRouteGrpcState(str, Enum):
    """
    Whether or not gRPC is enabled on this route. Permitted values are 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ActionType(str, Enum):
    """
    Describes what action to be applied when rule matches
    """
    ALLOW = "Allow"
    BLOCK = "Block"
    LOG = "Log"
    REDIRECT = "Redirect"


class AfdCertificateType(str, Enum):
    """
    Defines the source of the SSL certificate.
    """
    CUSTOMER_CERTIFICATE = "CustomerCertificate"
    MANAGED_CERTIFICATE = "ManagedCertificate"
    AZURE_FIRST_PARTY_MANAGED_CERTIFICATE = "AzureFirstPartyManagedCertificate"


class AfdCipherSuiteSetType(str, Enum):
    """
    cipher suite set type that will be used for Https
    """
    CUSTOMIZED = "Customized"
    TLS10_2019 = "TLS10_2019"
    TLS12_2022 = "TLS12_2022"
    TLS12_2023 = "TLS12_2023"


class AfdCustomizedCipherSuiteForTls10(str, Enum):
    ECDH_E_RS_A_AES128_SHA = "ECDHE_RSA_AES128_SHA"
    ECDH_E_RS_A_AES256_SHA = "ECDHE_RSA_AES256_SHA"
    AES256_SHA = "AES256_SHA"
    AES128_SHA = "AES128_SHA"


class AfdCustomizedCipherSuiteForTls12(str, Enum):
    ECDH_E_RS_A_AES128_GC_M_SHA256 = "ECDHE_RSA_AES128_GCM_SHA256"
    ECDH_E_RS_A_AES256_GC_M_SHA384 = "ECDHE_RSA_AES256_GCM_SHA384"
    DH_E_RS_A_AES256_GC_M_SHA384 = "DHE_RSA_AES256_GCM_SHA384"
    DH_E_RS_A_AES128_GC_M_SHA256 = "DHE_RSA_AES128_GCM_SHA256"
    ECDH_E_RS_A_AES128_SHA256 = "ECDHE_RSA_AES128_SHA256"
    ECDH_E_RS_A_AES256_SHA384 = "ECDHE_RSA_AES256_SHA384"
    AES256_GC_M_SHA384 = "AES256_GCM_SHA384"
    AES128_GC_M_SHA256 = "AES128_GCM_SHA256"
    AES256_SHA256 = "AES256_SHA256"
    AES128_SHA256 = "AES128_SHA256"


class AfdCustomizedCipherSuiteForTls13(str, Enum):
    TL_S_AE_S_128_GC_M_SHA256 = "TLS_AES_128_GCM_SHA256"
    TL_S_AE_S_256_GC_M_SHA384 = "TLS_AES_256_GCM_SHA384"


class AfdMinimumTlsVersion(str, Enum):
    """
    TLS protocol version that will be used for Https when cipherSuiteSetType is Customized.
    """
    TLS10 = "TLS10"
    TLS12 = "TLS12"
    TLS13 = "TLS13"


class AfdQueryStringCachingBehavior(str, Enum):
    """
    Defines how Frontdoor caches requests that include query strings. You can ignore any query strings when caching, ignore specific query strings, cache every request with a unique URL, or cache specific query strings.
    """
    IGNORE_QUERY_STRING = "IgnoreQueryString"
    USE_QUERY_STRING = "UseQueryString"
    IGNORE_SPECIFIED_QUERY_STRINGS = "IgnoreSpecifiedQueryStrings"
    INCLUDE_SPECIFIED_QUERY_STRINGS = "IncludeSpecifiedQueryStrings"


class Algorithm(str, Enum):
    """
    Algorithm to use for URL signing
    """
    SHA256 = "SHA256"


class AutoGeneratedDomainNameLabelScope(str, Enum):
    """
    Indicates the endpoint name reuse scope. The default value is TenantReuse.
    """
    TENANT_REUSE = "TenantReuse"
    SUBSCRIPTION_REUSE = "SubscriptionReuse"
    RESOURCE_GROUP_REUSE = "ResourceGroupReuse"
    NO_REUSE = "NoReuse"


class CacheBehavior(str, Enum):
    """
    Caching behavior for the requests
    """
    BYPASS_CACHE = "BypassCache"
    OVERRIDE = "Override"
    SET_IF_MISSING = "SetIfMissing"


class CacheType(str, Enum):
    """
    The level at which the content needs to be cached.
    """
    ALL = "All"


class ClientPortOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class CookiesOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class CustomRuleEnabledState(str, Enum):
    """
    Describes if the custom rule is in enabled or disabled state. Defaults to Enabled if not specified.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class DeliveryRuleAction(str, Enum):
    """
    The name of the action for the delivery rule.
    """
    CACHE_EXPIRATION = "CacheExpiration"
    CACHE_KEY_QUERY_STRING = "CacheKeyQueryString"
    MODIFY_REQUEST_HEADER = "ModifyRequestHeader"
    MODIFY_RESPONSE_HEADER = "ModifyResponseHeader"
    URL_REDIRECT = "UrlRedirect"
    URL_REWRITE = "UrlRewrite"
    URL_SIGNING = "UrlSigning"
    ORIGIN_GROUP_OVERRIDE = "OriginGroupOverride"
    ROUTE_CONFIGURATION_OVERRIDE = "RouteConfigurationOverride"
    AFD_URL_SIGNING = "AfdUrlSigning"


class DestinationProtocol(str, Enum):
    """
    Protocol to use for the redirect. The default value is MatchRequest
    """
    MATCH_REQUEST = "MatchRequest"
    HTTP = "Http"
    HTTPS = "Https"


class EnabledState(str, Enum):
    """
    Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ForwardingProtocol(str, Enum):
    """
    Protocol this rule will use when forwarding traffic to backends.
    """
    HTTP_ONLY = "HttpOnly"
    HTTPS_ONLY = "HttpsOnly"
    MATCH_REQUEST = "MatchRequest"


class GeoFilterActions(str, Enum):
    """
    Action of the geo filter, i.e. allow or block access.
    """
    BLOCK = "Block"
    ALLOW = "Allow"


class HeaderAction(str, Enum):
    """
    Action to perform
    """
    APPEND = "Append"
    OVERWRITE = "Overwrite"
    DELETE = "Delete"


class HealthProbeRequestType(str, Enum):
    """
    The type of health probe request that is made.
    """
    NOT_SET = "NotSet"
    GET = "GET"
    HEAD = "HEAD"


class HostNameOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class HttpVersionOperator(str, Enum):
    """
    Describes operator to be matched
    """
    EQUAL = "Equal"


class HttpsRedirect(str, Enum):
    """
    Whether to automatically redirect HTTP traffic to HTTPS traffic. Note that this is a easy way to set up this rule and it will be the first rule that gets executed.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class IsDeviceOperator(str, Enum):
    """
    Describes operator to be matched
    """
    EQUAL = "Equal"


class LinkToDefaultDomain(str, Enum):
    """
    whether this route will be linked to the default endpoint domain.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ManagedRuleEnabledState(str, Enum):
    """
    Describes if the managed rule is in enabled or disabled state. Defaults to Disabled if not specified.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class MatchProcessingBehavior(str, Enum):
    """
    If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue.
    """
    CONTINUE_ = "Continue"
    STOP = "Stop"


class MatchVariable(str, Enum):
    """
    The name of the condition for the delivery rule.
    """
    REMOTE_ADDRESS = "RemoteAddress"
    REQUEST_METHOD = "RequestMethod"
    QUERY_STRING = "QueryString"
    POST_ARGS = "PostArgs"
    REQUEST_URI = "RequestUri"
    REQUEST_HEADER = "RequestHeader"
    REQUEST_BODY = "RequestBody"
    REQUEST_SCHEME = "RequestScheme"
    URL_PATH = "UrlPath"
    URL_FILE_EXTENSION = "UrlFileExtension"
    URL_FILE_NAME = "UrlFileName"
    HTTP_VERSION = "HttpVersion"
    COOKIES = "Cookies"
    IS_DEVICE = "IsDevice"
    SOCKET_ADDR = "SocketAddr"
    CLIENT_PORT = "ClientPort"
    SERVER_PORT = "ServerPort"
    HOST_NAME = "HostName"
    SSL_PROTOCOL = "SslProtocol"


class Operator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    IP_MATCH = "IPMatch"
    GEO_MATCH = "GeoMatch"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    LESS_THAN = "LessThan"
    GREATER_THAN = "GreaterThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    REG_EX = "RegEx"


class OptimizationType(str, Enum):
    """
    Specifies what scenario the customer wants this CDN endpoint to optimize for, e.g. Download, Media services. With this information, CDN can apply scenario driven optimization.
    """
    GENERAL_WEB_DELIVERY = "GeneralWebDelivery"
    GENERAL_MEDIA_STREAMING = "GeneralMediaStreaming"
    VIDEO_ON_DEMAND_MEDIA_STREAMING = "VideoOnDemandMediaStreaming"
    LARGE_FILE_DOWNLOAD = "LargeFileDownload"
    DYNAMIC_SITE_ACCELERATION = "DynamicSiteAcceleration"


class ParamIndicator(str, Enum):
    """
    Indicates the purpose of the parameter
    """
    EXPIRES = "Expires"
    KEY_ID = "KeyId"
    SIGNATURE = "Signature"


class PolicyEnabledState(str, Enum):
    """
    describes if the policy is in enabled state or disabled state
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class PolicyMode(str, Enum):
    """
    Describes if it is in detection mode or prevention mode at policy level.
    """
    PREVENTION = "Prevention"
    DETECTION = "Detection"


class PostArgsOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class ProbeProtocol(str, Enum):
    """
    Protocol to use for health probe.
    """
    NOT_SET = "NotSet"
    HTTP = "Http"
    HTTPS = "Https"


class ProfileScrubbingState(str, Enum):
    """
    State of the log scrubbing config. Default value is Enabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class QueryStringBehavior(str, Enum):
    """
    Caching behavior for the requests
    """
    INCLUDE = "Include"
    INCLUDE_ALL = "IncludeAll"
    EXCLUDE = "Exclude"
    EXCLUDE_ALL = "ExcludeAll"


class QueryStringCachingBehavior(str, Enum):
    """
    Defines how CDN caches requests that include query strings. You can ignore any query strings when caching, bypass caching to prevent requests that contain query strings from being cached, or cache every request with a unique URL.
    """
    IGNORE_QUERY_STRING = "IgnoreQueryString"
    BYPASS_CACHING = "BypassCaching"
    USE_QUERY_STRING = "UseQueryString"
    NOT_SET = "NotSet"


class QueryStringOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class RedirectType(str, Enum):
    """
    The redirect type the rule will use when redirecting traffic.
    """
    MOVED = "Moved"
    FOUND = "Found"
    TEMPORARY_REDIRECT = "TemporaryRedirect"
    PERMANENT_REDIRECT = "PermanentRedirect"


class RemoteAddressOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    IP_MATCH = "IPMatch"
    GEO_MATCH = "GeoMatch"


class RequestBodyOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class RequestHeaderOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class RequestMethodOperator(str, Enum):
    """
    Describes operator to be matched
    """
    EQUAL = "Equal"


class RequestUriOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class ResponseBasedDetectedErrorTypes(str, Enum):
    """
    Type of response errors for real user requests for which origin will be deemed unhealthy
    """
    NONE = "None"
    TCP_ERRORS_ONLY = "TcpErrorsOnly"
    TCP_AND_HTTP_ERRORS = "TcpAndHttpErrors"


class RuleCacheBehavior(str, Enum):
    """
    Caching behavior for the requests
    """
    HONOR_ORIGIN = "HonorOrigin"
    OVERRIDE_ALWAYS = "OverrideAlways"
    OVERRIDE_IF_ORIGIN_MISSING = "OverrideIfOriginMissing"


class RuleIsCompressionEnabled(str, Enum):
    """
    Indicates whether content compression is enabled. If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on AzureFrontDoor when requested content is smaller than 1 byte or larger than 1 MB.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RuleQueryStringCachingBehavior(str, Enum):
    """
    Defines how Frontdoor caches requests that include query strings. You can ignore any query strings when caching, ignore specific query strings, cache every request with a unique URL, or cache specific query strings.
    """
    IGNORE_QUERY_STRING = "IgnoreQueryString"
    USE_QUERY_STRING = "UseQueryString"
    IGNORE_SPECIFIED_QUERY_STRINGS = "IgnoreSpecifiedQueryStrings"
    INCLUDE_SPECIFIED_QUERY_STRINGS = "IncludeSpecifiedQueryStrings"


class ScrubbingRuleEntryMatchOperator(str, Enum):
    """
    When matchVariable is a collection, operate on the selector to specify which elements in the collection this rule applies to.
    """
    EQUALS_ANY = "EqualsAny"


class ScrubbingRuleEntryMatchVariable(str, Enum):
    """
    The variable to be scrubbed from the logs.
    """
    REQUEST_IP_ADDRESS = "RequestIPAddress"
    REQUEST_URI = "RequestUri"
    QUERY_STRING_ARG_NAMES = "QueryStringArgNames"


class ScrubbingRuleEntryState(str, Enum):
    """
    Defines the state of a log scrubbing rule. Default value is enabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SecretType(str, Enum):
    """
    The type of the secret resource.
    """
    URL_SIGNING_KEY = "UrlSigningKey"
    CUSTOMER_CERTIFICATE = "CustomerCertificate"
    MANAGED_CERTIFICATE = "ManagedCertificate"
    AZURE_FIRST_PARTY_MANAGED_CERTIFICATE = "AzureFirstPartyManagedCertificate"
    MTLS_CERTIFICATE_CHAIN = "MtlsCertificateChain"


class SecurityPolicyType(str, Enum):
    """
    The type of the Security policy to create.
    """
    WEB_APPLICATION_FIREWALL = "WebApplicationFirewall"


class ServerPortOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class SharedPrivateLinkResourceStatus(str, Enum):
    """
    Status of the shared private link resource. Can be Pending, Approved, Rejected, Disconnected, or Timeout.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"
    TIMEOUT = "Timeout"


class SkuName(str, Enum):
    """
    Name of the pricing tier.
    """
    STANDARD_VERIZON = "Standard_Verizon"
    PREMIUM_VERIZON = "Premium_Verizon"
    CUSTOM_VERIZON = "Custom_Verizon"
    STANDARD_AKAMAI = "Standard_Akamai"
    STANDARD_CHINA_CDN = "Standard_ChinaCdn"
    STANDARD_MICROSOFT = "Standard_Microsoft"
    STANDARD_AZURE_FRONT_DOOR = "Standard_AzureFrontDoor"
    PREMIUM_AZURE_FRONT_DOOR = "Premium_AzureFrontDoor"
    STANDARD_955_BAND_WIDTH_CHINA_CDN = "Standard_955BandWidth_ChinaCdn"
    STANDARD_AVG_BAND_WIDTH_CHINA_CDN = "Standard_AvgBandWidth_ChinaCdn"
    STANDARD_PLUS_CHINA_CDN = "StandardPlus_ChinaCdn"
    STANDARD_PLUS_955_BAND_WIDTH_CHINA_CDN = "StandardPlus_955BandWidth_ChinaCdn"
    STANDARD_PLUS_AVG_BAND_WIDTH_CHINA_CDN = "StandardPlus_AvgBandWidth_ChinaCdn"


class SocketAddrOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    IP_MATCH = "IPMatch"


class SslProtocol(str, Enum):
    """
    The protocol of an established TLS connection.
    """
    TL_SV1 = "TLSv1"
    TL_SV1_1 = "TLSv1.1"
    TL_SV1_2 = "TLSv1.2"


class SslProtocolOperator(str, Enum):
    """
    Describes operator to be matched
    """
    EQUAL = "Equal"


class Transform(str, Enum):
    """
    Describes what transforms are applied before matching
    """
    LOWERCASE = "Lowercase"
    UPPERCASE = "Uppercase"
    TRIM = "Trim"
    URL_DECODE = "UrlDecode"
    URL_ENCODE = "UrlEncode"
    REMOVE_NULLS = "RemoveNulls"


class TransformType(str, Enum):
    """
    Describes what transforms were applied before matching.
    """
    LOWERCASE = "Lowercase"
    UPPERCASE = "Uppercase"
    TRIM = "Trim"
    URL_DECODE = "UrlDecode"
    URL_ENCODE = "UrlEncode"
    REMOVE_NULLS = "RemoveNulls"


class UrlFileExtensionOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class UrlFileNameOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    REG_EX = "RegEx"


class UrlPathOperator(str, Enum):
    """
    Describes operator to be matched
    """
    ANY = "Any"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    WILDCARD = "Wildcard"
    REG_EX = "RegEx"


class WafMatchVariable(str, Enum):
    """
    Match variable to compare against.
    """
    REMOTE_ADDR = "RemoteAddr"
    SOCKET_ADDR = "SocketAddr"
    REQUEST_METHOD = "RequestMethod"
    REQUEST_HEADER = "RequestHeader"
    REQUEST_URI = "RequestUri"
    QUERY_STRING = "QueryString"
    REQUEST_BODY = "RequestBody"
    COOKIES = "Cookies"
    POST_ARGS = "PostArgs"
