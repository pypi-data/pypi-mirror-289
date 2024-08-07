# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EnvironmentPermission',
    'PulumiOperation',
    'TeamStackPermissionScope',
    'WebhookFilters',
    'WebhookFormat',
]


class EnvironmentPermission(str, Enum):
    NONE = "none"
    """
    No permissions.
    """
    READ = "read"
    """
    Permission to read environment definition only.
    """
    OPEN = "open"
    """
    Permission to open and read the environment.
    """
    WRITE = "write"
    """
    Permission to open, read and update the environment.
    """
    ADMIN = "admin"
    """
    Permission for all operations on the environment.
    """


class PulumiOperation(str, Enum):
    UPDATE = "update"
    """
    Analogous to `pulumi up` command.
    """
    PREVIEW = "preview"
    """
    Analogous to `pulumi preview` command.
    """
    REFRESH = "refresh"
    """
    Analogous to `pulumi refresh` command.
    """
    DESTROY = "destroy"
    """
    Analogous to `pulumi destroy` command.
    """


class TeamStackPermissionScope(float, Enum):
    READ = 101
    """
    Grants read permissions to stack.
    """
    EDIT = 102
    """
    Grants edit permissions to stack.
    """
    ADMIN = 103
    """
    Grants admin permissions to stack.
    """


class WebhookFilters(str, Enum):
    STACK_CREATED = "stack_created"
    """
    Trigger a webhook when a stack is created. Only valid for org webhooks.
    """
    STACK_DELETED = "stack_deleted"
    """
    Trigger a webhook when a stack is deleted. Only valid for org webhooks.
    """
    UPDATE_SUCCEEDED = "update_succeeded"
    """
    Trigger a webhook when a stack update succeeds.
    """
    UPDATE_FAILED = "update_failed"
    """
    Trigger a webhook when a stack update fails.
    """
    PREVIEW_SUCCEEDED = "preview_succeeded"
    """
    Trigger a webhook when a stack preview succeeds.
    """
    PREVIEW_FAILED = "preview_failed"
    """
    Trigger a webhook when a stack preview fails.
    """
    DESTROY_SUCCEEDED = "destroy_succeeded"
    """
    Trigger a webhook when a stack destroy succeeds.
    """
    DESTROY_FAILED = "destroy_failed"
    """
    Trigger a webhook when a stack destroy fails.
    """
    REFRESH_SUCCEEDED = "refresh_succeeded"
    """
    Trigger a webhook when a stack refresh succeeds.
    """
    REFRESH_FAILED = "refresh_failed"
    """
    Trigger a webhook when a stack refresh fails.
    """
    DEPLOYMENT_QUEUED = "deployment_queued"
    """
    Trigger a webhook when a deployment is queued.
    """
    DEPLOYMENT_STARTED = "deployment_started"
    """
    Trigger a webhook when a deployment starts running.
    """
    DEPLOYMENT_SUCCEEDED = "deployment_succeeded"
    """
    Trigger a webhook when a deployment succeeds.
    """
    DEPLOYMENT_FAILED = "deployment_failed"
    """
    Trigger a webhook when a deployment fails.
    """
    DRIFT_DETECTED = "drift_detected"
    """
    Trigger a webhook when drift is detected.
    """
    DRIFT_DETECTION_SUCCEEDED = "drift_detection_succeeded"
    """
    Trigger a webhook when a drift detection run succeeds, regardless of whether drift is detected.
    """
    DRIFT_DETECTION_FAILED = "drift_detection_failed"
    """
    Trigger a webhook when a drift detection run fails.
    """
    DRIFT_REMEDIATION_SUCCEEDED = "drift_remediation_succeeded"
    """
    Trigger a webhook when a drift remediation run succeeds.
    """
    DRIFT_REMEDIATION_FAILED = "drift_remediation_failed"
    """
    Trigger a webhook when a drift remediation run fails.
    """


class WebhookFormat(str, Enum):
    RAW = "raw"
    """
    The default webhook format.
    """
    SLACK = "slack"
    """
    Messages formatted for consumption by Slack incoming webhooks.
    """
    PULUMI_DEPLOYMENTS = "pulumi_deployments"
    """
    Initiate deployments on a stack from a Pulumi Cloud webhook.
    """
    MICROSOFT_TEAMS = "ms_teams"
    """
    Messages formatted for consumption by Microsoft Teams incoming webhooks.
    """
