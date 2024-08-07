# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'PublicNetworkAccess',
]


class PublicNetworkAccess(str, Enum):
    """
    Gets or sets allow or disallow public network access to Azure Monitor Workspace
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
