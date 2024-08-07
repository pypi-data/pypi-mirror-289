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
from ._enums import *

__all__ = [
    'WorkspaceCappingArgs',
    'WorkspaceCappingArgsDict',
    'WorkspaceFeaturesArgs',
    'WorkspaceFeaturesArgsDict',
    'WorkspaceSkuArgs',
    'WorkspaceSkuArgsDict',
]

MYPY = False

if not MYPY:
    class WorkspaceCappingArgsDict(TypedDict):
        """
        The daily volume cap for ingestion.
        """
        daily_quota_gb: NotRequired[pulumi.Input[float]]
        """
        The workspace daily quota for ingestion.
        """
elif False:
    WorkspaceCappingArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkspaceCappingArgs:
    def __init__(__self__, *,
                 daily_quota_gb: Optional[pulumi.Input[float]] = None):
        """
        The daily volume cap for ingestion.
        :param pulumi.Input[float] daily_quota_gb: The workspace daily quota for ingestion.
        """
        if daily_quota_gb is not None:
            pulumi.set(__self__, "daily_quota_gb", daily_quota_gb)

    @property
    @pulumi.getter(name="dailyQuotaGb")
    def daily_quota_gb(self) -> Optional[pulumi.Input[float]]:
        """
        The workspace daily quota for ingestion.
        """
        return pulumi.get(self, "daily_quota_gb")

    @daily_quota_gb.setter
    def daily_quota_gb(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "daily_quota_gb", value)


if not MYPY:
    class WorkspaceFeaturesArgsDict(TypedDict):
        """
        Workspace features.
        """
        cluster_resource_id: NotRequired[pulumi.Input[str]]
        """
        Dedicated LA cluster resourceId that is linked to the workspaces.
        """
        disable_local_auth: NotRequired[pulumi.Input[bool]]
        """
        Disable Non-AAD based Auth.
        """
        enable_data_export: NotRequired[pulumi.Input[bool]]
        """
        Flag that indicate if data should be exported.
        """
        enable_log_access_using_only_resource_permissions: NotRequired[pulumi.Input[bool]]
        """
        Flag that indicate which permission to use - resource or workspace or both.
        """
        immediate_purge_data_on30_days: NotRequired[pulumi.Input[bool]]
        """
        Flag that describes if we want to remove the data after 30 days.
        """
elif False:
    WorkspaceFeaturesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkspaceFeaturesArgs:
    def __init__(__self__, *,
                 cluster_resource_id: Optional[pulumi.Input[str]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 enable_data_export: Optional[pulumi.Input[bool]] = None,
                 enable_log_access_using_only_resource_permissions: Optional[pulumi.Input[bool]] = None,
                 immediate_purge_data_on30_days: Optional[pulumi.Input[bool]] = None):
        """
        Workspace features.
        :param pulumi.Input[str] cluster_resource_id: Dedicated LA cluster resourceId that is linked to the workspaces.
        :param pulumi.Input[bool] disable_local_auth: Disable Non-AAD based Auth.
        :param pulumi.Input[bool] enable_data_export: Flag that indicate if data should be exported.
        :param pulumi.Input[bool] enable_log_access_using_only_resource_permissions: Flag that indicate which permission to use - resource or workspace or both.
        :param pulumi.Input[bool] immediate_purge_data_on30_days: Flag that describes if we want to remove the data after 30 days.
        """
        if cluster_resource_id is not None:
            pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if enable_data_export is not None:
            pulumi.set(__self__, "enable_data_export", enable_data_export)
        if enable_log_access_using_only_resource_permissions is not None:
            pulumi.set(__self__, "enable_log_access_using_only_resource_permissions", enable_log_access_using_only_resource_permissions)
        if immediate_purge_data_on30_days is not None:
            pulumi.set(__self__, "immediate_purge_data_on30_days", immediate_purge_data_on30_days)

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Dedicated LA cluster resourceId that is linked to the workspaces.
        """
        return pulumi.get(self, "cluster_resource_id")

    @cluster_resource_id.setter
    def cluster_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_resource_id", value)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable Non-AAD based Auth.
        """
        return pulumi.get(self, "disable_local_auth")

    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_local_auth", value)

    @property
    @pulumi.getter(name="enableDataExport")
    def enable_data_export(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag that indicate if data should be exported.
        """
        return pulumi.get(self, "enable_data_export")

    @enable_data_export.setter
    def enable_data_export(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_data_export", value)

    @property
    @pulumi.getter(name="enableLogAccessUsingOnlyResourcePermissions")
    def enable_log_access_using_only_resource_permissions(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag that indicate which permission to use - resource or workspace or both.
        """
        return pulumi.get(self, "enable_log_access_using_only_resource_permissions")

    @enable_log_access_using_only_resource_permissions.setter
    def enable_log_access_using_only_resource_permissions(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_log_access_using_only_resource_permissions", value)

    @property
    @pulumi.getter(name="immediatePurgeDataOn30Days")
    def immediate_purge_data_on30_days(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag that describes if we want to remove the data after 30 days.
        """
        return pulumi.get(self, "immediate_purge_data_on30_days")

    @immediate_purge_data_on30_days.setter
    def immediate_purge_data_on30_days(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "immediate_purge_data_on30_days", value)


if not MYPY:
    class WorkspaceSkuArgsDict(TypedDict):
        """
        The SKU (tier) of a workspace.
        """
        name: pulumi.Input[Union[str, 'WorkspaceSkuNameEnum']]
        """
        The name of the SKU.
        """
        capacity_reservation_level: NotRequired[pulumi.Input[int]]
        """
        The capacity reservation level for this workspace, when CapacityReservation sku is selected.
        """
elif False:
    WorkspaceSkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WorkspaceSkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'WorkspaceSkuNameEnum']],
                 capacity_reservation_level: Optional[pulumi.Input[int]] = None):
        """
        The SKU (tier) of a workspace.
        :param pulumi.Input[Union[str, 'WorkspaceSkuNameEnum']] name: The name of the SKU.
        :param pulumi.Input[int] capacity_reservation_level: The capacity reservation level for this workspace, when CapacityReservation sku is selected.
        """
        pulumi.set(__self__, "name", name)
        if capacity_reservation_level is not None:
            pulumi.set(__self__, "capacity_reservation_level", capacity_reservation_level)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'WorkspaceSkuNameEnum']]:
        """
        The name of the SKU.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'WorkspaceSkuNameEnum']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="capacityReservationLevel")
    def capacity_reservation_level(self) -> Optional[pulumi.Input[int]]:
        """
        The capacity reservation level for this workspace, when CapacityReservation sku is selected.
        """
        return pulumi.get(self, "capacity_reservation_level")

    @capacity_reservation_level.setter
    def capacity_reservation_level(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity_reservation_level", value)


