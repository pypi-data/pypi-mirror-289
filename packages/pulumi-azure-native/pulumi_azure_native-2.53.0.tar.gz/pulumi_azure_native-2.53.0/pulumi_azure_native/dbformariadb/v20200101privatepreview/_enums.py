# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ServerKeyType',
]


class ServerKeyType(str, Enum):
    """
    The key type like  'AzureKeyVault'.
    """
    AZURE_KEY_VAULT = "AzureKeyVault"
