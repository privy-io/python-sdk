# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .deposit_started_source import DepositStartedSource
from .deposit_started_destination import DepositStartedDestination

__all__ = ["DepositFailedData"]


class DepositFailedData(BaseModel):
    """
    Details of a fiat deposit that failed to convert and was refunded to the sender.
    """

    created_at: str

    destination: DepositStartedDestination
    """The crypto asset and chain the fiat deposit is being converted into."""

    reason: str

    reason_code: str

    refunded_at: str

    source: DepositStartedSource
    """The fiat deposit that was received, including amount, currency, and originator."""
