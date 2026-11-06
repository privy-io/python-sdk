# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .tmmf_fund import TmmfFund
from .tmmf_decimal_amount import TmmfDecimalAmount

__all__ = ["WisdomTreeSettlementFundAmount"]


class WisdomTreeSettlementFundAmount(BaseModel):
    """An amount of fund shares a tMMF order sends or receives."""

    amount: TmmfDecimalAmount
    """A positive decimal amount in the asset's standard unit, e.g. "1000.00"."""

    fund: TmmfFund
    """Fund ticker, e.g. "WTGXX". Case-insensitive."""
