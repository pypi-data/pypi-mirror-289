# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .contact import *
from .contact_profile import *
from .edge_site import *
from .get_contact import *
from .get_contact_profile import *
from .get_edge_site import *
from .get_ground_station import *
from .get_l2_connection import *
from .get_spacecraft import *
from .ground_station import *
from .l2_connection import *
from .list_edge_site_l2_connections import *
from .list_ground_station_l2_connections import *
from .list_spacecraft_available_contacts import *
from .spacecraft import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.orbital.v20220301 as __v20220301
    v20220301 = __v20220301
    import pulumi_azure_native.orbital.v20221101 as __v20221101
    v20221101 = __v20221101
    import pulumi_azure_native.orbital.v20240301 as __v20240301
    v20240301 = __v20240301
    import pulumi_azure_native.orbital.v20240301preview as __v20240301preview
    v20240301preview = __v20240301preview
else:
    v20220301 = _utilities.lazy_import('pulumi_azure_native.orbital.v20220301')
    v20221101 = _utilities.lazy_import('pulumi_azure_native.orbital.v20221101')
    v20240301 = _utilities.lazy_import('pulumi_azure_native.orbital.v20240301')
    v20240301preview = _utilities.lazy_import('pulumi_azure_native.orbital.v20240301preview')

