# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .automation_asset_spec_input_param import AutomationAssetSpecInputParam

__all__ = ["AutomationAssetFilterInputExcludeParam"]


class AutomationAssetFilterInputExcludeParam(TypedDict, total=False):
    """Match all assets except the specified ones (input form with alias support)."""

    mode: Required[Literal["exclude"]]

    values: Required[Iterable[AutomationAssetSpecInputParam]]
