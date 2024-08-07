# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ManagedClusterUpgradeType',
    'ManagedServiceIdentityType',
    'NodeImageSelectionType',
]


class ManagedClusterUpgradeType(str, Enum):
    """
    ManagedClusterUpgradeType is the type of upgrade to be applied.
    """
    FULL = "Full"
    """
    Full upgrades the control plane and all agent pools of the target ManagedClusters. Requires the ManagedClusterUpgradeSpec.KubernetesVersion property to be set.
    """
    NODE_IMAGE_ONLY = "NodeImageOnly"
    """
    NodeImageOnly upgrades only the node images of the target ManagedClusters. Requires the ManagedClusterUpgradeSpec.KubernetesVersion property to NOT be set.
    """
    CONTROL_PLANE_ONLY = "ControlPlaneOnly"
    """
    ControlPlaneOnly upgrades only targets the KubernetesVersion of the ManagedClusters and will not be applied to the AgentPool. Requires the ManagedClusterUpgradeSpec.KubernetesVersion property to be set.
    """


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class NodeImageSelectionType(str, Enum):
    """
    The node image upgrade type.
    """
    LATEST = "Latest"
    """
    Use the latest image version when upgrading nodes. Clusters may use different image versions (e.g., 'AKSUbuntu-1804gen2containerd-2021.10.12' and 'AKSUbuntu-1804gen2containerd-2021.10.19') because, for example, the latest available version is different in different regions.
    """
    CONSISTENT = "Consistent"
    """
    The image versions to upgrade nodes to are selected as described below: for each node pool in managed clusters affected by the update run, the system selects the latest image version such that it is available across all other node pools (in all other clusters) of the same image type. As a result, all node pools of the same image type will be upgraded to the same image version. For example, if the latest image version for image type 'AKSUbuntu-1804gen2containerd' is 'AKSUbuntu-1804gen2containerd-2021.10.12' for a node pool in cluster A in region X, and is 'AKSUbuntu-1804gen2containerd-2021.10.17' for a node pool in cluster B in region Y, the system will upgrade both node pools to image version 'AKSUbuntu-1804gen2containerd-2021.10.12'.
    """
