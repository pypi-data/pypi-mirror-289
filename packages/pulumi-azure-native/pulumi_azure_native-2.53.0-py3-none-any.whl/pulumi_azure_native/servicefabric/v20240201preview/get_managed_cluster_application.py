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
    'GetManagedClusterApplicationResult',
    'AwaitableGetManagedClusterApplicationResult',
    'get_managed_cluster_application',
    'get_managed_cluster_application_output',
]

@pulumi.output_type
class GetManagedClusterApplicationResult:
    """
    The application resource.
    """
    def __init__(__self__, id=None, identity=None, location=None, managed_identities=None, name=None, parameters=None, provisioning_state=None, system_data=None, tags=None, type=None, upgrade_policy=None, version=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_identities and not isinstance(managed_identities, list):
            raise TypeError("Expected argument 'managed_identities' to be a list")
        pulumi.set(__self__, "managed_identities", managed_identities)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
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
        if upgrade_policy and not isinstance(upgrade_policy, dict):
            raise TypeError("Expected argument 'upgrade_policy' to be a dict")
        pulumi.set(__self__, "upgrade_policy", upgrade_policy)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedIdentityResponse']:
        """
        Describes the managed identities for an Azure resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location depends on the parent resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedIdentities")
    def managed_identities(self) -> Optional[Sequence['outputs.ApplicationUserAssignedIdentityResponse']]:
        """
        List of user assigned identities for the application, each mapped to a friendly name.
        """
        return pulumi.get(self, "managed_identities")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, str]]:
        """
        List of application parameters with overridden values from their default values specified in the application manifest.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment or provisioning state, which only appears in the response
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional['outputs.ApplicationUpgradePolicyResponse']:
        """
        Describes the policy for a monitored application upgrade.
        """
        return pulumi.get(self, "upgrade_policy")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the application type as defined in the application manifest.
        This name must be the full Arm Resource ID for the referenced application type version.
        """
        return pulumi.get(self, "version")


class AwaitableGetManagedClusterApplicationResult(GetManagedClusterApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedClusterApplicationResult(
            id=self.id,
            identity=self.identity,
            location=self.location,
            managed_identities=self.managed_identities,
            name=self.name,
            parameters=self.parameters,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            upgrade_policy=self.upgrade_policy,
            version=self.version)


def get_managed_cluster_application(application_name: Optional[str] = None,
                                    cluster_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedClusterApplicationResult:
    """
    Get a Service Fabric managed application resource created or in the process of being created in the Service Fabric cluster resource.


    :param str application_name: The name of the application resource.
    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['applicationName'] = application_name
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabric/v20240201preview:getManagedClusterApplication', __args__, opts=opts, typ=GetManagedClusterApplicationResult).value

    return AwaitableGetManagedClusterApplicationResult(
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        managed_identities=pulumi.get(__ret__, 'managed_identities'),
        name=pulumi.get(__ret__, 'name'),
        parameters=pulumi.get(__ret__, 'parameters'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        upgrade_policy=pulumi.get(__ret__, 'upgrade_policy'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_managed_cluster_application)
def get_managed_cluster_application_output(application_name: Optional[pulumi.Input[str]] = None,
                                           cluster_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedClusterApplicationResult]:
    """
    Get a Service Fabric managed application resource created or in the process of being created in the Service Fabric cluster resource.


    :param str application_name: The name of the application resource.
    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    ...
