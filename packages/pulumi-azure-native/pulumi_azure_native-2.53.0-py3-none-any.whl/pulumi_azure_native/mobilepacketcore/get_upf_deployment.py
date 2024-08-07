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
    'GetUpfDeploymentResult',
    'AwaitableGetUpfDeploymentResult',
    'get_upf_deployment',
    'get_upf_deployment_output',
]

@pulumi.output_type
class GetUpfDeploymentResult:
    """
    Azure for Operators 5G Core User Plane Function (UPF) Deployment Resource
    """
    def __init__(__self__, cluster_service=None, component_parameters=None, id=None, location=None, name=None, operational_status=None, provisioning_state=None, release_version=None, secrets_parameters=None, system_data=None, tags=None, type=None):
        if cluster_service and not isinstance(cluster_service, str):
            raise TypeError("Expected argument 'cluster_service' to be a str")
        pulumi.set(__self__, "cluster_service", cluster_service)
        if component_parameters and not isinstance(component_parameters, str):
            raise TypeError("Expected argument 'component_parameters' to be a str")
        pulumi.set(__self__, "component_parameters", component_parameters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if operational_status and not isinstance(operational_status, dict):
            raise TypeError("Expected argument 'operational_status' to be a dict")
        pulumi.set(__self__, "operational_status", operational_status)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if release_version and not isinstance(release_version, str):
            raise TypeError("Expected argument 'release_version' to be a str")
        pulumi.set(__self__, "release_version", release_version)
        if secrets_parameters and not isinstance(secrets_parameters, str):
            raise TypeError("Expected argument 'secrets_parameters' to be a str")
        pulumi.set(__self__, "secrets_parameters", secrets_parameters)
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
    @pulumi.getter(name="clusterService")
    def cluster_service(self) -> str:
        """
        Reference to cluster where the Network Function is deployed
        """
        return pulumi.get(self, "cluster_service")

    @property
    @pulumi.getter(name="componentParameters")
    def component_parameters(self) -> str:
        """
        Azure for Operators 5G Core UPF component parameters
        """
        return pulumi.get(self, "component_parameters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
    @pulumi.getter(name="operationalStatus")
    def operational_status(self) -> 'outputs.OperationalStatusResponse':
        """
        Operational status
        """
        return pulumi.get(self, "operational_status")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> str:
        """
        Release version. This is inherited from the cluster
        """
        return pulumi.get(self, "release_version")

    @property
    @pulumi.getter(name="secretsParameters")
    def secrets_parameters(self) -> Optional[str]:
        """
        Azure for Operators 5G Core F secrets parameters
        """
        return pulumi.get(self, "secrets_parameters")

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


class AwaitableGetUpfDeploymentResult(GetUpfDeploymentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUpfDeploymentResult(
            cluster_service=self.cluster_service,
            component_parameters=self.component_parameters,
            id=self.id,
            location=self.location,
            name=self.name,
            operational_status=self.operational_status,
            provisioning_state=self.provisioning_state,
            release_version=self.release_version,
            secrets_parameters=self.secrets_parameters,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_upf_deployment(resource_group_name: Optional[str] = None,
                       upf_deployment_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUpfDeploymentResult:
    """
    Get a UpfDeploymentResource
    Azure REST API version: 2023-10-15-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str upf_deployment_name: The name of the UpfDeployment
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['upfDeploymentName'] = upf_deployment_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:mobilepacketcore:getUpfDeployment', __args__, opts=opts, typ=GetUpfDeploymentResult).value

    return AwaitableGetUpfDeploymentResult(
        cluster_service=pulumi.get(__ret__, 'cluster_service'),
        component_parameters=pulumi.get(__ret__, 'component_parameters'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        operational_status=pulumi.get(__ret__, 'operational_status'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        release_version=pulumi.get(__ret__, 'release_version'),
        secrets_parameters=pulumi.get(__ret__, 'secrets_parameters'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_upf_deployment)
def get_upf_deployment_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                              upf_deployment_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUpfDeploymentResult]:
    """
    Get a UpfDeploymentResource
    Azure REST API version: 2023-10-15-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str upf_deployment_name: The name of the UpfDeployment
    """
    ...
