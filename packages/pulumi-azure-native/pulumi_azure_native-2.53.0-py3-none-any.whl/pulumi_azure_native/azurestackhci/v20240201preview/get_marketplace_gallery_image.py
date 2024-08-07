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
    'GetMarketplaceGalleryImageResult',
    'AwaitableGetMarketplaceGalleryImageResult',
    'get_marketplace_gallery_image',
    'get_marketplace_gallery_image_output',
]

@pulumi.output_type
class GetMarketplaceGalleryImageResult:
    """
    The marketplace gallery image resource definition.
    """
    def __init__(__self__, cloud_init_data_source=None, container_id=None, extended_location=None, hyper_v_generation=None, id=None, identifier=None, location=None, name=None, os_type=None, provisioning_state=None, status=None, system_data=None, tags=None, type=None, version=None):
        if cloud_init_data_source and not isinstance(cloud_init_data_source, str):
            raise TypeError("Expected argument 'cloud_init_data_source' to be a str")
        pulumi.set(__self__, "cloud_init_data_source", cloud_init_data_source)
        if container_id and not isinstance(container_id, str):
            raise TypeError("Expected argument 'container_id' to be a str")
        pulumi.set(__self__, "container_id", container_id)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if hyper_v_generation and not isinstance(hyper_v_generation, str):
            raise TypeError("Expected argument 'hyper_v_generation' to be a str")
        pulumi.set(__self__, "hyper_v_generation", hyper_v_generation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identifier and not isinstance(identifier, dict):
            raise TypeError("Expected argument 'identifier' to be a dict")
        pulumi.set(__self__, "identifier", identifier)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
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
        if version and not isinstance(version, dict):
            raise TypeError("Expected argument 'version' to be a dict")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="cloudInitDataSource")
    def cloud_init_data_source(self) -> Optional[str]:
        """
        Datasource for the gallery image when provisioning with cloud-init [NoCloud, Azure]
        """
        return pulumi.get(self, "cloud_init_data_source")

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[str]:
        """
        Storage ContainerID of the storage container to be used for marketplace gallery image
        """
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[str]:
        """
        The hypervisor generation of the Virtual Machine [V1, V2]
        """
        return pulumi.get(self, "hyper_v_generation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identifier(self) -> Optional['outputs.GalleryImageIdentifierResponse']:
        """
        This is the gallery image definition identifier.
        """
        return pulumi.get(self, "identifier")

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
    @pulumi.getter(name="osType")
    def os_type(self) -> str:
        """
        Operating system type that the gallery image uses [Windows, Linux]
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the marketplace gallery image.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.MarketplaceGalleryImageStatusResponse':
        """
        The observed state of marketplace gallery images
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
    def version(self) -> Optional['outputs.GalleryImageVersionResponse']:
        """
        Specifies information about the gallery image version that you want to create or update.
        """
        return pulumi.get(self, "version")


class AwaitableGetMarketplaceGalleryImageResult(GetMarketplaceGalleryImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMarketplaceGalleryImageResult(
            cloud_init_data_source=self.cloud_init_data_source,
            container_id=self.container_id,
            extended_location=self.extended_location,
            hyper_v_generation=self.hyper_v_generation,
            id=self.id,
            identifier=self.identifier,
            location=self.location,
            name=self.name,
            os_type=self.os_type,
            provisioning_state=self.provisioning_state,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            version=self.version)


def get_marketplace_gallery_image(marketplace_gallery_image_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMarketplaceGalleryImageResult:
    """
    Gets a marketplace gallery image


    :param str marketplace_gallery_image_name: Name of the marketplace gallery image
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['marketplaceGalleryImageName'] = marketplace_gallery_image_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20240201preview:getMarketplaceGalleryImage', __args__, opts=opts, typ=GetMarketplaceGalleryImageResult).value

    return AwaitableGetMarketplaceGalleryImageResult(
        cloud_init_data_source=pulumi.get(__ret__, 'cloud_init_data_source'),
        container_id=pulumi.get(__ret__, 'container_id'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        hyper_v_generation=pulumi.get(__ret__, 'hyper_v_generation'),
        id=pulumi.get(__ret__, 'id'),
        identifier=pulumi.get(__ret__, 'identifier'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        os_type=pulumi.get(__ret__, 'os_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_marketplace_gallery_image)
def get_marketplace_gallery_image_output(marketplace_gallery_image_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMarketplaceGalleryImageResult]:
    """
    Gets a marketplace gallery image


    :param str marketplace_gallery_image_name: Name of the marketplace gallery image
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
