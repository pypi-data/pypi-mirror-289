# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccessTokenArgs', 'AccessToken']

@pulumi.input_type
class AccessTokenArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str]):
        """
        The set of arguments for constructing a AccessToken resource.
        :param pulumi.Input[str] description: Description of the access token.
        """
        pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        Description of the access token.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)


class AccessToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Access tokens allow a user to authenticate against the Pulumi Cloud

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the access token.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessTokenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Access tokens allow a user to authenticate against the Pulumi Cloud

        :param str resource_name: The name of the resource.
        :param AccessTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessTokenArgs.__new__(AccessTokenArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["value"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["value"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(AccessToken, __self__).__init__(
            'pulumiservice:index:AccessToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccessToken':
        """
        Get an existing AccessToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccessTokenArgs.__new__(AccessTokenArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["value"] = None
        return AccessToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the access token.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The token's value.
        """
        return pulumi.get(self, "value")

