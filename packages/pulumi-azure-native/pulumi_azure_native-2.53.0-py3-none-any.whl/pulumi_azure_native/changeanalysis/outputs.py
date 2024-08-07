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
from ._enums import *

__all__ = [
    'AzureMonitorWorkspacePropertiesResponse',
    'ConfigurationProfileResourcePropertiesResponse',
    'NotificationSettingsResponse',
    'ResourceIdentityResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class AzureMonitorWorkspacePropertiesResponse(dict):
    """
    Configuration properties of an Azure Monitor workspace that receives change notifications.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "includeChangeDetails":
            suggest = "include_change_details"
        elif key == "workspaceId":
            suggest = "workspace_id"
        elif key == "workspaceResourceId":
            suggest = "workspace_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AzureMonitorWorkspacePropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AzureMonitorWorkspacePropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AzureMonitorWorkspacePropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 include_change_details: Optional[str] = None,
                 workspace_id: Optional[str] = None,
                 workspace_resource_id: Optional[str] = None):
        """
        Configuration properties of an Azure Monitor workspace that receives change notifications.
        :param str include_change_details: The mode of includeChangeDetails feature. The flag configures whether to include or exclude content of the change before and after values.
        :param str workspace_id: The Azure Monitor workspace ID - the unique identifier for the Log Analytics workspace.
        :param str workspace_resource_id: The Azure Monitor workspace ARM Resource ID. The resource ID should be in the following format: /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}
        """
        if include_change_details is not None:
            pulumi.set(__self__, "include_change_details", include_change_details)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)
        if workspace_resource_id is not None:
            pulumi.set(__self__, "workspace_resource_id", workspace_resource_id)

    @property
    @pulumi.getter(name="includeChangeDetails")
    def include_change_details(self) -> Optional[str]:
        """
        The mode of includeChangeDetails feature. The flag configures whether to include or exclude content of the change before and after values.
        """
        return pulumi.get(self, "include_change_details")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[str]:
        """
        The Azure Monitor workspace ID - the unique identifier for the Log Analytics workspace.
        """
        return pulumi.get(self, "workspace_id")

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[str]:
        """
        The Azure Monitor workspace ARM Resource ID. The resource ID should be in the following format: /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}
        """
        return pulumi.get(self, "workspace_resource_id")


@pulumi.output_type
class ConfigurationProfileResourcePropertiesResponse(dict):
    """
    The properties of a configuration profile.
    """
    def __init__(__self__, *,
                 notifications: Optional['outputs.NotificationSettingsResponse'] = None):
        """
        The properties of a configuration profile.
        :param 'NotificationSettingsResponse' notifications: Settings of change notification configuration for a subscription.
        """
        if notifications is not None:
            pulumi.set(__self__, "notifications", notifications)

    @property
    @pulumi.getter
    def notifications(self) -> Optional['outputs.NotificationSettingsResponse']:
        """
        Settings of change notification configuration for a subscription.
        """
        return pulumi.get(self, "notifications")


@pulumi.output_type
class NotificationSettingsResponse(dict):
    """
    Settings of change notification configuration for a subscription.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "activationState":
            suggest = "activation_state"
        elif key == "azureMonitorWorkspaceProperties":
            suggest = "azure_monitor_workspace_properties"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NotificationSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NotificationSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NotificationSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 activation_state: Optional[str] = None,
                 azure_monitor_workspace_properties: Optional['outputs.AzureMonitorWorkspacePropertiesResponse'] = None):
        """
        Settings of change notification configuration for a subscription.
        :param str activation_state: The state of notifications feature.
        :param 'AzureMonitorWorkspacePropertiesResponse' azure_monitor_workspace_properties: Configuration properties of an Azure Monitor workspace that receives change notifications.
        """
        if activation_state is not None:
            pulumi.set(__self__, "activation_state", activation_state)
        if azure_monitor_workspace_properties is not None:
            pulumi.set(__self__, "azure_monitor_workspace_properties", azure_monitor_workspace_properties)

    @property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> Optional[str]:
        """
        The state of notifications feature.
        """
        return pulumi.get(self, "activation_state")

    @property
    @pulumi.getter(name="azureMonitorWorkspaceProperties")
    def azure_monitor_workspace_properties(self) -> Optional['outputs.AzureMonitorWorkspacePropertiesResponse']:
        """
        Configuration properties of an Azure Monitor workspace that receives change notifications.
        """
        return pulumi.get(self, "azure_monitor_workspace_properties")


@pulumi.output_type
class ResourceIdentityResponse(dict):
    """
    The identity block returned by ARM resource that supports managed identity.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourceIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourceIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourceIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        The identity block returned by ARM resource that supports managed identity.
        :param str principal_id: The principal id of the identity. This property will only be provided for a system-assigned identity.
        :param str tenant_id: The tenant id associated with the resource's identity. This property will only be provided for a system-assigned identity.
        :param str type: The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user-assigned identities. The type 'None' will remove any identities.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal id of the identity. This property will only be provided for a system-assigned identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant id associated with the resource's identity. This property will only be provided for a system-assigned identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user-assigned identities. The type 'None' will remove any identities.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources
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
                 created_at: str,
                 created_by: str,
                 created_by_type: str,
                 last_modified_at: str,
                 last_modified_by: str,
                 last_modified_by_type: str):
        """
        Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources
        :param str created_at: The timestamp of resource creation (UTC)
        :param str created_by: A string identifier for the identity that created the resource
        :param str created_by_type: The type of identity that created the resource: user, application, managedIdentity, key
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: A string identifier for the identity that last modified the resource
        :param str last_modified_by_type: The type of identity that last modified the resource: user, application, managedIdentity, key
        """
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "created_by", created_by)
        pulumi.set(__self__, "created_by_type", created_by_type)
        pulumi.set(__self__, "last_modified_at", last_modified_at)
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The timestamp of resource creation (UTC)
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> str:
        """
        A string identifier for the identity that created the resource
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> str:
        """
        The type of identity that created the resource: user, application, managedIdentity, key
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> str:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> str:
        """
        A string identifier for the identity that last modified the resource
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> str:
        """
        The type of identity that last modified the resource: user, application, managedIdentity, key
        """
        return pulumi.get(self, "last_modified_by_type")


