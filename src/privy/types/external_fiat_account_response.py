# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .external_fiat_account import ExternalFiatAccount

__all__ = ["ExternalFiatAccountResponse"]


class ExternalFiatAccountResponse(BaseModel):
    """Response containing a single external fiat account."""

    external_fiat_account: ExternalFiatAccount
    """A Bridge external fiat account linked to a user."""
