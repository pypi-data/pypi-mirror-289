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

__all__ = [
    'GetKafkaConnectorResult',
    'AwaitableGetKafkaConnectorResult',
    'get_kafka_connector',
    'get_kafka_connector_output',
]

@pulumi.output_type
class GetKafkaConnectorResult:
    """
    MQ kafkaConnector resource
    """
    def __init__(__self__, client_id_prefix=None, extended_location=None, id=None, image=None, instances=None, kafka_connection=None, local_broker_connection=None, location=None, log_level=None, name=None, node_tolerations=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if client_id_prefix and not isinstance(client_id_prefix, str):
            raise TypeError("Expected argument 'client_id_prefix' to be a str")
        pulumi.set(__self__, "client_id_prefix", client_id_prefix)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image and not isinstance(image, dict):
            raise TypeError("Expected argument 'image' to be a dict")
        pulumi.set(__self__, "image", image)
        if instances and not isinstance(instances, int):
            raise TypeError("Expected argument 'instances' to be a int")
        pulumi.set(__self__, "instances", instances)
        if kafka_connection and not isinstance(kafka_connection, dict):
            raise TypeError("Expected argument 'kafka_connection' to be a dict")
        pulumi.set(__self__, "kafka_connection", kafka_connection)
        if local_broker_connection and not isinstance(local_broker_connection, dict):
            raise TypeError("Expected argument 'local_broker_connection' to be a dict")
        pulumi.set(__self__, "local_broker_connection", local_broker_connection)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if log_level and not isinstance(log_level, str):
            raise TypeError("Expected argument 'log_level' to be a str")
        pulumi.set(__self__, "log_level", log_level)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_tolerations and not isinstance(node_tolerations, dict):
            raise TypeError("Expected argument 'node_tolerations' to be a dict")
        pulumi.set(__self__, "node_tolerations", node_tolerations)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="clientIdPrefix")
    def client_id_prefix(self) -> Optional[str]:
        """
        The client id prefix of the dynamically generated client ids.
        """
        return pulumi.get(self, "client_id_prefix")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationPropertyResponse':
        """
        Extended Location
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def image(self) -> Optional['outputs.ContainerImageResponse']:
        """
        The details of KafkaConnector Docker Image.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def instances(self) -> Optional[int]:
        """
        The number of KafkaConnector pods to spin up.
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="kafkaConnection")
    def kafka_connection(self) -> 'outputs.KafkaRemoteBrokerConnectionSpecResponse':
        """
        The details for connecting with Remote Kafka Broker.
        """
        return pulumi.get(self, "kafka_connection")

    @property
    @pulumi.getter(name="localBrokerConnection")
    def local_broker_connection(self) -> Optional['outputs.LocalBrokerConnectionSpecResponse']:
        """
        The details for connecting with Local Broker.
        """
        return pulumi.get(self, "local_broker_connection")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[str]:
        """
        The log level of the Bridge Connector instances.
        """
        return pulumi.get(self, "log_level")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeTolerations")
    def node_tolerations(self) -> Optional['outputs.NodeTolerationsResponse']:
        """
        The Node Tolerations for the Bridge Connector pods.
        """
        return pulumi.get(self, "node_tolerations")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetKafkaConnectorResult(GetKafkaConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaConnectorResult(
            client_id_prefix=self.client_id_prefix,
            extended_location=self.extended_location,
            id=self.id,
            image=self.image,
            instances=self.instances,
            kafka_connection=self.kafka_connection,
            local_broker_connection=self.local_broker_connection,
            location=self.location,
            log_level=self.log_level,
            name=self.name,
            node_tolerations=self.node_tolerations,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_kafka_connector(kafka_connector_name: Optional[str] = None,
                        mq_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaConnectorResult:
    """
    Get a KafkaConnectorResource


    :param str kafka_connector_name: Name of MQ kafkaConnector resource
    :param str mq_name: Name of MQ resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['kafkaConnectorName'] = kafka_connector_name
    __args__['mqName'] = mq_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:iotoperationsmq/v20231004preview:getKafkaConnector', __args__, opts=opts, typ=GetKafkaConnectorResult).value

    return AwaitableGetKafkaConnectorResult(
        client_id_prefix=pulumi.get(__ret__, 'client_id_prefix'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        image=pulumi.get(__ret__, 'image'),
        instances=pulumi.get(__ret__, 'instances'),
        kafka_connection=pulumi.get(__ret__, 'kafka_connection'),
        local_broker_connection=pulumi.get(__ret__, 'local_broker_connection'),
        location=pulumi.get(__ret__, 'location'),
        log_level=pulumi.get(__ret__, 'log_level'),
        name=pulumi.get(__ret__, 'name'),
        node_tolerations=pulumi.get(__ret__, 'node_tolerations'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_kafka_connector)
def get_kafka_connector_output(kafka_connector_name: Optional[pulumi.Input[str]] = None,
                               mq_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKafkaConnectorResult]:
    """
    Get a KafkaConnectorResource


    :param str kafka_connector_name: Name of MQ kafkaConnector resource
    :param str mq_name: Name of MQ resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
