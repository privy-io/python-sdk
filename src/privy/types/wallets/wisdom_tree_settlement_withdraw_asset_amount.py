# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .tmmf_currency import TmmfCurrency
from .tmmf_decimal_amount import TmmfDecimalAmount

__all__ = ["WisdomTreeSettlementWithdrawAssetAmount"]


class WisdomTreeSettlementWithdrawAssetAmount(BaseModel):
    """An amount of the currency a tMMF withdrawal receives."""

    amount: TmmfDecimalAmount
    """A positive decimal amount in the asset's standard unit, e.g. "1000.00"."""

    withdraw_asset: TmmfCurrency
    """Currency symbol, e.g. "USDC". Case-insensitive."""
