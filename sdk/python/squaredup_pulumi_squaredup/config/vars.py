# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('squaredup')


class _ExportableConfig(types.ModuleType):
    @property
    def api_key(self) -> Optional[str]:
        """
        API Key for SquaredUp API. May also be set via the SQUAREDUP_API_KEY environment variable.
        """
        return __config__.get('apiKey')

    @property
    def region(self) -> Optional[str]:
        """
        Region of your SquaredUp instance. May also be set via the SQUAREDUP_REGION environment variable.
        """
        return __config__.get('region')
