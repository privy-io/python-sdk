# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .ethereum_sign_7702_authorization import EthereumSign7702Authorization

__all__ = ["EthereumSign7702AuthorizationRpcResponseData"]


class EthereumSign7702AuthorizationRpcResponseData(BaseModel):
    """Data returned by the EVM `eth_sign7702Authorization` RPC."""

    authorization: EthereumSign7702Authorization
    """
    A signed EIP-7702 authorization that delegates code execution to a contract
    address.
    """
