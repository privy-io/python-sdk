# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .wallet_automation_reindex_asset_result import WalletAutomationReindexAssetResult

__all__ = ["WalletAutomationReindexResponse"]


class WalletAutomationReindexResponse(BaseModel):
    """Result of re-checking a wallet against its wallet automations."""

    results: List[WalletAutomationReindexAssetResult]

    wallet_id: str
