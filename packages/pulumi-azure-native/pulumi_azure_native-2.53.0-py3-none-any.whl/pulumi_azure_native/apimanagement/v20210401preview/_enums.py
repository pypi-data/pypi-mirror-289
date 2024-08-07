# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'SchemaType',
]


class SchemaType(str, Enum):
    """
    Schema Type. Immutable.
    """
    XML = "xml"
    """
    Xml schema type.
    """
    JSON = "json"
    """
    Json schema type.
    """
