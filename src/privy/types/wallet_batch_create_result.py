# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from .wallet import Wallet
from .._models import BaseModel

__all__ = ["WalletBatchCreateResult", "WalletBatchCreateSuccess", "WalletBatchCreateFailure"]


class WalletBatchCreateSuccess(BaseModel):
    """A successful wallet creation result within a batch operation."""

    index: float
    """The index of the wallet in the original request array."""

    success: Literal[True]

    wallet: Wallet
    """A wallet managed by Privy's wallet infrastructure."""


class WalletBatchCreateFailure(BaseModel):
    """A failed wallet creation result within a batch operation."""

    code: str
    """
    A PrivyErrorCode string identifying the error type (e.g., "invalid_data",
    "resource_conflict").
    """

    error: str
    """A human-readable error message with details about what went wrong."""

    index: float
    """The index of the wallet in the original request array."""

    success: Literal[False]


WalletBatchCreateResult: TypeAlias = Union[WalletBatchCreateSuccess, WalletBatchCreateFailure]
