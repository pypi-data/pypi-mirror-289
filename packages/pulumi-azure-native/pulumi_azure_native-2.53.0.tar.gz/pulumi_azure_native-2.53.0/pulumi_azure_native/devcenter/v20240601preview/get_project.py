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
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    """
    Represents a project resource.
    """
    def __init__(__self__, catalog_settings=None, description=None, dev_center_id=None, dev_center_uri=None, display_name=None, id=None, identity=None, location=None, max_dev_boxes_per_user=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if catalog_settings and not isinstance(catalog_settings, dict):
            raise TypeError("Expected argument 'catalog_settings' to be a dict")
        pulumi.set(__self__, "catalog_settings", catalog_settings)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dev_center_id and not isinstance(dev_center_id, str):
            raise TypeError("Expected argument 'dev_center_id' to be a str")
        pulumi.set(__self__, "dev_center_id", dev_center_id)
        if dev_center_uri and not isinstance(dev_center_uri, str):
            raise TypeError("Expected argument 'dev_center_uri' to be a str")
        pulumi.set(__self__, "dev_center_uri", dev_center_uri)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_dev_boxes_per_user and not isinstance(max_dev_boxes_per_user, int):
            raise TypeError("Expected argument 'max_dev_boxes_per_user' to be a int")
        pulumi.set(__self__, "max_dev_boxes_per_user", max_dev_boxes_per_user)
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
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="catalogSettings")
    def catalog_settings(self) -> Optional['outputs.ProjectCatalogSettingsResponse']:
        """
        Settings to be used when associating a project with a catalog.
        """
        return pulumi.get(self, "catalog_settings")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the project.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="devCenterId")
    def dev_center_id(self) -> Optional[str]:
        """
        Resource Id of an associated DevCenter
        """
        return pulumi.get(self, "dev_center_id")

    @property
    @pulumi.getter(name="devCenterUri")
    def dev_center_uri(self) -> str:
        """
        The URI of the Dev Center resource this project is associated with.
        """
        return pulumi.get(self, "dev_center_uri")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the project.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        Managed identity properties
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxDevBoxesPerUser")
    def max_dev_boxes_per_user(self) -> Optional[int]:
        """
        When specified, limits the maximum number of Dev Boxes a single user can create across all pools in the project. This will have no effect on existing Dev Boxes when reduced.
        """
        return pulumi.get(self, "max_dev_boxes_per_user")

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
        The provisioning state of the resource.
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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            catalog_settings=self.catalog_settings,
            description=self.description,
            dev_center_id=self.dev_center_id,
            dev_center_uri=self.dev_center_uri,
            display_name=self.display_name,
            id=self.id,
            identity=self.identity,
            location=self.location,
            max_dev_boxes_per_user=self.max_dev_boxes_per_user,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_project(project_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    Gets a specific project.


    :param str project_name: The name of the project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20240601preview:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        catalog_settings=pulumi.get(__ret__, 'catalog_settings'),
        description=pulumi.get(__ret__, 'description'),
        dev_center_id=pulumi.get(__ret__, 'dev_center_id'),
        dev_center_uri=pulumi.get(__ret__, 'dev_center_uri'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        max_dev_boxes_per_user=pulumi.get(__ret__, 'max_dev_boxes_per_user'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_project)
def get_project_output(project_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    Gets a specific project.


    :param str project_name: The name of the project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
