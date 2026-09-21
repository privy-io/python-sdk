# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AutomationAssetFilterAll"]


class AutomationAssetFilterAll(BaseModel):
    """Match all assets."""

    mode: Literal["all"]
