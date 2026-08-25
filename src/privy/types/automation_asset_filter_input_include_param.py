# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .automation_asset_spec_input_param import AutomationAssetSpecInputParam

__all__ = ["AutomationAssetFilterInputIncludeParam"]


class AutomationAssetFilterInputIncludeParam(TypedDict, total=False):
    """Match only the specified assets (input form with alias support)."""

    mode: Required[Literal["include"]]

    values: Required[Iterable[AutomationAssetSpecInputParam]]
