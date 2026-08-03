# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .hex import Hex
from .caip_2 import Caip2
from .._models import BaseModel
from .rpc_sponsor_options import RpcSponsorOptions
from .ethereum_send_calls_rpc_input_params import EthereumSendCallsRpcInputParams

__all__ = ["EthereumSendCallsRpcInput"]


class EthereumSendCallsRpcInput(BaseModel):
    """
    Executes the `wallet_sendCalls` RPC (EIP-5792) to batch multiple calls into a single atomic transaction.
    """

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    method: Literal["wallet_sendCalls"]

    params: EthereumSendCallsRpcInputParams
    """Parameters for the `wallet_sendCalls` RPC."""

    address: Optional[str] = None

    chain_type: Optional[Literal["ethereum"]] = None

    experimental_data_suffix: Optional[Hex] = None
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    sponsor: Optional[bool] = None

    sponsor_options: Optional[RpcSponsorOptions] = None
    """Options for user-pays gas sponsorship on the RPC endpoint.

    When provided alongside `sponsor: true`, controls which token asset the user
    pays gas with.
    """

    wallet_id: Optional[str] = None
