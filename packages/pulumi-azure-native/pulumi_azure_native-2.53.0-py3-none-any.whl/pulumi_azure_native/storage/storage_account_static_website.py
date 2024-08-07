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

__all__ = ['StorageAccountStaticWebsiteArgs', 'StorageAccountStaticWebsite']

@pulumi.input_type
class StorageAccountStaticWebsiteArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 error404_document: Optional[pulumi.Input[str]] = None,
                 index_document: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StorageAccountStaticWebsite resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] error404_document: The absolute path to a custom webpage that should be used when a request is made which does not correspond to an existing file.
        :param pulumi.Input[str] index_document: The webpage that Azure Storage serves for requests to the root of a website or any sub-folder. For example, 'index.html'. The value is case-sensitive.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if error404_document is not None:
            pulumi.set(__self__, "error404_document", error404_document)
        if index_document is not None:
            pulumi.set(__self__, "index_document", index_document)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the storage account within the specified resource group.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="error404Document")
    def error404_document(self) -> Optional[pulumi.Input[str]]:
        """
        The absolute path to a custom webpage that should be used when a request is made which does not correspond to an existing file.
        """
        return pulumi.get(self, "error404_document")

    @error404_document.setter
    def error404_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "error404_document", value)

    @property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> Optional[pulumi.Input[str]]:
        """
        The webpage that Azure Storage serves for requests to the root of a website or any sub-folder. For example, 'index.html'. The value is case-sensitive.
        """
        return pulumi.get(self, "index_document")

    @index_document.setter
    def index_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "index_document", value)


class StorageAccountStaticWebsite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 error404_document: Optional[pulumi.Input[str]] = None,
                 index_document: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Enables the static website feature of a storage account.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group.
        :param pulumi.Input[str] error404_document: The absolute path to a custom webpage that should be used when a request is made which does not correspond to an existing file.
        :param pulumi.Input[str] index_document: The webpage that Azure Storage serves for requests to the root of a website or any sub-folder. For example, 'index.html'. The value is case-sensitive.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageAccountStaticWebsiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Enables the static website feature of a storage account.

        :param str resource_name: The name of the resource.
        :param StorageAccountStaticWebsiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageAccountStaticWebsiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 error404_document: Optional[pulumi.Input[str]] = None,
                 index_document: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StorageAccountStaticWebsiteArgs.__new__(StorageAccountStaticWebsiteArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["error404_document"] = error404_document
            __props__.__dict__["index_document"] = index_document
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["container_name"] = None
        super(StorageAccountStaticWebsite, __self__).__init__(
            'azure-native:storage:StorageAccountStaticWebsite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageAccountStaticWebsite':
        """
        Get an existing StorageAccountStaticWebsite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StorageAccountStaticWebsiteArgs.__new__(StorageAccountStaticWebsiteArgs)

        __props__.__dict__["container_name"] = None
        __props__.__dict__["error404_document"] = None
        __props__.__dict__["index_document"] = None
        return StorageAccountStaticWebsite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[str]:
        """
        The name of the container to upload blobs to.
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="error404Document")
    def error404_document(self) -> pulumi.Output[Optional[str]]:
        """
        The absolute path to a custom webpage that should be used when a request is made which does not correspond to an existing file.
        """
        return pulumi.get(self, "error404_document")

    @property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> pulumi.Output[Optional[str]]:
        """
        The webpage that Azure Storage serves for requests to the root of a website or any sub-folder. For example, 'index.html'. The value is case-sensitive.
        """
        return pulumi.get(self, "index_document")

