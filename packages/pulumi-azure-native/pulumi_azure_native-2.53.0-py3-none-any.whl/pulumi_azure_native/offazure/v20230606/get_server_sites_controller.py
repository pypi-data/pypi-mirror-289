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
    'GetServerSitesControllerResult',
    'AwaitableGetServerSitesControllerResult',
    'get_server_sites_controller',
    'get_server_sites_controller_output',
]

@pulumi.output_type
class GetServerSitesControllerResult:
    """
    A ServerSiteResource
    """
    def __init__(__self__, agent_details=None, appliance_name=None, discovery_solution_id=None, id=None, location=None, master_site_id=None, name=None, provisioning_state=None, service_endpoint=None, service_principal_identity_details=None, system_data=None, tags=None, type=None):
        if agent_details and not isinstance(agent_details, dict):
            raise TypeError("Expected argument 'agent_details' to be a dict")
        pulumi.set(__self__, "agent_details", agent_details)
        if appliance_name and not isinstance(appliance_name, str):
            raise TypeError("Expected argument 'appliance_name' to be a str")
        pulumi.set(__self__, "appliance_name", appliance_name)
        if discovery_solution_id and not isinstance(discovery_solution_id, str):
            raise TypeError("Expected argument 'discovery_solution_id' to be a str")
        pulumi.set(__self__, "discovery_solution_id", discovery_solution_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if master_site_id and not isinstance(master_site_id, str):
            raise TypeError("Expected argument 'master_site_id' to be a str")
        pulumi.set(__self__, "master_site_id", master_site_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_endpoint and not isinstance(service_endpoint, str):
            raise TypeError("Expected argument 'service_endpoint' to be a str")
        pulumi.set(__self__, "service_endpoint", service_endpoint)
        if service_principal_identity_details and not isinstance(service_principal_identity_details, dict):
            raise TypeError("Expected argument 'service_principal_identity_details' to be a dict")
        pulumi.set(__self__, "service_principal_identity_details", service_principal_identity_details)
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
    @pulumi.getter(name="agentDetails")
    def agent_details(self) -> Optional['outputs.SiteAgentPropertiesResponse']:
        """
        Gets or sets the on-premises agent details.
        """
        return pulumi.get(self, "agent_details")

    @property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> Optional[str]:
        """
        Gets or sets the Appliance Name.
        """
        return pulumi.get(self, "appliance_name")

    @property
    @pulumi.getter(name="discoverySolutionId")
    def discovery_solution_id(self) -> Optional[str]:
        """
        Gets or sets the ARM ID of migration hub solution for SDS.
        """
        return pulumi.get(self, "discovery_solution_id")

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
    def master_site_id(self) -> str:
        """
        Gets the Master Site this site is linked to.
        """
        return pulumi.get(self, "master_site_id")

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
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> str:
        """
        Gets the service endpoint.
        """
        return pulumi.get(self, "service_endpoint")

    @property
    @pulumi.getter(name="servicePrincipalIdentityDetails")
    def service_principal_identity_details(self) -> Optional['outputs.SiteSpnPropertiesResponse']:
        """
        Gets or sets the service principal identity details used by agent for
        communication
                    to the service.
        """
        return pulumi.get(self, "service_principal_identity_details")

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


class AwaitableGetServerSitesControllerResult(GetServerSitesControllerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerSitesControllerResult(
            agent_details=self.agent_details,
            appliance_name=self.appliance_name,
            discovery_solution_id=self.discovery_solution_id,
            id=self.id,
            location=self.location,
            master_site_id=self.master_site_id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            service_endpoint=self.service_endpoint,
            service_principal_identity_details=self.service_principal_identity_details,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_server_sites_controller(resource_group_name: Optional[str] = None,
                                site_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerSitesControllerResult:
    """
    Get a ServerSiteResource


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['siteName'] = site_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:offazure/v20230606:getServerSitesController', __args__, opts=opts, typ=GetServerSitesControllerResult).value

    return AwaitableGetServerSitesControllerResult(
        agent_details=pulumi.get(__ret__, 'agent_details'),
        appliance_name=pulumi.get(__ret__, 'appliance_name'),
        discovery_solution_id=pulumi.get(__ret__, 'discovery_solution_id'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        master_site_id=pulumi.get(__ret__, 'master_site_id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        service_endpoint=pulumi.get(__ret__, 'service_endpoint'),
        service_principal_identity_details=pulumi.get(__ret__, 'service_principal_identity_details'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_server_sites_controller)
def get_server_sites_controller_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                       site_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerSitesControllerResult]:
    """
    Get a ServerSiteResource


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    """
    ...
