# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .wallet_automation_reindex_caip_2 import WalletAutomationReindexCaip2
from .wallet_automation_reindex_asset_status import WalletAutomationReindexAssetStatus

__all__ = ["WalletAutomationReindexAssetResult"]


class WalletAutomationReindexAssetResult(BaseModel):
    """The outcome of checking one asset on the requested chain during a reindex."""

    asset_address: str
    """Asset contract address; the native asset uses `native`."""

    caip2: WalletAutomationReindexCaip2
    """EVM CAIP-2 chain identifier (e.g.

    "eip155:4217" for Tempo, "eip155:1" for Ethereum).
    """

    existing_execution_id: Optional[str] = None
    """ID of the in-flight execution blocking a re-trigger.

    Populated only when `status` is `skipped_existing_execution`; `null` otherwise.
    """

    raw_balance: Optional[str] = None
    """On-chain balance in base units.

    Populated when `status` is `triggered` or `skipped_zero_balance`; `null`
    otherwise. For example, 1 USDC is `1000000`.
    """

    status: WalletAutomationReindexAssetStatus
    """Outcome of checking a single asset during a wallet automation reindex.

    One of `triggered`, `skipped_zero_balance`, `skipped_no_match`,
    `skipped_existing_execution`, or `failed`.
    """
