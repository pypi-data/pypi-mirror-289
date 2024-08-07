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
    'GetDatasetResult',
    'AwaitableGetDatasetResult',
    'get_dataset',
    'get_dataset_output',
]

@pulumi.output_type
class GetDatasetResult:
    """
    A Dataset resource belonging to an Instance resource.
    """
    def __init__(__self__, description=None, extended_location=None, id=None, keys=None, location=None, name=None, payload=None, provisioning_state=None, system_data=None, tags=None, timestamp=None, ttl=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if keys and not isinstance(keys, dict):
            raise TypeError("Expected argument 'keys' to be a dict")
        pulumi.set(__self__, "keys", keys)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if payload and not isinstance(payload, str):
            raise TypeError("Expected argument 'payload' to be a str")
        pulumi.set(__self__, "payload", payload)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if timestamp and not isinstance(timestamp, str):
            raise TypeError("Expected argument 'timestamp' to be a str")
        pulumi.set(__self__, "timestamp", timestamp)
        if ttl and not isinstance(ttl, str):
            raise TypeError("Expected argument 'ttl' to be a str")
        pulumi.set(__self__, "ttl", ttl)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Detailed description of the Dataset.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        Edge location of the resource.
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
    def keys(self) -> Optional[Mapping[str, 'outputs.DatasetPropertyKeyResponse']]:
        """
        List of keys that can be used for joining on enrich.
        """
        return pulumi.get(self, "keys")

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
    @pulumi.getter
    def payload(self) -> Optional[str]:
        """
        Path to the payload in the message. Enrich will add only the payload to the enriched message, other fields will not be kept except for in the indexes.
        """
        return pulumi.get(self, "payload")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
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
    def timestamp(self) -> Optional[str]:
        """
        Path to an RFC3339 timestamp in the message. If no path is provided, the ingestion time of the record is used for time-based joins.
        """
        return pulumi.get(self, "timestamp")

    @property
    @pulumi.getter
    def ttl(self) -> Optional[str]:
        """
        Time to live for individual records.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDatasetResult(GetDatasetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatasetResult(
            description=self.description,
            extended_location=self.extended_location,
            id=self.id,
            keys=self.keys,
            location=self.location,
            name=self.name,
            payload=self.payload,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            timestamp=self.timestamp,
            ttl=self.ttl,
            type=self.type)


def get_dataset(dataset_name: Optional[str] = None,
                instance_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatasetResult:
    """
    Get a Dataset
    Azure REST API version: 2023-10-04-preview.


    :param str dataset_name: Name of dataset.
    :param str instance_name: Name of instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['datasetName'] = dataset_name
    __args__['instanceName'] = instance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:iotoperationsdataprocessor:getDataset', __args__, opts=opts, typ=GetDatasetResult).value

    return AwaitableGetDatasetResult(
        description=pulumi.get(__ret__, 'description'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        keys=pulumi.get(__ret__, 'keys'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        payload=pulumi.get(__ret__, 'payload'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        timestamp=pulumi.get(__ret__, 'timestamp'),
        ttl=pulumi.get(__ret__, 'ttl'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_dataset)
def get_dataset_output(dataset_name: Optional[pulumi.Input[str]] = None,
                       instance_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatasetResult]:
    """
    Get a Dataset
    Azure REST API version: 2023-10-04-preview.


    :param str dataset_name: Name of dataset.
    :param str instance_name: Name of instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
