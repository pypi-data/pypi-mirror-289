# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApiKind',
    'DeploymentState',
    'EnvironmentKind',
    'EnvironmentServerType',
    'LifecycleStage',
    'ManagedServiceIdentityType',
    'MetadataAssignmentEntity',
]


class ApiKind(str, Enum):
    """
    Kind of API. For example, REST or GraphQL.
    """
    REST = "rest"
    """
    A Representational State Transfer Api
    """
    GRAPHQL = "graphql"
    """
    A Graph query language Api
    """
    GRPC = "grpc"
    """
    A gRPC Api
    """
    SOAP = "soap"
    """
    A SOAP Api
    """
    WEBHOOK = "webhook"
    """
    Web Hook
    """
    WEBSOCKET = "websocket"
    """
    Web Socket
    """


class DeploymentState(str, Enum):
    """
    State of API deployment.
    """
    ACTIVE = "active"
    """
    Active State
    """
    INACTIVE = "inactive"
    """
    Inactive State
    """


class EnvironmentKind(str, Enum):
    """
    Environment kind.
    """
    DEVELOPMENT = "development"
    """
    Development environment
    """
    TESTING = "testing"
    """
    Testing environment
    """
    STAGING = "staging"
    """
    Staging environment
    """
    PRODUCTION = "production"
    """
    Production environment
    """


class EnvironmentServerType(str, Enum):
    """
    Type of the server that represents the environment.
    """
    AZURE_AP_I_MANAGEMENT = "Azure API Management"
    """
    Api Management Server
    """
    AZURE_COMPUTE_SERVICE = "Azure compute service"
    """
    Compute server
    """
    APIGEE_AP_I_MANAGEMENT = "Apigee API Management"
    """
    Apigee server
    """
    AW_S_AP_I_GATEWAY = "AWS API Gateway"
    """
    AWS Api Gateway server
    """
    KONG_AP_I_GATEWAY = "Kong API Gateway"
    """
    Kong API Gateway server
    """
    KUBERNETES = "Kubernetes"
    """
    Kubernetes server
    """
    MULE_SOFT_AP_I_MANAGEMENT = "MuleSoft API Management"
    """
    Mulesoft Api Management server
    """


class LifecycleStage(str, Enum):
    """
    Current lifecycle stage of the API.
    """
    DESIGN = "design"
    """
    design stage
    """
    DEVELOPMENT = "development"
    """
    development stage
    """
    TESTING = "testing"
    """
    testing stage
    """
    PREVIEW = "preview"
    """
    In preview
    """
    PRODUCTION = "production"
    """
    In production
    """
    DEPRECATED = "deprecated"
    """
    deprecated stage
    """
    RETIRED = "retired"
    """
    Retired stage
    """


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class MetadataAssignmentEntity(str, Enum):
    """
    The entities this metadata schema component gets applied to.
    """
    API = "api"
    """
    Assigned to API
    """
    ENVIRONMENT = "environment"
    """
    Assigned to Environment
    """
    DEPLOYMENT = "deployment"
    """
    Assigned to Deployment
    """
