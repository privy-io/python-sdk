"""Solana wallet operations."""

from __future__ import annotations

import base64
from typing import TYPE_CHECKING, Any, cast

from ..types import wallet_rpc_params
from .request_options import PrivyRequestOptions
from ..types.rpc_sponsor_options_param import RpcSponsorOptionsParam
from ..types.solana_sign_message_rpc_response_data import SolanaSignMessageRpcResponseData
from ..types.solana_sign_transaction_rpc_response_data import SolanaSignTransactionRpcResponseData
from ..types.solana_sign_and_send_transaction_rpc_response_data import SolanaSignAndSendTransactionRpcResponseData

if TYPE_CHECKING:
    from .wallets import PrivyWalletsService

__all__ = ["PrivySolanaService"]


class PrivySolanaService:
    """Convenience methods for Solana wallet operations."""

    def __init__(self, wallets: PrivyWalletsService) -> None:
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

    def sign_transaction(
        self,
        wallet_id: str,
        transaction: str | bytes | bytearray,
        *,
        address: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> SolanaSignTransactionRpcResponseData:
        encoded_transaction = (
            base64.b64encode(bytes(transaction)).decode("ascii")
            if isinstance(transaction, (bytes, bytearray))
            else transaction
        )
        body: wallet_rpc_params.SolanaSignTransactionRpcInput = {
            "method": "signTransaction",
            "chain_type": "solana",
            "params": {"transaction": encoded_transaction, "encoding": "base64"},
        }
        if address is not None:
            body["address"] = address

        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "signTransaction":
            raise ValueError(
                f"Unexpected wallet RPC response method: expected 'signTransaction', got {response.method!r}"
            )
        response_values: Any = response
        return cast(SolanaSignTransactionRpcResponseData, response_values.data)

    def sign_and_send_transaction(
        self,
        wallet_id: str,
        transaction: str | bytes | bytearray,
        *,
        caip2: str,
        address: str | None = None,
        optimistic_broadcast: bool | None = None,
        reference_id: str | None = None,
        sponsor: bool | None = None,
        sponsor_options: RpcSponsorOptionsParam | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> SolanaSignAndSendTransactionRpcResponseData:
        encoded_transaction = (
            base64.b64encode(bytes(transaction)).decode("ascii")
            if isinstance(transaction, (bytes, bytearray))
            else transaction
        )
        body: wallet_rpc_params.SolanaSignAndSendTransactionRpcInput = {
            "method": "signAndSendTransaction",
            "chain_type": "solana",
            "caip2": caip2,
            "params": {"transaction": encoded_transaction, "encoding": "base64"},
        }
        if address is not None:
            body["address"] = address
        if optimistic_broadcast is not None:
            body["optimistic_broadcast"] = optimistic_broadcast
        if reference_id is not None:
            body["reference_id"] = reference_id
        if sponsor is not None:
            body["sponsor"] = sponsor
        if sponsor_options is not None:
            body["sponsor_options"] = sponsor_options

        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "signAndSendTransaction":
            raise ValueError(
                "Unexpected wallet RPC response method: expected "
                f"'signAndSendTransaction', got {response.method!r}"
            )
        response_values: Any = response
        return cast(SolanaSignAndSendTransactionRpcResponseData, response_values.data)
