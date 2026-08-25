# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .deposit_started_source import DepositStartedSource
from .deposit_completed_destination import DepositCompletedDestination

__all__ = ["DepositCompletedData"]


class DepositCompletedData(BaseModel):
    """
    Details of a fiat deposit that has finished converting and been delivered to the wallet.
    """

    created_at: str

    destination: DepositCompletedDestination
    """
    The crypto asset, chain, delivered amount, and settlement transaction for a
    completed deposit.
    """

    source: DepositStartedSource
    """The fiat deposit that was received, including amount, currency, and originator."""
