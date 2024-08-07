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
from ._inputs import *

__all__ = ['AgentPoolArgs', 'AgentPool']

@pulumi.input_type
class AgentPoolArgs:
    def __init__(__self__, *,
                 count: pulumi.Input[float],
                 kubernetes_cluster_name: pulumi.Input[str],
                 mode: pulumi.Input[Union[str, 'AgentPoolMode']],
                 resource_group_name: pulumi.Input[str],
                 vm_sku_name: pulumi.Input[str],
                 administrator_configuration: Optional[pulumi.Input['AdministratorConfigurationArgs']] = None,
                 agent_options: Optional[pulumi.Input['AgentOptionsArgs']] = None,
                 agent_pool_name: Optional[pulumi.Input[str]] = None,
                 attached_network_configuration: Optional[pulumi.Input['AttachedNetworkConfigurationArgs']] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesLabelArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesLabelArgs']]]] = None,
                 upgrade_settings: Optional[pulumi.Input['AgentPoolUpgradeSettingsArgs']] = None):
        """
        The set of arguments for constructing a AgentPool resource.
        :param pulumi.Input[float] count: The number of virtual machines that use this configuration.
        :param pulumi.Input[str] kubernetes_cluster_name: The name of the Kubernetes cluster.
        :param pulumi.Input[Union[str, 'AgentPoolMode']] mode: The selection of how this agent pool is utilized, either as a system pool or a user pool. System pools run the features and critical services for the Kubernetes Cluster, while user pools are dedicated to user workloads. Every Kubernetes cluster must contain at least one system node pool with at least one node.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] vm_sku_name: The name of the VM SKU that determines the size of resources allocated for node VMs.
        :param pulumi.Input['AdministratorConfigurationArgs'] administrator_configuration: The administrator credentials to be used for the nodes in this agent pool.
        :param pulumi.Input['AgentOptionsArgs'] agent_options: The configurations that will be applied to each agent in this agent pool.
        :param pulumi.Input[str] agent_pool_name: The name of the Kubernetes cluster agent pool.
        :param pulumi.Input['AttachedNetworkConfigurationArgs'] attached_network_configuration: The configuration of networks being attached to the agent pool for use by the workloads that run on this Kubernetes cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: The list of availability zones of the Network Cloud cluster used for the provisioning of nodes in this agent pool. If not specified, all availability zones will be used.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[Sequence[pulumi.Input['KubernetesLabelArgs']]] labels: The labels applied to the nodes in this agent pool.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input['KubernetesLabelArgs']]] taints: The taints applied to the nodes in this agent pool.
        :param pulumi.Input['AgentPoolUpgradeSettingsArgs'] upgrade_settings: The configuration of the agent pool.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "kubernetes_cluster_name", kubernetes_cluster_name)
        pulumi.set(__self__, "mode", mode)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vm_sku_name", vm_sku_name)
        if administrator_configuration is not None:
            pulumi.set(__self__, "administrator_configuration", administrator_configuration)
        if agent_options is not None:
            pulumi.set(__self__, "agent_options", agent_options)
        if agent_pool_name is not None:
            pulumi.set(__self__, "agent_pool_name", agent_pool_name)
        if attached_network_configuration is not None:
            pulumi.set(__self__, "attached_network_configuration", attached_network_configuration)
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if taints is not None:
            pulumi.set(__self__, "taints", taints)
        if upgrade_settings is not None:
            pulumi.set(__self__, "upgrade_settings", upgrade_settings)

    @property
    @pulumi.getter
    def count(self) -> pulumi.Input[float]:
        """
        The number of virtual machines that use this configuration.
        """
        return pulumi.get(self, "count")

    @count.setter
    def count(self, value: pulumi.Input[float]):
        pulumi.set(self, "count", value)

    @property
    @pulumi.getter(name="kubernetesClusterName")
    def kubernetes_cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the Kubernetes cluster.
        """
        return pulumi.get(self, "kubernetes_cluster_name")

    @kubernetes_cluster_name.setter
    def kubernetes_cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "kubernetes_cluster_name", value)

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Input[Union[str, 'AgentPoolMode']]:
        """
        The selection of how this agent pool is utilized, either as a system pool or a user pool. System pools run the features and critical services for the Kubernetes Cluster, while user pools are dedicated to user workloads. Every Kubernetes cluster must contain at least one system node pool with at least one node.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: pulumi.Input[Union[str, 'AgentPoolMode']]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="vmSkuName")
    def vm_sku_name(self) -> pulumi.Input[str]:
        """
        The name of the VM SKU that determines the size of resources allocated for node VMs.
        """
        return pulumi.get(self, "vm_sku_name")

    @vm_sku_name.setter
    def vm_sku_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vm_sku_name", value)

    @property
    @pulumi.getter(name="administratorConfiguration")
    def administrator_configuration(self) -> Optional[pulumi.Input['AdministratorConfigurationArgs']]:
        """
        The administrator credentials to be used for the nodes in this agent pool.
        """
        return pulumi.get(self, "administrator_configuration")

    @administrator_configuration.setter
    def administrator_configuration(self, value: Optional[pulumi.Input['AdministratorConfigurationArgs']]):
        pulumi.set(self, "administrator_configuration", value)

    @property
    @pulumi.getter(name="agentOptions")
    def agent_options(self) -> Optional[pulumi.Input['AgentOptionsArgs']]:
        """
        The configurations that will be applied to each agent in this agent pool.
        """
        return pulumi.get(self, "agent_options")

    @agent_options.setter
    def agent_options(self, value: Optional[pulumi.Input['AgentOptionsArgs']]):
        pulumi.set(self, "agent_options", value)

    @property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kubernetes cluster agent pool.
        """
        return pulumi.get(self, "agent_pool_name")

    @agent_pool_name.setter
    def agent_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_pool_name", value)

    @property
    @pulumi.getter(name="attachedNetworkConfiguration")
    def attached_network_configuration(self) -> Optional[pulumi.Input['AttachedNetworkConfigurationArgs']]:
        """
        The configuration of networks being attached to the agent pool for use by the workloads that run on this Kubernetes cluster.
        """
        return pulumi.get(self, "attached_network_configuration")

    @attached_network_configuration.setter
    def attached_network_configuration(self, value: Optional[pulumi.Input['AttachedNetworkConfigurationArgs']]):
        pulumi.set(self, "attached_network_configuration", value)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of availability zones of the Network Cloud cluster used for the provisioning of nodes in this agent pool. If not specified, all availability zones will be used.
        """
        return pulumi.get(self, "availability_zones")

    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "availability_zones", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesLabelArgs']]]]:
        """
        The labels applied to the nodes in this agent pool.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesLabelArgs']]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def taints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesLabelArgs']]]]:
        """
        The taints applied to the nodes in this agent pool.
        """
        return pulumi.get(self, "taints")

    @taints.setter
    def taints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesLabelArgs']]]]):
        pulumi.set(self, "taints", value)

    @property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional[pulumi.Input['AgentPoolUpgradeSettingsArgs']]:
        """
        The configuration of the agent pool.
        """
        return pulumi.get(self, "upgrade_settings")

    @upgrade_settings.setter
    def upgrade_settings(self, value: Optional[pulumi.Input['AgentPoolUpgradeSettingsArgs']]):
        pulumi.set(self, "upgrade_settings", value)


class AgentPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_configuration: Optional[pulumi.Input[Union['AdministratorConfigurationArgs', 'AdministratorConfigurationArgsDict']]] = None,
                 agent_options: Optional[pulumi.Input[Union['AgentOptionsArgs', 'AgentOptionsArgsDict']]] = None,
                 agent_pool_name: Optional[pulumi.Input[str]] = None,
                 attached_network_configuration: Optional[pulumi.Input[Union['AttachedNetworkConfigurationArgs', 'AttachedNetworkConfigurationArgsDict']]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 count: Optional[pulumi.Input[float]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 kubernetes_cluster_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union['KubernetesLabelArgs', 'KubernetesLabelArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[Union[str, 'AgentPoolMode']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input[Union['KubernetesLabelArgs', 'KubernetesLabelArgsDict']]]]] = None,
                 upgrade_settings: Optional[pulumi.Input[Union['AgentPoolUpgradeSettingsArgs', 'AgentPoolUpgradeSettingsArgsDict']]] = None,
                 vm_sku_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AgentPool resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['AdministratorConfigurationArgs', 'AdministratorConfigurationArgsDict']] administrator_configuration: The administrator credentials to be used for the nodes in this agent pool.
        :param pulumi.Input[Union['AgentOptionsArgs', 'AgentOptionsArgsDict']] agent_options: The configurations that will be applied to each agent in this agent pool.
        :param pulumi.Input[str] agent_pool_name: The name of the Kubernetes cluster agent pool.
        :param pulumi.Input[Union['AttachedNetworkConfigurationArgs', 'AttachedNetworkConfigurationArgsDict']] attached_network_configuration: The configuration of networks being attached to the agent pool for use by the workloads that run on this Kubernetes cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: The list of availability zones of the Network Cloud cluster used for the provisioning of nodes in this agent pool. If not specified, all availability zones will be used.
        :param pulumi.Input[float] count: The number of virtual machines that use this configuration.
        :param pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[str] kubernetes_cluster_name: The name of the Kubernetes cluster.
        :param pulumi.Input[Sequence[pulumi.Input[Union['KubernetesLabelArgs', 'KubernetesLabelArgsDict']]]] labels: The labels applied to the nodes in this agent pool.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'AgentPoolMode']] mode: The selection of how this agent pool is utilized, either as a system pool or a user pool. System pools run the features and critical services for the Kubernetes Cluster, while user pools are dedicated to user workloads. Every Kubernetes cluster must contain at least one system node pool with at least one node.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[Union['KubernetesLabelArgs', 'KubernetesLabelArgsDict']]]] taints: The taints applied to the nodes in this agent pool.
        :param pulumi.Input[Union['AgentPoolUpgradeSettingsArgs', 'AgentPoolUpgradeSettingsArgsDict']] upgrade_settings: The configuration of the agent pool.
        :param pulumi.Input[str] vm_sku_name: The name of the VM SKU that determines the size of resources allocated for node VMs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgentPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AgentPool resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AgentPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgentPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_configuration: Optional[pulumi.Input[Union['AdministratorConfigurationArgs', 'AdministratorConfigurationArgsDict']]] = None,
                 agent_options: Optional[pulumi.Input[Union['AgentOptionsArgs', 'AgentOptionsArgsDict']]] = None,
                 agent_pool_name: Optional[pulumi.Input[str]] = None,
                 attached_network_configuration: Optional[pulumi.Input[Union['AttachedNetworkConfigurationArgs', 'AttachedNetworkConfigurationArgsDict']]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 count: Optional[pulumi.Input[float]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 kubernetes_cluster_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union['KubernetesLabelArgs', 'KubernetesLabelArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[Union[str, 'AgentPoolMode']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input[Union['KubernetesLabelArgs', 'KubernetesLabelArgsDict']]]]] = None,
                 upgrade_settings: Optional[pulumi.Input[Union['AgentPoolUpgradeSettingsArgs', 'AgentPoolUpgradeSettingsArgsDict']]] = None,
                 vm_sku_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AgentPoolArgs.__new__(AgentPoolArgs)

            __props__.__dict__["administrator_configuration"] = administrator_configuration
            __props__.__dict__["agent_options"] = agent_options
            __props__.__dict__["agent_pool_name"] = agent_pool_name
            __props__.__dict__["attached_network_configuration"] = attached_network_configuration
            __props__.__dict__["availability_zones"] = availability_zones
            if count is None and not opts.urn:
                raise TypeError("Missing required property 'count'")
            __props__.__dict__["count"] = count
            __props__.__dict__["extended_location"] = extended_location
            if kubernetes_cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'kubernetes_cluster_name'")
            __props__.__dict__["kubernetes_cluster_name"] = kubernetes_cluster_name
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            if mode is None and not opts.urn:
                raise TypeError("Missing required property 'mode'")
            __props__.__dict__["mode"] = mode
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["taints"] = taints
            __props__.__dict__["upgrade_settings"] = upgrade_settings
            if vm_sku_name is None and not opts.urn:
                raise TypeError("Missing required property 'vm_sku_name'")
            __props__.__dict__["vm_sku_name"] = vm_sku_name
            __props__.__dict__["detailed_status"] = None
            __props__.__dict__["detailed_status_message"] = None
            __props__.__dict__["kubernetes_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkcloud:AgentPool"), pulumi.Alias(type_="azure-native:networkcloud/v20230701:AgentPool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AgentPool, __self__).__init__(
            'azure-native:networkcloud/v20231001preview:AgentPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AgentPool':
        """
        Get an existing AgentPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AgentPoolArgs.__new__(AgentPoolArgs)

        __props__.__dict__["administrator_configuration"] = None
        __props__.__dict__["agent_options"] = None
        __props__.__dict__["attached_network_configuration"] = None
        __props__.__dict__["availability_zones"] = None
        __props__.__dict__["count"] = None
        __props__.__dict__["detailed_status"] = None
        __props__.__dict__["detailed_status_message"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["kubernetes_version"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["taints"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["upgrade_settings"] = None
        __props__.__dict__["vm_sku_name"] = None
        return AgentPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorConfiguration")
    def administrator_configuration(self) -> pulumi.Output[Optional['outputs.AdministratorConfigurationResponse']]:
        """
        The administrator credentials to be used for the nodes in this agent pool.
        """
        return pulumi.get(self, "administrator_configuration")

    @property
    @pulumi.getter(name="agentOptions")
    def agent_options(self) -> pulumi.Output[Optional['outputs.AgentOptionsResponse']]:
        """
        The configurations that will be applied to each agent in this agent pool.
        """
        return pulumi.get(self, "agent_options")

    @property
    @pulumi.getter(name="attachedNetworkConfiguration")
    def attached_network_configuration(self) -> pulumi.Output[Optional['outputs.AttachedNetworkConfigurationResponse']]:
        """
        The configuration of networks being attached to the agent pool for use by the workloads that run on this Kubernetes cluster.
        """
        return pulumi.get(self, "attached_network_configuration")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of availability zones of the Network Cloud cluster used for the provisioning of nodes in this agent pool. If not specified, all availability zones will be used.
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter
    def count(self) -> pulumi.Output[float]:
        """
        The number of virtual machines that use this configuration.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[str]:
        """
        The current status of the agent pool.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[str]:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[str]:
        """
        The Kubernetes version running in this agent pool.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence['outputs.KubernetesLabelResponse']]]:
        """
        The labels applied to the nodes in this agent pool.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[str]:
        """
        The selection of how this agent pool is utilized, either as a system pool or a user pool. System pools run the features and critical services for the Kubernetes Cluster, while user pools are dedicated to user workloads. Every Kubernetes cluster must contain at least one system node pool with at least one node.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the agent pool.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def taints(self) -> pulumi.Output[Optional[Sequence['outputs.KubernetesLabelResponse']]]:
        """
        The taints applied to the nodes in this agent pool.
        """
        return pulumi.get(self, "taints")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> pulumi.Output[Optional['outputs.AgentPoolUpgradeSettingsResponse']]:
        """
        The configuration of the agent pool.
        """
        return pulumi.get(self, "upgrade_settings")

    @property
    @pulumi.getter(name="vmSkuName")
    def vm_sku_name(self) -> pulumi.Output[str]:
        """
        The name of the VM SKU that determines the size of resources allocated for node VMs.
        """
        return pulumi.get(self, "vm_sku_name")

