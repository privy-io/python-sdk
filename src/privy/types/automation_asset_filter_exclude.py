# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .automation_asset_spec import AutomationAssetSpec

__all__ = ["AutomationAssetFilterExclude"]


class AutomationAssetFilterExclude(BaseModel):
    """Match all assets except the specified ones."""

    mode: Literal["exclude"]

    values: List[AutomationAssetSpec]
