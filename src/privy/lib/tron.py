"""Tron wallet operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from ..types import wallet_rpc_params
from .request_options import PrivyRequestOptions
from ..types.tron_send_transaction_rpc_response_data import TronSendTransactionRpcResponseData
from ..types.tron_sign_transaction_rpc_response_data import TronSignTransactionRpcResponseData
from ..types.tron_send_transaction_rpc_input_params_param import TronSendTransactionRpcInputParamsParam
from ..types.tron_sign_transaction_rpc_input_params_param import TronSignTransactionRpcInputParamsParam

if TYPE_CHECKING:
    from .wallets import WalletsService

__all__ = ["TronWalletService"]


class TronWalletService:
    """Convenience methods for Tron wallet operations."""

    def __init__(self, wallets: WalletsService) -> None:
        self._wallets = wallets

    def sign_transaction(
        self,
        wallet_id: str,
        *,
        params: TronSignTransactionRpcInputParamsParam,
        request_options: PrivyRequestOptions | None = None,
    ) -> TronSignTransactionRpcResponseData:
        """Sign a Tron transaction without broadcasting it."""
        body: wallet_rpc_params.TronSignTransactionRpcInput = {
            "method": "tron_signTransaction",
            "params": params,
        }
        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "tron_signTransaction":
            raise ValueError(
                f"Unexpected wallet RPC response method: expected 'tron_signTransaction', got {response.method!r}"
            )
        response_values: Any = response
        return cast(TronSignTransactionRpcResponseData, response_values.data)

    def send_transaction(
        self,
        wallet_id: str,
        *,
        params: TronSendTransactionRpcInputParamsParam,
        caip2: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> TronSendTransactionRpcResponseData:
        """Sign and broadcast a Tron transaction."""
        body: wallet_rpc_params.TronSendTransactionRpcInput = {
            "method": "tron_sendTransaction",
            "params": params,
        }
        if caip2 is not None:
            body["caip2"] = caip2

        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "tron_sendTransaction":
            raise ValueError(
                f"Unexpected wallet RPC response method: expected 'tron_sendTransaction', got {response.method!r}"
            )
        response_values: Any = response
        return cast(TronSendTransactionRpcResponseData, response_values.data)
