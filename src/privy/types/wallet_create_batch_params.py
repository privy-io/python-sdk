# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .wallet_batch_item_input_param import WalletBatchItemInputParam

__all__ = ["WalletCreateBatchParams"]


class WalletCreateBatchParams(TypedDict, total=False):
    wallets: Required[Iterable[WalletBatchItemInputParam]]
    """Array of wallet creation requests. Minimum 1, maximum 100."""
