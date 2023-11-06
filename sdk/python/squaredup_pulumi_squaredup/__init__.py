# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .dashboard import *
from .datasource import *
from .get_data_streams import *
from .get_datasources import *
from .provider import *
from .workspace import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import squaredup_pulumi_squaredup.config as __config
    config = __config
else:
    config = _utilities.lazy_import('squaredup_pulumi_squaredup.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "squaredup",
  "mod": "index/dashboard",
  "fqn": "squaredup_pulumi_squaredup",
  "classes": {
   "squaredup:index/dashboard:Dashboard": "Dashboard"
  }
 },
 {
  "pkg": "squaredup",
  "mod": "index/datasource",
  "fqn": "squaredup_pulumi_squaredup",
  "classes": {
   "squaredup:index/datasource:Datasource": "Datasource"
  }
 },
 {
  "pkg": "squaredup",
  "mod": "index/workspace",
  "fqn": "squaredup_pulumi_squaredup",
  "classes": {
   "squaredup:index/workspace:Workspace": "Workspace"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "squaredup",
  "token": "pulumi:providers:squaredup",
  "fqn": "squaredup_pulumi_squaredup",
  "class": "Provider"
 }
]
"""
)