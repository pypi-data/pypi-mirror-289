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

__all__ = [
    'GetApiManagementServiceDomainOwnershipIdentifierResult',
    'AwaitableGetApiManagementServiceDomainOwnershipIdentifierResult',
    'get_api_management_service_domain_ownership_identifier',
    'get_api_management_service_domain_ownership_identifier_output',
]

@pulumi.output_type
class GetApiManagementServiceDomainOwnershipIdentifierResult:
    """
    Response of the GetDomainOwnershipIdentifier operation.
    """
    def __init__(__self__, domain_ownership_identifier=None):
        if domain_ownership_identifier and not isinstance(domain_ownership_identifier, str):
            raise TypeError("Expected argument 'domain_ownership_identifier' to be a str")
        pulumi.set(__self__, "domain_ownership_identifier", domain_ownership_identifier)

    @property
    @pulumi.getter(name="domainOwnershipIdentifier")
    def domain_ownership_identifier(self) -> str:
        """
        The domain ownership identifier value.
        """
        return pulumi.get(self, "domain_ownership_identifier")


class AwaitableGetApiManagementServiceDomainOwnershipIdentifierResult(GetApiManagementServiceDomainOwnershipIdentifierResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiManagementServiceDomainOwnershipIdentifierResult(
            domain_ownership_identifier=self.domain_ownership_identifier)


def get_api_management_service_domain_ownership_identifier(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiManagementServiceDomainOwnershipIdentifierResult:
    """
    Get the custom domain ownership identifier for an API Management service.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20220401preview:getApiManagementServiceDomainOwnershipIdentifier', __args__, opts=opts, typ=GetApiManagementServiceDomainOwnershipIdentifierResult).value

    return AwaitableGetApiManagementServiceDomainOwnershipIdentifierResult(
        domain_ownership_identifier=pulumi.get(__ret__, 'domain_ownership_identifier'))


@_utilities.lift_output_func(get_api_management_service_domain_ownership_identifier)
def get_api_management_service_domain_ownership_identifier_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiManagementServiceDomainOwnershipIdentifierResult]:
    """
    Get the custom domain ownership identifier for an API Management service.
    """
    ...
