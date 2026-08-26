# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .crypto_deposit_asset import CryptoDepositAsset

__all__ = ["CryptoDepositAssetFilterExclude"]


class CryptoDepositAssetFilterExclude(BaseModel):
    """
    Match all assets except the specified ones, using human-readable aliases when known.
    """

    mode: Literal["exclude"]

    values: List[CryptoDepositAsset]
