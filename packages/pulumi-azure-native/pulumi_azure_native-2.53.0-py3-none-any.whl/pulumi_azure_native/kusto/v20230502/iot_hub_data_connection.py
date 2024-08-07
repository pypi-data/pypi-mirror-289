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

__all__ = ['IotHubDataConnectionArgs', 'IotHubDataConnection']

@pulumi.input_type
class IotHubDataConnectionArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 consumer_group: pulumi.Input[str],
                 database_name: pulumi.Input[str],
                 iot_hub_resource_id: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 shared_access_policy_name: pulumi.Input[str],
                 data_connection_name: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'IotHubDataFormat']]] = None,
                 database_routing: Optional[pulumi.Input[Union[str, 'DatabaseRouting']]] = None,
                 event_system_properties: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 retrieval_start_date: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IotHubDataConnection resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] consumer_group: The iot hub consumer group.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto cluster.
        :param pulumi.Input[str] iot_hub_resource_id: The resource ID of the Iot hub to be used to create a data connection.
        :param pulumi.Input[str] kind: Kind of the endpoint for the data connection
               Expected value is 'IotHub'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] shared_access_policy_name: The name of the share access policy
        :param pulumi.Input[str] data_connection_name: The name of the data connection.
        :param pulumi.Input[Union[str, 'IotHubDataFormat']] data_format: The data format of the message. Optionally the data format can be added to each message.
        :param pulumi.Input[Union[str, 'DatabaseRouting']] database_routing: Indication for database routing information from the data connection, by default only database routing information is allowed
        :param pulumi.Input[Sequence[pulumi.Input[str]]] event_system_properties: System properties of the iot hub
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] mapping_rule_name: The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        :param pulumi.Input[str] retrieval_start_date: When defined, the data connection retrieves existing Event hub events created since the Retrieval start date. It can only retrieve events retained by the Event hub, based on its retention period.
        :param pulumi.Input[str] table_name: The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "consumer_group", consumer_group)
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "iot_hub_resource_id", iot_hub_resource_id)
        pulumi.set(__self__, "kind", 'IotHub')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "shared_access_policy_name", shared_access_policy_name)
        if data_connection_name is not None:
            pulumi.set(__self__, "data_connection_name", data_connection_name)
        if data_format is not None:
            pulumi.set(__self__, "data_format", data_format)
        if database_routing is None:
            database_routing = 'Single'
        if database_routing is not None:
            pulumi.set(__self__, "database_routing", database_routing)
        if event_system_properties is not None:
            pulumi.set(__self__, "event_system_properties", event_system_properties)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mapping_rule_name is not None:
            pulumi.set(__self__, "mapping_rule_name", mapping_rule_name)
        if retrieval_start_date is not None:
            pulumi.set(__self__, "retrieval_start_date", retrieval_start_date)
        if table_name is not None:
            pulumi.set(__self__, "table_name", table_name)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the Kusto cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Input[str]:
        """
        The iot hub consumer group.
        """
        return pulumi.get(self, "consumer_group")

    @consumer_group.setter
    def consumer_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "consumer_group", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the database in the Kusto cluster.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="iotHubResourceId")
    def iot_hub_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Iot hub to be used to create a data connection.
        """
        return pulumi.get(self, "iot_hub_resource_id")

    @iot_hub_resource_id.setter
    def iot_hub_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "iot_hub_resource_id", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Kind of the endpoint for the data connection
        Expected value is 'IotHub'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> pulumi.Input[str]:
        """
        The name of the share access policy
        """
        return pulumi.get(self, "shared_access_policy_name")

    @shared_access_policy_name.setter
    def shared_access_policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "shared_access_policy_name", value)

    @property
    @pulumi.getter(name="dataConnectionName")
    def data_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the data connection.
        """
        return pulumi.get(self, "data_connection_name")

    @data_connection_name.setter
    def data_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_connection_name", value)

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[pulumi.Input[Union[str, 'IotHubDataFormat']]]:
        """
        The data format of the message. Optionally the data format can be added to each message.
        """
        return pulumi.get(self, "data_format")

    @data_format.setter
    def data_format(self, value: Optional[pulumi.Input[Union[str, 'IotHubDataFormat']]]):
        pulumi.set(self, "data_format", value)

    @property
    @pulumi.getter(name="databaseRouting")
    def database_routing(self) -> Optional[pulumi.Input[Union[str, 'DatabaseRouting']]]:
        """
        Indication for database routing information from the data connection, by default only database routing information is allowed
        """
        return pulumi.get(self, "database_routing")

    @database_routing.setter
    def database_routing(self, value: Optional[pulumi.Input[Union[str, 'DatabaseRouting']]]):
        pulumi.set(self, "database_routing", value)

    @property
    @pulumi.getter(name="eventSystemProperties")
    def event_system_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        System properties of the iot hub
        """
        return pulumi.get(self, "event_system_properties")

    @event_system_properties.setter
    def event_system_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "event_system_properties", value)

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
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        """
        return pulumi.get(self, "mapping_rule_name")

    @mapping_rule_name.setter
    def mapping_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mapping_rule_name", value)

    @property
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> Optional[pulumi.Input[str]]:
        """
        When defined, the data connection retrieves existing Event hub events created since the Retrieval start date. It can only retrieve events retained by the Event hub, based on its retention period.
        """
        return pulumi.get(self, "retrieval_start_date")

    @retrieval_start_date.setter
    def retrieval_start_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retrieval_start_date", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[str]]:
        """
        The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_name", value)


class IotHubDataConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 consumer_group: Optional[pulumi.Input[str]] = None,
                 data_connection_name: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'IotHubDataFormat']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 database_routing: Optional[pulumi.Input[Union[str, 'DatabaseRouting']]] = None,
                 event_system_properties: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 iot_hub_resource_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retrieval_start_date: Optional[pulumi.Input[str]] = None,
                 shared_access_policy_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing an iot hub data connection.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] consumer_group: The iot hub consumer group.
        :param pulumi.Input[str] data_connection_name: The name of the data connection.
        :param pulumi.Input[Union[str, 'IotHubDataFormat']] data_format: The data format of the message. Optionally the data format can be added to each message.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto cluster.
        :param pulumi.Input[Union[str, 'DatabaseRouting']] database_routing: Indication for database routing information from the data connection, by default only database routing information is allowed
        :param pulumi.Input[Sequence[pulumi.Input[str]]] event_system_properties: System properties of the iot hub
        :param pulumi.Input[str] iot_hub_resource_id: The resource ID of the Iot hub to be used to create a data connection.
        :param pulumi.Input[str] kind: Kind of the endpoint for the data connection
               Expected value is 'IotHub'.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] mapping_rule_name: The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] retrieval_start_date: When defined, the data connection retrieves existing Event hub events created since the Retrieval start date. It can only retrieve events retained by the Event hub, based on its retention period.
        :param pulumi.Input[str] shared_access_policy_name: The name of the share access policy
        :param pulumi.Input[str] table_name: The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IotHubDataConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing an iot hub data connection.

        :param str resource_name: The name of the resource.
        :param IotHubDataConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IotHubDataConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 consumer_group: Optional[pulumi.Input[str]] = None,
                 data_connection_name: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'IotHubDataFormat']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 database_routing: Optional[pulumi.Input[Union[str, 'DatabaseRouting']]] = None,
                 event_system_properties: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 iot_hub_resource_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retrieval_start_date: Optional[pulumi.Input[str]] = None,
                 shared_access_policy_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IotHubDataConnectionArgs.__new__(IotHubDataConnectionArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if consumer_group is None and not opts.urn:
                raise TypeError("Missing required property 'consumer_group'")
            __props__.__dict__["consumer_group"] = consumer_group
            __props__.__dict__["data_connection_name"] = data_connection_name
            __props__.__dict__["data_format"] = data_format
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            if database_routing is None:
                database_routing = 'Single'
            __props__.__dict__["database_routing"] = database_routing
            __props__.__dict__["event_system_properties"] = event_system_properties
            if iot_hub_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'iot_hub_resource_id'")
            __props__.__dict__["iot_hub_resource_id"] = iot_hub_resource_id
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'IotHub'
            __props__.__dict__["location"] = location
            __props__.__dict__["mapping_rule_name"] = mapping_rule_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["retrieval_start_date"] = retrieval_start_date
            if shared_access_policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'shared_access_policy_name'")
            __props__.__dict__["shared_access_policy_name"] = shared_access_policy_name
            __props__.__dict__["table_name"] = table_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:kusto:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20190121:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20190515:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20190907:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20191109:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20200215:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20200614:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20200918:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20210101:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20210827:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20220201:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20220707:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20221111:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20221229:IotHubDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20230815:IotHubDataConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IotHubDataConnection, __self__).__init__(
            'azure-native:kusto/v20230502:IotHubDataConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IotHubDataConnection':
        """
        Get an existing IotHubDataConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IotHubDataConnectionArgs.__new__(IotHubDataConnectionArgs)

        __props__.__dict__["consumer_group"] = None
        __props__.__dict__["data_format"] = None
        __props__.__dict__["database_routing"] = None
        __props__.__dict__["event_system_properties"] = None
        __props__.__dict__["iot_hub_resource_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mapping_rule_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["retrieval_start_date"] = None
        __props__.__dict__["shared_access_policy_name"] = None
        __props__.__dict__["table_name"] = None
        __props__.__dict__["type"] = None
        return IotHubDataConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Output[str]:
        """
        The iot hub consumer group.
        """
        return pulumi.get(self, "consumer_group")

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Output[Optional[str]]:
        """
        The data format of the message. Optionally the data format can be added to each message.
        """
        return pulumi.get(self, "data_format")

    @property
    @pulumi.getter(name="databaseRouting")
    def database_routing(self) -> pulumi.Output[Optional[str]]:
        """
        Indication for database routing information from the data connection, by default only database routing information is allowed
        """
        return pulumi.get(self, "database_routing")

    @property
    @pulumi.getter(name="eventSystemProperties")
    def event_system_properties(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        System properties of the iot hub
        """
        return pulumi.get(self, "event_system_properties")

    @property
    @pulumi.getter(name="iotHubResourceId")
    def iot_hub_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Iot hub to be used to create a data connection.
        """
        return pulumi.get(self, "iot_hub_resource_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of the endpoint for the data connection
        Expected value is 'IotHub'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> pulumi.Output[Optional[str]]:
        """
        The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        """
        return pulumi.get(self, "mapping_rule_name")

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
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> pulumi.Output[Optional[str]]:
        """
        When defined, the data connection retrieves existing Event hub events created since the Retrieval start date. It can only retrieve events retained by the Event hub, based on its retention period.
        """
        return pulumi.get(self, "retrieval_start_date")

    @property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> pulumi.Output[str]:
        """
        The name of the share access policy
        """
        return pulumi.get(self, "shared_access_policy_name")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[Optional[str]]:
        """
        The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

