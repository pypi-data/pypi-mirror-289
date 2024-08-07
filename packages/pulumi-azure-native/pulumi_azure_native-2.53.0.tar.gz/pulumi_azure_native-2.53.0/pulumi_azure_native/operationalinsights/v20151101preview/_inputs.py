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
from ._enums import *

__all__ = [
    'MachineReferenceWithHintsArgs',
    'MachineReferenceWithHintsArgsDict',
    'SkuArgs',
    'SkuArgsDict',
]

MYPY = False

if not MYPY:
    class MachineReferenceWithHintsArgsDict(TypedDict):
        """
        A machine reference with a hint of the machine's name and operating system.
        """
        id: pulumi.Input[str]
        """
        Resource URI.
        """
        kind: pulumi.Input[str]
        """
        Specifies the sub-class of the reference.
        Expected value is 'ref:machinewithhints'.
        """
elif False:
    MachineReferenceWithHintsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MachineReferenceWithHintsArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 kind: pulumi.Input[str]):
        """
        A machine reference with a hint of the machine's name and operating system.
        :param pulumi.Input[str] id: Resource URI.
        :param pulumi.Input[str] kind: Specifies the sub-class of the reference.
               Expected value is 'ref:machinewithhints'.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "kind", 'ref:machinewithhints')

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Resource URI.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Specifies the sub-class of the reference.
        Expected value is 'ref:machinewithhints'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)


if not MYPY:
    class SkuArgsDict(TypedDict):
        """
        The SKU (tier) of a workspace.
        """
        name: pulumi.Input[Union[str, 'SkuNameEnum']]
        """
        The name of the SKU.
        """
elif False:
    SkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'SkuNameEnum']]):
        """
        The SKU (tier) of a workspace.
        :param pulumi.Input[Union[str, 'SkuNameEnum']] name: The name of the SKU.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'SkuNameEnum']]:
        """
        The name of the SKU.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'SkuNameEnum']]):
        pulumi.set(self, "name", value)


