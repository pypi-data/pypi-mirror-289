# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from ... import _utilities
from ._enums import *

__all__ = [
    'BgpSessionArgs',
    'BgpSessionArgsDict',
    'ContactDetailArgs',
    'ContactDetailArgsDict',
    'DirectConnectionArgs',
    'DirectConnectionArgsDict',
    'ExchangeConnectionArgs',
    'ExchangeConnectionArgsDict',
    'PeeringPropertiesDirectArgs',
    'PeeringPropertiesDirectArgsDict',
    'PeeringPropertiesExchangeArgs',
    'PeeringPropertiesExchangeArgsDict',
    'PeeringServiceSkuArgs',
    'PeeringServiceSkuArgsDict',
    'PeeringSkuArgs',
    'PeeringSkuArgsDict',
    'SubResourceArgs',
    'SubResourceArgsDict',
]

MYPY = False

if not MYPY:
    class BgpSessionArgsDict(TypedDict):
        """
        The properties that define a BGP session.
        """
        max_prefixes_advertised_v4: NotRequired[pulumi.Input[int]]
        """
        The maximum number of prefixes advertised over the IPv4 session.
        """
        max_prefixes_advertised_v6: NotRequired[pulumi.Input[int]]
        """
        The maximum number of prefixes advertised over the IPv6 session.
        """
        md5_authentication_key: NotRequired[pulumi.Input[str]]
        """
        The MD5 authentication key of the session.
        """
        microsoft_session_i_pv4_address: NotRequired[pulumi.Input[str]]
        """
        The IPv4 session address on Microsoft's end.
        """
        microsoft_session_i_pv6_address: NotRequired[pulumi.Input[str]]
        """
        The IPv6 session address on Microsoft's end.
        """
        peer_session_i_pv4_address: NotRequired[pulumi.Input[str]]
        """
        The IPv4 session address on peer's end.
        """
        peer_session_i_pv6_address: NotRequired[pulumi.Input[str]]
        """
        The IPv6 session address on peer's end.
        """
        session_prefix_v4: NotRequired[pulumi.Input[str]]
        """
        The IPv4 prefix that contains both ends' IPv4 addresses.
        """
        session_prefix_v6: NotRequired[pulumi.Input[str]]
        """
        The IPv6 prefix that contains both ends' IPv6 addresses.
        """
elif False:
    BgpSessionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class BgpSessionArgs:
    def __init__(__self__, *,
                 max_prefixes_advertised_v4: Optional[pulumi.Input[int]] = None,
                 max_prefixes_advertised_v6: Optional[pulumi.Input[int]] = None,
                 md5_authentication_key: Optional[pulumi.Input[str]] = None,
                 microsoft_session_i_pv4_address: Optional[pulumi.Input[str]] = None,
                 microsoft_session_i_pv6_address: Optional[pulumi.Input[str]] = None,
                 peer_session_i_pv4_address: Optional[pulumi.Input[str]] = None,
                 peer_session_i_pv6_address: Optional[pulumi.Input[str]] = None,
                 session_prefix_v4: Optional[pulumi.Input[str]] = None,
                 session_prefix_v6: Optional[pulumi.Input[str]] = None):
        """
        The properties that define a BGP session.
        :param pulumi.Input[int] max_prefixes_advertised_v4: The maximum number of prefixes advertised over the IPv4 session.
        :param pulumi.Input[int] max_prefixes_advertised_v6: The maximum number of prefixes advertised over the IPv6 session.
        :param pulumi.Input[str] md5_authentication_key: The MD5 authentication key of the session.
        :param pulumi.Input[str] microsoft_session_i_pv4_address: The IPv4 session address on Microsoft's end.
        :param pulumi.Input[str] microsoft_session_i_pv6_address: The IPv6 session address on Microsoft's end.
        :param pulumi.Input[str] peer_session_i_pv4_address: The IPv4 session address on peer's end.
        :param pulumi.Input[str] peer_session_i_pv6_address: The IPv6 session address on peer's end.
        :param pulumi.Input[str] session_prefix_v4: The IPv4 prefix that contains both ends' IPv4 addresses.
        :param pulumi.Input[str] session_prefix_v6: The IPv6 prefix that contains both ends' IPv6 addresses.
        """
        if max_prefixes_advertised_v4 is not None:
            pulumi.set(__self__, "max_prefixes_advertised_v4", max_prefixes_advertised_v4)
        if max_prefixes_advertised_v6 is not None:
            pulumi.set(__self__, "max_prefixes_advertised_v6", max_prefixes_advertised_v6)
        if md5_authentication_key is not None:
            pulumi.set(__self__, "md5_authentication_key", md5_authentication_key)
        if microsoft_session_i_pv4_address is not None:
            pulumi.set(__self__, "microsoft_session_i_pv4_address", microsoft_session_i_pv4_address)
        if microsoft_session_i_pv6_address is not None:
            pulumi.set(__self__, "microsoft_session_i_pv6_address", microsoft_session_i_pv6_address)
        if peer_session_i_pv4_address is not None:
            pulumi.set(__self__, "peer_session_i_pv4_address", peer_session_i_pv4_address)
        if peer_session_i_pv6_address is not None:
            pulumi.set(__self__, "peer_session_i_pv6_address", peer_session_i_pv6_address)
        if session_prefix_v4 is not None:
            pulumi.set(__self__, "session_prefix_v4", session_prefix_v4)
        if session_prefix_v6 is not None:
            pulumi.set(__self__, "session_prefix_v6", session_prefix_v6)

    @property
    @pulumi.getter(name="maxPrefixesAdvertisedV4")
    def max_prefixes_advertised_v4(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of prefixes advertised over the IPv4 session.
        """
        return pulumi.get(self, "max_prefixes_advertised_v4")

    @max_prefixes_advertised_v4.setter
    def max_prefixes_advertised_v4(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_prefixes_advertised_v4", value)

    @property
    @pulumi.getter(name="maxPrefixesAdvertisedV6")
    def max_prefixes_advertised_v6(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of prefixes advertised over the IPv6 session.
        """
        return pulumi.get(self, "max_prefixes_advertised_v6")

    @max_prefixes_advertised_v6.setter
    def max_prefixes_advertised_v6(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_prefixes_advertised_v6", value)

    @property
    @pulumi.getter(name="md5AuthenticationKey")
    def md5_authentication_key(self) -> Optional[pulumi.Input[str]]:
        """
        The MD5 authentication key of the session.
        """
        return pulumi.get(self, "md5_authentication_key")

    @md5_authentication_key.setter
    def md5_authentication_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "md5_authentication_key", value)

    @property
    @pulumi.getter(name="microsoftSessionIPv4Address")
    def microsoft_session_i_pv4_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 session address on Microsoft's end.
        """
        return pulumi.get(self, "microsoft_session_i_pv4_address")

    @microsoft_session_i_pv4_address.setter
    def microsoft_session_i_pv4_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "microsoft_session_i_pv4_address", value)

    @property
    @pulumi.getter(name="microsoftSessionIPv6Address")
    def microsoft_session_i_pv6_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 session address on Microsoft's end.
        """
        return pulumi.get(self, "microsoft_session_i_pv6_address")

    @microsoft_session_i_pv6_address.setter
    def microsoft_session_i_pv6_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "microsoft_session_i_pv6_address", value)

    @property
    @pulumi.getter(name="peerSessionIPv4Address")
    def peer_session_i_pv4_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 session address on peer's end.
        """
        return pulumi.get(self, "peer_session_i_pv4_address")

    @peer_session_i_pv4_address.setter
    def peer_session_i_pv4_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_session_i_pv4_address", value)

    @property
    @pulumi.getter(name="peerSessionIPv6Address")
    def peer_session_i_pv6_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 session address on peer's end.
        """
        return pulumi.get(self, "peer_session_i_pv6_address")

    @peer_session_i_pv6_address.setter
    def peer_session_i_pv6_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_session_i_pv6_address", value)

    @property
    @pulumi.getter(name="sessionPrefixV4")
    def session_prefix_v4(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 prefix that contains both ends' IPv4 addresses.
        """
        return pulumi.get(self, "session_prefix_v4")

    @session_prefix_v4.setter
    def session_prefix_v4(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_prefix_v4", value)

    @property
    @pulumi.getter(name="sessionPrefixV6")
    def session_prefix_v6(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 prefix that contains both ends' IPv6 addresses.
        """
        return pulumi.get(self, "session_prefix_v6")

    @session_prefix_v6.setter
    def session_prefix_v6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_prefix_v6", value)


if not MYPY:
    class ContactDetailArgsDict(TypedDict):
        """
        The contact detail class.
        """
        email: NotRequired[pulumi.Input[str]]
        """
        The e-mail address of the contact.
        """
        phone: NotRequired[pulumi.Input[str]]
        """
        The phone number of the contact.
        """
        role: NotRequired[pulumi.Input[Union[str, 'Role']]]
        """
        The role of the contact.
        """
elif False:
    ContactDetailArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ContactDetailArgs:
    def __init__(__self__, *,
                 email: Optional[pulumi.Input[str]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[Union[str, 'Role']]] = None):
        """
        The contact detail class.
        :param pulumi.Input[str] email: The e-mail address of the contact.
        :param pulumi.Input[str] phone: The phone number of the contact.
        :param pulumi.Input[Union[str, 'Role']] role: The role of the contact.
        """
        if email is not None:
            pulumi.set(__self__, "email", email)
        if phone is not None:
            pulumi.set(__self__, "phone", phone)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The e-mail address of the contact.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def phone(self) -> Optional[pulumi.Input[str]]:
        """
        The phone number of the contact.
        """
        return pulumi.get(self, "phone")

    @phone.setter
    def phone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[Union[str, 'Role']]]:
        """
        The role of the contact.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[Union[str, 'Role']]]):
        pulumi.set(self, "role", value)


if not MYPY:
    class DirectConnectionArgsDict(TypedDict):
        """
        The properties that define a direct connection.
        """
        bandwidth_in_mbps: NotRequired[pulumi.Input[int]]
        """
        The bandwidth of the connection.
        """
        bgp_session: NotRequired[pulumi.Input['BgpSessionArgsDict']]
        """
        The BGP session associated with the connection.
        """
        connection_identifier: NotRequired[pulumi.Input[str]]
        """
        The unique identifier (GUID) for the connection.
        """
        peering_db_facility_id: NotRequired[pulumi.Input[int]]
        """
        The PeeringDB.com ID of the facility at which the connection has to be set up.
        """
        session_address_provider: NotRequired[pulumi.Input[Union[str, 'SessionAddressProvider']]]
        """
        The field indicating if Microsoft provides session ip addresses.
        """
        use_for_peering_service: NotRequired[pulumi.Input[bool]]
        """
        The flag that indicates whether or not the connection is used for peering service.
        """
elif False:
    DirectConnectionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DirectConnectionArgs:
    def __init__(__self__, *,
                 bandwidth_in_mbps: Optional[pulumi.Input[int]] = None,
                 bgp_session: Optional[pulumi.Input['BgpSessionArgs']] = None,
                 connection_identifier: Optional[pulumi.Input[str]] = None,
                 peering_db_facility_id: Optional[pulumi.Input[int]] = None,
                 session_address_provider: Optional[pulumi.Input[Union[str, 'SessionAddressProvider']]] = None,
                 use_for_peering_service: Optional[pulumi.Input[bool]] = None):
        """
        The properties that define a direct connection.
        :param pulumi.Input[int] bandwidth_in_mbps: The bandwidth of the connection.
        :param pulumi.Input['BgpSessionArgs'] bgp_session: The BGP session associated with the connection.
        :param pulumi.Input[str] connection_identifier: The unique identifier (GUID) for the connection.
        :param pulumi.Input[int] peering_db_facility_id: The PeeringDB.com ID of the facility at which the connection has to be set up.
        :param pulumi.Input[Union[str, 'SessionAddressProvider']] session_address_provider: The field indicating if Microsoft provides session ip addresses.
        :param pulumi.Input[bool] use_for_peering_service: The flag that indicates whether or not the connection is used for peering service.
        """
        if bandwidth_in_mbps is not None:
            pulumi.set(__self__, "bandwidth_in_mbps", bandwidth_in_mbps)
        if bgp_session is not None:
            pulumi.set(__self__, "bgp_session", bgp_session)
        if connection_identifier is not None:
            pulumi.set(__self__, "connection_identifier", connection_identifier)
        if peering_db_facility_id is not None:
            pulumi.set(__self__, "peering_db_facility_id", peering_db_facility_id)
        if session_address_provider is not None:
            pulumi.set(__self__, "session_address_provider", session_address_provider)
        if use_for_peering_service is not None:
            pulumi.set(__self__, "use_for_peering_service", use_for_peering_service)

    @property
    @pulumi.getter(name="bandwidthInMbps")
    def bandwidth_in_mbps(self) -> Optional[pulumi.Input[int]]:
        """
        The bandwidth of the connection.
        """
        return pulumi.get(self, "bandwidth_in_mbps")

    @bandwidth_in_mbps.setter
    def bandwidth_in_mbps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bandwidth_in_mbps", value)

    @property
    @pulumi.getter(name="bgpSession")
    def bgp_session(self) -> Optional[pulumi.Input['BgpSessionArgs']]:
        """
        The BGP session associated with the connection.
        """
        return pulumi.get(self, "bgp_session")

    @bgp_session.setter
    def bgp_session(self, value: Optional[pulumi.Input['BgpSessionArgs']]):
        pulumi.set(self, "bgp_session", value)

    @property
    @pulumi.getter(name="connectionIdentifier")
    def connection_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier (GUID) for the connection.
        """
        return pulumi.get(self, "connection_identifier")

    @connection_identifier.setter
    def connection_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_identifier", value)

    @property
    @pulumi.getter(name="peeringDBFacilityId")
    def peering_db_facility_id(self) -> Optional[pulumi.Input[int]]:
        """
        The PeeringDB.com ID of the facility at which the connection has to be set up.
        """
        return pulumi.get(self, "peering_db_facility_id")

    @peering_db_facility_id.setter
    def peering_db_facility_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "peering_db_facility_id", value)

    @property
    @pulumi.getter(name="sessionAddressProvider")
    def session_address_provider(self) -> Optional[pulumi.Input[Union[str, 'SessionAddressProvider']]]:
        """
        The field indicating if Microsoft provides session ip addresses.
        """
        return pulumi.get(self, "session_address_provider")

    @session_address_provider.setter
    def session_address_provider(self, value: Optional[pulumi.Input[Union[str, 'SessionAddressProvider']]]):
        pulumi.set(self, "session_address_provider", value)

    @property
    @pulumi.getter(name="useForPeeringService")
    def use_for_peering_service(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag that indicates whether or not the connection is used for peering service.
        """
        return pulumi.get(self, "use_for_peering_service")

    @use_for_peering_service.setter
    def use_for_peering_service(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_for_peering_service", value)


if not MYPY:
    class ExchangeConnectionArgsDict(TypedDict):
        """
        The properties that define an exchange connection.
        """
        bgp_session: NotRequired[pulumi.Input['BgpSessionArgsDict']]
        """
        The BGP session associated with the connection.
        """
        connection_identifier: NotRequired[pulumi.Input[str]]
        """
        The unique identifier (GUID) for the connection.
        """
        peering_db_facility_id: NotRequired[pulumi.Input[int]]
        """
        The PeeringDB.com ID of the facility at which the connection has to be set up.
        """
elif False:
    ExchangeConnectionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ExchangeConnectionArgs:
    def __init__(__self__, *,
                 bgp_session: Optional[pulumi.Input['BgpSessionArgs']] = None,
                 connection_identifier: Optional[pulumi.Input[str]] = None,
                 peering_db_facility_id: Optional[pulumi.Input[int]] = None):
        """
        The properties that define an exchange connection.
        :param pulumi.Input['BgpSessionArgs'] bgp_session: The BGP session associated with the connection.
        :param pulumi.Input[str] connection_identifier: The unique identifier (GUID) for the connection.
        :param pulumi.Input[int] peering_db_facility_id: The PeeringDB.com ID of the facility at which the connection has to be set up.
        """
        if bgp_session is not None:
            pulumi.set(__self__, "bgp_session", bgp_session)
        if connection_identifier is not None:
            pulumi.set(__self__, "connection_identifier", connection_identifier)
        if peering_db_facility_id is not None:
            pulumi.set(__self__, "peering_db_facility_id", peering_db_facility_id)

    @property
    @pulumi.getter(name="bgpSession")
    def bgp_session(self) -> Optional[pulumi.Input['BgpSessionArgs']]:
        """
        The BGP session associated with the connection.
        """
        return pulumi.get(self, "bgp_session")

    @bgp_session.setter
    def bgp_session(self, value: Optional[pulumi.Input['BgpSessionArgs']]):
        pulumi.set(self, "bgp_session", value)

    @property
    @pulumi.getter(name="connectionIdentifier")
    def connection_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier (GUID) for the connection.
        """
        return pulumi.get(self, "connection_identifier")

    @connection_identifier.setter
    def connection_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_identifier", value)

    @property
    @pulumi.getter(name="peeringDBFacilityId")
    def peering_db_facility_id(self) -> Optional[pulumi.Input[int]]:
        """
        The PeeringDB.com ID of the facility at which the connection has to be set up.
        """
        return pulumi.get(self, "peering_db_facility_id")

    @peering_db_facility_id.setter
    def peering_db_facility_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "peering_db_facility_id", value)


if not MYPY:
    class PeeringPropertiesDirectArgsDict(TypedDict):
        """
        The properties that define a direct peering.
        """
        connections: NotRequired[pulumi.Input[Sequence[pulumi.Input['DirectConnectionArgsDict']]]]
        """
        The set of connections that constitute a direct peering.
        """
        direct_peering_type: NotRequired[pulumi.Input[Union[str, 'DirectPeeringType']]]
        """
        The type of direct peering.
        """
        peer_asn: NotRequired[pulumi.Input['SubResourceArgsDict']]
        """
        The reference of the peer ASN.
        """
elif False:
    PeeringPropertiesDirectArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PeeringPropertiesDirectArgs:
    def __init__(__self__, *,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input['DirectConnectionArgs']]]] = None,
                 direct_peering_type: Optional[pulumi.Input[Union[str, 'DirectPeeringType']]] = None,
                 peer_asn: Optional[pulumi.Input['SubResourceArgs']] = None):
        """
        The properties that define a direct peering.
        :param pulumi.Input[Sequence[pulumi.Input['DirectConnectionArgs']]] connections: The set of connections that constitute a direct peering.
        :param pulumi.Input[Union[str, 'DirectPeeringType']] direct_peering_type: The type of direct peering.
        :param pulumi.Input['SubResourceArgs'] peer_asn: The reference of the peer ASN.
        """
        if connections is not None:
            pulumi.set(__self__, "connections", connections)
        if direct_peering_type is not None:
            pulumi.set(__self__, "direct_peering_type", direct_peering_type)
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)

    @property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DirectConnectionArgs']]]]:
        """
        The set of connections that constitute a direct peering.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DirectConnectionArgs']]]]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter(name="directPeeringType")
    def direct_peering_type(self) -> Optional[pulumi.Input[Union[str, 'DirectPeeringType']]]:
        """
        The type of direct peering.
        """
        return pulumi.get(self, "direct_peering_type")

    @direct_peering_type.setter
    def direct_peering_type(self, value: Optional[pulumi.Input[Union[str, 'DirectPeeringType']]]):
        pulumi.set(self, "direct_peering_type", value)

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The reference of the peer ASN.
        """
        return pulumi.get(self, "peer_asn")

    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "peer_asn", value)


if not MYPY:
    class PeeringPropertiesExchangeArgsDict(TypedDict):
        """
        The properties that define an exchange peering.
        """
        connections: NotRequired[pulumi.Input[Sequence[pulumi.Input['ExchangeConnectionArgsDict']]]]
        """
        The set of connections that constitute an exchange peering.
        """
        peer_asn: NotRequired[pulumi.Input['SubResourceArgsDict']]
        """
        The reference of the peer ASN.
        """
elif False:
    PeeringPropertiesExchangeArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PeeringPropertiesExchangeArgs:
    def __init__(__self__, *,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input['ExchangeConnectionArgs']]]] = None,
                 peer_asn: Optional[pulumi.Input['SubResourceArgs']] = None):
        """
        The properties that define an exchange peering.
        :param pulumi.Input[Sequence[pulumi.Input['ExchangeConnectionArgs']]] connections: The set of connections that constitute an exchange peering.
        :param pulumi.Input['SubResourceArgs'] peer_asn: The reference of the peer ASN.
        """
        if connections is not None:
            pulumi.set(__self__, "connections", connections)
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)

    @property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExchangeConnectionArgs']]]]:
        """
        The set of connections that constitute an exchange peering.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExchangeConnectionArgs']]]]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The reference of the peer ASN.
        """
        return pulumi.get(self, "peer_asn")

    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "peer_asn", value)


if not MYPY:
    class PeeringServiceSkuArgsDict(TypedDict):
        """
        The SKU that defines the type of the peering service.
        """
        name: NotRequired[pulumi.Input[str]]
        """
        The name of the peering service SKU.
        """
elif False:
    PeeringServiceSkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PeeringServiceSkuArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The SKU that defines the type of the peering service.
        :param pulumi.Input[str] name: The name of the peering service SKU.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the peering service SKU.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


if not MYPY:
    class PeeringSkuArgsDict(TypedDict):
        """
        The SKU that defines the tier and kind of the peering.
        """
        name: NotRequired[pulumi.Input[str]]
        """
        The name of the peering SKU.
        """
elif False:
    PeeringSkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PeeringSkuArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The SKU that defines the tier and kind of the peering.
        :param pulumi.Input[str] name: The name of the peering SKU.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the peering SKU.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


if not MYPY:
    class SubResourceArgsDict(TypedDict):
        """
        The sub resource.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        Sub-resource ID. Both absolute resource ID and a relative resource ID are accepted.
        An absolute ID starts with /subscriptions/ and contains the entire ID of the parent resource and the ID of the sub-resource in the end.
        A relative ID replaces the ID of the parent resource with a token '$self', followed by the sub-resource ID itself.
        Example of a relative ID: $self/frontEndConfigurations/my-frontend.
        """
elif False:
    SubResourceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SubResourceArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        The sub resource.
        :param pulumi.Input[str] id: Sub-resource ID. Both absolute resource ID and a relative resource ID are accepted.
               An absolute ID starts with /subscriptions/ and contains the entire ID of the parent resource and the ID of the sub-resource in the end.
               A relative ID replaces the ID of the parent resource with a token '$self', followed by the sub-resource ID itself.
               Example of a relative ID: $self/frontEndConfigurations/my-frontend.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Sub-resource ID. Both absolute resource ID and a relative resource ID are accepted.
        An absolute ID starts with /subscriptions/ and contains the entire ID of the parent resource and the ID of the sub-resource in the end.
        A relative ID replaces the ID of the parent resource with a token '$self', followed by the sub-resource ID itself.
        Example of a relative ID: $self/frontEndConfigurations/my-frontend.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


