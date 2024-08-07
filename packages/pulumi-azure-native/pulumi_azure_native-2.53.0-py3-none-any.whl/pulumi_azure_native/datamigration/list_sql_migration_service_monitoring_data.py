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
    'ListSqlMigrationServiceMonitoringDataResult',
    'AwaitableListSqlMigrationServiceMonitoringDataResult',
    'list_sql_migration_service_monitoring_data',
    'list_sql_migration_service_monitoring_data_output',
]

@pulumi.output_type
class ListSqlMigrationServiceMonitoringDataResult:
    """
    Integration Runtime Monitoring Data.
    """
    def __init__(__self__, name=None, nodes=None):
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nodes and not isinstance(nodes, list):
            raise TypeError("Expected argument 'nodes' to be a list")
        pulumi.set(__self__, "nodes", nodes)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of Integration Runtime.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nodes(self) -> Sequence['outputs.NodeMonitoringDataResponse']:
        """
        Integration Runtime node monitoring data.
        """
        return pulumi.get(self, "nodes")


class AwaitableListSqlMigrationServiceMonitoringDataResult(ListSqlMigrationServiceMonitoringDataResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSqlMigrationServiceMonitoringDataResult(
            name=self.name,
            nodes=self.nodes)


def list_sql_migration_service_monitoring_data(resource_group_name: Optional[str] = None,
                                               sql_migration_service_name: Optional[str] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSqlMigrationServiceMonitoringDataResult:
    """
    Retrieve the registered Integration Runtime nodes and their monitoring data for a given Database Migration Service.
    Azure REST API version: 2022-03-30-preview.

    Other available API versions: 2023-07-15-preview.


    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_migration_service_name: Name of the SQL Migration Service.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['sqlMigrationServiceName'] = sql_migration_service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datamigration:listSqlMigrationServiceMonitoringData', __args__, opts=opts, typ=ListSqlMigrationServiceMonitoringDataResult).value

    return AwaitableListSqlMigrationServiceMonitoringDataResult(
        name=pulumi.get(__ret__, 'name'),
        nodes=pulumi.get(__ret__, 'nodes'))


@_utilities.lift_output_func(list_sql_migration_service_monitoring_data)
def list_sql_migration_service_monitoring_data_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                      sql_migration_service_name: Optional[pulumi.Input[str]] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListSqlMigrationServiceMonitoringDataResult]:
    """
    Retrieve the registered Integration Runtime nodes and their monitoring data for a given Database Migration Service.
    Azure REST API version: 2022-03-30-preview.

    Other available API versions: 2023-07-15-preview.


    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_migration_service_name: Name of the SQL Migration Service.
    """
    ...
