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
    'GetSapDiscoverySiteResult',
    'AwaitableGetSapDiscoverySiteResult',
    'get_sap_discovery_site',
    'get_sap_discovery_site_output',
]

@pulumi.output_type
class GetSapDiscoverySiteResult:
    """
    Define the SAP Migration discovery site resource.
    """
    def __init__(__self__, errors=None, extended_location=None, id=None, location=None, master_site_id=None, migrate_project_id=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if errors and not isinstance(errors, dict):
            raise TypeError("Expected argument 'errors' to be a dict")
        pulumi.set(__self__, "errors", errors)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if master_site_id and not isinstance(master_site_id, str):
            raise TypeError("Expected argument 'master_site_id' to be a str")
        pulumi.set(__self__, "master_site_id", master_site_id)
        if migrate_project_id and not isinstance(migrate_project_id, str):
            raise TypeError("Expected argument 'migrate_project_id' to be a str")
        pulumi.set(__self__, "migrate_project_id", migrate_project_id)
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
    @pulumi.getter
    def errors(self) -> 'outputs.SAPMigrateErrorResponse':
        """
        Indicates any errors on the SAP Migration discovery site resource.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extended location definition.
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
    @pulumi.getter(name="masterSiteId")
    def master_site_id(self) -> Optional[str]:
        """
        The master site ID from Azure Migrate.
        """
        return pulumi.get(self, "master_site_id")

    @property
    @pulumi.getter(name="migrateProjectId")
    def migrate_project_id(self) -> Optional[str]:
        """
        The migrate project ID from Azure Migrate.
        """
        return pulumi.get(self, "migrate_project_id")

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
        Defines the provisioning states.
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


class AwaitableGetSapDiscoverySiteResult(GetSapDiscoverySiteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSapDiscoverySiteResult(
            errors=self.errors,
            extended_location=self.extended_location,
            id=self.id,
            location=self.location,
            master_site_id=self.master_site_id,
            migrate_project_id=self.migrate_project_id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_sap_discovery_site(resource_group_name: Optional[str] = None,
                           sap_discovery_site_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSapDiscoverySiteResult:
    """
    Gets a SAP Migration discovery site resource.
    Azure REST API version: 2023-10-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sap_discovery_site_name: The name of the discovery site resource for SAP Migration.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['sapDiscoverySiteName'] = sap_discovery_site_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:workloads:getSapDiscoverySite', __args__, opts=opts, typ=GetSapDiscoverySiteResult).value

    return AwaitableGetSapDiscoverySiteResult(
        errors=pulumi.get(__ret__, 'errors'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        master_site_id=pulumi.get(__ret__, 'master_site_id'),
        migrate_project_id=pulumi.get(__ret__, 'migrate_project_id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_sap_discovery_site)
def get_sap_discovery_site_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                  sap_discovery_site_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSapDiscoverySiteResult]:
    """
    Gets a SAP Migration discovery site resource.
    Azure REST API version: 2023-10-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sap_discovery_site_name: The name of the discovery site resource for SAP Migration.
    """
    ...
