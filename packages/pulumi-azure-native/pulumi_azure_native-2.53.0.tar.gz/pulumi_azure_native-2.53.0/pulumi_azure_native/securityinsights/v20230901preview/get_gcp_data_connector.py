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
    'GetGCPDataConnectorResult',
    'AwaitableGetGCPDataConnectorResult',
    'get_gcp_data_connector',
    'get_gcp_data_connector_output',
]

@pulumi.output_type
class GetGCPDataConnectorResult:
    """
    Represents Google Cloud Platform data connector.
    """
    def __init__(__self__, auth=None, connector_definition_name=None, dcr_config=None, etag=None, id=None, kind=None, name=None, request=None, system_data=None, type=None):
        if auth and not isinstance(auth, dict):
            raise TypeError("Expected argument 'auth' to be a dict")
        pulumi.set(__self__, "auth", auth)
        if connector_definition_name and not isinstance(connector_definition_name, str):
            raise TypeError("Expected argument 'connector_definition_name' to be a str")
        pulumi.set(__self__, "connector_definition_name", connector_definition_name)
        if dcr_config and not isinstance(dcr_config, dict):
            raise TypeError("Expected argument 'dcr_config' to be a dict")
        pulumi.set(__self__, "dcr_config", dcr_config)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if request and not isinstance(request, dict):
            raise TypeError("Expected argument 'request' to be a dict")
        pulumi.set(__self__, "request", request)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def auth(self) -> 'outputs.GCPAuthPropertiesResponse':
        """
        The auth section of the connector.
        """
        return pulumi.get(self, "auth")

    @property
    @pulumi.getter(name="connectorDefinitionName")
    def connector_definition_name(self) -> str:
        """
        The name of the connector definition that represents the UI config.
        """
        return pulumi.get(self, "connector_definition_name")

    @property
    @pulumi.getter(name="dcrConfig")
    def dcr_config(self) -> Optional['outputs.DCRConfigurationResponse']:
        """
        The configuration of the destination of the data.
        """
        return pulumi.get(self, "dcr_config")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
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
    def kind(self) -> str:
        """
        The kind of the data connector
        Expected value is 'GCP'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def request(self) -> 'outputs.GCPRequestPropertiesResponse':
        """
        The request section of the connector.
        """
        return pulumi.get(self, "request")

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


class AwaitableGetGCPDataConnectorResult(GetGCPDataConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGCPDataConnectorResult(
            auth=self.auth,
            connector_definition_name=self.connector_definition_name,
            dcr_config=self.dcr_config,
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            name=self.name,
            request=self.request,
            system_data=self.system_data,
            type=self.type)


def get_gcp_data_connector(data_connector_id: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           workspace_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGCPDataConnectorResult:
    """
    Gets a data connector.


    :param str data_connector_id: Connector ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['dataConnectorId'] = data_connector_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20230901preview:getGCPDataConnector', __args__, opts=opts, typ=GetGCPDataConnectorResult).value

    return AwaitableGetGCPDataConnectorResult(
        auth=pulumi.get(__ret__, 'auth'),
        connector_definition_name=pulumi.get(__ret__, 'connector_definition_name'),
        dcr_config=pulumi.get(__ret__, 'dcr_config'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        request=pulumi.get(__ret__, 'request'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_gcp_data_connector)
def get_gcp_data_connector_output(data_connector_id: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  workspace_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGCPDataConnectorResult]:
    """
    Gets a data connector.


    :param str data_connector_id: Connector ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
