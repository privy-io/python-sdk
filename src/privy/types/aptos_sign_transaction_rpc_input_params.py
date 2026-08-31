# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .aptos_bcs_hex import AptosBcsHex

__all__ = ["AptosSignTransactionRpcInputParams"]


class AptosSignTransactionRpcInputParams(BaseModel):
    """Parameters for the Aptos `aptos_signTransaction` RPC."""

    transaction: AptosBcsHex
    """A non-empty, 0x-prefixed, even-length BCS hex string."""
