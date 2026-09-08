# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletFundsBtknAsset"]


class WalletFundsBtknAsset(BaseModel):
    """A token issued on Spark, identified by its BTKN identifier."""

    identifier: str

    type: Literal["btkn"]
