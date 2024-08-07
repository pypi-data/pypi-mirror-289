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
    'GetOriginGroupResult',
    'AwaitableGetOriginGroupResult',
    'get_origin_group',
    'get_origin_group_output',
]

@pulumi.output_type
class GetOriginGroupResult:
    """
    Origin group comprising of origins is used for load balancing to origins when the content cannot be served from CDN.
    """
    def __init__(__self__, health_probe_settings=None, id=None, name=None, origins=None, provisioning_state=None, resource_state=None, response_based_origin_error_detection_settings=None, system_data=None, traffic_restoration_time_to_healed_or_new_endpoints_in_minutes=None, type=None):
        if health_probe_settings and not isinstance(health_probe_settings, dict):
            raise TypeError("Expected argument 'health_probe_settings' to be a dict")
        pulumi.set(__self__, "health_probe_settings", health_probe_settings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if origins and not isinstance(origins, list):
            raise TypeError("Expected argument 'origins' to be a list")
        pulumi.set(__self__, "origins", origins)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if response_based_origin_error_detection_settings and not isinstance(response_based_origin_error_detection_settings, dict):
            raise TypeError("Expected argument 'response_based_origin_error_detection_settings' to be a dict")
        pulumi.set(__self__, "response_based_origin_error_detection_settings", response_based_origin_error_detection_settings)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if traffic_restoration_time_to_healed_or_new_endpoints_in_minutes and not isinstance(traffic_restoration_time_to_healed_or_new_endpoints_in_minutes, int):
            raise TypeError("Expected argument 'traffic_restoration_time_to_healed_or_new_endpoints_in_minutes' to be a int")
        pulumi.set(__self__, "traffic_restoration_time_to_healed_or_new_endpoints_in_minutes", traffic_restoration_time_to_healed_or_new_endpoints_in_minutes)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional['outputs.HealthProbeParametersResponse']:
        """
        Health probe settings to the origin that is used to determine the health of the origin.
        """
        return pulumi.get(self, "health_probe_settings")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def origins(self) -> Sequence['outputs.ResourceReferenceResponse']:
        """
        The source of the content being delivered via CDN within given origin group.
        """
        return pulumi.get(self, "origins")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning status of the origin group.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        Resource status of the origin group.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="responseBasedOriginErrorDetectionSettings")
    def response_based_origin_error_detection_settings(self) -> Optional['outputs.ResponseBasedOriginErrorDetectionParametersResponse']:
        """
        The JSON object that contains the properties to determine origin health using real requests/responses. This property is currently not supported.
        """
        return pulumi.get(self, "response_based_origin_error_detection_settings")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="trafficRestorationTimeToHealedOrNewEndpointsInMinutes")
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(self) -> Optional[int]:
        """
        Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported.
        """
        return pulumi.get(self, "traffic_restoration_time_to_healed_or_new_endpoints_in_minutes")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetOriginGroupResult(GetOriginGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOriginGroupResult(
            health_probe_settings=self.health_probe_settings,
            id=self.id,
            name=self.name,
            origins=self.origins,
            provisioning_state=self.provisioning_state,
            resource_state=self.resource_state,
            response_based_origin_error_detection_settings=self.response_based_origin_error_detection_settings,
            system_data=self.system_data,
            traffic_restoration_time_to_healed_or_new_endpoints_in_minutes=self.traffic_restoration_time_to_healed_or_new_endpoints_in_minutes,
            type=self.type)


def get_origin_group(endpoint_name: Optional[str] = None,
                     origin_group_name: Optional[str] = None,
                     profile_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOriginGroupResult:
    """
    Gets an existing origin group within an endpoint.
    Azure REST API version: 2023-05-01.

    Other available API versions: 2023-07-01-preview, 2024-02-01, 2024-05-01-preview.


    :param str endpoint_name: Name of the endpoint under the profile which is unique globally.
    :param str origin_group_name: Name of the origin group which is unique within the endpoint.
    :param str profile_name: Name of the CDN profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['originGroupName'] = origin_group_name
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cdn:getOriginGroup', __args__, opts=opts, typ=GetOriginGroupResult).value

    return AwaitableGetOriginGroupResult(
        health_probe_settings=pulumi.get(__ret__, 'health_probe_settings'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        origins=pulumi.get(__ret__, 'origins'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_state=pulumi.get(__ret__, 'resource_state'),
        response_based_origin_error_detection_settings=pulumi.get(__ret__, 'response_based_origin_error_detection_settings'),
        system_data=pulumi.get(__ret__, 'system_data'),
        traffic_restoration_time_to_healed_or_new_endpoints_in_minutes=pulumi.get(__ret__, 'traffic_restoration_time_to_healed_or_new_endpoints_in_minutes'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_origin_group)
def get_origin_group_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                            origin_group_name: Optional[pulumi.Input[str]] = None,
                            profile_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOriginGroupResult]:
    """
    Gets an existing origin group within an endpoint.
    Azure REST API version: 2023-05-01.

    Other available API versions: 2023-07-01-preview, 2024-02-01, 2024-05-01-preview.


    :param str endpoint_name: Name of the endpoint under the profile which is unique globally.
    :param str origin_group_name: Name of the origin group which is unique within the endpoint.
    :param str profile_name: Name of the CDN profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
