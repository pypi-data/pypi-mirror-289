# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Architecture',
    'BaseImageTriggerType',
    'OS',
    'SecretObjectType',
    'SourceControlType',
    'SourceRegistryLoginMode',
    'SourceTriggerEvent',
    'TaskStatus',
    'TokenType',
    'TriggerStatus',
    'Variant',
]


class Architecture(str, Enum):
    """
    The OS architecture.
    """
    AMD64 = "amd64"
    X86 = "x86"
    ARM = "arm"


class BaseImageTriggerType(str, Enum):
    """
    The type of the auto trigger for base image dependency updates.
    """
    ALL = "All"
    RUNTIME = "Runtime"


class OS(str, Enum):
    """
    The operating system type required for the run.
    """
    WINDOWS = "Windows"
    LINUX = "Linux"


class SecretObjectType(str, Enum):
    """
    The type of the secret object which determines how the value of the secret object has to be
    interpreted.
    """
    OPAQUE = "Opaque"


class SourceControlType(str, Enum):
    """
    The type of source control service.
    """
    GITHUB = "Github"
    VISUAL_STUDIO_TEAM_SERVICE = "VisualStudioTeamService"


class SourceRegistryLoginMode(str, Enum):
    """
    The authentication mode which determines the source registry login scope. The credentials for the source registry
    will be generated using the given scope. These credentials will be used to login to
    the source registry during the run.
    """
    NONE = "None"
    DEFAULT = "Default"


class SourceTriggerEvent(str, Enum):
    COMMIT = "commit"
    PULLREQUEST = "pullrequest"


class TaskStatus(str, Enum):
    """
    The current status of task.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class TokenType(str, Enum):
    """
    The type of Auth token.
    """
    PAT = "PAT"
    O_AUTH = "OAuth"


class TriggerStatus(str, Enum):
    """
    The current status of trigger.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class Variant(str, Enum):
    """
    Variant of the CPU.
    """
    V6 = "v6"
    V7 = "v7"
    V8 = "v8"
