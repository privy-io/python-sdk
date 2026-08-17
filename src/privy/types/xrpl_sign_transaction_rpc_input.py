# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .xrpl_sign_transaction_rpc_input_params import XrplSignTransactionRpcInputParams

__all__ = ["XrplSignTransactionRpcInput"]


class XrplSignTransactionRpcInput(BaseModel):
    """Executes the XRPL `xrpl_signTransaction` RPC to sign a transaction.

    The caller is responsible for broadcasting.
    """

    method: Literal["xrpl_signTransaction"]

    params: XrplSignTransactionRpcInputParams
    """Parameters for the XRPL `xrpl_signTransaction` RPC."""
