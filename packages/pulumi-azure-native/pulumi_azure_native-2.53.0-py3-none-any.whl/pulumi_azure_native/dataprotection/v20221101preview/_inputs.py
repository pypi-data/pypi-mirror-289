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
    'DppIdentityDetailsArgs',
    'DppIdentityDetailsArgsDict',
    'ResourceGuardArgs',
    'ResourceGuardArgsDict',
]

MYPY = False

if not MYPY:
    class DppIdentityDetailsArgsDict(TypedDict):
        """
        Identity details
        """
        type: NotRequired[pulumi.Input[str]]
        """
        The identityType which can be either SystemAssigned or None
        """
elif False:
    DppIdentityDetailsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DppIdentityDetailsArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Identity details
        :param pulumi.Input[str] type: The identityType which can be either SystemAssigned or None
        """
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The identityType which can be either SystemAssigned or None
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


if not MYPY:
    class ResourceGuardArgsDict(TypedDict):
        vault_critical_operation_exclusion_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        List of critical operations which are not protected by this resourceGuard
        """
elif False:
    ResourceGuardArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceGuardArgs:
    def __init__(__self__, *,
                 vault_critical_operation_exclusion_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vault_critical_operation_exclusion_list: List of critical operations which are not protected by this resourceGuard
        """
        if vault_critical_operation_exclusion_list is not None:
            pulumi.set(__self__, "vault_critical_operation_exclusion_list", vault_critical_operation_exclusion_list)

    @property
    @pulumi.getter(name="vaultCriticalOperationExclusionList")
    def vault_critical_operation_exclusion_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of critical operations which are not protected by this resourceGuard
        """
        return pulumi.get(self, "vault_critical_operation_exclusion_list")

    @vault_critical_operation_exclusion_list.setter
    def vault_critical_operation_exclusion_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "vault_critical_operation_exclusion_list", value)


