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
    'GetImageResult',
    'AwaitableGetImageResult',
    'get_image',
    'get_image_output',
]

@pulumi.output_type
class GetImageResult:
    """
    An image resource belonging to a catalog resource.
    """
    def __init__(__self__, component_id=None, description=None, id=None, image=None, image_id=None, image_name=None, image_type=None, name=None, provisioning_state=None, regional_data_boundary=None, system_data=None, type=None, uri=None):
        if component_id and not isinstance(component_id, str):
            raise TypeError("Expected argument 'component_id' to be a str")
        pulumi.set(__self__, "component_id", component_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image and not isinstance(image, str):
            raise TypeError("Expected argument 'image' to be a str")
        pulumi.set(__self__, "image", image)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if image_name and not isinstance(image_name, str):
            raise TypeError("Expected argument 'image_name' to be a str")
        pulumi.set(__self__, "image_name", image_name)
        if image_type and not isinstance(image_type, str):
            raise TypeError("Expected argument 'image_type' to be a str")
        pulumi.set(__self__, "image_type", image_type)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if regional_data_boundary and not isinstance(regional_data_boundary, str):
            raise TypeError("Expected argument 'regional_data_boundary' to be a str")
        pulumi.set(__self__, "regional_data_boundary", regional_data_boundary)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uri and not isinstance(uri, str):
            raise TypeError("Expected argument 'uri' to be a str")
        pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="componentId")
    def component_id(self) -> str:
        """
        The image component id.
        """
        return pulumi.get(self, "component_id")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The image description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def image(self) -> Optional[str]:
        """
        Image as a UTF-8 encoded base 64 string on image create. This field contains the image URI on image reads.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[str]:
        """
        Image ID
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> str:
        """
        Image name
        """
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="imageType")
    def image_type(self) -> str:
        """
        The image type.
        """
        return pulumi.get(self, "image_type")

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
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="regionalDataBoundary")
    def regional_data_boundary(self) -> Optional[str]:
        """
        Regional data boundary for an image
        """
        return pulumi.get(self, "regional_data_boundary")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uri(self) -> str:
        """
        Location the image
        """
        return pulumi.get(self, "uri")


class AwaitableGetImageResult(GetImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageResult(
            component_id=self.component_id,
            description=self.description,
            id=self.id,
            image=self.image,
            image_id=self.image_id,
            image_name=self.image_name,
            image_type=self.image_type,
            name=self.name,
            provisioning_state=self.provisioning_state,
            regional_data_boundary=self.regional_data_boundary,
            system_data=self.system_data,
            type=self.type,
            uri=self.uri)


def get_image(catalog_name: Optional[str] = None,
              image_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImageResult:
    """
    Get a Image
    Azure REST API version: 2022-09-01-preview.

    Other available API versions: 2024-04-01.


    :param str catalog_name: Name of catalog
    :param str image_name: Image name. Use an image GUID for GA versions of the API.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['catalogName'] = catalog_name
    __args__['imageName'] = image_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azuresphere:getImage', __args__, opts=opts, typ=GetImageResult).value

    return AwaitableGetImageResult(
        component_id=pulumi.get(__ret__, 'component_id'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        image=pulumi.get(__ret__, 'image'),
        image_id=pulumi.get(__ret__, 'image_id'),
        image_name=pulumi.get(__ret__, 'image_name'),
        image_type=pulumi.get(__ret__, 'image_type'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        regional_data_boundary=pulumi.get(__ret__, 'regional_data_boundary'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        uri=pulumi.get(__ret__, 'uri'))


@_utilities.lift_output_func(get_image)
def get_image_output(catalog_name: Optional[pulumi.Input[str]] = None,
                     image_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImageResult]:
    """
    Get a Image
    Azure REST API version: 2022-09-01-preview.

    Other available API versions: 2024-04-01.


    :param str catalog_name: Name of catalog
    :param str image_name: Image name. Use an image GUID for GA versions of the API.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
