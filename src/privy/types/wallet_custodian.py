# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WalletCustodian"]


class WalletCustodian(BaseModel):
    """Information about the custodian managing this wallet."""

    provider: str
    """The custodian responsible for the wallet."""

    provider_user_id: str
    """The resource ID of the beneficiary of the custodial wallet."""
