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
    'GetVideoAnalyzerResult',
    'AwaitableGetVideoAnalyzerResult',
    'get_video_analyzer',
    'get_video_analyzer_output',
]

@pulumi.output_type
class GetVideoAnalyzerResult:
    """
    The Video Analyzer account.
    """
    def __init__(__self__, encryption=None, endpoints=None, id=None, identity=None, iot_hubs=None, location=None, name=None, network_access_control=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, storage_accounts=None, system_data=None, tags=None, type=None):
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        pulumi.set(__self__, "endpoints", endpoints)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if iot_hubs and not isinstance(iot_hubs, list):
            raise TypeError("Expected argument 'iot_hubs' to be a list")
        pulumi.set(__self__, "iot_hubs", iot_hubs)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_access_control and not isinstance(network_access_control, dict):
            raise TypeError("Expected argument 'network_access_control' to be a dict")
        pulumi.set(__self__, "network_access_control", network_access_control)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if storage_accounts and not isinstance(storage_accounts, list):
            raise TypeError("Expected argument 'storage_accounts' to be a list")
        pulumi.set(__self__, "storage_accounts", storage_accounts)
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
    def encryption(self) -> Optional['outputs.AccountEncryptionResponse']:
        """
        The account encryption properties.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence['outputs.EndpointResponse']:
        """
        The endpoints associated with this resource.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.VideoAnalyzerIdentityResponse']:
        """
        The identities associated to the Video Analyzer resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(self) -> Optional[Sequence['outputs.IotHubResponse']]:
        """
        The IoT Hubs for this resource.
        """
        return pulumi.get(self, "iot_hubs")

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
    @pulumi.getter(name="networkAccessControl")
    def network_access_control(self) -> Optional['outputs.NetworkAccessControlResponse']:
        """
        Network access control for Video Analyzer.
        """
        return pulumi.get(self, "network_access_control")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        Private Endpoint Connections created under Video Analyzer account.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the Video Analyzer account.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Whether or not public network access is allowed for resources under the Video Analyzer account.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> Sequence['outputs.StorageAccountResponse']:
        """
        The storage accounts for this resource.
        """
        return pulumi.get(self, "storage_accounts")

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


class AwaitableGetVideoAnalyzerResult(GetVideoAnalyzerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVideoAnalyzerResult(
            encryption=self.encryption,
            endpoints=self.endpoints,
            id=self.id,
            identity=self.identity,
            iot_hubs=self.iot_hubs,
            location=self.location,
            name=self.name,
            network_access_control=self.network_access_control,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            storage_accounts=self.storage_accounts,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_video_analyzer(account_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVideoAnalyzerResult:
    """
    Get the details of the specified Video Analyzer account


    :param str account_name: The Video Analyzer account name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:videoanalyzer/v20211101preview:getVideoAnalyzer', __args__, opts=opts, typ=GetVideoAnalyzerResult).value

    return AwaitableGetVideoAnalyzerResult(
        encryption=pulumi.get(__ret__, 'encryption'),
        endpoints=pulumi.get(__ret__, 'endpoints'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        iot_hubs=pulumi.get(__ret__, 'iot_hubs'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_access_control=pulumi.get(__ret__, 'network_access_control'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        storage_accounts=pulumi.get(__ret__, 'storage_accounts'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_video_analyzer)
def get_video_analyzer_output(account_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVideoAnalyzerResult]:
    """
    Get the details of the specified Video Analyzer account


    :param str account_name: The Video Analyzer account name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
