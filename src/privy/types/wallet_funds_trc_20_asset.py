# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletFundsTrc20Asset"]


class WalletFundsTrc20Asset(BaseModel):
    """A Tron TRC-20 token asset."""

    address: str

    type: Literal["trc20"]
