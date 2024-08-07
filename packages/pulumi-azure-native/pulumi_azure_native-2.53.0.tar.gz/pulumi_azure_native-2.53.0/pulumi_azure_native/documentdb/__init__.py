# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .cassandra_cluster import *
from .cassandra_data_center import *
from .cassandra_resource_cassandra_keyspace import *
from .cassandra_resource_cassandra_table import *
from .cassandra_resource_cassandra_view import *
from .database_account import *
from .firewall_rule import *
from .get_cassandra_cluster import *
from .get_cassandra_data_center import *
from .get_cassandra_resource_cassandra_keyspace import *
from .get_cassandra_resource_cassandra_table import *
from .get_cassandra_resource_cassandra_view import *
from .get_database_account import *
from .get_firewall_rule import *
from .get_graph_resource_graph import *
from .get_gremlin_resource_gremlin_database import *
from .get_gremlin_resource_gremlin_graph import *
from .get_mongo_cluster import *
from .get_mongo_cluster_firewall_rule import *
from .get_mongo_db_resource_mongo_db_collection import *
from .get_mongo_db_resource_mongo_db_database import *
from .get_mongo_db_resource_mongo_role_definition import *
from .get_mongo_db_resource_mongo_user_definition import *
from .get_notebook_workspace import *
from .get_private_endpoint_connection import *
from .get_service import *
from .get_sql_resource_sql_container import *
from .get_sql_resource_sql_database import *
from .get_sql_resource_sql_role_assignment import *
from .get_sql_resource_sql_role_definition import *
from .get_sql_resource_sql_stored_procedure import *
from .get_sql_resource_sql_trigger import *
from .get_sql_resource_sql_user_defined_function import *
from .get_table_resource_table import *
from .get_throughput_pool import *
from .get_throughput_pool_account import *
from .graph_resource_graph import *
from .gremlin_resource_gremlin_database import *
from .gremlin_resource_gremlin_graph import *
from .list_database_account_connection_strings import *
from .list_database_account_keys import *
from .list_mongo_cluster_connection_strings import *
from .list_notebook_workspace_connection_info import *
from .mongo_cluster import *
from .mongo_cluster_firewall_rule import *
from .mongo_db_resource_mongo_db_collection import *
from .mongo_db_resource_mongo_db_database import *
from .mongo_db_resource_mongo_role_definition import *
from .mongo_db_resource_mongo_user_definition import *
from .notebook_workspace import *
from .private_endpoint_connection import *
from .service import *
from .sql_resource_sql_container import *
from .sql_resource_sql_database import *
from .sql_resource_sql_role_assignment import *
from .sql_resource_sql_role_definition import *
from .sql_resource_sql_stored_procedure import *
from .sql_resource_sql_trigger import *
from .sql_resource_sql_user_defined_function import *
from .table_resource_table import *
from .throughput_pool import *
from .throughput_pool_account import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.documentdb.v20210401preview as __v20210401preview
    v20210401preview = __v20210401preview
    import pulumi_azure_native.documentdb.v20210701preview as __v20210701preview
    v20210701preview = __v20210701preview
    import pulumi_azure_native.documentdb.v20230301preview as __v20230301preview
    v20230301preview = __v20230301preview
    import pulumi_azure_native.documentdb.v20230315preview as __v20230315preview
    v20230315preview = __v20230315preview
    import pulumi_azure_native.documentdb.v20230415 as __v20230415
    v20230415 = __v20230415
    import pulumi_azure_native.documentdb.v20230915 as __v20230915
    v20230915 = __v20230915
    import pulumi_azure_native.documentdb.v20230915preview as __v20230915preview
    v20230915preview = __v20230915preview
    import pulumi_azure_native.documentdb.v20231115 as __v20231115
    v20231115 = __v20231115
    import pulumi_azure_native.documentdb.v20231115preview as __v20231115preview
    v20231115preview = __v20231115preview
    import pulumi_azure_native.documentdb.v20240215preview as __v20240215preview
    v20240215preview = __v20240215preview
    import pulumi_azure_native.documentdb.v20240301preview as __v20240301preview
    v20240301preview = __v20240301preview
    import pulumi_azure_native.documentdb.v20240515 as __v20240515
    v20240515 = __v20240515
    import pulumi_azure_native.documentdb.v20240515preview as __v20240515preview
    v20240515preview = __v20240515preview
else:
    v20210401preview = _utilities.lazy_import('pulumi_azure_native.documentdb.v20210401preview')
    v20210701preview = _utilities.lazy_import('pulumi_azure_native.documentdb.v20210701preview')
    v20230301preview = _utilities.lazy_import('pulumi_azure_native.documentdb.v20230301preview')
    v20230315preview = _utilities.lazy_import('pulumi_azure_native.documentdb.v20230315preview')
    v20230415 = _utilities.lazy_import('pulumi_azure_native.documentdb.v20230415')
    v20230915 = _utilities.lazy_import('pulumi_azure_native.documentdb.v20230915')
    v20230915preview = _utilities.lazy_import('pulumi_azure_native.documentdb.v20230915preview')
    v20231115 = _utilities.lazy_import('pulumi_azure_native.documentdb.v20231115')
    v20231115preview = _utilities.lazy_import('pulumi_azure_native.documentdb.v20231115preview')
    v20240215preview = _utilities.lazy_import('pulumi_azure_native.documentdb.v20240215preview')
    v20240301preview = _utilities.lazy_import('pulumi_azure_native.documentdb.v20240301preview')
    v20240515 = _utilities.lazy_import('pulumi_azure_native.documentdb.v20240515')
    v20240515preview = _utilities.lazy_import('pulumi_azure_native.documentdb.v20240515preview')

