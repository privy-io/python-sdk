"""Ethereum wallet operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from ..types import wallet_rpc_params
from .request_options import PrivyRequestOptions
from ..types.signature_options_param import SignatureOptionsParam
from ..types.ethereum_personal_sign_rpc_response_data import EthereumPersonalSignRpcResponseData
from ..types.ethereum_sign_typed_data_rpc_response_data import EthereumSignTypedDataRpcResponseData
from ..types.ethereum_secp_256k_1_sign_rpc_response_data import EthereumSecp256k1SignRpcResponseData
from ..types.ethereum_sign_transaction_rpc_response_data import EthereumSignTransactionRpcResponseData
from ..types.ethereum_personal_sign_rpc_input_params_param import EthereumPersonalSignRpcInputParamsParam
from ..types.ethereum_sign_user_operation_rpc_response_data import EthereumSignUserOperationRpcResponseData
from ..types.ethereum_sign_typed_data_rpc_input_params_param import EthereumSignTypedDataRpcInputParamsParam
from ..types.ethereum_secp_256k_1_sign_rpc_input_params_param import EthereumSecp256k1SignRpcInputParamsParam
from ..types.ethereum_sign_transaction_rpc_input_params_param import EthereumSignTransactionRpcInputParamsParam
from ..types.ethereum_sign_7702_authorization_rpc_response_data import (
    EthereumSign7702AuthorizationRpcResponseData,
)
from ..types.ethereum_sign_user_operation_rpc_input_params_param import EthereumSignUserOperationRpcInputParamsParam
from ..types.ethereum_sign_7702_authorization_rpc_input_params_param import (
    EthereumSign7702AuthorizationRpcInputParamsParam,
)

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

    def sign_secp256k1(
        self,
        wallet_id: str,
        *,
        params: EthereumSecp256k1SignRpcInputParamsParam,
        address: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> EthereumSecp256k1SignRpcResponseData:
        body: wallet_rpc_params.EthereumSecp256k1SignRpcInput = {
            "method": "secp256k1_sign",
            "chain_type": "ethereum",
            "params": params,
        }
        if address is not None:
            body["address"] = address

        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "secp256k1_sign":
            raise ValueError(
                f"Unexpected wallet RPC response method: expected 'secp256k1_sign', got {response.method!r}"
            )
        response_values: Any = response
        return cast(EthereumSecp256k1SignRpcResponseData, response_values.data)

    def sign_7702_authorization(
        self,
        wallet_id: str,
        *,
        params: EthereumSign7702AuthorizationRpcInputParamsParam,
        address: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> EthereumSign7702AuthorizationRpcResponseData:
        body: wallet_rpc_params.EthereumSign7702AuthorizationRpcInput = {
            "method": "eth_sign7702Authorization",
            "chain_type": "ethereum",
            "params": params,
        }
        if address is not None:
            body["address"] = address

        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "eth_sign7702Authorization":
            raise ValueError(
                "Unexpected wallet RPC response method: "
                f"expected 'eth_sign7702Authorization', got {response.method!r}"
            )
        response_values: Any = response
        return cast(EthereumSign7702AuthorizationRpcResponseData, response_values.data)

    def sign_transaction(
        self,
        wallet_id: str,
        *,
        params: EthereumSignTransactionRpcInputParamsParam,
        address: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> EthereumSignTransactionRpcResponseData:
        body: wallet_rpc_params.EthereumSignTransactionRpcInput = {
            "method": "eth_signTransaction",
            "chain_type": "ethereum",
            "params": params,
        }
        if address is not None:
            body["address"] = address

        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "eth_signTransaction":
            raise ValueError(
                f"Unexpected wallet RPC response method: expected 'eth_signTransaction', got {response.method!r}"
            )
        response_values: Any = response
        return cast(EthereumSignTransactionRpcResponseData, response_values.data)

    def sign_typed_data(
        self,
        wallet_id: str,
        *,
        params: EthereumSignTypedDataRpcInputParamsParam,
        address: str | None = None,
        caip2: str | None = None,
        signature_options: SignatureOptionsParam | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> EthereumSignTypedDataRpcResponseData:
        body: wallet_rpc_params.EthereumSignTypedDataRpcInput = {
            "method": "eth_signTypedData_v4",
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
        if response.method != "eth_signTypedData_v4":
            raise ValueError(
                f"Unexpected wallet RPC response method: expected 'eth_signTypedData_v4', got {response.method!r}"
            )
        response_values: Any = response
        return cast(EthereumSignTypedDataRpcResponseData, response_values.data)

    def sign_user_operation(
        self,
        wallet_id: str,
        *,
        params: EthereumSignUserOperationRpcInputParamsParam,
        address: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> EthereumSignUserOperationRpcResponseData:
        body: wallet_rpc_params.EthereumSignUserOperationRpcInput = {
            "method": "eth_signUserOperation",
            "chain_type": "ethereum",
            "params": params,
        }
        if address is not None:
            body["address"] = address

        response = self._wallets.rpc(
            wallet_id,
            wallet_rpc_request_body=body,
            request_options=request_options,
        )
        if response.method != "eth_signUserOperation":
            raise ValueError(
                f"Unexpected wallet RPC response method: expected 'eth_signUserOperation', got {response.method!r}"
            )
        response_values: Any = response
        return cast(EthereumSignUserOperationRpcResponseData, response_values.data)
