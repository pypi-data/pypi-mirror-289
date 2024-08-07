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

__all__ = ['FlowLogArgs', 'FlowLog']

@pulumi.input_type
class FlowLogArgs:
    def __init__(__self__, *,
                 network_watcher_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_id: pulumi.Input[str],
                 target_resource_id: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 flow_analytics_configuration: Optional[pulumi.Input['TrafficAnalyticsPropertiesArgs']] = None,
                 flow_log_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input['FlowLogFormatParametersArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 retention_policy: Optional[pulumi.Input['RetentionPolicyParametersArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a FlowLog resource.
        :param pulumi.Input[str] network_watcher_name: The name of the network watcher.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] storage_id: ID of the storage account which is used to store the flow log.
        :param pulumi.Input[str] target_resource_id: ID of network security group to which flow log will be applied.
        :param pulumi.Input[bool] enabled: Flag to enable/disable flow logging.
        :param pulumi.Input['TrafficAnalyticsPropertiesArgs'] flow_analytics_configuration: Parameters that define the configuration of traffic analytics.
        :param pulumi.Input[str] flow_log_name: The name of the flow log.
        :param pulumi.Input['FlowLogFormatParametersArgs'] format: Parameters that define the flow log format.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input['RetentionPolicyParametersArgs'] retention_policy: Parameters that define the retention policy for flow log.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "network_watcher_name", network_watcher_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_id", storage_id)
        pulumi.set(__self__, "target_resource_id", target_resource_id)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if flow_analytics_configuration is not None:
            pulumi.set(__self__, "flow_analytics_configuration", flow_analytics_configuration)
        if flow_log_name is not None:
            pulumi.set(__self__, "flow_log_name", flow_log_name)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if retention_policy is not None:
            pulumi.set(__self__, "retention_policy", retention_policy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="networkWatcherName")
    def network_watcher_name(self) -> pulumi.Input[str]:
        """
        The name of the network watcher.
        """
        return pulumi.get(self, "network_watcher_name")

    @network_watcher_name.setter
    def network_watcher_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_watcher_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageId")
    def storage_id(self) -> pulumi.Input[str]:
        """
        ID of the storage account which is used to store the flow log.
        """
        return pulumi.get(self, "storage_id")

    @storage_id.setter
    def storage_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_id", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Input[str]:
        """
        ID of network security group to which flow log will be applied.
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag to enable/disable flow logging.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="flowAnalyticsConfiguration")
    def flow_analytics_configuration(self) -> Optional[pulumi.Input['TrafficAnalyticsPropertiesArgs']]:
        """
        Parameters that define the configuration of traffic analytics.
        """
        return pulumi.get(self, "flow_analytics_configuration")

    @flow_analytics_configuration.setter
    def flow_analytics_configuration(self, value: Optional[pulumi.Input['TrafficAnalyticsPropertiesArgs']]):
        pulumi.set(self, "flow_analytics_configuration", value)

    @property
    @pulumi.getter(name="flowLogName")
    def flow_log_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the flow log.
        """
        return pulumi.get(self, "flow_log_name")

    @flow_log_name.setter
    def flow_log_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "flow_log_name", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input['FlowLogFormatParametersArgs']]:
        """
        Parameters that define the flow log format.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input['FlowLogFormatParametersArgs']]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input['RetentionPolicyParametersArgs']]:
        """
        Parameters that define the retention policy for flow log.
        """
        return pulumi.get(self, "retention_policy")

    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input['RetentionPolicyParametersArgs']]):
        pulumi.set(self, "retention_policy", value)

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


class FlowLog(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 flow_analytics_configuration: Optional[pulumi.Input[Union['TrafficAnalyticsPropertiesArgs', 'TrafficAnalyticsPropertiesArgsDict']]] = None,
                 flow_log_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union['FlowLogFormatParametersArgs', 'FlowLogFormatParametersArgsDict']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_watcher_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_policy: Optional[pulumi.Input[Union['RetentionPolicyParametersArgs', 'RetentionPolicyParametersArgsDict']]] = None,
                 storage_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A flow log resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Flag to enable/disable flow logging.
        :param pulumi.Input[Union['TrafficAnalyticsPropertiesArgs', 'TrafficAnalyticsPropertiesArgsDict']] flow_analytics_configuration: Parameters that define the configuration of traffic analytics.
        :param pulumi.Input[str] flow_log_name: The name of the flow log.
        :param pulumi.Input[Union['FlowLogFormatParametersArgs', 'FlowLogFormatParametersArgsDict']] format: Parameters that define the flow log format.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] network_watcher_name: The name of the network watcher.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union['RetentionPolicyParametersArgs', 'RetentionPolicyParametersArgsDict']] retention_policy: Parameters that define the retention policy for flow log.
        :param pulumi.Input[str] storage_id: ID of the storage account which is used to store the flow log.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] target_resource_id: ID of network security group to which flow log will be applied.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FlowLogArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A flow log resource.

        :param str resource_name: The name of the resource.
        :param FlowLogArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FlowLogArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 flow_analytics_configuration: Optional[pulumi.Input[Union['TrafficAnalyticsPropertiesArgs', 'TrafficAnalyticsPropertiesArgsDict']]] = None,
                 flow_log_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union['FlowLogFormatParametersArgs', 'FlowLogFormatParametersArgsDict']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_watcher_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_policy: Optional[pulumi.Input[Union['RetentionPolicyParametersArgs', 'RetentionPolicyParametersArgsDict']]] = None,
                 storage_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FlowLogArgs.__new__(FlowLogArgs)

            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["flow_analytics_configuration"] = flow_analytics_configuration
            __props__.__dict__["flow_log_name"] = flow_log_name
            __props__.__dict__["format"] = format
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            if network_watcher_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_watcher_name'")
            __props__.__dict__["network_watcher_name"] = network_watcher_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["retention_policy"] = retention_policy
            if storage_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_id'")
            __props__.__dict__["storage_id"] = storage_id
            __props__.__dict__["tags"] = tags
            if target_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_resource_id'")
            __props__.__dict__["target_resource_id"] = target_resource_id
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["target_resource_guid"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:FlowLog"), pulumi.Alias(type_="azure-native:network/v20191101:FlowLog"), pulumi.Alias(type_="azure-native:network/v20191201:FlowLog"), pulumi.Alias(type_="azure-native:network/v20200301:FlowLog"), pulumi.Alias(type_="azure-native:network/v20200401:FlowLog"), pulumi.Alias(type_="azure-native:network/v20200501:FlowLog"), pulumi.Alias(type_="azure-native:network/v20200601:FlowLog"), pulumi.Alias(type_="azure-native:network/v20200701:FlowLog"), pulumi.Alias(type_="azure-native:network/v20200801:FlowLog"), pulumi.Alias(type_="azure-native:network/v20201101:FlowLog"), pulumi.Alias(type_="azure-native:network/v20210201:FlowLog"), pulumi.Alias(type_="azure-native:network/v20210301:FlowLog"), pulumi.Alias(type_="azure-native:network/v20210501:FlowLog"), pulumi.Alias(type_="azure-native:network/v20210801:FlowLog"), pulumi.Alias(type_="azure-native:network/v20220101:FlowLog"), pulumi.Alias(type_="azure-native:network/v20220501:FlowLog"), pulumi.Alias(type_="azure-native:network/v20220701:FlowLog"), pulumi.Alias(type_="azure-native:network/v20220901:FlowLog"), pulumi.Alias(type_="azure-native:network/v20221101:FlowLog"), pulumi.Alias(type_="azure-native:network/v20230201:FlowLog"), pulumi.Alias(type_="azure-native:network/v20230401:FlowLog"), pulumi.Alias(type_="azure-native:network/v20230501:FlowLog"), pulumi.Alias(type_="azure-native:network/v20230601:FlowLog"), pulumi.Alias(type_="azure-native:network/v20231101:FlowLog"), pulumi.Alias(type_="azure-native:network/v20240101:FlowLog")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FlowLog, __self__).__init__(
            'azure-native:network/v20230901:FlowLog',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FlowLog':
        """
        Get an existing FlowLog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FlowLogArgs.__new__(FlowLogArgs)

        __props__.__dict__["enabled"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["flow_analytics_configuration"] = None
        __props__.__dict__["format"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["retention_policy"] = None
        __props__.__dict__["storage_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_resource_guid"] = None
        __props__.__dict__["target_resource_id"] = None
        __props__.__dict__["type"] = None
        return FlowLog(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag to enable/disable flow logging.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="flowAnalyticsConfiguration")
    def flow_analytics_configuration(self) -> pulumi.Output[Optional['outputs.TrafficAnalyticsPropertiesResponse']]:
        """
        Parameters that define the configuration of traffic analytics.
        """
        return pulumi.get(self, "flow_analytics_configuration")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional['outputs.FlowLogFormatParametersResponse']]:
        """
        Parameters that define the flow log format.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the flow log.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> pulumi.Output[Optional['outputs.RetentionPolicyParametersResponse']]:
        """
        Parameters that define the retention policy for flow log.
        """
        return pulumi.get(self, "retention_policy")

    @property
    @pulumi.getter(name="storageId")
    def storage_id(self) -> pulumi.Output[str]:
        """
        ID of the storage account which is used to store the flow log.
        """
        return pulumi.get(self, "storage_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetResourceGuid")
    def target_resource_guid(self) -> pulumi.Output[str]:
        """
        Guid of network security group to which flow log will be applied.
        """
        return pulumi.get(self, "target_resource_guid")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[str]:
        """
        ID of network security group to which flow log will be applied.
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

