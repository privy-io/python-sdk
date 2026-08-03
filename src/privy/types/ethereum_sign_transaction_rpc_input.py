# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_sign_transaction_rpc_input_params import EthereumSignTransactionRpcInputParams

__all__ = ["EthereumSignTransactionRpcInput"]


class EthereumSignTransactionRpcInput(BaseModel):
    """Executes the EVM `eth_signTransaction` RPC to sign a transaction."""

    method: Literal["eth_signTransaction"]

    params: EthereumSignTransactionRpcInputParams
    """Parameters for the EVM `eth_signTransaction` RPC."""

    address: Optional[str] = None

    chain_type: Optional[Literal["ethereum"]] = None

    wallet_id: Optional[str] = None
