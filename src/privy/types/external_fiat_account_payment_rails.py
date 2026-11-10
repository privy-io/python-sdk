# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["ExternalFiatAccountPaymentRails"]


class ExternalFiatAccountPaymentRails(BaseModel):
    """
    Payment rails supported by an external fiat account and reasons other rails are unavailable.
    """

    supported: List[str]
    """
    Supported payment rails, using the same names as `payment_rail` on payouts, such
    as ach, ach_same_day, wire, or fednow.
    """

    unsupported_reasons: Dict[str, str]
    """Reasons payment rails are unavailable, keyed by rail name."""
