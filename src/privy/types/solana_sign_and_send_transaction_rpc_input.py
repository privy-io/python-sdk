# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .caip_2 import Caip2
from .._models import BaseModel
from .rpc_sponsor_options import RpcSponsorOptions
from .solana_sign_and_send_transaction_rpc_input_params import SolanaSignAndSendTransactionRpcInputParams

__all__ = ["SolanaSignAndSendTransactionRpcInput"]


class SolanaSignAndSendTransactionRpcInput(BaseModel):
    """
    Executes the SVM `signAndSendTransaction` RPC to sign and broadcast a transaction.
    """

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    method: Literal["signAndSendTransaction"]

    params: SolanaSignAndSendTransactionRpcInputParams
    """Parameters for the SVM `signAndSendTransaction` RPC."""

    address: Optional[str] = None

    chain_type: Optional[Literal["solana"]] = None

    optimistic_broadcast: Optional[bool] = None

    reference_id: Optional[str] = None
    """Developer-provided identifier for this request. Must be unique per app."""

    sponsor: Optional[bool] = None

    sponsor_options: Optional[RpcSponsorOptions] = None
    """Options for user-pays gas sponsorship on the RPC endpoint.

    When provided alongside `sponsor: true`, controls which token asset the user
    pays gas with.
    """

    wallet_id: Optional[str] = None
