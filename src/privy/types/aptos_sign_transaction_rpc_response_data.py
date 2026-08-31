# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .aptos_signed_transaction_bcs_hex import AptosSignedTransactionBcsHex

__all__ = ["AptosSignTransactionRpcResponseData"]


class AptosSignTransactionRpcResponseData(BaseModel):
    """Data returned by the Aptos `aptos_signTransaction` RPC."""

    encoding: Literal["hex"]

    signed_transaction: AptosSignedTransactionBcsHex
    """A non-empty, 0x-prefixed, even-length BCS legacy Ed25519 SignedTransaction."""
