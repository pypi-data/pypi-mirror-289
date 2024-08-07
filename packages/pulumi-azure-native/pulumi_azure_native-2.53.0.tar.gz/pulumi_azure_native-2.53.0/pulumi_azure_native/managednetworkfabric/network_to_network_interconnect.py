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

__all__ = ['NetworkToNetworkInterconnectArgs', 'NetworkToNetworkInterconnect']

@pulumi.input_type
class NetworkToNetworkInterconnectArgs:
    def __init__(__self__, *,
                 is_management_type: pulumi.Input[Union[str, 'BooleanEnumProperty']],
                 network_fabric_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 use_option_b: pulumi.Input[Union[str, 'BooleanEnumProperty']],
                 layer2_configuration: Optional[pulumi.Input['Layer2ConfigurationArgs']] = None,
                 layer3_configuration: Optional[pulumi.Input['Layer3ConfigurationArgs']] = None,
                 network_to_network_interconnect_name: Optional[pulumi.Input[str]] = None,
                 nni_type: Optional[pulumi.Input[Union[str, 'NniType']]] = None):
        """
        The set of arguments for constructing a NetworkToNetworkInterconnect resource.
        :param pulumi.Input[Union[str, 'BooleanEnumProperty']] is_management_type: Configuration to use NNI for Infrastructure Management. Example: True/False.
        :param pulumi.Input[str] network_fabric_name: Name of the NetworkFabric.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'BooleanEnumProperty']] use_option_b: Based on this parameter the layer2/layer3 is made as mandatory. Example: True/False
        :param pulumi.Input['Layer2ConfigurationArgs'] layer2_configuration: Common properties for Layer2Configuration.
        :param pulumi.Input['Layer3ConfigurationArgs'] layer3_configuration: Common properties for Layer3Configuration.
        :param pulumi.Input[str] network_to_network_interconnect_name: Name of the NetworkToNetworkInterconnectName
        :param pulumi.Input[Union[str, 'NniType']] nni_type: Type of NNI used. Example: CE | NPB
        """
        pulumi.set(__self__, "is_management_type", is_management_type)
        pulumi.set(__self__, "network_fabric_name", network_fabric_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "use_option_b", use_option_b)
        if layer2_configuration is not None:
            pulumi.set(__self__, "layer2_configuration", layer2_configuration)
        if layer3_configuration is not None:
            pulumi.set(__self__, "layer3_configuration", layer3_configuration)
        if network_to_network_interconnect_name is not None:
            pulumi.set(__self__, "network_to_network_interconnect_name", network_to_network_interconnect_name)
        if nni_type is None:
            nni_type = 'CE'
        if nni_type is not None:
            pulumi.set(__self__, "nni_type", nni_type)

    @property
    @pulumi.getter(name="isManagementType")
    def is_management_type(self) -> pulumi.Input[Union[str, 'BooleanEnumProperty']]:
        """
        Configuration to use NNI for Infrastructure Management. Example: True/False.
        """
        return pulumi.get(self, "is_management_type")

    @is_management_type.setter
    def is_management_type(self, value: pulumi.Input[Union[str, 'BooleanEnumProperty']]):
        pulumi.set(self, "is_management_type", value)

    @property
    @pulumi.getter(name="networkFabricName")
    def network_fabric_name(self) -> pulumi.Input[str]:
        """
        Name of the NetworkFabric.
        """
        return pulumi.get(self, "network_fabric_name")

    @network_fabric_name.setter
    def network_fabric_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_fabric_name", value)

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
    @pulumi.getter(name="useOptionB")
    def use_option_b(self) -> pulumi.Input[Union[str, 'BooleanEnumProperty']]:
        """
        Based on this parameter the layer2/layer3 is made as mandatory. Example: True/False
        """
        return pulumi.get(self, "use_option_b")

    @use_option_b.setter
    def use_option_b(self, value: pulumi.Input[Union[str, 'BooleanEnumProperty']]):
        pulumi.set(self, "use_option_b", value)

    @property
    @pulumi.getter(name="layer2Configuration")
    def layer2_configuration(self) -> Optional[pulumi.Input['Layer2ConfigurationArgs']]:
        """
        Common properties for Layer2Configuration.
        """
        return pulumi.get(self, "layer2_configuration")

    @layer2_configuration.setter
    def layer2_configuration(self, value: Optional[pulumi.Input['Layer2ConfigurationArgs']]):
        pulumi.set(self, "layer2_configuration", value)

    @property
    @pulumi.getter(name="layer3Configuration")
    def layer3_configuration(self) -> Optional[pulumi.Input['Layer3ConfigurationArgs']]:
        """
        Common properties for Layer3Configuration.
        """
        return pulumi.get(self, "layer3_configuration")

    @layer3_configuration.setter
    def layer3_configuration(self, value: Optional[pulumi.Input['Layer3ConfigurationArgs']]):
        pulumi.set(self, "layer3_configuration", value)

    @property
    @pulumi.getter(name="networkToNetworkInterconnectName")
    def network_to_network_interconnect_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the NetworkToNetworkInterconnectName
        """
        return pulumi.get(self, "network_to_network_interconnect_name")

    @network_to_network_interconnect_name.setter
    def network_to_network_interconnect_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_to_network_interconnect_name", value)

    @property
    @pulumi.getter(name="nniType")
    def nni_type(self) -> Optional[pulumi.Input[Union[str, 'NniType']]]:
        """
        Type of NNI used. Example: CE | NPB
        """
        return pulumi.get(self, "nni_type")

    @nni_type.setter
    def nni_type(self, value: Optional[pulumi.Input[Union[str, 'NniType']]]):
        pulumi.set(self, "nni_type", value)


class NetworkToNetworkInterconnect(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_management_type: Optional[pulumi.Input[Union[str, 'BooleanEnumProperty']]] = None,
                 layer2_configuration: Optional[pulumi.Input[Union['Layer2ConfigurationArgs', 'Layer2ConfigurationArgsDict']]] = None,
                 layer3_configuration: Optional[pulumi.Input[Union['Layer3ConfigurationArgs', 'Layer3ConfigurationArgsDict']]] = None,
                 network_fabric_name: Optional[pulumi.Input[str]] = None,
                 network_to_network_interconnect_name: Optional[pulumi.Input[str]] = None,
                 nni_type: Optional[pulumi.Input[Union[str, 'NniType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 use_option_b: Optional[pulumi.Input[Union[str, 'BooleanEnumProperty']]] = None,
                 __props__=None):
        """
        The NetworkToNetworkInterconnect resource definition.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview.

        Other available API versions: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'BooleanEnumProperty']] is_management_type: Configuration to use NNI for Infrastructure Management. Example: True/False.
        :param pulumi.Input[Union['Layer2ConfigurationArgs', 'Layer2ConfigurationArgsDict']] layer2_configuration: Common properties for Layer2Configuration.
        :param pulumi.Input[Union['Layer3ConfigurationArgs', 'Layer3ConfigurationArgsDict']] layer3_configuration: Common properties for Layer3Configuration.
        :param pulumi.Input[str] network_fabric_name: Name of the NetworkFabric.
        :param pulumi.Input[str] network_to_network_interconnect_name: Name of the NetworkToNetworkInterconnectName
        :param pulumi.Input[Union[str, 'NniType']] nni_type: Type of NNI used. Example: CE | NPB
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'BooleanEnumProperty']] use_option_b: Based on this parameter the layer2/layer3 is made as mandatory. Example: True/False
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkToNetworkInterconnectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The NetworkToNetworkInterconnect resource definition.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview.

        Other available API versions: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param NetworkToNetworkInterconnectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkToNetworkInterconnectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_management_type: Optional[pulumi.Input[Union[str, 'BooleanEnumProperty']]] = None,
                 layer2_configuration: Optional[pulumi.Input[Union['Layer2ConfigurationArgs', 'Layer2ConfigurationArgsDict']]] = None,
                 layer3_configuration: Optional[pulumi.Input[Union['Layer3ConfigurationArgs', 'Layer3ConfigurationArgsDict']]] = None,
                 network_fabric_name: Optional[pulumi.Input[str]] = None,
                 network_to_network_interconnect_name: Optional[pulumi.Input[str]] = None,
                 nni_type: Optional[pulumi.Input[Union[str, 'NniType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 use_option_b: Optional[pulumi.Input[Union[str, 'BooleanEnumProperty']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkToNetworkInterconnectArgs.__new__(NetworkToNetworkInterconnectArgs)

            if is_management_type is None and not opts.urn:
                raise TypeError("Missing required property 'is_management_type'")
            __props__.__dict__["is_management_type"] = is_management_type
            __props__.__dict__["layer2_configuration"] = layer2_configuration
            __props__.__dict__["layer3_configuration"] = layer3_configuration
            if network_fabric_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_fabric_name'")
            __props__.__dict__["network_fabric_name"] = network_fabric_name
            __props__.__dict__["network_to_network_interconnect_name"] = network_to_network_interconnect_name
            if nni_type is None:
                nni_type = 'CE'
            __props__.__dict__["nni_type"] = nni_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if use_option_b is None and not opts.urn:
                raise TypeError("Missing required property 'use_option_b'")
            __props__.__dict__["use_option_b"] = use_option_b
            __props__.__dict__["administrative_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric/v20230201preview:NetworkToNetworkInterconnect"), pulumi.Alias(type_="azure-native:managednetworkfabric/v20230615:NetworkToNetworkInterconnect")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkToNetworkInterconnect, __self__).__init__(
            'azure-native:managednetworkfabric:NetworkToNetworkInterconnect',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkToNetworkInterconnect':
        """
        Get an existing NetworkToNetworkInterconnect resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkToNetworkInterconnectArgs.__new__(NetworkToNetworkInterconnectArgs)

        __props__.__dict__["administrative_state"] = None
        __props__.__dict__["is_management_type"] = None
        __props__.__dict__["layer2_configuration"] = None
        __props__.__dict__["layer3_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["nni_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["use_option_b"] = None
        return NetworkToNetworkInterconnect(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[str]:
        """
        Gets the administrativeState of the resource. Example -Enabled/Disabled
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter(name="isManagementType")
    def is_management_type(self) -> pulumi.Output[str]:
        """
        Configuration to use NNI for Infrastructure Management. Example: True/False.
        """
        return pulumi.get(self, "is_management_type")

    @property
    @pulumi.getter(name="layer2Configuration")
    def layer2_configuration(self) -> pulumi.Output[Optional['outputs.Layer2ConfigurationResponse']]:
        """
        Common properties for Layer2Configuration.
        """
        return pulumi.get(self, "layer2_configuration")

    @property
    @pulumi.getter(name="layer3Configuration")
    def layer3_configuration(self) -> pulumi.Output[Optional['outputs.Layer3ConfigurationResponse']]:
        """
        Common properties for Layer3Configuration.
        """
        return pulumi.get(self, "layer3_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nniType")
    def nni_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of NNI used. Example: CE | NPB
        """
        return pulumi.get(self, "nni_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the provisioning state of the resource.
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
    @pulumi.getter(name="useOptionB")
    def use_option_b(self) -> pulumi.Output[str]:
        """
        Based on this parameter the layer2/layer3 is made as mandatory. Example: True/False
        """
        return pulumi.get(self, "use_option_b")

