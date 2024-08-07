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
    'EnterpriseKnowledgeGraphPropertiesResponse',
    'SkuResponse',
]

@pulumi.output_type
class EnterpriseKnowledgeGraphPropertiesResponse(dict):
    """
    The parameters to provide for the EnterpriseKnowledgeGraph.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EnterpriseKnowledgeGraphPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EnterpriseKnowledgeGraphPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EnterpriseKnowledgeGraphPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: Optional[str] = None,
                 metadata: Optional[Any] = None,
                 provisioning_state: Optional[str] = None):
        """
        The parameters to provide for the EnterpriseKnowledgeGraph.
        :param str description: The description of the EnterpriseKnowledgeGraph
        :param Any metadata: Specifies the metadata  of the resource.
        :param str provisioning_state: The state of EnterpriseKnowledgeGraph provisioning
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the EnterpriseKnowledgeGraph
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        Specifies the metadata  of the resource.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The state of EnterpriseKnowledgeGraph provisioning
        """
        return pulumi.get(self, "provisioning_state")


@pulumi.output_type
class SkuResponse(dict):
    """
    The SKU of the EnterpriseKnowledgeGraph service account.
    """
    def __init__(__self__, *,
                 name: str):
        """
        The SKU of the EnterpriseKnowledgeGraph service account.
        :param str name: The sku name
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The sku name
        """
        return pulumi.get(self, "name")


