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
    'GetWebPubSubCustomDomainResult',
    'AwaitableGetWebPubSubCustomDomainResult',
    'get_web_pub_sub_custom_domain',
    'get_web_pub_sub_custom_domain_output',
]

@pulumi.output_type
class GetWebPubSubCustomDomainResult:
    """
    A custom domain
    """
    def __init__(__self__, custom_certificate=None, domain_name=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if custom_certificate and not isinstance(custom_certificate, dict):
            raise TypeError("Expected argument 'custom_certificate' to be a dict")
        pulumi.set(__self__, "custom_certificate", custom_certificate)
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="customCertificate")
    def custom_certificate(self) -> 'outputs.ResourceReferenceResponse':
        """
        Reference to a resource.
        """
        return pulumi.get(self, "custom_certificate")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        """
        The custom domain name.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

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
        Provisioning state of the resource.
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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWebPubSubCustomDomainResult(GetWebPubSubCustomDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebPubSubCustomDomainResult(
            custom_certificate=self.custom_certificate,
            domain_name=self.domain_name,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_web_pub_sub_custom_domain(name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  resource_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebPubSubCustomDomainResult:
    """
    Get a custom domain.


    :param str name: Custom domain name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:webpubsub/v20230601preview:getWebPubSubCustomDomain', __args__, opts=opts, typ=GetWebPubSubCustomDomainResult).value

    return AwaitableGetWebPubSubCustomDomainResult(
        custom_certificate=pulumi.get(__ret__, 'custom_certificate'),
        domain_name=pulumi.get(__ret__, 'domain_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_web_pub_sub_custom_domain)
def get_web_pub_sub_custom_domain_output(name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         resource_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebPubSubCustomDomainResult]:
    """
    Get a custom domain.


    :param str name: Custom domain name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource.
    """
    ...
