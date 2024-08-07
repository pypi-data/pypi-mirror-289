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
from ._inputs import *

__all__ = ['HypervCollectorsOperationArgs', 'HypervCollectorsOperation']

@pulumi.input_type
class HypervCollectorsOperationArgs:
    def __init__(__self__, *,
                 project_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 agent_properties: Optional[pulumi.Input['CollectorAgentPropertiesBaseArgs']] = None,
                 discovery_site_id: Optional[pulumi.Input[str]] = None,
                 hyperv_collector_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None):
        """
        The set of arguments for constructing a HypervCollectorsOperation resource.
        :param pulumi.Input[str] project_name: Assessment Project Name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['CollectorAgentPropertiesBaseArgs'] agent_properties: Gets or sets the collector agent properties.
        :param pulumi.Input[str] discovery_site_id: Gets the discovery site id.
        :param pulumi.Input[str] hyperv_collector_name: Hyper-V collector ARM name
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        """
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if agent_properties is not None:
            pulumi.set(__self__, "agent_properties", agent_properties)
        if discovery_site_id is not None:
            pulumi.set(__self__, "discovery_site_id", discovery_site_id)
        if hyperv_collector_name is not None:
            pulumi.set(__self__, "hyperv_collector_name", hyperv_collector_name)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        Assessment Project Name
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

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
    @pulumi.getter(name="agentProperties")
    def agent_properties(self) -> Optional[pulumi.Input['CollectorAgentPropertiesBaseArgs']]:
        """
        Gets or sets the collector agent properties.
        """
        return pulumi.get(self, "agent_properties")

    @agent_properties.setter
    def agent_properties(self, value: Optional[pulumi.Input['CollectorAgentPropertiesBaseArgs']]):
        pulumi.set(self, "agent_properties", value)

    @property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets the discovery site id.
        """
        return pulumi.get(self, "discovery_site_id")

    @discovery_site_id.setter
    def discovery_site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "discovery_site_id", value)

    @property
    @pulumi.getter(name="hypervCollectorName")
    def hyperv_collector_name(self) -> Optional[pulumi.Input[str]]:
        """
        Hyper-V collector ARM name
        """
        return pulumi.get(self, "hyperv_collector_name")

    @hyperv_collector_name.setter
    def hyperv_collector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hyperv_collector_name", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningState']]]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)


class HypervCollectorsOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_properties: Optional[pulumi.Input[Union['CollectorAgentPropertiesBaseArgs', 'CollectorAgentPropertiesBaseArgsDict']]] = None,
                 discovery_site_id: Optional[pulumi.Input[str]] = None,
                 hyperv_collector_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Hyper-V collector resource.
        Azure REST API version: 2023-03-15.

        Other available API versions: 2023-04-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['CollectorAgentPropertiesBaseArgs', 'CollectorAgentPropertiesBaseArgsDict']] agent_properties: Gets or sets the collector agent properties.
        :param pulumi.Input[str] discovery_site_id: Gets the discovery site id.
        :param pulumi.Input[str] hyperv_collector_name: Hyper-V collector ARM name
        :param pulumi.Input[str] project_name: Assessment Project Name
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HypervCollectorsOperationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Hyper-V collector resource.
        Azure REST API version: 2023-03-15.

        Other available API versions: 2023-04-01-preview.

        :param str resource_name: The name of the resource.
        :param HypervCollectorsOperationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HypervCollectorsOperationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_properties: Optional[pulumi.Input[Union['CollectorAgentPropertiesBaseArgs', 'CollectorAgentPropertiesBaseArgsDict']]] = None,
                 discovery_site_id: Optional[pulumi.Input[str]] = None,
                 hyperv_collector_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HypervCollectorsOperationArgs.__new__(HypervCollectorsOperationArgs)

            __props__.__dict__["agent_properties"] = agent_properties
            __props__.__dict__["discovery_site_id"] = discovery_site_id
            __props__.__dict__["hyperv_collector_name"] = hyperv_collector_name
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["created_timestamp"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_timestamp"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:migrate/v20191001:HypervCollectorsOperation"), pulumi.Alias(type_="azure-native:migrate/v20230315:HypervCollectorsOperation"), pulumi.Alias(type_="azure-native:migrate/v20230401preview:HypervCollectorsOperation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HypervCollectorsOperation, __self__).__init__(
            'azure-native:migrate:HypervCollectorsOperation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HypervCollectorsOperation':
        """
        Get an existing HypervCollectorsOperation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HypervCollectorsOperationArgs.__new__(HypervCollectorsOperationArgs)

        __props__.__dict__["agent_properties"] = None
        __props__.__dict__["created_timestamp"] = None
        __props__.__dict__["discovery_site_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_timestamp"] = None
        return HypervCollectorsOperation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentProperties")
    def agent_properties(self) -> pulumi.Output[Optional['outputs.CollectorAgentPropertiesBaseResponse']]:
        """
        Gets or sets the collector agent properties.
        """
        return pulumi.get(self, "agent_properties")

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[str]:
        """
        Gets the Timestamp when collector was created.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the discovery site id.
        """
        return pulumi.get(self, "discovery_site_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the last operation.
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
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> pulumi.Output[str]:
        """
        Timestamp when collector was last updated.
        """
        return pulumi.get(self, "updated_timestamp")

