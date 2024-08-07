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
from ._enums import *

__all__ = [
    'GitCatalogArgs',
    'GitCatalogArgsDict',
    'ImageReferenceArgs',
    'ImageReferenceArgsDict',
    'ManagedServiceIdentityArgs',
    'ManagedServiceIdentityArgsDict',
    'ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs',
    'ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgsDict',
    'SkuArgs',
    'SkuArgsDict',
    'StopOnDisconnectConfigurationArgs',
    'StopOnDisconnectConfigurationArgsDict',
    'UserRoleAssignmentArgs',
    'UserRoleAssignmentArgsDict',
]

MYPY = False

if not MYPY:
    class GitCatalogArgsDict(TypedDict):
        """
        Properties for a Git repository catalog.
        """
        branch: NotRequired[pulumi.Input[str]]
        """
        Git branch.
        """
        path: NotRequired[pulumi.Input[str]]
        """
        The folder where the catalog items can be found inside the repository.
        """
        secret_identifier: NotRequired[pulumi.Input[str]]
        """
        A reference to the Key Vault secret containing a security token to authenticate to a Git repository.
        """
        uri: NotRequired[pulumi.Input[str]]
        """
        Git URI.
        """
elif False:
    GitCatalogArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GitCatalogArgs:
    def __init__(__self__, *,
                 branch: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 secret_identifier: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        Properties for a Git repository catalog.
        :param pulumi.Input[str] branch: Git branch.
        :param pulumi.Input[str] path: The folder where the catalog items can be found inside the repository.
        :param pulumi.Input[str] secret_identifier: A reference to the Key Vault secret containing a security token to authenticate to a Git repository.
        :param pulumi.Input[str] uri: Git URI.
        """
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if secret_identifier is not None:
            pulumi.set(__self__, "secret_identifier", secret_identifier)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[str]]:
        """
        Git branch.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The folder where the catalog items can be found inside the repository.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="secretIdentifier")
    def secret_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the Key Vault secret containing a security token to authenticate to a Git repository.
        """
        return pulumi.get(self, "secret_identifier")

    @secret_identifier.setter
    def secret_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_identifier", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        Git URI.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


if not MYPY:
    class ImageReferenceArgsDict(TypedDict):
        """
        Image reference information
        """
        id: NotRequired[pulumi.Input[str]]
        """
        Image ID, or Image version ID. When Image ID is provided, its latest version will be used.
        """
elif False:
    ImageReferenceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ImageReferenceArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        Image reference information
        :param pulumi.Input[str] id: Image ID, or Image version ID. When Image ID is provided, its latest version will be used.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Image ID, or Image version ID. When Image ID is provided, its latest version will be used.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


if not MYPY:
    class ManagedServiceIdentityArgsDict(TypedDict):
        """
        Managed service identity (system assigned and/or user assigned identities)
        """
        type: pulumi.Input[Union[str, 'ManagedServiceIdentityType']]
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
elif False:
    ManagedServiceIdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'ManagedServiceIdentityType']],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Managed service identity (system assigned and/or user assigned identities)
        :param pulumi.Input[Union[str, 'ManagedServiceIdentityType']] type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ManagedServiceIdentityType']]:
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ManagedServiceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


if not MYPY:
    class ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgsDict(TypedDict):
        """
        The role definition assigned to the environment creator on backing resources.
        """
        roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        A map of roles to assign to the environment creator.
        """
elif False:
    ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs:
    def __init__(__self__, *,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The role definition assigned to the environment creator on backing resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A map of roles to assign to the environment creator.
        """
        if roles is not None:
            pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A map of roles to assign to the environment creator.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)


if not MYPY:
    class SkuArgsDict(TypedDict):
        """
        The resource model definition representing SKU
        """
        name: pulumi.Input[str]
        """
        The name of the SKU. E.g. P3. It is typically a letter+number code
        """
        capacity: NotRequired[pulumi.Input[int]]
        """
        If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        """
        family: NotRequired[pulumi.Input[str]]
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here.
        """
        size: NotRequired[pulumi.Input[str]]
        """
        The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        """
        tier: NotRequired[pulumi.Input['SkuTier']]
        """
        This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
elif False:
    SkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 capacity: Optional[pulumi.Input[int]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input['SkuTier']] = None):
        """
        The resource model definition representing SKU
        :param pulumi.Input[str] name: The name of the SKU. E.g. P3. It is typically a letter+number code
        :param pulumi.Input[int] capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        :param pulumi.Input[str] family: If the service has different generations of hardware, for the same SKU, then that can be captured here.
        :param pulumi.Input[str] size: The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        :param pulumi.Input['SkuTier'] tier: This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the SKU. E.g. P3. It is typically a letter+number code
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[str]]:
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input['SkuTier']]:
        """
        This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input['SkuTier']]):
        pulumi.set(self, "tier", value)


if not MYPY:
    class StopOnDisconnectConfigurationArgsDict(TypedDict):
        """
        Stop on disconnect configuration settings for Dev Boxes created in this pool.
        """
        grace_period_minutes: NotRequired[pulumi.Input[int]]
        """
        The specified time in minutes to wait before stopping a Dev Box once disconnect is detected.
        """
        status: NotRequired[pulumi.Input[Union[str, 'StopOnDisconnectEnableStatus']]]
        """
        Whether the feature to stop the Dev Box on disconnect once the grace period has lapsed is enabled.
        """
elif False:
    StopOnDisconnectConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class StopOnDisconnectConfigurationArgs:
    def __init__(__self__, *,
                 grace_period_minutes: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[Union[str, 'StopOnDisconnectEnableStatus']]] = None):
        """
        Stop on disconnect configuration settings for Dev Boxes created in this pool.
        :param pulumi.Input[int] grace_period_minutes: The specified time in minutes to wait before stopping a Dev Box once disconnect is detected.
        :param pulumi.Input[Union[str, 'StopOnDisconnectEnableStatus']] status: Whether the feature to stop the Dev Box on disconnect once the grace period has lapsed is enabled.
        """
        if grace_period_minutes is not None:
            pulumi.set(__self__, "grace_period_minutes", grace_period_minutes)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="gracePeriodMinutes")
    def grace_period_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The specified time in minutes to wait before stopping a Dev Box once disconnect is detected.
        """
        return pulumi.get(self, "grace_period_minutes")

    @grace_period_minutes.setter
    def grace_period_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "grace_period_minutes", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'StopOnDisconnectEnableStatus']]]:
        """
        Whether the feature to stop the Dev Box on disconnect once the grace period has lapsed is enabled.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'StopOnDisconnectEnableStatus']]]):
        pulumi.set(self, "status", value)


if not MYPY:
    class UserRoleAssignmentArgsDict(TypedDict):
        """
        Mapping of user object ID to role assignments.
        """
        roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        A map of roles to assign to the parent user.
        """
elif False:
    UserRoleAssignmentArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class UserRoleAssignmentArgs:
    def __init__(__self__, *,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Mapping of user object ID to role assignments.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A map of roles to assign to the parent user.
        """
        if roles is not None:
            pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A map of roles to assign to the parent user.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)


