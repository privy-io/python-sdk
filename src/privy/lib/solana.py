"""Solana wallet operations."""

from __future__ import annotations

import base64
from typing import TYPE_CHECKING, Any, cast

from ..types import wallet_rpc_params
from .request_options import PrivyRequestOptions
from ..types.solana_sign_message_rpc_response_data import SolanaSignMessageRpcResponseData

if TYPE_CHECKING:
    from .wallets import WalletsService

__all__ = ["SolanaWalletService"]


class SolanaWalletService:
    """Convenience methods for Solana wallet operations."""

    def __init__(self, wallets: WalletsService) -> None:
        self._wallets = wallets

    def sign_message(
        self,
        wallet_id: str,
        message: str | bytes | bytearray,
        *,
        address: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> SolanaSignMessageRpcResponseData:
        encoded_message = (
            base64.b64encode(bytes(message)).decode("ascii") if isinstance(message, (bytes, bytearray)) else message
        )
        body: wallet_rpc_params.SolanaSignMessageRpcInput = {
            "method": "signMessage",
            "chain_type": "solana",
            "params": {"message": encoded_message, "encoding": "base64"},
        }
        if address is not None:
            body["address"] = address

        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "signMessage":
            raise ValueError(
                f"Unexpected wallet RPC response method: expected 'signMessage', got {response.method!r}"
            )
        response_values: Any = response
        return cast(SolanaSignMessageRpcResponseData, response_values.data)
