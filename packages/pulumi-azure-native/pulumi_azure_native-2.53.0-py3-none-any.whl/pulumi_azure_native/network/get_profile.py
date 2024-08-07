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
from .. import _utilities
from . import outputs

__all__ = [
    'GetProfileResult',
    'AwaitableGetProfileResult',
    'get_profile',
    'get_profile_output',
]

@pulumi.output_type
class GetProfileResult:
    """
    Class representing a Traffic Manager profile.
    """
    def __init__(__self__, allowed_endpoint_record_types=None, dns_config=None, endpoints=None, id=None, location=None, max_return=None, monitor_config=None, name=None, profile_status=None, tags=None, traffic_routing_method=None, traffic_view_enrollment_status=None, type=None):
        if allowed_endpoint_record_types and not isinstance(allowed_endpoint_record_types, list):
            raise TypeError("Expected argument 'allowed_endpoint_record_types' to be a list")
        pulumi.set(__self__, "allowed_endpoint_record_types", allowed_endpoint_record_types)
        if dns_config and not isinstance(dns_config, dict):
            raise TypeError("Expected argument 'dns_config' to be a dict")
        pulumi.set(__self__, "dns_config", dns_config)
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        pulumi.set(__self__, "endpoints", endpoints)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_return and not isinstance(max_return, float):
            raise TypeError("Expected argument 'max_return' to be a float")
        pulumi.set(__self__, "max_return", max_return)
        if monitor_config and not isinstance(monitor_config, dict):
            raise TypeError("Expected argument 'monitor_config' to be a dict")
        pulumi.set(__self__, "monitor_config", monitor_config)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if profile_status and not isinstance(profile_status, str):
            raise TypeError("Expected argument 'profile_status' to be a str")
        pulumi.set(__self__, "profile_status", profile_status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if traffic_routing_method and not isinstance(traffic_routing_method, str):
            raise TypeError("Expected argument 'traffic_routing_method' to be a str")
        pulumi.set(__self__, "traffic_routing_method", traffic_routing_method)
        if traffic_view_enrollment_status and not isinstance(traffic_view_enrollment_status, str):
            raise TypeError("Expected argument 'traffic_view_enrollment_status' to be a str")
        pulumi.set(__self__, "traffic_view_enrollment_status", traffic_view_enrollment_status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="allowedEndpointRecordTypes")
    def allowed_endpoint_record_types(self) -> Optional[Sequence[str]]:
        """
        The list of allowed endpoint record types.
        """
        return pulumi.get(self, "allowed_endpoint_record_types")

    @property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional['outputs.DnsConfigResponse']:
        """
        The DNS settings of the Traffic Manager profile.
        """
        return pulumi.get(self, "dns_config")

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence['outputs.EndpointResponse']]:
        """
        The list of endpoints in the Traffic Manager profile.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The Azure Region where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxReturn")
    def max_return(self) -> Optional[float]:
        """
        Maximum number of endpoints to be returned for MultiValue routing type.
        """
        return pulumi.get(self, "max_return")

    @property
    @pulumi.getter(name="monitorConfig")
    def monitor_config(self) -> Optional['outputs.MonitorConfigResponse']:
        """
        The endpoint monitoring settings of the Traffic Manager profile.
        """
        return pulumi.get(self, "monitor_config")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileStatus")
    def profile_status(self) -> Optional[str]:
        """
        The status of the Traffic Manager profile.
        """
        return pulumi.get(self, "profile_status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trafficRoutingMethod")
    def traffic_routing_method(self) -> Optional[str]:
        """
        The traffic routing method of the Traffic Manager profile.
        """
        return pulumi.get(self, "traffic_routing_method")

    @property
    @pulumi.getter(name="trafficViewEnrollmentStatus")
    def traffic_view_enrollment_status(self) -> Optional[str]:
        """
        Indicates whether Traffic View is 'Enabled' or 'Disabled' for the Traffic Manager profile. Null, indicates 'Disabled'. Enabling this feature will increase the cost of the Traffic Manage profile.
        """
        return pulumi.get(self, "traffic_view_enrollment_status")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.
        """
        return pulumi.get(self, "type")


class AwaitableGetProfileResult(GetProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProfileResult(
            allowed_endpoint_record_types=self.allowed_endpoint_record_types,
            dns_config=self.dns_config,
            endpoints=self.endpoints,
            id=self.id,
            location=self.location,
            max_return=self.max_return,
            monitor_config=self.monitor_config,
            name=self.name,
            profile_status=self.profile_status,
            tags=self.tags,
            traffic_routing_method=self.traffic_routing_method,
            traffic_view_enrollment_status=self.traffic_view_enrollment_status,
            type=self.type)


def get_profile(profile_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProfileResult:
    """
    Gets a Traffic Manager profile.
    Azure REST API version: 2022-04-01.

    Other available API versions: 2017-03-01, 2018-02-01, 2022-04-01-preview.


    :param str profile_name: The name of the Traffic Manager profile.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network:getProfile', __args__, opts=opts, typ=GetProfileResult).value

    return AwaitableGetProfileResult(
        allowed_endpoint_record_types=pulumi.get(__ret__, 'allowed_endpoint_record_types'),
        dns_config=pulumi.get(__ret__, 'dns_config'),
        endpoints=pulumi.get(__ret__, 'endpoints'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        max_return=pulumi.get(__ret__, 'max_return'),
        monitor_config=pulumi.get(__ret__, 'monitor_config'),
        name=pulumi.get(__ret__, 'name'),
        profile_status=pulumi.get(__ret__, 'profile_status'),
        tags=pulumi.get(__ret__, 'tags'),
        traffic_routing_method=pulumi.get(__ret__, 'traffic_routing_method'),
        traffic_view_enrollment_status=pulumi.get(__ret__, 'traffic_view_enrollment_status'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_profile)
def get_profile_output(profile_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProfileResult]:
    """
    Gets a Traffic Manager profile.
    Azure REST API version: 2022-04-01.

    Other available API versions: 2017-03-01, 2018-02-01, 2022-04-01-preview.


    :param str profile_name: The name of the Traffic Manager profile.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
