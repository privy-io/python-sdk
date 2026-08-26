# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .crypto_deposit_asset import CryptoDepositAsset

__all__ = ["CryptoDepositAssetFilterInclude"]


class CryptoDepositAssetFilterInclude(BaseModel):
    """Match only the specified assets, using human-readable aliases when known."""

    mode: Literal["include"]

    values: List[CryptoDepositAsset]
