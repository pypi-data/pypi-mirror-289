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
from . import outputs

__all__ = [
    'GetAssetEndpointProfileResult',
    'AwaitableGetAssetEndpointProfileResult',
    'get_asset_endpoint_profile',
    'get_asset_endpoint_profile_output',
]

@pulumi.output_type
class GetAssetEndpointProfileResult:
    """
    Asset Endpoint Profile definition.
    """
    def __init__(__self__, additional_configuration=None, extended_location=None, id=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, target_address=None, transport_authentication=None, type=None, user_authentication=None, uuid=None):
        if additional_configuration and not isinstance(additional_configuration, str):
            raise TypeError("Expected argument 'additional_configuration' to be a str")
        pulumi.set(__self__, "additional_configuration", additional_configuration)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_address and not isinstance(target_address, str):
            raise TypeError("Expected argument 'target_address' to be a str")
        pulumi.set(__self__, "target_address", target_address)
        if transport_authentication and not isinstance(transport_authentication, dict):
            raise TypeError("Expected argument 'transport_authentication' to be a dict")
        pulumi.set(__self__, "transport_authentication", transport_authentication)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_authentication and not isinstance(user_authentication, dict):
            raise TypeError("Expected argument 'user_authentication' to be a dict")
        pulumi.set(__self__, "user_authentication", user_authentication)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> Optional[str]:
        """
        Contains connectivity type specific further configuration (e.g. OPC UA, Modbus, ONVIF).
        """
        return pulumi.get(self, "additional_configuration")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetAddress")
    def target_address(self) -> str:
        """
        The local valid URI specifying the network address/DNS name of a southbound device. The scheme part of the targetAddress URI specifies the type of the device. The additionalConfiguration field holds further connector type specific configuration.
        """
        return pulumi.get(self, "target_address")

    @property
    @pulumi.getter(name="transportAuthentication")
    def transport_authentication(self) -> Optional['outputs.TransportAuthenticationResponse']:
        """
        Defines the authentication mechanism for the southbound connector connecting to the shop floor/OT device.
        """
        return pulumi.get(self, "transport_authentication")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAuthentication")
    def user_authentication(self) -> Optional['outputs.UserAuthenticationResponse']:
        """
        Defines the client authentication mechanism to the server.
        """
        return pulumi.get(self, "user_authentication")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        Globally unique, immutable, non-reusable id.
        """
        return pulumi.get(self, "uuid")


class AwaitableGetAssetEndpointProfileResult(GetAssetEndpointProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssetEndpointProfileResult(
            additional_configuration=self.additional_configuration,
            extended_location=self.extended_location,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            target_address=self.target_address,
            transport_authentication=self.transport_authentication,
            type=self.type,
            user_authentication=self.user_authentication,
            uuid=self.uuid)


def get_asset_endpoint_profile(asset_endpoint_profile_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssetEndpointProfileResult:
    """
    Get a AssetEndpointProfile


    :param str asset_endpoint_profile_name: Asset Endpoint Profile name parameter.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['assetEndpointProfileName'] = asset_endpoint_profile_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:deviceregistry/v20231101preview:getAssetEndpointProfile', __args__, opts=opts, typ=GetAssetEndpointProfileResult).value

    return AwaitableGetAssetEndpointProfileResult(
        additional_configuration=pulumi.get(__ret__, 'additional_configuration'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        target_address=pulumi.get(__ret__, 'target_address'),
        transport_authentication=pulumi.get(__ret__, 'transport_authentication'),
        type=pulumi.get(__ret__, 'type'),
        user_authentication=pulumi.get(__ret__, 'user_authentication'),
        uuid=pulumi.get(__ret__, 'uuid'))


@_utilities.lift_output_func(get_asset_endpoint_profile)
def get_asset_endpoint_profile_output(asset_endpoint_profile_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssetEndpointProfileResult]:
    """
    Get a AssetEndpointProfile


    :param str asset_endpoint_profile_name: Asset Endpoint Profile name parameter.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
