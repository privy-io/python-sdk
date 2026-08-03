# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletFundsErc20Asset"]


class WalletFundsErc20Asset(BaseModel):
    """An ERC-20 token asset."""

    address: str

    type: Literal["erc20"]
