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
    'GetSqlDWTableDataSetResult',
    'AwaitableGetSqlDWTableDataSetResult',
    'get_sql_dw_table_data_set',
    'get_sql_dw_table_data_set_output',
]

@pulumi.output_type
class GetSqlDWTableDataSetResult:
    """
    A SQL DW table data set.
    """
    def __init__(__self__, data_set_id=None, data_warehouse_name=None, id=None, kind=None, name=None, schema_name=None, sql_server_resource_id=None, system_data=None, table_name=None, type=None):
        if data_set_id and not isinstance(data_set_id, str):
            raise TypeError("Expected argument 'data_set_id' to be a str")
        pulumi.set(__self__, "data_set_id", data_set_id)
        if data_warehouse_name and not isinstance(data_warehouse_name, str):
            raise TypeError("Expected argument 'data_warehouse_name' to be a str")
        pulumi.set(__self__, "data_warehouse_name", data_warehouse_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schema_name and not isinstance(schema_name, str):
            raise TypeError("Expected argument 'schema_name' to be a str")
        pulumi.set(__self__, "schema_name", schema_name)
        if sql_server_resource_id and not isinstance(sql_server_resource_id, str):
            raise TypeError("Expected argument 'sql_server_resource_id' to be a str")
        pulumi.set(__self__, "sql_server_resource_id", sql_server_resource_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if table_name and not isinstance(table_name, str):
            raise TypeError("Expected argument 'table_name' to be a str")
        pulumi.set(__self__, "table_name", table_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> str:
        """
        Unique id for identifying a data set resource
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter(name="dataWarehouseName")
    def data_warehouse_name(self) -> str:
        """
        DataWarehouse name of the source data set
        """
        return pulumi.get(self, "data_warehouse_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of data set.
        Expected value is 'SqlDWTable'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> str:
        """
        Schema of the table. Default value is dbo.
        """
        return pulumi.get(self, "schema_name")

    @property
    @pulumi.getter(name="sqlServerResourceId")
    def sql_server_resource_id(self) -> str:
        """
        Resource id of SQL server
        """
        return pulumi.get(self, "sql_server_resource_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> str:
        """
        SQL DW table name.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")


class AwaitableGetSqlDWTableDataSetResult(GetSqlDWTableDataSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlDWTableDataSetResult(
            data_set_id=self.data_set_id,
            data_warehouse_name=self.data_warehouse_name,
            id=self.id,
            kind=self.kind,
            name=self.name,
            schema_name=self.schema_name,
            sql_server_resource_id=self.sql_server_resource_id,
            system_data=self.system_data,
            table_name=self.table_name,
            type=self.type)


def get_sql_dw_table_data_set(account_name: Optional[str] = None,
                              data_set_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              share_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlDWTableDataSetResult:
    """
    Get a DataSet in a share
    Azure REST API version: 2021-08-01.


    :param str account_name: The name of the share account.
    :param str data_set_name: The name of the dataSet.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetName'] = data_set_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datashare:getSqlDWTableDataSet', __args__, opts=opts, typ=GetSqlDWTableDataSetResult).value

    return AwaitableGetSqlDWTableDataSetResult(
        data_set_id=pulumi.get(__ret__, 'data_set_id'),
        data_warehouse_name=pulumi.get(__ret__, 'data_warehouse_name'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        schema_name=pulumi.get(__ret__, 'schema_name'),
        sql_server_resource_id=pulumi.get(__ret__, 'sql_server_resource_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        table_name=pulumi.get(__ret__, 'table_name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_sql_dw_table_data_set)
def get_sql_dw_table_data_set_output(account_name: Optional[pulumi.Input[str]] = None,
                                     data_set_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     share_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlDWTableDataSetResult]:
    """
    Get a DataSet in a share
    Azure REST API version: 2021-08-01.


    :param str account_name: The name of the share account.
    :param str data_set_name: The name of the dataSet.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    """
    ...
