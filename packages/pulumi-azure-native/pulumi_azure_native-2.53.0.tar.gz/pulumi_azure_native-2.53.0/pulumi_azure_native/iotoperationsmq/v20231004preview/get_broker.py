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
    'GetBrokerResult',
    'AwaitableGetBrokerResult',
    'get_broker',
    'get_broker_output',
]

@pulumi.output_type
class GetBrokerResult:
    """
    MQ broker resource
    """
    def __init__(__self__, auth_image=None, broker_image=None, broker_node_tolerations=None, cardinality=None, diagnostics=None, disk_backed_message_buffer_settings=None, encrypt_internal_traffic=None, extended_location=None, health_manager_image=None, health_manager_node_tolerations=None, id=None, internal_certs=None, location=None, memory_profile=None, mode=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if auth_image and not isinstance(auth_image, dict):
            raise TypeError("Expected argument 'auth_image' to be a dict")
        pulumi.set(__self__, "auth_image", auth_image)
        if broker_image and not isinstance(broker_image, dict):
            raise TypeError("Expected argument 'broker_image' to be a dict")
        pulumi.set(__self__, "broker_image", broker_image)
        if broker_node_tolerations and not isinstance(broker_node_tolerations, dict):
            raise TypeError("Expected argument 'broker_node_tolerations' to be a dict")
        pulumi.set(__self__, "broker_node_tolerations", broker_node_tolerations)
        if cardinality and not isinstance(cardinality, dict):
            raise TypeError("Expected argument 'cardinality' to be a dict")
        pulumi.set(__self__, "cardinality", cardinality)
        if diagnostics and not isinstance(diagnostics, dict):
            raise TypeError("Expected argument 'diagnostics' to be a dict")
        pulumi.set(__self__, "diagnostics", diagnostics)
        if disk_backed_message_buffer_settings and not isinstance(disk_backed_message_buffer_settings, dict):
            raise TypeError("Expected argument 'disk_backed_message_buffer_settings' to be a dict")
        pulumi.set(__self__, "disk_backed_message_buffer_settings", disk_backed_message_buffer_settings)
        if encrypt_internal_traffic and not isinstance(encrypt_internal_traffic, bool):
            raise TypeError("Expected argument 'encrypt_internal_traffic' to be a bool")
        pulumi.set(__self__, "encrypt_internal_traffic", encrypt_internal_traffic)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if health_manager_image and not isinstance(health_manager_image, dict):
            raise TypeError("Expected argument 'health_manager_image' to be a dict")
        pulumi.set(__self__, "health_manager_image", health_manager_image)
        if health_manager_node_tolerations and not isinstance(health_manager_node_tolerations, dict):
            raise TypeError("Expected argument 'health_manager_node_tolerations' to be a dict")
        pulumi.set(__self__, "health_manager_node_tolerations", health_manager_node_tolerations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if internal_certs and not isinstance(internal_certs, dict):
            raise TypeError("Expected argument 'internal_certs' to be a dict")
        pulumi.set(__self__, "internal_certs", internal_certs)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if memory_profile and not isinstance(memory_profile, str):
            raise TypeError("Expected argument 'memory_profile' to be a str")
        pulumi.set(__self__, "memory_profile", memory_profile)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
    @pulumi.getter(name="authImage")
    def auth_image(self) -> 'outputs.ContainerImageResponse':
        """
        The details of Authentication Docker Image.
        """
        return pulumi.get(self, "auth_image")

    @property
    @pulumi.getter(name="brokerImage")
    def broker_image(self) -> 'outputs.ContainerImageResponse':
        """
        The details of Broker Docker Image.
        """
        return pulumi.get(self, "broker_image")

    @property
    @pulumi.getter(name="brokerNodeTolerations")
    def broker_node_tolerations(self) -> Optional['outputs.NodeTolerationsResponse']:
        """
        The details of Node Tolerations for Broker Pods.
        """
        return pulumi.get(self, "broker_node_tolerations")

    @property
    @pulumi.getter
    def cardinality(self) -> Optional['outputs.CardinalityResponse']:
        """
        The cardinality details of the broker.
        """
        return pulumi.get(self, "cardinality")

    @property
    @pulumi.getter
    def diagnostics(self) -> Optional['outputs.BrokerDiagnosticsResponse']:
        """
        The diagnostic details of the broker deployment.
        """
        return pulumi.get(self, "diagnostics")

    @property
    @pulumi.getter(name="diskBackedMessageBufferSettings")
    def disk_backed_message_buffer_settings(self) -> Optional['outputs.DiskBackedMessageBufferSettingsResponse']:
        """
        The settings of the disk-backed message buffer.
        """
        return pulumi.get(self, "disk_backed_message_buffer_settings")

    @property
    @pulumi.getter(name="encryptInternalTraffic")
    def encrypt_internal_traffic(self) -> Optional[bool]:
        """
        The setting to enable or disable encryption of internal Traffic.
        """
        return pulumi.get(self, "encrypt_internal_traffic")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationPropertyResponse':
        """
        Extended Location
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="healthManagerImage")
    def health_manager_image(self) -> 'outputs.ContainerImageResponse':
        """
        The details of Health Manager Docker Image.
        """
        return pulumi.get(self, "health_manager_image")

    @property
    @pulumi.getter(name="healthManagerNodeTolerations")
    def health_manager_node_tolerations(self) -> Optional['outputs.NodeTolerationsResponse']:
        """
        The details of Node Tolerations for Health Manager Pods.
        """
        return pulumi.get(self, "health_manager_node_tolerations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internalCerts")
    def internal_certs(self) -> Optional['outputs.CertManagerCertOptionsResponse']:
        """
        Details of the internal CA cert that will be used to secure communication between pods.
        """
        return pulumi.get(self, "internal_certs")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="memoryProfile")
    def memory_profile(self) -> Optional[str]:
        """
        Memory profile of broker.
        """
        return pulumi.get(self, "memory_profile")

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        The Running Mode of the Broker Deployment.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

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


class AwaitableGetBrokerResult(GetBrokerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBrokerResult(
            auth_image=self.auth_image,
            broker_image=self.broker_image,
            broker_node_tolerations=self.broker_node_tolerations,
            cardinality=self.cardinality,
            diagnostics=self.diagnostics,
            disk_backed_message_buffer_settings=self.disk_backed_message_buffer_settings,
            encrypt_internal_traffic=self.encrypt_internal_traffic,
            extended_location=self.extended_location,
            health_manager_image=self.health_manager_image,
            health_manager_node_tolerations=self.health_manager_node_tolerations,
            id=self.id,
            internal_certs=self.internal_certs,
            location=self.location,
            memory_profile=self.memory_profile,
            mode=self.mode,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_broker(broker_name: Optional[str] = None,
               mq_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBrokerResult:
    """
    Get a BrokerResource


    :param str broker_name: Name of MQ broker resource
    :param str mq_name: Name of MQ resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['brokerName'] = broker_name
    __args__['mqName'] = mq_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:iotoperationsmq/v20231004preview:getBroker', __args__, opts=opts, typ=GetBrokerResult).value

    return AwaitableGetBrokerResult(
        auth_image=pulumi.get(__ret__, 'auth_image'),
        broker_image=pulumi.get(__ret__, 'broker_image'),
        broker_node_tolerations=pulumi.get(__ret__, 'broker_node_tolerations'),
        cardinality=pulumi.get(__ret__, 'cardinality'),
        diagnostics=pulumi.get(__ret__, 'diagnostics'),
        disk_backed_message_buffer_settings=pulumi.get(__ret__, 'disk_backed_message_buffer_settings'),
        encrypt_internal_traffic=pulumi.get(__ret__, 'encrypt_internal_traffic'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        health_manager_image=pulumi.get(__ret__, 'health_manager_image'),
        health_manager_node_tolerations=pulumi.get(__ret__, 'health_manager_node_tolerations'),
        id=pulumi.get(__ret__, 'id'),
        internal_certs=pulumi.get(__ret__, 'internal_certs'),
        location=pulumi.get(__ret__, 'location'),
        memory_profile=pulumi.get(__ret__, 'memory_profile'),
        mode=pulumi.get(__ret__, 'mode'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_broker)
def get_broker_output(broker_name: Optional[pulumi.Input[str]] = None,
                      mq_name: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBrokerResult]:
    """
    Get a BrokerResource


    :param str broker_name: Name of MQ broker resource
    :param str mq_name: Name of MQ resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
