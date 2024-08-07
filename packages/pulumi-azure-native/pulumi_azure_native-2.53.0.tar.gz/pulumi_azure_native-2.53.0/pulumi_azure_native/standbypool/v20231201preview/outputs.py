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
from ._enums import *

__all__ = [
    'ContainerGroupProfileResponse',
    'ContainerGroupPropertiesResponse',
    'StandbyContainerGroupPoolElasticityProfileResponse',
    'StandbyVirtualMachinePoolElasticityProfileResponse',
    'SubnetResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class ContainerGroupProfileResponse(dict):
    """
    Details of the ContainerGroupProfile.
    """
    def __init__(__self__, *,
                 id: str,
                 revision: Optional[float] = None):
        """
        Details of the ContainerGroupProfile.
        :param str id: Specifies container group profile id of standby container groups.
        :param float revision: Specifies revision of container group profile.
        """
        pulumi.set(__self__, "id", id)
        if revision is not None:
            pulumi.set(__self__, "revision", revision)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Specifies container group profile id of standby container groups.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def revision(self) -> Optional[float]:
        """
        Specifies revision of container group profile.
        """
        return pulumi.get(self, "revision")


@pulumi.output_type
class ContainerGroupPropertiesResponse(dict):
    """
    Details of the ContainerGroupProperties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "containerGroupProfile":
            suggest = "container_group_profile"
        elif key == "subnetIds":
            suggest = "subnet_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerGroupPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerGroupPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerGroupPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 container_group_profile: 'outputs.ContainerGroupProfileResponse',
                 subnet_ids: Optional[Sequence['outputs.SubnetResponse']] = None):
        """
        Details of the ContainerGroupProperties.
        :param 'ContainerGroupProfileResponse' container_group_profile: Specifies container group profile of standby container groups.
        :param Sequence['SubnetResponse'] subnet_ids: Specifies subnet Ids for container group.
        """
        pulumi.set(__self__, "container_group_profile", container_group_profile)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="containerGroupProfile")
    def container_group_profile(self) -> 'outputs.ContainerGroupProfileResponse':
        """
        Specifies container group profile of standby container groups.
        """
        return pulumi.get(self, "container_group_profile")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence['outputs.SubnetResponse']]:
        """
        Specifies subnet Ids for container group.
        """
        return pulumi.get(self, "subnet_ids")


@pulumi.output_type
class StandbyContainerGroupPoolElasticityProfileResponse(dict):
    """
    Specifies the elasticity profile of the standby container group pools.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maxReadyCapacity":
            suggest = "max_ready_capacity"
        elif key == "refillPolicy":
            suggest = "refill_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StandbyContainerGroupPoolElasticityProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StandbyContainerGroupPoolElasticityProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StandbyContainerGroupPoolElasticityProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 max_ready_capacity: float,
                 refill_policy: Optional[str] = None):
        """
        Specifies the elasticity profile of the standby container group pools.
        :param float max_ready_capacity: Specifies maximum number of standby container groups in the standby pool.
        :param str refill_policy: Specifies refill policy of the pool.
        """
        pulumi.set(__self__, "max_ready_capacity", max_ready_capacity)
        if refill_policy is not None:
            pulumi.set(__self__, "refill_policy", refill_policy)

    @property
    @pulumi.getter(name="maxReadyCapacity")
    def max_ready_capacity(self) -> float:
        """
        Specifies maximum number of standby container groups in the standby pool.
        """
        return pulumi.get(self, "max_ready_capacity")

    @property
    @pulumi.getter(name="refillPolicy")
    def refill_policy(self) -> Optional[str]:
        """
        Specifies refill policy of the pool.
        """
        return pulumi.get(self, "refill_policy")


@pulumi.output_type
class StandbyVirtualMachinePoolElasticityProfileResponse(dict):
    """
    Details of the elasticity profile.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maxReadyCapacity":
            suggest = "max_ready_capacity"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StandbyVirtualMachinePoolElasticityProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StandbyVirtualMachinePoolElasticityProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StandbyVirtualMachinePoolElasticityProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 max_ready_capacity: float):
        """
        Details of the elasticity profile.
        :param float max_ready_capacity: Specifies the maximum number of virtual machines in the standby virtual machine pool.
        """
        pulumi.set(__self__, "max_ready_capacity", max_ready_capacity)

    @property
    @pulumi.getter(name="maxReadyCapacity")
    def max_ready_capacity(self) -> float:
        """
        Specifies the maximum number of virtual machines in the standby virtual machine pool.
        """
        return pulumi.get(self, "max_ready_capacity")


@pulumi.output_type
class SubnetResponse(dict):
    """
    Subnet of container group
    """
    def __init__(__self__, *,
                 id: str):
        """
        Subnet of container group
        :param str id: Specifies ARM resource id of the subnet.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Specifies ARM resource id of the subnet.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


