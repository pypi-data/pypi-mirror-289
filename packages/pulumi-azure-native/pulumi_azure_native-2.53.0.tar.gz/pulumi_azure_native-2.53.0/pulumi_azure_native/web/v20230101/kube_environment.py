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

__all__ = ['KubeEnvironmentArgs', 'KubeEnvironment']

@pulumi.input_type
class KubeEnvironmentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 aks_resource_id: Optional[pulumi.Input[str]] = None,
                 app_logs_configuration: Optional[pulumi.Input['AppLogsConfigurationArgs']] = None,
                 arc_configuration: Optional[pulumi.Input['ArcConfigurationArgs']] = None,
                 container_apps_configuration: Optional[pulumi.Input['ContainerAppsConfigurationArgs']] = None,
                 environment_type: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 internal_load_balancer_enabled: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 static_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a KubeEnvironment resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input['AppLogsConfigurationArgs'] app_logs_configuration: Cluster configuration which enables the log daemon to export
               app logs to a destination. Currently only "log-analytics" is
               supported
        :param pulumi.Input['ArcConfigurationArgs'] arc_configuration: Cluster configuration which determines the ARC cluster
               components types. Eg: Choosing between BuildService kind,
               FrontEnd Service ArtifactsStorageType etc.
        :param pulumi.Input['ContainerAppsConfigurationArgs'] container_apps_configuration: Cluster configuration for Container Apps Environments to configure Dapr Instrumentation Key and VNET Configuration
        :param pulumi.Input[str] environment_type: Type of Kubernetes Environment. Only supported for Container App Environments with value as Managed
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: Extended Location.
        :param pulumi.Input[bool] internal_load_balancer_enabled: Only visible within Vnet/Subnet
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] location: Resource Location.
        :param pulumi.Input[str] name: Name of the Kubernetes Environment.
        :param pulumi.Input[str] static_ip: Static IP of the KubeEnvironment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if aks_resource_id is not None:
            pulumi.set(__self__, "aks_resource_id", aks_resource_id)
        if app_logs_configuration is not None:
            pulumi.set(__self__, "app_logs_configuration", app_logs_configuration)
        if arc_configuration is not None:
            pulumi.set(__self__, "arc_configuration", arc_configuration)
        if container_apps_configuration is not None:
            pulumi.set(__self__, "container_apps_configuration", container_apps_configuration)
        if environment_type is not None:
            pulumi.set(__self__, "environment_type", environment_type)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if internal_load_balancer_enabled is not None:
            pulumi.set(__self__, "internal_load_balancer_enabled", internal_load_balancer_enabled)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if static_ip is not None:
            pulumi.set(__self__, "static_ip", static_ip)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="aksResourceID")
    def aks_resource_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "aks_resource_id")

    @aks_resource_id.setter
    def aks_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aks_resource_id", value)

    @property
    @pulumi.getter(name="appLogsConfiguration")
    def app_logs_configuration(self) -> Optional[pulumi.Input['AppLogsConfigurationArgs']]:
        """
        Cluster configuration which enables the log daemon to export
        app logs to a destination. Currently only "log-analytics" is
        supported
        """
        return pulumi.get(self, "app_logs_configuration")

    @app_logs_configuration.setter
    def app_logs_configuration(self, value: Optional[pulumi.Input['AppLogsConfigurationArgs']]):
        pulumi.set(self, "app_logs_configuration", value)

    @property
    @pulumi.getter(name="arcConfiguration")
    def arc_configuration(self) -> Optional[pulumi.Input['ArcConfigurationArgs']]:
        """
        Cluster configuration which determines the ARC cluster
        components types. Eg: Choosing between BuildService kind,
        FrontEnd Service ArtifactsStorageType etc.
        """
        return pulumi.get(self, "arc_configuration")

    @arc_configuration.setter
    def arc_configuration(self, value: Optional[pulumi.Input['ArcConfigurationArgs']]):
        pulumi.set(self, "arc_configuration", value)

    @property
    @pulumi.getter(name="containerAppsConfiguration")
    def container_apps_configuration(self) -> Optional[pulumi.Input['ContainerAppsConfigurationArgs']]:
        """
        Cluster configuration for Container Apps Environments to configure Dapr Instrumentation Key and VNET Configuration
        """
        return pulumi.get(self, "container_apps_configuration")

    @container_apps_configuration.setter
    def container_apps_configuration(self, value: Optional[pulumi.Input['ContainerAppsConfigurationArgs']]):
        pulumi.set(self, "container_apps_configuration", value)

    @property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of Kubernetes Environment. Only supported for Container App Environments with value as Managed
        """
        return pulumi.get(self, "environment_type")

    @environment_type.setter
    def environment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_type", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        Extended Location.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="internalLoadBalancerEnabled")
    def internal_load_balancer_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Only visible within Vnet/Subnet
        """
        return pulumi.get(self, "internal_load_balancer_enabled")

    @internal_load_balancer_enabled.setter
    def internal_load_balancer_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "internal_load_balancer_enabled", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Kubernetes Environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Static IP of the KubeEnvironment
        """
        return pulumi.get(self, "static_ip")

    @static_ip.setter
    def static_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "static_ip", value)

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


class KubeEnvironment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aks_resource_id: Optional[pulumi.Input[str]] = None,
                 app_logs_configuration: Optional[pulumi.Input[Union['AppLogsConfigurationArgs', 'AppLogsConfigurationArgsDict']]] = None,
                 arc_configuration: Optional[pulumi.Input[Union['ArcConfigurationArgs', 'ArcConfigurationArgsDict']]] = None,
                 container_apps_configuration: Optional[pulumi.Input[Union['ContainerAppsConfigurationArgs', 'ContainerAppsConfigurationArgsDict']]] = None,
                 environment_type: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 internal_load_balancer_enabled: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 static_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A Kubernetes cluster specialized for web workloads by Azure App Service

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['AppLogsConfigurationArgs', 'AppLogsConfigurationArgsDict']] app_logs_configuration: Cluster configuration which enables the log daemon to export
               app logs to a destination. Currently only "log-analytics" is
               supported
        :param pulumi.Input[Union['ArcConfigurationArgs', 'ArcConfigurationArgsDict']] arc_configuration: Cluster configuration which determines the ARC cluster
               components types. Eg: Choosing between BuildService kind,
               FrontEnd Service ArtifactsStorageType etc.
        :param pulumi.Input[Union['ContainerAppsConfigurationArgs', 'ContainerAppsConfigurationArgsDict']] container_apps_configuration: Cluster configuration for Container Apps Environments to configure Dapr Instrumentation Key and VNET Configuration
        :param pulumi.Input[str] environment_type: Type of Kubernetes Environment. Only supported for Container App Environments with value as Managed
        :param pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']] extended_location: Extended Location.
        :param pulumi.Input[bool] internal_load_balancer_enabled: Only visible within Vnet/Subnet
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] location: Resource Location.
        :param pulumi.Input[str] name: Name of the Kubernetes Environment.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] static_ip: Static IP of the KubeEnvironment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KubeEnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Kubernetes cluster specialized for web workloads by Azure App Service

        :param str resource_name: The name of the resource.
        :param KubeEnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KubeEnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aks_resource_id: Optional[pulumi.Input[str]] = None,
                 app_logs_configuration: Optional[pulumi.Input[Union['AppLogsConfigurationArgs', 'AppLogsConfigurationArgsDict']]] = None,
                 arc_configuration: Optional[pulumi.Input[Union['ArcConfigurationArgs', 'ArcConfigurationArgsDict']]] = None,
                 container_apps_configuration: Optional[pulumi.Input[Union['ContainerAppsConfigurationArgs', 'ContainerAppsConfigurationArgsDict']]] = None,
                 environment_type: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 internal_load_balancer_enabled: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 static_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KubeEnvironmentArgs.__new__(KubeEnvironmentArgs)

            __props__.__dict__["aks_resource_id"] = aks_resource_id
            __props__.__dict__["app_logs_configuration"] = app_logs_configuration
            __props__.__dict__["arc_configuration"] = arc_configuration
            __props__.__dict__["container_apps_configuration"] = container_apps_configuration
            __props__.__dict__["environment_type"] = environment_type
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["internal_load_balancer_enabled"] = internal_load_balancer_enabled
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["static_ip"] = static_ip
            __props__.__dict__["tags"] = tags
            __props__.__dict__["default_domain"] = None
            __props__.__dict__["deployment_errors"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:KubeEnvironment"), pulumi.Alias(type_="azure-native:web/v20210101:KubeEnvironment"), pulumi.Alias(type_="azure-native:web/v20210115:KubeEnvironment"), pulumi.Alias(type_="azure-native:web/v20210201:KubeEnvironment"), pulumi.Alias(type_="azure-native:web/v20210301:KubeEnvironment"), pulumi.Alias(type_="azure-native:web/v20220301:KubeEnvironment"), pulumi.Alias(type_="azure-native:web/v20220901:KubeEnvironment"), pulumi.Alias(type_="azure-native:web/v20231201:KubeEnvironment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(KubeEnvironment, __self__).__init__(
            'azure-native:web/v20230101:KubeEnvironment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'KubeEnvironment':
        """
        Get an existing KubeEnvironment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KubeEnvironmentArgs.__new__(KubeEnvironmentArgs)

        __props__.__dict__["aks_resource_id"] = None
        __props__.__dict__["app_logs_configuration"] = None
        __props__.__dict__["arc_configuration"] = None
        __props__.__dict__["container_apps_configuration"] = None
        __props__.__dict__["default_domain"] = None
        __props__.__dict__["deployment_errors"] = None
        __props__.__dict__["environment_type"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["internal_load_balancer_enabled"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["static_ip"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return KubeEnvironment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aksResourceID")
    def aks_resource_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "aks_resource_id")

    @property
    @pulumi.getter(name="appLogsConfiguration")
    def app_logs_configuration(self) -> pulumi.Output[Optional['outputs.AppLogsConfigurationResponse']]:
        """
        Cluster configuration which enables the log daemon to export
        app logs to a destination. Currently only "log-analytics" is
        supported
        """
        return pulumi.get(self, "app_logs_configuration")

    @property
    @pulumi.getter(name="arcConfiguration")
    def arc_configuration(self) -> pulumi.Output[Optional['outputs.ArcConfigurationResponse']]:
        """
        Cluster configuration which determines the ARC cluster
        components types. Eg: Choosing between BuildService kind,
        FrontEnd Service ArtifactsStorageType etc.
        """
        return pulumi.get(self, "arc_configuration")

    @property
    @pulumi.getter(name="containerAppsConfiguration")
    def container_apps_configuration(self) -> pulumi.Output[Optional['outputs.ContainerAppsConfigurationResponse']]:
        """
        Cluster configuration for Container Apps Environments to configure Dapr Instrumentation Key and VNET Configuration
        """
        return pulumi.get(self, "container_apps_configuration")

    @property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> pulumi.Output[str]:
        """
        Default Domain Name for the cluster
        """
        return pulumi.get(self, "default_domain")

    @property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> pulumi.Output[str]:
        """
        Any errors that occurred during deployment or deployment validation
        """
        return pulumi.get(self, "deployment_errors")

    @property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of Kubernetes Environment. Only supported for Container App Environments with value as Managed
        """
        return pulumi.get(self, "environment_type")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        Extended Location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="internalLoadBalancerEnabled")
    def internal_load_balancer_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Only visible within Vnet/Subnet
        """
        return pulumi.get(self, "internal_load_balancer_enabled")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the Kubernetes Environment.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> pulumi.Output[Optional[str]]:
        """
        Static IP of the KubeEnvironment
        """
        return pulumi.get(self, "static_ip")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

