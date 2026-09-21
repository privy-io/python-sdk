# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["DepositAccountCryptoQuoteResponse"]


class DepositAccountCryptoQuoteResponse(BaseModel):
    """An indicative crypto deposit-account quote.

    Amounts are in token standard units.
    """

    created_at: datetime

    estimated_output_amount: str
    """
    Estimated output amount as a decimal string in the destination token's standard
    unit. Not in the smallest on-chain unit.
    """

    input_amount: str
    """Quoted input amount as a decimal string in the source token's standard unit
    (e.g.

    "0.02" for 0.02 ETH). Not in the smallest on-chain unit.
    """
