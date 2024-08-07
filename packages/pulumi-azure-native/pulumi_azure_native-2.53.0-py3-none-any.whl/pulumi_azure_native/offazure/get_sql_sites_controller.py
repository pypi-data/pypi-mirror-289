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
    'GetSqlSitesControllerResult',
    'AwaitableGetSqlSitesControllerResult',
    'get_sql_sites_controller',
    'get_sql_sites_controller_output',
]

@pulumi.output_type
class GetSqlSitesControllerResult:
    """
    SQL site web model.
    """
    def __init__(__self__, discovery_scenario=None, id=None, name=None, provisioning_state=None, service_endpoint=None, site_appliance_properties_collection=None, system_data=None, type=None):
        if discovery_scenario and not isinstance(discovery_scenario, str):
            raise TypeError("Expected argument 'discovery_scenario' to be a str")
        pulumi.set(__self__, "discovery_scenario", discovery_scenario)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_endpoint and not isinstance(service_endpoint, str):
            raise TypeError("Expected argument 'service_endpoint' to be a str")
        pulumi.set(__self__, "service_endpoint", service_endpoint)
        if site_appliance_properties_collection and not isinstance(site_appliance_properties_collection, list):
            raise TypeError("Expected argument 'site_appliance_properties_collection' to be a list")
        pulumi.set(__self__, "site_appliance_properties_collection", site_appliance_properties_collection)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="discoveryScenario")
    def discovery_scenario(self) -> Optional[str]:
        """
        Gets or sets the discovery scenario.
        """
        return pulumi.get(self, "discovery_scenario")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

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
        provisioning state enum
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> str:
        """
        Gets the service endpoint.
        """
        return pulumi.get(self, "service_endpoint")

    @property
    @pulumi.getter(name="siteAppliancePropertiesCollection")
    def site_appliance_properties_collection(self) -> Optional[Sequence['outputs.SiteAppliancePropertiesResponse']]:
        """
        Gets or sets the appliance details used by service to communicate
                   
        to the appliance.
        """
        return pulumi.get(self, "site_appliance_properties_collection")

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


class AwaitableGetSqlSitesControllerResult(GetSqlSitesControllerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlSitesControllerResult(
            discovery_scenario=self.discovery_scenario,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            service_endpoint=self.service_endpoint,
            site_appliance_properties_collection=self.site_appliance_properties_collection,
            system_data=self.system_data,
            type=self.type)


def get_sql_sites_controller(resource_group_name: Optional[str] = None,
                             site_name: Optional[str] = None,
                             sql_site_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlSitesControllerResult:
    """
    Method to get a site.
    Azure REST API version: 2023-06-06.

    Other available API versions: 2023-10-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    :param str sql_site_name: SQL site name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['siteName'] = site_name
    __args__['sqlSiteName'] = sql_site_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:offazure:getSqlSitesController', __args__, opts=opts, typ=GetSqlSitesControllerResult).value

    return AwaitableGetSqlSitesControllerResult(
        discovery_scenario=pulumi.get(__ret__, 'discovery_scenario'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        service_endpoint=pulumi.get(__ret__, 'service_endpoint'),
        site_appliance_properties_collection=pulumi.get(__ret__, 'site_appliance_properties_collection'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_sql_sites_controller)
def get_sql_sites_controller_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                    site_name: Optional[pulumi.Input[str]] = None,
                                    sql_site_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlSitesControllerResult]:
    """
    Method to get a site.
    Azure REST API version: 2023-06-06.

    Other available API versions: 2023-10-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    :param str sql_site_name: SQL site name.
    """
    ...
