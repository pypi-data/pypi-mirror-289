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

__all__ = ['ServiceConfigurationArgs', 'ServiceConfiguration']

@pulumi.input_type
class ServiceConfigurationArgs:
    def __init__(__self__, *,
                 endpoint_name: pulumi.Input[str],
                 resource_uri: pulumi.Input[str],
                 service_name: pulumi.Input[Union[str, 'ServiceName']],
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 port: Optional[pulumi.Input[float]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 service_configuration_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServiceConfiguration resource.
        :param pulumi.Input[str] endpoint_name: The endpoint name.
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
        :param pulumi.Input[Union[str, 'ServiceName']] service_name: Name of the service.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[float] port: The port on which service is enabled.
        :param pulumi.Input[str] resource_id: The resource Id of the connectivity endpoint (optional).
        :param pulumi.Input[str] service_configuration_name: The service name.
        """
        pulumi.set(__self__, "endpoint_name", endpoint_name)
        pulumi.set(__self__, "resource_uri", resource_uri)
        pulumi.set(__self__, "service_name", service_name)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if service_configuration_name is not None:
            pulumi.set(__self__, "service_configuration_name", service_configuration_name)

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[str]:
        """
        The endpoint name.
        """
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[str]:
        """
        The fully qualified Azure Resource manager identifier of the resource to be connected.
        """
        return pulumi.get(self, "resource_uri")

    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_uri", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[Union[str, 'ServiceName']]:
        """
        Name of the service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[Union[str, 'ServiceName']]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @created_by_type.setter
    def created_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "created_by_type", value)

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_at", value)

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @last_modified_by.setter
    def last_modified_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_by", value)

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @last_modified_by_type.setter
    def last_modified_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "last_modified_by_type", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[float]]:
        """
        The port on which service is enabled.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource Id of the connectivity endpoint (optional).
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="serviceConfigurationName")
    def service_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The service name.
        """
        return pulumi.get(self, "service_configuration_name")

    @service_configuration_name.setter
    def service_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_configuration_name", value)


class ServiceConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 port: Optional[pulumi.Input[float]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 service_configuration_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[Union[str, 'ServiceName']]] = None,
                 __props__=None):
        """
        The service configuration details associated with the target resource.
        Azure REST API version: 2023-03-15.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input[str] endpoint_name: The endpoint name.
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[float] port: The port on which service is enabled.
        :param pulumi.Input[str] resource_id: The resource Id of the connectivity endpoint (optional).
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
        :param pulumi.Input[str] service_configuration_name: The service name.
        :param pulumi.Input[Union[str, 'ServiceName']] service_name: Name of the service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The service configuration details associated with the target resource.
        Azure REST API version: 2023-03-15.

        :param str resource_name: The name of the resource.
        :param ServiceConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 port: Optional[pulumi.Input[float]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 service_configuration_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[Union[str, 'ServiceName']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceConfigurationArgs.__new__(ServiceConfigurationArgs)

            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["created_by_type"] = created_by_type
            if endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_name'")
            __props__.__dict__["endpoint_name"] = endpoint_name
            __props__.__dict__["last_modified_at"] = last_modified_at
            __props__.__dict__["last_modified_by"] = last_modified_by
            __props__.__dict__["last_modified_by_type"] = last_modified_by_type
            __props__.__dict__["port"] = port
            __props__.__dict__["resource_id"] = resource_id
            if resource_uri is None and not opts.urn:
                raise TypeError("Missing required property 'resource_uri'")
            __props__.__dict__["resource_uri"] = resource_uri
            __props__.__dict__["service_configuration_name"] = service_configuration_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybridconnectivity/v20230315:ServiceConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServiceConfiguration, __self__).__init__(
            'azure-native:hybridconnectivity:ServiceConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceConfiguration':
        """
        Get an existing ServiceConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceConfigurationArgs.__new__(ServiceConfigurationArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["created_by_type"] = None
        __props__.__dict__["last_modified_at"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_by_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["port"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["service_name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ServiceConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[float]]:
        """
        The port on which service is enabled.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource Id of the connectivity endpoint (optional).
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        Name of the service.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

