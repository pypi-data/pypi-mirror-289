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

__all__ = ['ChangeDataCaptureArgs', 'ChangeDataCapture']

@pulumi.input_type
class ChangeDataCaptureArgs:
    def __init__(__self__, *,
                 factory_name: pulumi.Input[str],
                 policy: pulumi.Input['MapperPolicyArgs'],
                 resource_group_name: pulumi.Input[str],
                 source_connections_info: pulumi.Input[Sequence[pulumi.Input['MapperSourceConnectionsInfoArgs']]],
                 target_connections_info: pulumi.Input[Sequence[pulumi.Input['MapperTargetConnectionsInfoArgs']]],
                 allow_v_net_override: Optional[pulumi.Input[bool]] = None,
                 change_data_capture_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input['ChangeDataCaptureFolderArgs']] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ChangeDataCapture resource.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input['MapperPolicyArgs'] policy: CDC policy
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Sequence[pulumi.Input['MapperSourceConnectionsInfoArgs']]] source_connections_info: List of sources connections that can be used as sources in the CDC.
        :param pulumi.Input[Sequence[pulumi.Input['MapperTargetConnectionsInfoArgs']]] target_connections_info: List of target connections that can be used as sources in the CDC.
        :param pulumi.Input[bool] allow_v_net_override: A boolean to determine if the vnet configuration needs to be overwritten.
        :param pulumi.Input[str] change_data_capture_name: The change data capture name.
        :param pulumi.Input[str] description: The description of the change data capture.
        :param pulumi.Input['ChangeDataCaptureFolderArgs'] folder: The folder that this CDC is in. If not specified, CDC will appear at the root level.
        :param pulumi.Input[str] status: Status of the CDC as to if it is running or stopped.
        """
        pulumi.set(__self__, "factory_name", factory_name)
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source_connections_info", source_connections_info)
        pulumi.set(__self__, "target_connections_info", target_connections_info)
        if allow_v_net_override is not None:
            pulumi.set(__self__, "allow_v_net_override", allow_v_net_override)
        if change_data_capture_name is not None:
            pulumi.set(__self__, "change_data_capture_name", change_data_capture_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[str]:
        """
        The factory name.
        """
        return pulumi.get(self, "factory_name")

    @factory_name.setter
    def factory_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "factory_name", value)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input['MapperPolicyArgs']:
        """
        CDC policy
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input['MapperPolicyArgs']):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sourceConnectionsInfo")
    def source_connections_info(self) -> pulumi.Input[Sequence[pulumi.Input['MapperSourceConnectionsInfoArgs']]]:
        """
        List of sources connections that can be used as sources in the CDC.
        """
        return pulumi.get(self, "source_connections_info")

    @source_connections_info.setter
    def source_connections_info(self, value: pulumi.Input[Sequence[pulumi.Input['MapperSourceConnectionsInfoArgs']]]):
        pulumi.set(self, "source_connections_info", value)

    @property
    @pulumi.getter(name="targetConnectionsInfo")
    def target_connections_info(self) -> pulumi.Input[Sequence[pulumi.Input['MapperTargetConnectionsInfoArgs']]]:
        """
        List of target connections that can be used as sources in the CDC.
        """
        return pulumi.get(self, "target_connections_info")

    @target_connections_info.setter
    def target_connections_info(self, value: pulumi.Input[Sequence[pulumi.Input['MapperTargetConnectionsInfoArgs']]]):
        pulumi.set(self, "target_connections_info", value)

    @property
    @pulumi.getter(name="allowVNetOverride")
    def allow_v_net_override(self) -> Optional[pulumi.Input[bool]]:
        """
        A boolean to determine if the vnet configuration needs to be overwritten.
        """
        return pulumi.get(self, "allow_v_net_override")

    @allow_v_net_override.setter
    def allow_v_net_override(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_v_net_override", value)

    @property
    @pulumi.getter(name="changeDataCaptureName")
    def change_data_capture_name(self) -> Optional[pulumi.Input[str]]:
        """
        The change data capture name.
        """
        return pulumi.get(self, "change_data_capture_name")

    @change_data_capture_name.setter
    def change_data_capture_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "change_data_capture_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the change data capture.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input['ChangeDataCaptureFolderArgs']]:
        """
        The folder that this CDC is in. If not specified, CDC will appear at the root level.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input['ChangeDataCaptureFolderArgs']]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the CDC as to if it is running or stopped.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class ChangeDataCapture(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_v_net_override: Optional[pulumi.Input[bool]] = None,
                 change_data_capture_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input[Union['ChangeDataCaptureFolderArgs', 'ChangeDataCaptureFolderArgsDict']]] = None,
                 policy: Optional[pulumi.Input[Union['MapperPolicyArgs', 'MapperPolicyArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_connections_info: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MapperSourceConnectionsInfoArgs', 'MapperSourceConnectionsInfoArgsDict']]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 target_connections_info: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MapperTargetConnectionsInfoArgs', 'MapperTargetConnectionsInfoArgsDict']]]]] = None,
                 __props__=None):
        """
        Change data capture resource type.
        Azure REST API version: 2018-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_v_net_override: A boolean to determine if the vnet configuration needs to be overwritten.
        :param pulumi.Input[str] change_data_capture_name: The change data capture name.
        :param pulumi.Input[str] description: The description of the change data capture.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[Union['ChangeDataCaptureFolderArgs', 'ChangeDataCaptureFolderArgsDict']] folder: The folder that this CDC is in. If not specified, CDC will appear at the root level.
        :param pulumi.Input[Union['MapperPolicyArgs', 'MapperPolicyArgsDict']] policy: CDC policy
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Sequence[pulumi.Input[Union['MapperSourceConnectionsInfoArgs', 'MapperSourceConnectionsInfoArgsDict']]]] source_connections_info: List of sources connections that can be used as sources in the CDC.
        :param pulumi.Input[str] status: Status of the CDC as to if it is running or stopped.
        :param pulumi.Input[Sequence[pulumi.Input[Union['MapperTargetConnectionsInfoArgs', 'MapperTargetConnectionsInfoArgsDict']]]] target_connections_info: List of target connections that can be used as sources in the CDC.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChangeDataCaptureArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Change data capture resource type.
        Azure REST API version: 2018-06-01.

        :param str resource_name: The name of the resource.
        :param ChangeDataCaptureArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChangeDataCaptureArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_v_net_override: Optional[pulumi.Input[bool]] = None,
                 change_data_capture_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input[Union['ChangeDataCaptureFolderArgs', 'ChangeDataCaptureFolderArgsDict']]] = None,
                 policy: Optional[pulumi.Input[Union['MapperPolicyArgs', 'MapperPolicyArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_connections_info: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MapperSourceConnectionsInfoArgs', 'MapperSourceConnectionsInfoArgsDict']]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 target_connections_info: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MapperTargetConnectionsInfoArgs', 'MapperTargetConnectionsInfoArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ChangeDataCaptureArgs.__new__(ChangeDataCaptureArgs)

            __props__.__dict__["allow_v_net_override"] = allow_v_net_override
            __props__.__dict__["change_data_capture_name"] = change_data_capture_name
            __props__.__dict__["description"] = description
            if factory_name is None and not opts.urn:
                raise TypeError("Missing required property 'factory_name'")
            __props__.__dict__["factory_name"] = factory_name
            __props__.__dict__["folder"] = folder
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source_connections_info is None and not opts.urn:
                raise TypeError("Missing required property 'source_connections_info'")
            __props__.__dict__["source_connections_info"] = source_connections_info
            __props__.__dict__["status"] = status
            if target_connections_info is None and not opts.urn:
                raise TypeError("Missing required property 'target_connections_info'")
            __props__.__dict__["target_connections_info"] = target_connections_info
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datafactory/v20180601:ChangeDataCapture")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ChangeDataCapture, __self__).__init__(
            'azure-native:datafactory:ChangeDataCapture',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ChangeDataCapture':
        """
        Get an existing ChangeDataCapture resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ChangeDataCaptureArgs.__new__(ChangeDataCaptureArgs)

        __props__.__dict__["allow_v_net_override"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["folder"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policy"] = None
        __props__.__dict__["source_connections_info"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["target_connections_info"] = None
        __props__.__dict__["type"] = None
        return ChangeDataCapture(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowVNetOverride")
    def allow_v_net_override(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean to determine if the vnet configuration needs to be overwritten.
        """
        return pulumi.get(self, "allow_v_net_override")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the change data capture.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Etag identifies change in the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def folder(self) -> pulumi.Output[Optional['outputs.ChangeDataCaptureResponseFolder']]:
        """
        The folder that this CDC is in. If not specified, CDC will appear at the root level.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output['outputs.MapperPolicyResponse']:
        """
        CDC policy
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="sourceConnectionsInfo")
    def source_connections_info(self) -> pulumi.Output[Sequence['outputs.MapperSourceConnectionsInfoResponse']]:
        """
        List of sources connections that can be used as sources in the CDC.
        """
        return pulumi.get(self, "source_connections_info")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Status of the CDC as to if it is running or stopped.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="targetConnectionsInfo")
    def target_connections_info(self) -> pulumi.Output[Sequence['outputs.MapperTargetConnectionsInfoResponse']]:
        """
        List of target connections that can be used as sources in the CDC.
        """
        return pulumi.get(self, "target_connections_info")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

