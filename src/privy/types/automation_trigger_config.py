# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .automation_asset_filter import AutomationAssetFilter

__all__ = ["AutomationTriggerConfig"]


class AutomationTriggerConfig(BaseModel):
    """Trigger configuration for deposit events."""

    assets: AutomationAssetFilter
    """Which assets to include/exclude for an automation trigger."""

    type: Literal["deposit"]
