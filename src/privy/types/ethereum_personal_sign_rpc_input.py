# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .caip_2 import Caip2
from .._models import BaseModel
from .signature_options import SignatureOptions
from .ethereum_personal_sign_rpc_input_params import EthereumPersonalSignRpcInputParams

__all__ = ["EthereumPersonalSignRpcInput"]


class EthereumPersonalSignRpcInput(BaseModel):
    """Executes the EVM `personal_sign` RPC (EIP-191) to sign a message."""

    method: Literal["personal_sign"]

    params: EthereumPersonalSignRpcInputParams
    """Parameters for the EVM `personal_sign` RPC."""

    address: Optional[str] = None

    caip2: Optional[Caip2] = None
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    chain_type: Optional[Literal["ethereum"]] = None

    signature_options: Optional[SignatureOptions] = None
    """
    Options controlling signature production for personal_sign and
    eth_signTypedData_v4.
    """

    wallet_id: Optional[str] = None
