# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...bps import Bps
from ...deposit_account_crypto_quote_amount import DepositAccountCryptoQuoteAmount
from ...deposit_account_crypto_quote_asset_param import DepositAccountCryptoQuoteAssetParam

__all__ = ["CryptoQuoteParams"]


class CryptoQuoteParams(TypedDict, total=False):
    destination: Required[DepositAccountCryptoQuoteAssetParam]
    """An asset and chain for an indicative crypto deposit-account quote."""

    source: Required[DepositAccountCryptoQuoteAssetParam]
    """An asset and chain for an indicative crypto deposit-account quote."""

    input_amount: DepositAccountCryptoQuoteAmount
    """
    A positive decimal amount in the source token’s standard unit, not its smallest
    on-chain unit.
    """

    slippage_bps: Bps
    """Value in basis points: integer from 0 to 10000 (0% to 100%)."""
