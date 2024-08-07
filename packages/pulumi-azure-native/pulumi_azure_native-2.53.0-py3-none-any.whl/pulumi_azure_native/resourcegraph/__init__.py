# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from .get_graph_query import *
from .graph_query import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.resourcegraph.v20180901preview as __v20180901preview
    v20180901preview = __v20180901preview
    import pulumi_azure_native.resourcegraph.v20190401 as __v20190401
    v20190401 = __v20190401
    import pulumi_azure_native.resourcegraph.v20200401preview as __v20200401preview
    v20200401preview = __v20200401preview
    import pulumi_azure_native.resourcegraph.v20210301 as __v20210301
    v20210301 = __v20210301
    import pulumi_azure_native.resourcegraph.v20221001 as __v20221001
    v20221001 = __v20221001
    import pulumi_azure_native.resourcegraph.v20240401 as __v20240401
    v20240401 = __v20240401
else:
    v20180901preview = _utilities.lazy_import('pulumi_azure_native.resourcegraph.v20180901preview')
    v20190401 = _utilities.lazy_import('pulumi_azure_native.resourcegraph.v20190401')
    v20200401preview = _utilities.lazy_import('pulumi_azure_native.resourcegraph.v20200401preview')
    v20210301 = _utilities.lazy_import('pulumi_azure_native.resourcegraph.v20210301')
    v20221001 = _utilities.lazy_import('pulumi_azure_native.resourcegraph.v20221001')
    v20240401 = _utilities.lazy_import('pulumi_azure_native.resourcegraph.v20240401')

