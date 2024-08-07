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
    'GetAzureMonitorWorkspaceResult',
    'AwaitableGetAzureMonitorWorkspaceResult',
    'get_azure_monitor_workspace',
    'get_azure_monitor_workspace_output',
]

@pulumi.output_type
class GetAzureMonitorWorkspaceResult:
    """
    An Azure Monitor Workspace definition
    """
    def __init__(__self__, account_id=None, default_ingestion_settings=None, etag=None, id=None, location=None, metrics=None, name=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, system_data=None, tags=None, type=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if default_ingestion_settings and not isinstance(default_ingestion_settings, dict):
            raise TypeError("Expected argument 'default_ingestion_settings' to be a dict")
        pulumi.set(__self__, "default_ingestion_settings", default_ingestion_settings)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if metrics and not isinstance(metrics, dict):
            raise TypeError("Expected argument 'metrics' to be a dict")
        pulumi.set(__self__, "metrics", metrics)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
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
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The immutable Id of the Azure Monitor Workspace. This property is read-only.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="defaultIngestionSettings")
    def default_ingestion_settings(self) -> 'outputs.AzureMonitorWorkspaceResponseDefaultIngestionSettings':
        """
        The Data Collection Rule and Endpoint used for ingestion by default.
        """
        return pulumi.get(self, "default_ingestion_settings")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Resource entity tag (ETag)
        """
        return pulumi.get(self, "etag")

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
    def metrics(self) -> 'outputs.AzureMonitorWorkspaceResponseMetrics':
        """
        Properties related to the metrics container in the Azure Monitor Workspace
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        List of private endpoint connections
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the Azure Monitor Workspace. Set to Succeeded if everything is healthy.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Gets or sets allow or disallow public network access to Azure Monitor Workspace
        """
        return pulumi.get(self, "public_network_access")

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


class AwaitableGetAzureMonitorWorkspaceResult(GetAzureMonitorWorkspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAzureMonitorWorkspaceResult(
            account_id=self.account_id,
            default_ingestion_settings=self.default_ingestion_settings,
            etag=self.etag,
            id=self.id,
            location=self.location,
            metrics=self.metrics,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_azure_monitor_workspace(azure_monitor_workspace_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAzureMonitorWorkspaceResult:
    """
    Returns the specified Azure Monitor Workspace


    :param str azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case insensitive
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['azureMonitorWorkspaceName'] = azure_monitor_workspace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:monitor/v20230403:getAzureMonitorWorkspace', __args__, opts=opts, typ=GetAzureMonitorWorkspaceResult).value

    return AwaitableGetAzureMonitorWorkspaceResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        default_ingestion_settings=pulumi.get(__ret__, 'default_ingestion_settings'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        metrics=pulumi.get(__ret__, 'metrics'),
        name=pulumi.get(__ret__, 'name'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_azure_monitor_workspace)
def get_azure_monitor_workspace_output(azure_monitor_workspace_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAzureMonitorWorkspaceResult]:
    """
    Returns the specified Azure Monitor Workspace


    :param str azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case insensitive
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
