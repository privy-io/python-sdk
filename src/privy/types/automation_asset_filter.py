# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .automation_asset_filter_all import AutomationAssetFilterAll
from .automation_asset_filter_exclude import AutomationAssetFilterExclude
from .automation_asset_filter_include import AutomationAssetFilterInclude

__all__ = ["AutomationAssetFilter"]

AutomationAssetFilter: TypeAlias = Annotated[
    Union[AutomationAssetFilterAll, AutomationAssetFilterInclude, AutomationAssetFilterExclude],
    PropertyInfo(discriminator="mode"),
]
