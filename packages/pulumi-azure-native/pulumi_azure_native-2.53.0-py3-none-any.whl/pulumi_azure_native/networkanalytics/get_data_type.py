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
    'GetDataTypeResult',
    'AwaitableGetDataTypeResult',
    'get_data_type',
    'get_data_type_output',
]

@pulumi.output_type
class GetDataTypeResult:
    """
    The data type resource.
    """
    def __init__(__self__, database_cache_retention=None, database_retention=None, id=None, name=None, provisioning_state=None, state=None, state_reason=None, storage_output_retention=None, system_data=None, type=None, visualization_url=None):
        if database_cache_retention and not isinstance(database_cache_retention, int):
            raise TypeError("Expected argument 'database_cache_retention' to be a int")
        pulumi.set(__self__, "database_cache_retention", database_cache_retention)
        if database_retention and not isinstance(database_retention, int):
            raise TypeError("Expected argument 'database_retention' to be a int")
        pulumi.set(__self__, "database_retention", database_retention)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_reason and not isinstance(state_reason, str):
            raise TypeError("Expected argument 'state_reason' to be a str")
        pulumi.set(__self__, "state_reason", state_reason)
        if storage_output_retention and not isinstance(storage_output_retention, int):
            raise TypeError("Expected argument 'storage_output_retention' to be a int")
        pulumi.set(__self__, "storage_output_retention", storage_output_retention)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if visualization_url and not isinstance(visualization_url, str):
            raise TypeError("Expected argument 'visualization_url' to be a str")
        pulumi.set(__self__, "visualization_url", visualization_url)

    @property
    @pulumi.getter(name="databaseCacheRetention")
    def database_cache_retention(self) -> Optional[int]:
        """
        Field for database cache retention in days.
        """
        return pulumi.get(self, "database_cache_retention")

    @property
    @pulumi.getter(name="databaseRetention")
    def database_retention(self) -> Optional[int]:
        """
        Field for database data retention in days.
        """
        return pulumi.get(self, "database_retention")

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
        Latest provisioning state  of data product.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        State of data type.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> str:
        """
        Reason for the state of data type.
        """
        return pulumi.get(self, "state_reason")

    @property
    @pulumi.getter(name="storageOutputRetention")
    def storage_output_retention(self) -> Optional[int]:
        """
        Field for storage output retention in days.
        """
        return pulumi.get(self, "storage_output_retention")

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

    @property
    @pulumi.getter(name="visualizationUrl")
    def visualization_url(self) -> str:
        """
        Url for data visualization.
        """
        return pulumi.get(self, "visualization_url")


class AwaitableGetDataTypeResult(GetDataTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataTypeResult(
            database_cache_retention=self.database_cache_retention,
            database_retention=self.database_retention,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            state=self.state,
            state_reason=self.state_reason,
            storage_output_retention=self.storage_output_retention,
            system_data=self.system_data,
            type=self.type,
            visualization_url=self.visualization_url)


def get_data_type(data_product_name: Optional[str] = None,
                  data_type_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataTypeResult:
    """
    Retrieve data type resource.
    Azure REST API version: 2023-11-15.


    :param str data_product_name: The data product resource name
    :param str data_type_name: The data type name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['dataProductName'] = data_product_name
    __args__['dataTypeName'] = data_type_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkanalytics:getDataType', __args__, opts=opts, typ=GetDataTypeResult).value

    return AwaitableGetDataTypeResult(
        database_cache_retention=pulumi.get(__ret__, 'database_cache_retention'),
        database_retention=pulumi.get(__ret__, 'database_retention'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        state=pulumi.get(__ret__, 'state'),
        state_reason=pulumi.get(__ret__, 'state_reason'),
        storage_output_retention=pulumi.get(__ret__, 'storage_output_retention'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        visualization_url=pulumi.get(__ret__, 'visualization_url'))


@_utilities.lift_output_func(get_data_type)
def get_data_type_output(data_product_name: Optional[pulumi.Input[str]] = None,
                         data_type_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataTypeResult]:
    """
    Retrieve data type resource.
    Azure REST API version: 2023-11-15.


    :param str data_product_name: The data product resource name
    :param str data_type_name: The data type name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
