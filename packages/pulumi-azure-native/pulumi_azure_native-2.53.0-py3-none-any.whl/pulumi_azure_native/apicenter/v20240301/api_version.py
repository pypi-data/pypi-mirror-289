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

__all__ = ['ApiVersionArgs', 'ApiVersion']

@pulumi.input_type
class ApiVersionArgs:
    def __init__(__self__, *,
                 api_name: pulumi.Input[str],
                 lifecycle_stage: pulumi.Input[Union[str, 'LifecycleStage']],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 title: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 version_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApiVersion resource.
        :param pulumi.Input[str] api_name: The name of the API.
        :param pulumi.Input[Union[str, 'LifecycleStage']] lifecycle_stage: Current lifecycle stage of the API.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of Azure API Center service.
        :param pulumi.Input[str] title: API version title.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] version_name: The name of the API version.
        """
        pulumi.set(__self__, "api_name", api_name)
        pulumi.set(__self__, "lifecycle_stage", lifecycle_stage)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if version_name is not None:
            pulumi.set(__self__, "version_name", version_name)

    @property
    @pulumi.getter(name="apiName")
    def api_name(self) -> pulumi.Input[str]:
        """
        The name of the API.
        """
        return pulumi.get(self, "api_name")

    @api_name.setter
    def api_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_name", value)

    @property
    @pulumi.getter(name="lifecycleStage")
    def lifecycle_stage(self) -> pulumi.Input[Union[str, 'LifecycleStage']]:
        """
        Current lifecycle stage of the API.
        """
        return pulumi.get(self, "lifecycle_stage")

    @lifecycle_stage.setter
    def lifecycle_stage(self, value: pulumi.Input[Union[str, 'LifecycleStage']]):
        pulumi.set(self, "lifecycle_stage", value)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of Azure API Center service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        API version title.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="versionName")
    def version_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the API version.
        """
        return pulumi.get(self, "version_name")

    @version_name.setter
    def version_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_name", value)


class ApiVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_name: Optional[pulumi.Input[str]] = None,
                 lifecycle_stage: Optional[pulumi.Input[Union[str, 'LifecycleStage']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 version_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        API version entity.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_name: The name of the API.
        :param pulumi.Input[Union[str, 'LifecycleStage']] lifecycle_stage: Current lifecycle stage of the API.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of Azure API Center service.
        :param pulumi.Input[str] title: API version title.
        :param pulumi.Input[str] version_name: The name of the API version.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        API version entity.

        :param str resource_name: The name of the resource.
        :param ApiVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_name: Optional[pulumi.Input[str]] = None,
                 lifecycle_stage: Optional[pulumi.Input[Union[str, 'LifecycleStage']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 version_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiVersionArgs.__new__(ApiVersionArgs)

            if api_name is None and not opts.urn:
                raise TypeError("Missing required property 'api_name'")
            __props__.__dict__["api_name"] = api_name
            if lifecycle_stage is None and not opts.urn:
                raise TypeError("Missing required property 'lifecycle_stage'")
            __props__.__dict__["lifecycle_stage"] = lifecycle_stage
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["version_name"] = version_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apicenter:ApiVersion"), pulumi.Alias(type_="azure-native:apicenter/v20240315preview:ApiVersion")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApiVersion, __self__).__init__(
            'azure-native:apicenter/v20240301:ApiVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiVersion':
        """
        Get an existing ApiVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiVersionArgs.__new__(ApiVersionArgs)

        __props__.__dict__["lifecycle_stage"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        return ApiVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="lifecycleStage")
    def lifecycle_stage(self) -> pulumi.Output[str]:
        """
        Current lifecycle stage of the API.
        """
        return pulumi.get(self, "lifecycle_stage")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        API version title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

