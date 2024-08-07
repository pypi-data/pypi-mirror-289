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

__all__ = [
    'GetAssociationResult',
    'AwaitableGetAssociationResult',
    'get_association',
    'get_association_output',
]

@pulumi.output_type
class GetAssociationResult:
    """
    The resource definition of this association.
    """
    def __init__(__self__, id=None, name=None, provisioning_state=None, target_resource_id=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if target_resource_id and not isinstance(target_resource_id, str):
            raise TypeError("Expected argument 'target_resource_id' to be a str")
        pulumi.set(__self__, "target_resource_id", target_resource_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The association id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The association name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the association.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[str]:
        """
        The REST resource instance of the target resource for this association.
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The association type.
        """
        return pulumi.get(self, "type")


class AwaitableGetAssociationResult(GetAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssociationResult(
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            target_resource_id=self.target_resource_id,
            type=self.type)


def get_association(association_name: Optional[str] = None,
                    scope: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssociationResult:
    """
    Get an association.
    Azure REST API version: 2018-09-01-preview.


    :param str association_name: The name of the association.
    :param str scope: The scope of the association.
    """
    __args__ = dict()
    __args__['associationName'] = association_name
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:customproviders:getAssociation', __args__, opts=opts, typ=GetAssociationResult).value

    return AwaitableGetAssociationResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        target_resource_id=pulumi.get(__ret__, 'target_resource_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_association)
def get_association_output(association_name: Optional[pulumi.Input[str]] = None,
                           scope: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssociationResult]:
    """
    Get an association.
    Azure REST API version: 2018-09-01-preview.


    :param str association_name: The name of the association.
    :param str scope: The scope of the association.
    """
    ...
