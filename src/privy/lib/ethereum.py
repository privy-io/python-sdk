"""Ethereum wallet operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from ..types import wallet_rpc_params
from .request_options import PrivyRequestOptions
from ..types.signature_options_param import SignatureOptionsParam
from ..types.ethereum_personal_sign_rpc_response_data import EthereumPersonalSignRpcResponseData
from ..types.ethereum_personal_sign_rpc_input_params_param import EthereumPersonalSignRpcInputParamsParam

if TYPE_CHECKING:
    from .wallets import WalletsService

__all__ = ["EthereumWalletService"]


class EthereumWalletService:
    """Convenience methods for Ethereum wallet operations."""

    def __init__(self, wallets: WalletsService) -> None:
        self._wallets = wallets

    def sign_message(
        self,
        wallet_id: str,
        message: str | bytes | bytearray,
        *,
        address: str | None = None,
        caip2: str | None = None,
        signature_options: SignatureOptionsParam | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> EthereumPersonalSignRpcResponseData:
        params: EthereumPersonalSignRpcInputParamsParam
        if isinstance(message, (bytes, bytearray)):
            params = {"message": bytes(message).hex(), "encoding": "hex"}
        elif message.startswith("0x"):
            params = {"message": message[2:], "encoding": "hex"}
        else:
            params = {"message": message, "encoding": "utf-8"}

        body: wallet_rpc_params.EthereumPersonalSignRpcInput = {
            "method": "personal_sign",
            "chain_type": "ethereum",
            "params": params,
        }
        if address is not None:
            body["address"] = address
        if caip2 is not None:
            body["caip2"] = caip2
        if signature_options is not None:
            body["signature_options"] = signature_options

        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "personal_sign":
            raise ValueError(
                f"Unexpected wallet RPC response method: expected 'personal_sign', got {response.method!r}"
            )
        response_values: Any = response
        return cast(EthereumPersonalSignRpcResponseData, response_values.data)
