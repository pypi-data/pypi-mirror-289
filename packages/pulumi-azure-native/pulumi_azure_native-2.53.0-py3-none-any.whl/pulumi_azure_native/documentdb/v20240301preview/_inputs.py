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
    'MongoClusterRestoreParametersArgs',
    'MongoClusterRestoreParametersArgsDict',
    'NodeGroupSpecArgs',
    'NodeGroupSpecArgsDict',
    'PrivateLinkServiceConnectionStateArgs',
    'PrivateLinkServiceConnectionStateArgsDict',
]

MYPY = False

if not MYPY:
    class MongoClusterRestoreParametersArgsDict(TypedDict):
        """
        Parameters used for restore operations
        """
        point_in_time_utc: NotRequired[pulumi.Input[str]]
        """
        UTC point in time to restore a mongo cluster
        """
        source_resource_id: NotRequired[pulumi.Input[str]]
        """
        Resource ID to locate the source cluster to restore
        """
elif False:
    MongoClusterRestoreParametersArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MongoClusterRestoreParametersArgs:
    def __init__(__self__, *,
                 point_in_time_utc: Optional[pulumi.Input[str]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Parameters used for restore operations
        :param pulumi.Input[str] point_in_time_utc: UTC point in time to restore a mongo cluster
        :param pulumi.Input[str] source_resource_id: Resource ID to locate the source cluster to restore
        """
        if point_in_time_utc is not None:
            pulumi.set(__self__, "point_in_time_utc", point_in_time_utc)
        if source_resource_id is not None:
            pulumi.set(__self__, "source_resource_id", source_resource_id)

    @property
    @pulumi.getter(name="pointInTimeUTC")
    def point_in_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        UTC point in time to restore a mongo cluster
        """
        return pulumi.get(self, "point_in_time_utc")

    @point_in_time_utc.setter
    def point_in_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "point_in_time_utc", value)

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID to locate the source cluster to restore
        """
        return pulumi.get(self, "source_resource_id")

    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_id", value)


if not MYPY:
    class NodeGroupSpecArgsDict(TypedDict):
        """
        Specification for a node group.
        """
        disk_size_gb: NotRequired[pulumi.Input[float]]
        """
        The disk storage size for the node group in GB. Example values: 128, 256, 512, 1024.
        """
        enable_ha: NotRequired[pulumi.Input[bool]]
        """
        Whether high availability is enabled on the node group.
        """
        kind: NotRequired[pulumi.Input[Union[str, 'NodeKind']]]
        """
        The node type deployed in the node group.
        """
        node_count: NotRequired[pulumi.Input[int]]
        """
        The number of nodes in the node group.
        """
        sku: NotRequired[pulumi.Input[str]]
        """
        The resource sku for the node group. This defines the size of CPU and memory that is provisioned for each node. Example values: 'M30', 'M40'.
        """
elif False:
    NodeGroupSpecArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class NodeGroupSpecArgs:
    def __init__(__self__, *,
                 disk_size_gb: Optional[pulumi.Input[float]] = None,
                 enable_ha: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'NodeKind']]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 sku: Optional[pulumi.Input[str]] = None):
        """
        Specification for a node group.
        :param pulumi.Input[float] disk_size_gb: The disk storage size for the node group in GB. Example values: 128, 256, 512, 1024.
        :param pulumi.Input[bool] enable_ha: Whether high availability is enabled on the node group.
        :param pulumi.Input[Union[str, 'NodeKind']] kind: The node type deployed in the node group.
        :param pulumi.Input[int] node_count: The number of nodes in the node group.
        :param pulumi.Input[str] sku: The resource sku for the node group. This defines the size of CPU and memory that is provisioned for each node. Example values: 'M30', 'M40'.
        """
        if disk_size_gb is not None:
            pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if enable_ha is not None:
            pulumi.set(__self__, "enable_ha", enable_ha)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if node_count is not None:
            pulumi.set(__self__, "node_count", node_count)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[float]]:
        """
        The disk storage size for the node group in GB. Example values: 128, 256, 512, 1024.
        """
        return pulumi.get(self, "disk_size_gb")

    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "disk_size_gb", value)

    @property
    @pulumi.getter(name="enableHa")
    def enable_ha(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether high availability is enabled on the node group.
        """
        return pulumi.get(self, "enable_ha")

    @enable_ha.setter
    def enable_ha(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_ha", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'NodeKind']]]:
        """
        The node type deployed in the node group.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'NodeKind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes in the node group.
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_count", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[str]]:
        """
        The resource sku for the node group. This defines the size of CPU and memory that is provisioned for each node. Example values: 'M30', 'M40'.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku", value)


if not MYPY:
    class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        actions_required: NotRequired[pulumi.Input[str]]
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        description: NotRequired[pulumi.Input[str]]
        """
        The reason for approval/rejection of the connection.
        """
        status: NotRequired[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
elif False:
    PrivateLinkServiceConnectionStateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[str] description: The reason for approval/rejection of the connection.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


