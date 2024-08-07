# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'RpSkuTier',
]


class RpSkuTier(str, Enum):
    """
    The name of the Azure pricing tier to which the SKU applies.
    """
    FABRIC = "Fabric"
    """
    Fabric tier
    """
