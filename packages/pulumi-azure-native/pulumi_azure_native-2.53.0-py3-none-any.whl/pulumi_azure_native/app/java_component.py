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

__all__ = ['JavaComponentArgs', 'JavaComponent']

@pulumi.input_type
class JavaComponentArgs:
    def __init__(__self__, *,
                 environment_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 component_type: Optional[pulumi.Input[Union[str, 'JavaComponentType']]] = None,
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input['JavaComponentConfigurationPropertyArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_binds: Optional[pulumi.Input[Sequence[pulumi.Input['JavaComponentServiceBindArgs']]]] = None):
        """
        The set of arguments for constructing a JavaComponent resource.
        :param pulumi.Input[str] environment_name: Name of the Managed Environment.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'JavaComponentType']] component_type: Type of the Java Component.
        :param pulumi.Input[Sequence[pulumi.Input['JavaComponentConfigurationPropertyArgs']]] configurations: List of Java Components configuration properties
        :param pulumi.Input[str] name: Name of the Java Component.
        :param pulumi.Input[Sequence[pulumi.Input['JavaComponentServiceBindArgs']]] service_binds: List of Java Components that are bound to the Java component
        """
        pulumi.set(__self__, "environment_name", environment_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if component_type is not None:
            pulumi.set(__self__, "component_type", component_type)
        if configurations is not None:
            pulumi.set(__self__, "configurations", configurations)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service_binds is not None:
            pulumi.set(__self__, "service_binds", service_binds)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[str]:
        """
        Name of the Managed Environment.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_name", value)

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
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[pulumi.Input[Union[str, 'JavaComponentType']]]:
        """
        Type of the Java Component.
        """
        return pulumi.get(self, "component_type")

    @component_type.setter
    def component_type(self, value: Optional[pulumi.Input[Union[str, 'JavaComponentType']]]):
        pulumi.set(self, "component_type", value)

    @property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['JavaComponentConfigurationPropertyArgs']]]]:
        """
        List of Java Components configuration properties
        """
        return pulumi.get(self, "configurations")

    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['JavaComponentConfigurationPropertyArgs']]]]):
        pulumi.set(self, "configurations", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Java Component.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['JavaComponentServiceBindArgs']]]]:
        """
        List of Java Components that are bound to the Java component
        """
        return pulumi.get(self, "service_binds")

    @service_binds.setter
    def service_binds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['JavaComponentServiceBindArgs']]]]):
        pulumi.set(self, "service_binds", value)


class JavaComponent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 component_type: Optional[pulumi.Input[Union[str, 'JavaComponentType']]] = None,
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union['JavaComponentConfigurationPropertyArgs', 'JavaComponentConfigurationPropertyArgsDict']]]]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_binds: Optional[pulumi.Input[Sequence[pulumi.Input[Union['JavaComponentServiceBindArgs', 'JavaComponentServiceBindArgsDict']]]]] = None,
                 __props__=None):
        """
        Java Component.
        Azure REST API version: 2023-11-02-preview.

        Other available API versions: 2024-02-02-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'JavaComponentType']] component_type: Type of the Java Component.
        :param pulumi.Input[Sequence[pulumi.Input[Union['JavaComponentConfigurationPropertyArgs', 'JavaComponentConfigurationPropertyArgsDict']]]] configurations: List of Java Components configuration properties
        :param pulumi.Input[str] environment_name: Name of the Managed Environment.
        :param pulumi.Input[str] name: Name of the Java Component.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[Union['JavaComponentServiceBindArgs', 'JavaComponentServiceBindArgsDict']]]] service_binds: List of Java Components that are bound to the Java component
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JavaComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Java Component.
        Azure REST API version: 2023-11-02-preview.

        Other available API versions: 2024-02-02-preview.

        :param str resource_name: The name of the resource.
        :param JavaComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JavaComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 component_type: Optional[pulumi.Input[Union[str, 'JavaComponentType']]] = None,
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union['JavaComponentConfigurationPropertyArgs', 'JavaComponentConfigurationPropertyArgsDict']]]]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_binds: Optional[pulumi.Input[Sequence[pulumi.Input[Union['JavaComponentServiceBindArgs', 'JavaComponentServiceBindArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JavaComponentArgs.__new__(JavaComponentArgs)

            __props__.__dict__["component_type"] = component_type
            __props__.__dict__["configurations"] = configurations
            if environment_name is None and not opts.urn:
                raise TypeError("Missing required property 'environment_name'")
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["service_binds"] = service_binds
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app/v20231102preview:JavaComponent"), pulumi.Alias(type_="azure-native:app/v20240202preview:JavaComponent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(JavaComponent, __self__).__init__(
            'azure-native:app:JavaComponent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JavaComponent':
        """
        Get an existing JavaComponent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JavaComponentArgs.__new__(JavaComponentArgs)

        __props__.__dict__["component_type"] = None
        __props__.__dict__["configurations"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_binds"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return JavaComponent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of the Java Component.
        """
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter
    def configurations(self) -> pulumi.Output[Optional[Sequence['outputs.JavaComponentConfigurationPropertyResponse']]]:
        """
        List of Java Components configuration properties
        """
        return pulumi.get(self, "configurations")

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
        Provisioning state of the Java Component.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> pulumi.Output[Optional[Sequence['outputs.JavaComponentServiceBindResponse']]]:
        """
        List of Java Components that are bound to the Java component
        """
        return pulumi.get(self, "service_binds")

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

