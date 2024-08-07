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
    'GetCommunityTrainingResult',
    'AwaitableGetCommunityTrainingResult',
    'get_community_training',
    'get_community_training_output',
]

@pulumi.output_type
class GetCommunityTrainingResult:
    """
    A CommunityProviderHub resource
    """
    def __init__(__self__, disaster_recovery_enabled=None, id=None, identity_configuration=None, location=None, name=None, portal_admin_email_address=None, portal_name=None, portal_owner_email_address=None, portal_owner_organization_name=None, provisioning_state=None, sku=None, system_data=None, tags=None, type=None, zone_redundancy_enabled=None):
        if disaster_recovery_enabled and not isinstance(disaster_recovery_enabled, bool):
            raise TypeError("Expected argument 'disaster_recovery_enabled' to be a bool")
        pulumi.set(__self__, "disaster_recovery_enabled", disaster_recovery_enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_configuration and not isinstance(identity_configuration, dict):
            raise TypeError("Expected argument 'identity_configuration' to be a dict")
        pulumi.set(__self__, "identity_configuration", identity_configuration)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if portal_admin_email_address and not isinstance(portal_admin_email_address, str):
            raise TypeError("Expected argument 'portal_admin_email_address' to be a str")
        pulumi.set(__self__, "portal_admin_email_address", portal_admin_email_address)
        if portal_name and not isinstance(portal_name, str):
            raise TypeError("Expected argument 'portal_name' to be a str")
        pulumi.set(__self__, "portal_name", portal_name)
        if portal_owner_email_address and not isinstance(portal_owner_email_address, str):
            raise TypeError("Expected argument 'portal_owner_email_address' to be a str")
        pulumi.set(__self__, "portal_owner_email_address", portal_owner_email_address)
        if portal_owner_organization_name and not isinstance(portal_owner_organization_name, str):
            raise TypeError("Expected argument 'portal_owner_organization_name' to be a str")
        pulumi.set(__self__, "portal_owner_organization_name", portal_owner_organization_name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zone_redundancy_enabled and not isinstance(zone_redundancy_enabled, bool):
            raise TypeError("Expected argument 'zone_redundancy_enabled' to be a bool")
        pulumi.set(__self__, "zone_redundancy_enabled", zone_redundancy_enabled)

    @property
    @pulumi.getter(name="disasterRecoveryEnabled")
    def disaster_recovery_enabled(self) -> bool:
        """
        To indicate whether the Community Training instance has Disaster Recovery enabled
        """
        return pulumi.get(self, "disaster_recovery_enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityConfiguration")
    def identity_configuration(self) -> 'outputs.IdentityConfigurationPropertiesResponse':
        """
        The identity configuration of the Community Training resource
        """
        return pulumi.get(self, "identity_configuration")

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
    @pulumi.getter(name="portalAdminEmailAddress")
    def portal_admin_email_address(self) -> str:
        """
        The email address of the portal admin
        """
        return pulumi.get(self, "portal_admin_email_address")

    @property
    @pulumi.getter(name="portalName")
    def portal_name(self) -> str:
        """
        The portal name (website name) of the Community Training instance
        """
        return pulumi.get(self, "portal_name")

    @property
    @pulumi.getter(name="portalOwnerEmailAddress")
    def portal_owner_email_address(self) -> str:
        """
        The email address of the portal owner. Will be used as the primary contact
        """
        return pulumi.get(self, "portal_owner_email_address")

    @property
    @pulumi.getter(name="portalOwnerOrganizationName")
    def portal_owner_organization_name(self) -> str:
        """
        The organization name of the portal owner
        """
        return pulumi.get(self, "portal_owner_organization_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The SKU (Stock Keeping Unit) assigned to this resource.
        """
        return pulumi.get(self, "sku")

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
    @pulumi.getter(name="zoneRedundancyEnabled")
    def zone_redundancy_enabled(self) -> bool:
        """
        To indicate whether the Community Training instance has Zone Redundancy enabled
        """
        return pulumi.get(self, "zone_redundancy_enabled")


class AwaitableGetCommunityTrainingResult(GetCommunityTrainingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCommunityTrainingResult(
            disaster_recovery_enabled=self.disaster_recovery_enabled,
            id=self.id,
            identity_configuration=self.identity_configuration,
            location=self.location,
            name=self.name,
            portal_admin_email_address=self.portal_admin_email_address,
            portal_name=self.portal_name,
            portal_owner_email_address=self.portal_owner_email_address,
            portal_owner_organization_name=self.portal_owner_organization_name,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            zone_redundancy_enabled=self.zone_redundancy_enabled)


def get_community_training(community_training_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCommunityTrainingResult:
    """
    Get a CommunityTraining
    Azure REST API version: 2023-11-01.


    :param str community_training_name: The name of the Community Training Resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['communityTrainingName'] = community_training_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:community:getCommunityTraining', __args__, opts=opts, typ=GetCommunityTrainingResult).value

    return AwaitableGetCommunityTrainingResult(
        disaster_recovery_enabled=pulumi.get(__ret__, 'disaster_recovery_enabled'),
        id=pulumi.get(__ret__, 'id'),
        identity_configuration=pulumi.get(__ret__, 'identity_configuration'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        portal_admin_email_address=pulumi.get(__ret__, 'portal_admin_email_address'),
        portal_name=pulumi.get(__ret__, 'portal_name'),
        portal_owner_email_address=pulumi.get(__ret__, 'portal_owner_email_address'),
        portal_owner_organization_name=pulumi.get(__ret__, 'portal_owner_organization_name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        zone_redundancy_enabled=pulumi.get(__ret__, 'zone_redundancy_enabled'))


@_utilities.lift_output_func(get_community_training)
def get_community_training_output(community_training_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCommunityTrainingResult]:
    """
    Get a CommunityTraining
    Azure REST API version: 2023-11-01.


    :param str community_training_name: The name of the Community Training Resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
