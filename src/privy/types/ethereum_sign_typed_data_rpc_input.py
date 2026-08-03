# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .caip_2 import Caip2
from .._models import BaseModel
from .signature_options import SignatureOptions
from .ethereum_sign_typed_data_rpc_input_params import EthereumSignTypedDataRpcInputParams

__all__ = ["EthereumSignTypedDataRpcInput"]


class EthereumSignTypedDataRpcInput(BaseModel):
    """
    Executes the EVM `eth_signTypedData_v4` RPC (EIP-712) to sign a typed data object.
    """

    method: Literal["eth_signTypedData_v4"]

    params: EthereumSignTypedDataRpcInputParams
    """Parameters for the EVM `eth_signTypedData_v4` RPC."""

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
