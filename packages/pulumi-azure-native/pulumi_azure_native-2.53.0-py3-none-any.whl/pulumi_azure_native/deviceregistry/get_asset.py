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
    'GetAssetResult',
    'AwaitableGetAssetResult',
    'get_asset',
    'get_asset_output',
]

@pulumi.output_type
class GetAssetResult:
    """
    Asset definition.
    """
    def __init__(__self__, asset_endpoint_profile_uri=None, asset_type=None, attributes=None, data_points=None, default_data_points_configuration=None, default_events_configuration=None, description=None, display_name=None, documentation_uri=None, enabled=None, events=None, extended_location=None, external_asset_id=None, hardware_revision=None, id=None, location=None, manufacturer=None, manufacturer_uri=None, model=None, name=None, product_code=None, provisioning_state=None, serial_number=None, software_revision=None, status=None, system_data=None, tags=None, type=None, uuid=None, version=None):
        if asset_endpoint_profile_uri and not isinstance(asset_endpoint_profile_uri, str):
            raise TypeError("Expected argument 'asset_endpoint_profile_uri' to be a str")
        pulumi.set(__self__, "asset_endpoint_profile_uri", asset_endpoint_profile_uri)
        if asset_type and not isinstance(asset_type, str):
            raise TypeError("Expected argument 'asset_type' to be a str")
        pulumi.set(__self__, "asset_type", asset_type)
        if attributes and not isinstance(attributes, dict):
            raise TypeError("Expected argument 'attributes' to be a dict")
        pulumi.set(__self__, "attributes", attributes)
        if data_points and not isinstance(data_points, list):
            raise TypeError("Expected argument 'data_points' to be a list")
        pulumi.set(__self__, "data_points", data_points)
        if default_data_points_configuration and not isinstance(default_data_points_configuration, str):
            raise TypeError("Expected argument 'default_data_points_configuration' to be a str")
        pulumi.set(__self__, "default_data_points_configuration", default_data_points_configuration)
        if default_events_configuration and not isinstance(default_events_configuration, str):
            raise TypeError("Expected argument 'default_events_configuration' to be a str")
        pulumi.set(__self__, "default_events_configuration", default_events_configuration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if documentation_uri and not isinstance(documentation_uri, str):
            raise TypeError("Expected argument 'documentation_uri' to be a str")
        pulumi.set(__self__, "documentation_uri", documentation_uri)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if events and not isinstance(events, list):
            raise TypeError("Expected argument 'events' to be a list")
        pulumi.set(__self__, "events", events)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if external_asset_id and not isinstance(external_asset_id, str):
            raise TypeError("Expected argument 'external_asset_id' to be a str")
        pulumi.set(__self__, "external_asset_id", external_asset_id)
        if hardware_revision and not isinstance(hardware_revision, str):
            raise TypeError("Expected argument 'hardware_revision' to be a str")
        pulumi.set(__self__, "hardware_revision", hardware_revision)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if manufacturer and not isinstance(manufacturer, str):
            raise TypeError("Expected argument 'manufacturer' to be a str")
        pulumi.set(__self__, "manufacturer", manufacturer)
        if manufacturer_uri and not isinstance(manufacturer_uri, str):
            raise TypeError("Expected argument 'manufacturer_uri' to be a str")
        pulumi.set(__self__, "manufacturer_uri", manufacturer_uri)
        if model and not isinstance(model, str):
            raise TypeError("Expected argument 'model' to be a str")
        pulumi.set(__self__, "model", model)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if product_code and not isinstance(product_code, str):
            raise TypeError("Expected argument 'product_code' to be a str")
        pulumi.set(__self__, "product_code", product_code)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if serial_number and not isinstance(serial_number, str):
            raise TypeError("Expected argument 'serial_number' to be a str")
        pulumi.set(__self__, "serial_number", serial_number)
        if software_revision and not isinstance(software_revision, str):
            raise TypeError("Expected argument 'software_revision' to be a str")
        pulumi.set(__self__, "software_revision", software_revision)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="assetEndpointProfileUri")
    def asset_endpoint_profile_uri(self) -> str:
        """
        A reference to the asset endpoint profile (connection information) used by brokers to connect to an endpoint that provides data points for this asset. Must have the format <ModuleCR.metadata.namespace>/<ModuleCR.metadata.name>.
        """
        return pulumi.get(self, "asset_endpoint_profile_uri")

    @property
    @pulumi.getter(name="assetType")
    def asset_type(self) -> Optional[str]:
        """
        Resource path to asset type (model) definition.
        """
        return pulumi.get(self, "asset_type")

    @property
    @pulumi.getter
    def attributes(self) -> Optional[Any]:
        """
        A set of key-value pairs that contain custom attributes set by the customer.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="dataPoints")
    def data_points(self) -> Optional[Sequence['outputs.DataPointResponse']]:
        """
        Array of data points that are part of the asset. Each data point can reference an asset type capability and have per-data point configuration. See below for more details for the definition of the dataPoints element.
        """
        return pulumi.get(self, "data_points")

    @property
    @pulumi.getter(name="defaultDataPointsConfiguration")
    def default_data_points_configuration(self) -> Optional[str]:
        """
        Protocol-specific default configuration for all data points. Each data point can have its own configuration that overrides the default settings here. This assumes that each asset instance has one protocol.
        """
        return pulumi.get(self, "default_data_points_configuration")

    @property
    @pulumi.getter(name="defaultEventsConfiguration")
    def default_events_configuration(self) -> Optional[str]:
        """
        Protocol-specific default configuration for all events. Each event can have its own configuration that overrides the default settings here. This assumes that each asset instance has one protocol.
        """
        return pulumi.get(self, "default_events_configuration")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Human-readable description of the asset.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Human-readable display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="documentationUri")
    def documentation_uri(self) -> Optional[str]:
        """
        Reference to the documentation.
        """
        return pulumi.get(self, "documentation_uri")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Enabled/Disabled status of the asset.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def events(self) -> Optional[Sequence['outputs.EventResponse']]:
        """
        Array of events that are part of the asset. Each event can reference an asset type capability and have per-event configuration. See below for more details about the definition of the events element.
        """
        return pulumi.get(self, "events")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="externalAssetId")
    def external_asset_id(self) -> Optional[str]:
        """
        Asset id provided by the customer.
        """
        return pulumi.get(self, "external_asset_id")

    @property
    @pulumi.getter(name="hardwareRevision")
    def hardware_revision(self) -> Optional[str]:
        """
        Revision number of the hardware.
        """
        return pulumi.get(self, "hardware_revision")

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
    def manufacturer(self) -> Optional[str]:
        """
        Asset manufacturer name.
        """
        return pulumi.get(self, "manufacturer")

    @property
    @pulumi.getter(name="manufacturerUri")
    def manufacturer_uri(self) -> Optional[str]:
        """
        Asset manufacturer URI.
        """
        return pulumi.get(self, "manufacturer_uri")

    @property
    @pulumi.getter
    def model(self) -> Optional[str]:
        """
        Asset model name.
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[str]:
        """
        Asset product code.
        """
        return pulumi.get(self, "product_code")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[str]:
        """
        Asset serial number.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="softwareRevision")
    def software_revision(self) -> Optional[str]:
        """
        Revision number of the software.
        """
        return pulumi.get(self, "software_revision")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.AssetStatusResponse':
        """
        Read only object to reflect changes that have occurred on the Edge. Similar to Kubernetes status property for custom resources.
        """
        return pulumi.get(self, "status")

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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        Globally unique, immutable, non-reusable id.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        An integer that is incremented each time the resource is modified.
        """
        return pulumi.get(self, "version")


class AwaitableGetAssetResult(GetAssetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssetResult(
            asset_endpoint_profile_uri=self.asset_endpoint_profile_uri,
            asset_type=self.asset_type,
            attributes=self.attributes,
            data_points=self.data_points,
            default_data_points_configuration=self.default_data_points_configuration,
            default_events_configuration=self.default_events_configuration,
            description=self.description,
            display_name=self.display_name,
            documentation_uri=self.documentation_uri,
            enabled=self.enabled,
            events=self.events,
            extended_location=self.extended_location,
            external_asset_id=self.external_asset_id,
            hardware_revision=self.hardware_revision,
            id=self.id,
            location=self.location,
            manufacturer=self.manufacturer,
            manufacturer_uri=self.manufacturer_uri,
            model=self.model,
            name=self.name,
            product_code=self.product_code,
            provisioning_state=self.provisioning_state,
            serial_number=self.serial_number,
            software_revision=self.software_revision,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            uuid=self.uuid,
            version=self.version)


def get_asset(asset_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssetResult:
    """
    Get a Asset
    Azure REST API version: 2023-11-01-preview.


    :param str asset_name: Asset name parameter.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['assetName'] = asset_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:deviceregistry:getAsset', __args__, opts=opts, typ=GetAssetResult).value

    return AwaitableGetAssetResult(
        asset_endpoint_profile_uri=pulumi.get(__ret__, 'asset_endpoint_profile_uri'),
        asset_type=pulumi.get(__ret__, 'asset_type'),
        attributes=pulumi.get(__ret__, 'attributes'),
        data_points=pulumi.get(__ret__, 'data_points'),
        default_data_points_configuration=pulumi.get(__ret__, 'default_data_points_configuration'),
        default_events_configuration=pulumi.get(__ret__, 'default_events_configuration'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        documentation_uri=pulumi.get(__ret__, 'documentation_uri'),
        enabled=pulumi.get(__ret__, 'enabled'),
        events=pulumi.get(__ret__, 'events'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        external_asset_id=pulumi.get(__ret__, 'external_asset_id'),
        hardware_revision=pulumi.get(__ret__, 'hardware_revision'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        manufacturer=pulumi.get(__ret__, 'manufacturer'),
        manufacturer_uri=pulumi.get(__ret__, 'manufacturer_uri'),
        model=pulumi.get(__ret__, 'model'),
        name=pulumi.get(__ret__, 'name'),
        product_code=pulumi.get(__ret__, 'product_code'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        serial_number=pulumi.get(__ret__, 'serial_number'),
        software_revision=pulumi.get(__ret__, 'software_revision'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        uuid=pulumi.get(__ret__, 'uuid'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_asset)
def get_asset_output(asset_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssetResult]:
    """
    Get a Asset
    Azure REST API version: 2023-11-01-preview.


    :param str asset_name: Asset name parameter.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
