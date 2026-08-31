# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .hex import Hex
from .caip_2 import Caip2
from .._models import BaseModel
from .rpc_sponsor_options import RpcSponsorOptions
from .ethereum_send_transaction_rpc_input_params import EthereumSendTransactionRpcInputParams

__all__ = ["EthereumSendTransactionRpcInput"]


class EthereumSendTransactionRpcInput(BaseModel):
    """Executes the EVM `eth_sendTransaction` RPC to sign and broadcast a transaction."""

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    method: Literal["eth_sendTransaction"]

    params: EthereumSendTransactionRpcInputParams
    """Parameters for the EVM `eth_sendTransaction` RPC."""

    address: Optional[str] = None

    chain_type: Optional[Literal["ethereum"]] = None

    experimental_data_suffix: Optional[Hex] = None
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    reference_id: Optional[str] = None
    """Developer-provided identifier for this request. Must be unique per app."""

    sponsor: Optional[bool] = None

    sponsor_options: Optional[RpcSponsorOptions] = None
    """Options for user-pays gas sponsorship on the RPC endpoint.

    When provided alongside `sponsor: true`, controls which token asset the user
    pays gas with.
    """

    wallet_id: Optional[str] = None
