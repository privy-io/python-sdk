# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .automation_asset_filter_all_param import AutomationAssetFilterAllParam
from .automation_asset_filter_input_exclude_param import AutomationAssetFilterInputExcludeParam
from .automation_asset_filter_input_include_param import AutomationAssetFilterInputIncludeParam

__all__ = ["AutomationAssetFilterInputParam"]

AutomationAssetFilterInputParam: TypeAlias = Union[
    AutomationAssetFilterAllParam, AutomationAssetFilterInputIncludeParam, AutomationAssetFilterInputExcludeParam
]
