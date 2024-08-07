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
    'GetOrganizationApiKeyResult',
    'AwaitableGetOrganizationApiKeyResult',
    'get_organization_api_key',
    'get_organization_api_key_output',
]

@pulumi.output_type
class GetOrganizationApiKeyResult:
    """
    The User Api Key created for the Organization associated with the User Email Id that was passed in the request
    """
    def __init__(__self__, properties=None):
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.UserApiKeyResponsePropertiesResponse':
        return pulumi.get(self, "properties")


class AwaitableGetOrganizationApiKeyResult(GetOrganizationApiKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationApiKeyResult(
            properties=self.properties)


def get_organization_api_key(email_id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationApiKeyResult:
    """
    Fetch User API Key from internal database, if it was generated and stored while creating the Elasticsearch Organization.


    :param str email_id: The User email Id
    """
    __args__ = dict()
    __args__['emailId'] = email_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic/v20240501preview:getOrganizationApiKey', __args__, opts=opts, typ=GetOrganizationApiKeyResult).value

    return AwaitableGetOrganizationApiKeyResult(
        properties=pulumi.get(__ret__, 'properties'))


@_utilities.lift_output_func(get_organization_api_key)
def get_organization_api_key_output(email_id: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationApiKeyResult]:
    """
    Fetch User API Key from internal database, if it was generated and stored while creating the Elasticsearch Organization.


    :param str email_id: The User email Id
    """
    ...
