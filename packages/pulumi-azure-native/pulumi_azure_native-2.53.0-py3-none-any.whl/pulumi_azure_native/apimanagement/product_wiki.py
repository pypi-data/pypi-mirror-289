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
from ._inputs import *

__all__ = ['ProductWikiArgs', 'ProductWiki']

@pulumi.input_type
class ProductWikiArgs:
    def __init__(__self__, *,
                 product_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 documents: Optional[pulumi.Input[Sequence[pulumi.Input['WikiDocumentationContractArgs']]]] = None):
        """
        The set of arguments for constructing a ProductWiki resource.
        :param pulumi.Input[str] product_id: Product identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Sequence[pulumi.Input['WikiDocumentationContractArgs']]] documents: Collection wiki documents included into this wiki.
        """
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if documents is not None:
            pulumi.set(__self__, "documents", documents)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Input[str]:
        """
        Product identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "product_id", value)

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
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def documents(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WikiDocumentationContractArgs']]]]:
        """
        Collection wiki documents included into this wiki.
        """
        return pulumi.get(self, "documents")

    @documents.setter
    def documents(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WikiDocumentationContractArgs']]]]):
        pulumi.set(self, "documents", value)


class ProductWiki(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 documents: Optional[pulumi.Input[Sequence[pulumi.Input[Union['WikiDocumentationContractArgs', 'WikiDocumentationContractArgsDict']]]]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Wiki properties
        Azure REST API version: 2022-08-01.

        Other available API versions: 2022-09-01-preview, 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['WikiDocumentationContractArgs', 'WikiDocumentationContractArgsDict']]]] documents: Collection wiki documents included into this wiki.
        :param pulumi.Input[str] product_id: Product identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProductWikiArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Wiki properties
        Azure REST API version: 2022-08-01.

        Other available API versions: 2022-09-01-preview, 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param ProductWikiArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProductWikiArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 documents: Optional[pulumi.Input[Sequence[pulumi.Input[Union['WikiDocumentationContractArgs', 'WikiDocumentationContractArgsDict']]]]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProductWikiArgs.__new__(ProductWikiArgs)

            __props__.__dict__["documents"] = documents
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20220801:ProductWiki"), pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:ProductWiki"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:ProductWiki"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:ProductWiki"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:ProductWiki")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ProductWiki, __self__).__init__(
            'azure-native:apimanagement:ProductWiki',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProductWiki':
        """
        Get an existing ProductWiki resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProductWikiArgs.__new__(ProductWikiArgs)

        __props__.__dict__["documents"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return ProductWiki(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def documents(self) -> pulumi.Output[Optional[Sequence['outputs.WikiDocumentationContractResponse']]]:
        """
        Collection wiki documents included into this wiki.
        """
        return pulumi.get(self, "documents")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

