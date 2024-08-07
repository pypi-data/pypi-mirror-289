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
from ._inputs import *

__all__ = ['FileArgs', 'File']

@pulumi.input_type
class FileArgs:
    def __init__(__self__, *,
                 group_name: pulumi.Input[str],
                 project_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 file_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['ProjectFilePropertiesArgs']] = None):
        """
        The set of arguments for constructing a File resource.
        :param pulumi.Input[str] group_name: Name of the resource group
        :param pulumi.Input[str] project_name: Name of the project
        :param pulumi.Input[str] service_name: Name of the service
        :param pulumi.Input[str] file_name: Name of the File
        :param pulumi.Input['ProjectFilePropertiesArgs'] properties: Custom file properties
        """
        pulumi.set(__self__, "group_name", group_name)
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "service_name", service_name)
        if file_name is not None:
            pulumi.set(__self__, "file_name", file_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        Name of the project
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        Name of the service
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the File
        """
        return pulumi.get(self, "file_name")

    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['ProjectFilePropertiesArgs']]:
        """
        Custom file properties
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ProjectFilePropertiesArgs']]):
        pulumi.set(self, "properties", value)


class File(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 file_name: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['ProjectFilePropertiesArgs', 'ProjectFilePropertiesArgsDict']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A file resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] file_name: Name of the File
        :param pulumi.Input[str] group_name: Name of the resource group
        :param pulumi.Input[str] project_name: Name of the project
        :param pulumi.Input[Union['ProjectFilePropertiesArgs', 'ProjectFilePropertiesArgsDict']] properties: Custom file properties
        :param pulumi.Input[str] service_name: Name of the service
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A file resource

        :param str resource_name: The name of the resource.
        :param FileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 file_name: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['ProjectFilePropertiesArgs', 'ProjectFilePropertiesArgsDict']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FileArgs.__new__(FileArgs)

            __props__.__dict__["file_name"] = file_name
            if group_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_name'")
            __props__.__dict__["group_name"] = group_name
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            __props__.__dict__["properties"] = properties
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datamigration:File"), pulumi.Alias(type_="azure-native:datamigration/v20180715preview:File"), pulumi.Alias(type_="azure-native:datamigration/v20210630:File"), pulumi.Alias(type_="azure-native:datamigration/v20211030preview:File"), pulumi.Alias(type_="azure-native:datamigration/v20220130preview:File"), pulumi.Alias(type_="azure-native:datamigration/v20220330preview:File")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(File, __self__).__init__(
            'azure-native:datamigration/v20230715preview:File',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'File':
        """
        Get an existing File resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FileArgs.__new__(FileArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return File(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        HTTP strong entity tag value. This is ignored if submitted.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ProjectFilePropertiesResponse']:
        """
        Custom file properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

