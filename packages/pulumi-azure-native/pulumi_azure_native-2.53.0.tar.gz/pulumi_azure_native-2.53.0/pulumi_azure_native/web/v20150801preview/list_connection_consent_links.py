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
from ._inputs import *

__all__ = [
    'ListConnectionConsentLinksResult',
    'AwaitableListConnectionConsentLinksResult',
    'list_connection_consent_links',
    'list_connection_consent_links_output',
]

@pulumi.output_type
class ListConnectionConsentLinksResult:
    """
    Collection of consent links
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.ConsentLinkResponse']]:
        """
        Collection of resources
        """
        return pulumi.get(self, "value")


class AwaitableListConnectionConsentLinksResult(ListConnectionConsentLinksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListConnectionConsentLinksResult(
            value=self.value)


def list_connection_consent_links(connection_name: Optional[str] = None,
                                  id: Optional[str] = None,
                                  kind: Optional[str] = None,
                                  location: Optional[str] = None,
                                  name: Optional[str] = None,
                                  parameters: Optional[Sequence[Union['ConsentLinkInputParameter', 'ConsentLinkInputParameterDict']]] = None,
                                  resource_group_name: Optional[str] = None,
                                  tags: Optional[Mapping[str, str]] = None,
                                  type: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListConnectionConsentLinksResult:
    """
    Lists consent links of a connection.


    :param str connection_name: The connection name.
    :param str id: Resource Id
    :param str kind: Kind of resource
    :param str location: Resource Location
    :param str name: Resource Name
    :param Sequence[Union['ConsentLinkInputParameter', 'ConsentLinkInputParameterDict']] parameters: Array of links
    :param str resource_group_name: The resource group name.
    :param Mapping[str, str] tags: Resource tags
    :param str type: Resource type
    """
    __args__ = dict()
    __args__['connectionName'] = connection_name
    __args__['id'] = id
    __args__['kind'] = kind
    __args__['location'] = location
    __args__['name'] = name
    __args__['parameters'] = parameters
    __args__['resourceGroupName'] = resource_group_name
    __args__['tags'] = tags
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20150801preview:listConnectionConsentLinks', __args__, opts=opts, typ=ListConnectionConsentLinksResult).value

    return AwaitableListConnectionConsentLinksResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_connection_consent_links)
def list_connection_consent_links_output(connection_name: Optional[pulumi.Input[str]] = None,
                                         id: Optional[pulumi.Input[Optional[str]]] = None,
                                         kind: Optional[pulumi.Input[Optional[str]]] = None,
                                         location: Optional[pulumi.Input[Optional[str]]] = None,
                                         name: Optional[pulumi.Input[Optional[str]]] = None,
                                         parameters: Optional[pulumi.Input[Optional[Sequence[Union['ConsentLinkInputParameter', 'ConsentLinkInputParameterDict']]]]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                         type: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListConnectionConsentLinksResult]:
    """
    Lists consent links of a connection.


    :param str connection_name: The connection name.
    :param str id: Resource Id
    :param str kind: Kind of resource
    :param str location: Resource Location
    :param str name: Resource Name
    :param Sequence[Union['ConsentLinkInputParameter', 'ConsentLinkInputParameterDict']] parameters: Array of links
    :param str resource_group_name: The resource group name.
    :param Mapping[str, str] tags: Resource tags
    :param str type: Resource type
    """
    ...
