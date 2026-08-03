# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .gas_spend_currency import GasSpendCurrency

__all__ = ["GasSpendResponseBody"]


class GasSpendResponseBody(BaseModel):
    """Aggregated Privy gas credits charged for a set of wallets over a time range."""

    currency: GasSpendCurrency
    """Currency for gas spend values."""

    value: str
    """Total Privy credits charged as a decimal string."""
