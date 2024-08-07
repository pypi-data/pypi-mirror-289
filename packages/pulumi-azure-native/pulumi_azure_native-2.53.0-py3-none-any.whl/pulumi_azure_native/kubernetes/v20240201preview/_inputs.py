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
    'AadProfileArgs',
    'AadProfileArgsDict',
    'ArcAgentProfileArgs',
    'ArcAgentProfileArgsDict',
    'ConnectedClusterIdentityArgs',
    'ConnectedClusterIdentityArgsDict',
    'SystemComponentArgs',
    'SystemComponentArgsDict',
]

MYPY = False

if not MYPY:
    class AadProfileArgsDict(TypedDict):
        """
        AAD Profile specifies attributes for Azure Active Directory integration.
        """
        admin_group_object_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The list of AAD group object IDs that will have admin role of the cluster.
        """
        enable_azure_rbac: NotRequired[pulumi.Input[bool]]
        """
        Whether to enable Azure RBAC for Kubernetes authorization.
        """
        tenant_id: NotRequired[pulumi.Input[str]]
        """
        The AAD tenant ID to use for authentication. If not specified, will use the tenant of the deployment subscription.
        """
elif False:
    AadProfileArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AadProfileArgs:
    def __init__(__self__, *,
                 admin_group_object_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_azure_rbac: Optional[pulumi.Input[bool]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        AAD Profile specifies attributes for Azure Active Directory integration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] admin_group_object_ids: The list of AAD group object IDs that will have admin role of the cluster.
        :param pulumi.Input[bool] enable_azure_rbac: Whether to enable Azure RBAC for Kubernetes authorization.
        :param pulumi.Input[str] tenant_id: The AAD tenant ID to use for authentication. If not specified, will use the tenant of the deployment subscription.
        """
        if admin_group_object_ids is not None:
            pulumi.set(__self__, "admin_group_object_ids", admin_group_object_ids)
        if enable_azure_rbac is not None:
            pulumi.set(__self__, "enable_azure_rbac", enable_azure_rbac)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="adminGroupObjectIDs")
    def admin_group_object_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of AAD group object IDs that will have admin role of the cluster.
        """
        return pulumi.get(self, "admin_group_object_ids")

    @admin_group_object_ids.setter
    def admin_group_object_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "admin_group_object_ids", value)

    @property
    @pulumi.getter(name="enableAzureRBAC")
    def enable_azure_rbac(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable Azure RBAC for Kubernetes authorization.
        """
        return pulumi.get(self, "enable_azure_rbac")

    @enable_azure_rbac.setter
    def enable_azure_rbac(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_azure_rbac", value)

    @property
    @pulumi.getter(name="tenantID")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AAD tenant ID to use for authentication. If not specified, will use the tenant of the deployment subscription.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


if not MYPY:
    class ArcAgentProfileArgsDict(TypedDict):
        """
        Defines the Arc Agent properties for the clusters.
        """
        agent_auto_upgrade: NotRequired[pulumi.Input[Union[str, 'AutoUpgradeOptions']]]
        """
        Indicates whether the Arc agents on the be upgraded automatically to the latest version. Defaults to Enabled.
        """
        desired_agent_version: NotRequired[pulumi.Input[str]]
        """
        Version of the Arc agents to be installed on the cluster resource
        """
        system_components: NotRequired[pulumi.Input[Sequence[pulumi.Input['SystemComponentArgsDict']]]]
        """
        List of system extensions can be installed on the cluster resource.
        """
elif False:
    ArcAgentProfileArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ArcAgentProfileArgs:
    def __init__(__self__, *,
                 agent_auto_upgrade: Optional[pulumi.Input[Union[str, 'AutoUpgradeOptions']]] = None,
                 desired_agent_version: Optional[pulumi.Input[str]] = None,
                 system_components: Optional[pulumi.Input[Sequence[pulumi.Input['SystemComponentArgs']]]] = None):
        """
        Defines the Arc Agent properties for the clusters.
        :param pulumi.Input[Union[str, 'AutoUpgradeOptions']] agent_auto_upgrade: Indicates whether the Arc agents on the be upgraded automatically to the latest version. Defaults to Enabled.
        :param pulumi.Input[str] desired_agent_version: Version of the Arc agents to be installed on the cluster resource
        :param pulumi.Input[Sequence[pulumi.Input['SystemComponentArgs']]] system_components: List of system extensions can be installed on the cluster resource.
        """
        if agent_auto_upgrade is None:
            agent_auto_upgrade = 'Enabled'
        if agent_auto_upgrade is not None:
            pulumi.set(__self__, "agent_auto_upgrade", agent_auto_upgrade)
        if desired_agent_version is not None:
            pulumi.set(__self__, "desired_agent_version", desired_agent_version)
        if system_components is not None:
            pulumi.set(__self__, "system_components", system_components)

    @property
    @pulumi.getter(name="agentAutoUpgrade")
    def agent_auto_upgrade(self) -> Optional[pulumi.Input[Union[str, 'AutoUpgradeOptions']]]:
        """
        Indicates whether the Arc agents on the be upgraded automatically to the latest version. Defaults to Enabled.
        """
        return pulumi.get(self, "agent_auto_upgrade")

    @agent_auto_upgrade.setter
    def agent_auto_upgrade(self, value: Optional[pulumi.Input[Union[str, 'AutoUpgradeOptions']]]):
        pulumi.set(self, "agent_auto_upgrade", value)

    @property
    @pulumi.getter(name="desiredAgentVersion")
    def desired_agent_version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of the Arc agents to be installed on the cluster resource
        """
        return pulumi.get(self, "desired_agent_version")

    @desired_agent_version.setter
    def desired_agent_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "desired_agent_version", value)

    @property
    @pulumi.getter(name="systemComponents")
    def system_components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SystemComponentArgs']]]]:
        """
        List of system extensions can be installed on the cluster resource.
        """
        return pulumi.get(self, "system_components")

    @system_components.setter
    def system_components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SystemComponentArgs']]]]):
        pulumi.set(self, "system_components", value)


if not MYPY:
    class ConnectedClusterIdentityArgsDict(TypedDict):
        """
        Identity for the connected cluster.
        """
        type: pulumi.Input['ResourceIdentityType']
        """
        The type of identity used for the connected cluster. The type 'SystemAssigned, includes a system created identity. The type 'None' means no identity is assigned to the connected cluster.
        """
elif False:
    ConnectedClusterIdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ConnectedClusterIdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input['ResourceIdentityType']] = None):
        """
        Identity for the connected cluster.
        :param pulumi.Input['ResourceIdentityType'] type: The type of identity used for the connected cluster. The type 'SystemAssigned, includes a system created identity. The type 'None' means no identity is assigned to the connected cluster.
        """
        if type is None:
            type = 'SystemAssigned'
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['ResourceIdentityType']:
        """
        The type of identity used for the connected cluster. The type 'SystemAssigned, includes a system created identity. The type 'None' means no identity is assigned to the connected cluster.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['ResourceIdentityType']):
        pulumi.set(self, "type", value)


if not MYPY:
    class SystemComponentArgsDict(TypedDict):
        """
        System Extension and its desired versions to be installed on the cluster resource.
        """
        major_version: NotRequired[pulumi.Input[int]]
        """
        Major Version of the system extension to be installed on the cluster resource.
        """
        type: NotRequired[pulumi.Input[str]]
        """
        Type of the system extension
        """
        user_specified_version: NotRequired[pulumi.Input[str]]
        """
        Version of the system extension to be installed on the cluster resource.
        """
elif False:
    SystemComponentArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SystemComponentArgs:
    def __init__(__self__, *,
                 major_version: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user_specified_version: Optional[pulumi.Input[str]] = None):
        """
        System Extension and its desired versions to be installed on the cluster resource.
        :param pulumi.Input[int] major_version: Major Version of the system extension to be installed on the cluster resource.
        :param pulumi.Input[str] type: Type of the system extension
        :param pulumi.Input[str] user_specified_version: Version of the system extension to be installed on the cluster resource.
        """
        if major_version is not None:
            pulumi.set(__self__, "major_version", major_version)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_specified_version is not None:
            pulumi.set(__self__, "user_specified_version", user_specified_version)

    @property
    @pulumi.getter(name="majorVersion")
    def major_version(self) -> Optional[pulumi.Input[int]]:
        """
        Major Version of the system extension to be installed on the cluster resource.
        """
        return pulumi.get(self, "major_version")

    @major_version.setter
    def major_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "major_version", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the system extension
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userSpecifiedVersion")
    def user_specified_version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of the system extension to be installed on the cluster resource.
        """
        return pulumi.get(self, "user_specified_version")

    @user_specified_version.setter
    def user_specified_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_specified_version", value)


