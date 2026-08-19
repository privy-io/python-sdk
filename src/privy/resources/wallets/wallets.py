# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Any, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from .swap import (
    SwapResource,
    AsyncSwapResource,
    SwapResourceWithRawResponse,
    AsyncSwapResourceWithRawResponse,
    SwapResourceWithStreamingResponse,
    AsyncSwapResourceWithStreamingResponse,
)
from ...types import (
    Hex,
    Caip2,
    Address,
    EntityID,
    AmountType,
    OwnerIDInput,
    SparkNetwork,
    HpkeEncryption,
    WalletChainType,
    WalletEntityType,
    WalletActionNonce,
    RawSignInputParams,
    WalletImportSupportedChains,
    wallet_get_params,
    wallet_rpc_params,
    wallet_list_params,
    wallet_create_params,
    wallet_export_params,
    wallet_update_params,
    wallet_raw_sign_params,
    wallet_transfer_params,
    wallet_init_import_params,
    wallet_create_batch_params,
    wallet_assign_entity_params,
    wallet_submit_import_params,
    wallet_authenticate_with_jwt_params,
    wallet_get_wallet_by_address_params,
    wallet_create_wallets_with_recovery_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from .balance import (
    BalanceResource,
    AsyncBalanceResource,
    BalanceResourceWithRawResponse,
    AsyncBalanceResourceWithRawResponse,
    BalanceResourceWithStreamingResponse,
    AsyncBalanceResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from .earn.earn import (
    EarnResource,
    AsyncEarnResource,
    EarnResourceWithRawResponse,
    AsyncEarnResourceWithRawResponse,
    EarnResourceWithStreamingResponse,
    AsyncEarnResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.hex import Hex
from ...pagination import SyncCursor, AsyncCursor
from .transactions import (
    TransactionsResource,
    AsyncTransactionsResource,
    TransactionsResourceWithRawResponse,
    AsyncTransactionsResourceWithRawResponse,
    TransactionsResourceWithStreamingResponse,
    AsyncTransactionsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.caip_2 import Caip2
from ...types.wallet import Wallet
from ...types.address import Address
from ...types.entity_id import EntityID
from ...types.amount_type import AmountType
from ...types.spark_network import SparkNetwork
from ...types.owner_id_input import OwnerIDInput
from ...types.hpke_encryption import HpkeEncryption
from ...types.owner_input_param import OwnerInputParam
from ...types.raw_sign_response import RawSignResponse
from ...types.wallet_chain_type import WalletChainType
from ...types.policy_input_param import PolicyInputParam
from ...types.wallet_entity_type import WalletEntityType
from ...types.wallet_action_nonce import WalletActionNonce
from ...types.wallet_rpc_response import WalletRpcResponse
from ...types.raw_sign_input_params import RawSignInputParams
from ...types.fee_configuration_param import FeeConfigurationParam
from ...types.signature_options_param import SignatureOptionsParam
from ...types.rpc_sponsor_options_param import RpcSponsorOptionsParam
from ...types.token_transfer_source_param import TokenTransferSourceParam
from ...types.wallet_export_response_body import WalletExportResponseBody
from ...types.wallet_init_import_response import WalletInitImportResponse
from ...types.wallet_batch_create_response import WalletBatchCreateResponse
from ...types.additional_signer_input_param import AdditionalSignerInputParam
from ...types.wallet_batch_item_input_param import WalletBatchItemInputParam
from ...types.private_key_export_input_param import PrivateKeyExportInputParam
from ...types.seed_phrase_export_input_param import SeedPhraseExportInputParam
from ...types.wallet_import_supported_chains import WalletImportSupportedChains
from ...types.token_transfer_destination_param import TokenTransferDestinationParam
from ...types.wallets.transfer_action_response import TransferActionResponse
from ...types.wallet_entity_assignment_response import WalletEntityAssignmentResponse
from ...types.spark_transfer_rpc_input_params_param import SparkTransferRpcInputParamsParam
from ...types.spark_withdraw_rpc_input_params_param import SparkWithdrawRpcInputParamsParam
from ...types.wallet_authenticate_with_jwt_response import WalletAuthenticateWithJwtResponse
from ...types.ethereum_send_calls_rpc_input_params_param import EthereumSendCallsRpcInputParamsParam
from ...types.solana_sign_message_rpc_input_params_param import SolanaSignMessageRpcInputParamsParam
from ...types.wallet_entity_assignment_request_body_param import WalletEntityAssignmentRequestBodyParam
from ...types.spark_transfer_tokens_rpc_input_params_param import SparkTransferTokensRpcInputParamsParam
from ...types.tron_send_transaction_rpc_input_params_param import TronSendTransactionRpcInputParamsParam
from ...types.tron_sign_transaction_rpc_input_params_param import TronSignTransactionRpcInputParamsParam
from ...types.wallet_create_wallets_with_recovery_response import WalletCreateWalletsWithRecoveryResponse
from ...types.xrpl_sign_transaction_rpc_input_params_param import XrplSignTransactionRpcInputParamsParam
from ...types.ethereum_personal_sign_rpc_input_params_param import EthereumPersonalSignRpcInputParamsParam
from ...types.solana_sign_transaction_rpc_input_params_param import SolanaSignTransactionRpcInputParamsParam
from ...types.ethereum_sign_typed_data_rpc_input_params_param import EthereumSignTypedDataRpcInputParamsParam
from ...types.ethereum_secp_256k_1_sign_rpc_input_params_param import EthereumSecp256k1SignRpcInputParamsParam
from ...types.ethereum_send_transaction_rpc_input_params_param import EthereumSendTransactionRpcInputParamsParam
from ...types.ethereum_sign_transaction_rpc_input_params_param import EthereumSignTransactionRpcInputParamsParam
from ...types.spark_claim_static_deposit_rpc_input_params_param import SparkClaimStaticDepositRpcInputParamsParam
from ...types.spark_pay_lightning_invoice_rpc_input_params_param import SparkPayLightningInvoiceRpcInputParamsParam
from ...types.ethereum_sign_user_operation_rpc_input_params_param import EthereumSignUserOperationRpcInputParamsParam
from ...types.spark_create_lightning_invoice_rpc_input_params_param import (
    SparkCreateLightningInvoiceRpcInputParamsParam,
)
from ...types.spark_get_withdrawal_fee_quote_rpc_input_params_param import SparkGetWithdrawalFeeQuoteRpcInputParamsParam
from ...types.ethereum_sign_7702_authorization_rpc_input_params_param import (
    EthereumSign7702AuthorizationRpcInputParamsParam,
)
from ...types.solana_sign_and_send_transaction_rpc_input_params_param import (
    SolanaSignAndSendTransactionRpcInputParamsParam,
)
from ...types.spark_get_claim_static_deposit_quote_rpc_input_params_param import (
    SparkGetClaimStaticDepositQuoteRpcInputParamsParam,
)
from ...types.spark_sign_message_with_identity_key_rpc_input_params_param import (
    SparkSignMessageWithIdentityKeyRpcInputParamsParam,
)

__all__ = ["WalletsResource", "AsyncWalletsResource"]


class WalletsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        """Operations related to wallet actions"""
        return ActionsResource(self._client)

    @cached_property
    def earn(self) -> EarnResource:
        return EarnResource(self._client)

    @cached_property
    def transactions(self) -> TransactionsResource:
        """Operations related to wallets"""
        return TransactionsResource(self._client)

    @cached_property
    def balance(self) -> BalanceResource:
        """Operations related to wallets"""
        return BalanceResource(self._client)

    @cached_property
    def swap(self) -> SwapResource:
        """Operations for swapping tokens within wallets"""
        return SwapResource(self._client)

    @cached_property
    def with_raw_response(self) -> WalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return WalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return WalletsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        chain_type: WalletChainType,
        additional_signers: AdditionalSignerInputParam | Omit = omit,
        display_name: str | Omit = omit,
        entity: WalletEntityAssignmentRequestBodyParam | Omit = omit,
        external_id: str | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        policy_ids: PolicyInputParam | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Creates a new wallet on the requested chain and for the requested owner.

        Args:
          chain_type: The wallet chain types.

          additional_signers: Additional signers for the wallet.

          display_name: A human-readable label for the wallet.

          entity: Request body for assigning an entity to a wallet.

          external_id: A customer-provided identifier for mapping to external systems. URL-safe
              characters only ([a-zA-Z0-9_-]), max 64 chars. Write-once: cannot be changed
              after creation.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          policy_ids: An optional list of up to one policy ID to enforce on the wallet.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"privy-idempotency-key": privy_idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/v1/wallets",
            body=maybe_transform(
                {
                    "chain_type": chain_type,
                    "additional_signers": additional_signers,
                    "display_name": display_name,
                    "entity": entity,
                    "external_id": external_id,
                    "owner": owner,
                    "owner_id": owner_id,
                    "policy_ids": policy_ids,
                },
                wallet_create_params.WalletCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    def list(
        self,
        *,
        address: Address | Omit = omit,
        authorization_key: str | Omit = omit,
        chain_type: WalletChainType | Omit = omit,
        cursor: str | Omit = omit,
        entity_id: str | Omit = omit,
        external_id: str | Omit = omit,
        include_archived: bool | Omit = omit,
        limit: Optional[float] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[Wallet]:
        """Get all wallets in your app.

        Args:
          address: A blockchain wallet address.

        Ethereum addresses are normalized to EIP-55
              checksum format. Solana addresses are validated as base58. All other chain
              addresses (Stellar, Tron, Sui, Aptos, etc.) are accepted as-is.

          authorization_key: Filter wallets by authorization public key. Returns wallets owned by key quorums
              that include the specified P-256 public key (base64-encoded DER format). Cannot
              be used together with user_id.

          chain_type: The wallet chain types.

          entity_id: Filter wallets by the entity ID the wallet is attributed to.

          external_id: Filter wallets by external ID.

          include_archived: Include archived wallets in lookup. Defaults to false.

          user_id: Filter wallets by user ID. Cannot be used together with authorization_key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/wallets",
            page=SyncCursor[Wallet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "address": address,
                        "authorization_key": authorization_key,
                        "chain_type": chain_type,
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "external_id": external_id,
                        "include_archived": include_archived,
                        "limit": limit,
                        "user_id": user_id,
                    },
                    wallet_list_params.WalletListParams,
                ),
            ),
            model=Wallet,
        )

    def _export(
        self,
        wallet_id: str,
        *,
        encryption_type: HpkeEncryption,
        recipient_public_key: str,
        export_seed_phrase: bool | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletExportResponseBody:
        """
        Export a wallet's private key

        Args:
          wallet_id: ID of the wallet.

          encryption_type: The encryption type of the wallet to import. Currently only supports `HPKE`.

          recipient_public_key: The base64-encoded encryption public key to encrypt the wallet private key with.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v1/wallets/{wallet_id}/export", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "encryption_type": encryption_type,
                    "recipient_public_key": recipient_public_key,
                    "export_seed_phrase": export_seed_phrase,
                },
                wallet_export_params.WalletExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletExportResponseBody,
        )

    @overload
    def _init_import(
        self,
        *,
        address: str,
        chain_type: WalletImportSupportedChains,
        encryption_type: HpkeEncryption,
        entropy_type: Literal["hd"],
        index: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletInitImportResponse:
        """Initialize a wallet import.

        Complete by submitting the import.

        Args:
          address: The address of the wallet to import.

          chain_type: The chain type of the wallet to import. Supports `ethereum`, `solana`,
              `stellar`, `tron`, `sui`, `aptos`, and `xrpl`.

          encryption_type: The encryption type of the wallet to import. Currently only supports `HPKE`.

          entropy_type: The entropy type of the wallet to import.

          index: The index of the wallet to import.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _init_import(
        self,
        *,
        address: str,
        chain_type: WalletImportSupportedChains,
        encryption_type: HpkeEncryption,
        entropy_type: Literal["private-key"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletInitImportResponse:
        """Initialize a wallet import.

        Complete by submitting the import.

        Args:
          address: The address of the wallet to import.

          chain_type: The chain type of the wallet to import. Supports `ethereum`, `solana`,
              `stellar`, `tron`, `sui`, `aptos`, and `xrpl`.

          encryption_type: The encryption type of the wallet to import. Currently only supports `HPKE`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["address", "chain_type", "encryption_type", "entropy_type", "index"],
        ["address", "chain_type", "encryption_type", "entropy_type"],
    )
    def _init_import(
        self,
        *,
        address: str,
        chain_type: WalletImportSupportedChains,
        encryption_type: HpkeEncryption,
        entropy_type: Literal["hd"] | Literal["private-key"],
        index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletInitImportResponse:
        return self._post(
            "/v1/wallets/import/init",
            body=maybe_transform(
                {
                    "address": address,
                    "chain_type": chain_type,
                    "encryption_type": encryption_type,
                    "entropy_type": entropy_type,
                    "index": index,
                },
                wallet_init_import_params.WalletInitImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletInitImportResponse,
        )

    def _raw_sign(
        self,
        wallet_id: str,
        *,
        params: RawSignInputParams,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RawSignResponse:
        """
        Sign a message with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          params: Parameters for the `raw_sign` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v1/wallets/{wallet_id}/raw_sign", wallet_id=wallet_id),
            body=maybe_transform({"params": params}, wallet_raw_sign_params.WalletRawSignParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RawSignResponse,
        )

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signTransaction"],
        params: EthereumSignTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signTransaction` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        caip2: Caip2,
        method: Literal["eth_sendTransaction"],
        params: EthereumSendTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        experimental_data_suffix: Hex | Omit = omit,
        reference_id: str | Omit = omit,
        sponsor: bool | Omit = omit,
        sponsor_options: RpcSponsorOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the EVM `eth_sendTransaction` RPC.

          experimental_data_suffix: A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
              bytes).

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["personal_sign"],
        params: EthereumPersonalSignRpcInputParamsParam,
        address: str | Omit = omit,
        caip2: Caip2 | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        signature_options: SignatureOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `personal_sign` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          signature_options: Options controlling signature production for personal_sign and
              eth_signTypedData_v4.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signTypedData_v4"],
        params: EthereumSignTypedDataRpcInputParamsParam,
        address: str | Omit = omit,
        caip2: Caip2 | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        signature_options: SignatureOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signTypedData_v4` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          signature_options: Options controlling signature production for personal_sign and
              eth_signTypedData_v4.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["secp256k1_sign"],
        params: EthereumSecp256k1SignRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `secp256k1_sign` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_sign7702Authorization"],
        params: EthereumSign7702AuthorizationRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_sign7702Authorization` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signUserOperation"],
        params: EthereumSignUserOperationRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signUserOperation` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        caip2: Caip2,
        method: Literal["wallet_sendCalls"],
        params: EthereumSendCallsRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        experimental_data_suffix: Hex | Omit = omit,
        sponsor: bool | Omit = omit,
        sponsor_options: RpcSponsorOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the `wallet_sendCalls` RPC.

          experimental_data_suffix: A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
              bytes).

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signTransaction"],
        params: SolanaSignTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the SVM `signTransaction` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        caip2: Caip2,
        method: Literal["signAndSendTransaction"],
        params: SolanaSignAndSendTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        optimistic_broadcast: bool | Omit = omit,
        reference_id: str | Omit = omit,
        sponsor: bool | Omit = omit,
        sponsor_options: RpcSponsorOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the SVM `signAndSendTransaction` RPC.

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signMessage"],
        params: SolanaSignMessageRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the SVM `signMessage` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["transfer"],
        params: SparkTransferRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `transfer` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getBalance"],
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["transferTokens"],
        params: SparkTransferTokensRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `transferTokens` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getStaticDepositAddress"],
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getClaimStaticDepositQuote"],
        params: SparkGetClaimStaticDepositQuoteRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `getClaimStaticDepositQuote` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["claimStaticDeposit"],
        params: SparkClaimStaticDepositRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `claimStaticDeposit` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["createLightningInvoice"],
        params: SparkCreateLightningInvoiceRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `createLightningInvoice` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["payLightningInvoice"],
        params: SparkPayLightningInvoiceRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `payLightningInvoice` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signMessageWithIdentityKey"],
        params: SparkSignMessageWithIdentityKeyRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `signMessageWithIdentityKey` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["withdraw"],
        params: SparkWithdrawRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `withdraw` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getWithdrawalFeeQuote"],
        params: SparkGetWithdrawalFeeQuoteRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `getWithdrawalFeeQuote` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["tron_signTransaction"],
        params: TronSignTransactionRpcInputParamsParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Tron `tron_signTransaction` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["tron_sendTransaction"],
        params: TronSendTransactionRpcInputParamsParam,
        caip2: Caip2 | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Tron `tron_sendTransaction` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["xrpl_signTransaction"],
        params: XrplSignTransactionRpcInputParamsParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the XRPL `xrpl_signTransaction` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        address: str,
        method: Literal["exportPrivateKey"],
        params: PrivateKeyExportInputParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Input for exporting a wallet (private key or seed phrase) with HPKE encryption.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        address: str,
        method: Literal["exportSeedPhrase"],
        params: SeedPhraseExportInputParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Input for exporting a wallet (private key or seed phrase) with HPKE encryption.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["method", "params"], ["caip2", "method", "params"], ["method"], ["address", "method", "params"])
    def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signTransaction"]
        | Literal["eth_sendTransaction"]
        | Literal["personal_sign"]
        | Literal["eth_signTypedData_v4"]
        | Literal["secp256k1_sign"]
        | Literal["eth_sign7702Authorization"]
        | Literal["eth_signUserOperation"]
        | Literal["wallet_sendCalls"]
        | Literal["signTransaction"]
        | Literal["signAndSendTransaction"]
        | Literal["signMessage"]
        | Literal["transfer"]
        | Literal["getBalance"]
        | Literal["transferTokens"]
        | Literal["getStaticDepositAddress"]
        | Literal["getClaimStaticDepositQuote"]
        | Literal["claimStaticDeposit"]
        | Literal["createLightningInvoice"]
        | Literal["payLightningInvoice"]
        | Literal["signMessageWithIdentityKey"]
        | Literal["withdraw"]
        | Literal["getWithdrawalFeeQuote"]
        | Literal["tron_signTransaction"]
        | Literal["tron_sendTransaction"]
        | Literal["xrpl_signTransaction"]
        | Literal["exportPrivateKey"]
        | Literal["exportSeedPhrase"],
        params: EthereumSignTransactionRpcInputParamsParam
        | EthereumSendTransactionRpcInputParamsParam
        | EthereumPersonalSignRpcInputParamsParam
        | EthereumSignTypedDataRpcInputParamsParam
        | EthereumSecp256k1SignRpcInputParamsParam
        | EthereumSign7702AuthorizationRpcInputParamsParam
        | EthereumSignUserOperationRpcInputParamsParam
        | EthereumSendCallsRpcInputParamsParam
        | SolanaSignTransactionRpcInputParamsParam
        | SolanaSignAndSendTransactionRpcInputParamsParam
        | SolanaSignMessageRpcInputParamsParam
        | SparkTransferRpcInputParamsParam
        | SparkTransferTokensRpcInputParamsParam
        | SparkGetClaimStaticDepositQuoteRpcInputParamsParam
        | SparkClaimStaticDepositRpcInputParamsParam
        | SparkCreateLightningInvoiceRpcInputParamsParam
        | SparkPayLightningInvoiceRpcInputParamsParam
        | SparkSignMessageWithIdentityKeyRpcInputParamsParam
        | SparkWithdrawRpcInputParamsParam
        | SparkGetWithdrawalFeeQuoteRpcInputParamsParam
        | TronSignTransactionRpcInputParamsParam
        | TronSendTransactionRpcInputParamsParam
        | XrplSignTransactionRpcInputParamsParam
        | PrivateKeyExportInputParam
        | SeedPhraseExportInputParam
        | Omit = omit,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        caip2: Caip2 | Omit = omit,
        experimental_data_suffix: Hex | Omit = omit,
        reference_id: str | Omit = omit,
        sponsor: bool | Omit = omit,
        sponsor_options: RpcSponsorOptionsParam | Omit = omit,
        signature_options: SignatureOptionsParam | Omit = omit,
        optimistic_broadcast: bool | Omit = omit,
        network: SparkNetwork | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        if not path_wallet_id:
            raise ValueError(f"Expected a non-empty value for `path_wallet_id` but received {path_wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            WalletRpcResponse,
            self._post(
                path_template("/v1/wallets/{path_wallet_id}/rpc", path_wallet_id=path_wallet_id),
                body=maybe_transform(
                    {
                        "method": method,
                        "params": params,
                        "address": address,
                        "chain_type": chain_type,
                        "body_wallet_id": body_wallet_id,
                        "caip2": caip2,
                        "experimental_data_suffix": experimental_data_suffix,
                        "reference_id": reference_id,
                        "sponsor": sponsor,
                        "sponsor_options": sponsor_options,
                        "signature_options": signature_options,
                        "optimistic_broadcast": optimistic_broadcast,
                        "network": network,
                    },
                    wallet_rpc_params.WalletRpcParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, WalletRpcResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def _submit_import(
        self,
        *,
        wallet: wallet_submit_import_params.Wallet,
        additional_signers: AdditionalSignerInputParam | Omit = omit,
        display_name: str | Omit = omit,
        external_id: str | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        policy_ids: PolicyInputParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Submit a wallet import request.

        Args:
          wallet: The submission input for importing an HD wallet.

          additional_signers: Additional signers for the wallet.

          display_name: A human-readable label for the wallet.

          external_id: A customer-provided identifier for mapping to external systems. URL-safe
              characters only ([a-zA-Z0-9_-]), max 64 chars. Write-once: cannot be changed
              after creation.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          policy_ids: An optional list of up to one policy ID to enforce on the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/wallets/import/submit",
            body=maybe_transform(
                {
                    "wallet": wallet,
                    "additional_signers": additional_signers,
                    "display_name": display_name,
                    "external_id": external_id,
                    "owner": owner,
                    "owner_id": owner_id,
                    "policy_ids": policy_ids,
                },
                wallet_submit_import_params.WalletSubmitImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    def _transfer(
        self,
        wallet_id: str,
        *,
        destination: TokenTransferDestinationParam,
        source: TokenTransferSourceParam,
        amount: str | Omit = omit,
        amount_type: AmountType | Omit = omit,
        fee_configuration: FeeConfigurationParam | Omit = omit,
        nonce: WalletActionNonce | Omit = omit,
        slippage_bps: int | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferActionResponse:
        """
        Transfer tokens from a wallet to a destination address.

        Args:
          wallet_id: ID of the wallet.

          destination: The destination address for a token transfer. Optionally specify a different
              asset or chain for cross-asset or cross-chain transfers.

          source: The source asset, amount, and chain for a token transfer. Specify either `asset`
              (named) or `asset_address` (custom), not both.

          amount: Amount as a decimal string in the token's standard unit (e.g. "1.5" for 1.5
              USDC). For exact_input, the amount to send. For exact_output, the exact amount
              to receive. Takes precedence over source.amount when both are provided.

          amount_type: Whether the amount refers to the input token or output token.

          fee_configuration: Total fees assessed on a transfer, in BPS

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          slippage_bps: Maximum allowed slippage in basis points (1 bps = 0.01%). Only applicable for
              cross-chain or cross-asset transfers; omit to use the provider default.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v1/wallets/{wallet_id}/transfer", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                    "amount": amount,
                    "amount_type": amount_type,
                    "fee_configuration": fee_configuration,
                    "nonce": nonce,
                    "slippage_bps": slippage_bps,
                },
                wallet_transfer_params.WalletTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferActionResponse,
        )

    def _update(
        self,
        wallet_id: str,
        *,
        additional_signers: AdditionalSignerInputParam | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Update a wallet's policies or authorization key configuration.

        Args:
          wallet_id: ID of the wallet.

          additional_signers: Additional signers for the wallet.

          display_name: A human-readable label for the wallet. Set to null to clear.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          policy_ids: New policy IDs to enforce on the wallet. Currently, only one policy is supported
              per wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/v1/wallets/{wallet_id}", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "additional_signers": additional_signers,
                    "display_name": display_name,
                    "owner": owner,
                    "owner_id": owner_id,
                    "policy_ids": policy_ids,
                },
                wallet_update_params.WalletUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    def archive(
        self,
        wallet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Archives a wallet, preventing it from being used in any write or signing
        operations. Archived wallets are hidden from list endpoints by default. Returns
        404 if the wallet does not exist or is already archived.

        Args:
          wallet_id: ID of the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._post(
            path_template("/v1/wallets/{wallet_id}/archive", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    def assign_entity(
        self,
        wallet_id: str,
        *,
        id: EntityID,
        type: WalletEntityType,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletEntityAssignmentResponse:
        """
        Assign a user or organization to a wallet.

        Args:
          wallet_id: ID of the wallet.

          id: A Privy entity ID.

          type: The type of entity a wallet is attributed to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._post(
            path_template("/v1/wallets/{wallet_id}/entity", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "id": id,
                    "type": type,
                },
                wallet_assign_entity_params.WalletAssignEntityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletEntityAssignmentResponse,
        )

    def authenticate_with_jwt(
        self,
        *,
        encryption_type: Literal["HPKE"],
        recipient_public_key: str,
        user_jwt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAuthenticateWithJwtResponse:
        """
        Exchange a user JWT for a session key authorized to act on the user's wallets.
        Returns the encrypted authorization key and the list of wallets it can access.

        Args:
          encryption_type: The encryption type for the authentication response. Currently only supports
              HPKE.

          recipient_public_key: The public key of your ECDH keypair, in base64-encoded, SPKI-format, whose
              private key will be able to decrypt the session key.

          user_jwt: The user's JWT, to be used to authenticate the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            WalletAuthenticateWithJwtResponse,
            self._post(
                "/v1/wallets/authenticate",
                body=maybe_transform(
                    {
                        "encryption_type": encryption_type,
                        "recipient_public_key": recipient_public_key,
                        "user_jwt": user_jwt,
                    },
                    wallet_authenticate_with_jwt_params.WalletAuthenticateWithJwtParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, WalletAuthenticateWithJwtResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def create_batch(
        self,
        *,
        wallets: Iterable[WalletBatchItemInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletBatchCreateResponse:
        """Creates multiple wallets in a single request.

        Each wallet creation is
        independent; failures for one wallet do not affect others. Maximum batch size is
        100 wallets.

        Args:
          wallets: Array of wallet creation requests. Minimum 1, maximum 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/wallets/batch",
            body=maybe_transform({"wallets": wallets}, wallet_create_batch_params.WalletCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletBatchCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def create_wallets_with_recovery(
        self,
        *,
        primary_signer: wallet_create_wallets_with_recovery_params.PrimarySigner,
        recovery_user: wallet_create_wallets_with_recovery_params.RecoveryUser,
        wallets: Iterable[wallet_create_wallets_with_recovery_params.Wallet],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletCreateWalletsWithRecoveryResponse:
        """
        Create one or more wallets associated with a recovery user, so the user can
        later regain wallet access via the linked accounts. Deprecated; prefer the
        standard wallet creation flow combined with a separate recovery setup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/wallets_with_recovery",
            body=maybe_transform(
                {
                    "primary_signer": primary_signer,
                    "recovery_user": recovery_user,
                    "wallets": wallets,
                },
                wallet_create_wallets_with_recovery_params.WalletCreateWalletsWithRecoveryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletCreateWalletsWithRecoveryResponse,
        )

    def get(
        self,
        wallet_id: str,
        *,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Get a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          include_archived: Include archived wallets in lookup. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            path_template("/v1/wallets/{wallet_id}", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_archived": include_archived}, wallet_get_params.WalletGetParams),
            ),
            cast_to=Wallet,
        )

    def get_wallet_by_address(
        self,
        *,
        address: Address,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """Look up a wallet by its blockchain address.

        Returns the wallet object if found.

        Args:
          address: A blockchain wallet address. Ethereum addresses are normalized to EIP-55
              checksum format. Solana addresses are validated as base58. All other chain
              addresses (Stellar, Tron, Sui, Aptos, etc.) are accepted as-is.

          include_archived: Include archived wallets in lookup. Defaults to false (archived wallets return
              404).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/wallets/address",
            body=maybe_transform(
                {
                    "address": address,
                    "include_archived": include_archived,
                },
                wallet_get_wallet_by_address_params.WalletGetWalletByAddressParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )


class AsyncWalletsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        """Operations related to wallet actions"""
        return AsyncActionsResource(self._client)

    @cached_property
    def earn(self) -> AsyncEarnResource:
        return AsyncEarnResource(self._client)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        """Operations related to wallets"""
        return AsyncTransactionsResource(self._client)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        """Operations related to wallets"""
        return AsyncBalanceResource(self._client)

    @cached_property
    def swap(self) -> AsyncSwapResource:
        """Operations for swapping tokens within wallets"""
        return AsyncSwapResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncWalletsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        chain_type: WalletChainType,
        additional_signers: AdditionalSignerInputParam | Omit = omit,
        display_name: str | Omit = omit,
        entity: WalletEntityAssignmentRequestBodyParam | Omit = omit,
        external_id: str | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        policy_ids: PolicyInputParam | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Creates a new wallet on the requested chain and for the requested owner.

        Args:
          chain_type: The wallet chain types.

          additional_signers: Additional signers for the wallet.

          display_name: A human-readable label for the wallet.

          entity: Request body for assigning an entity to a wallet.

          external_id: A customer-provided identifier for mapping to external systems. URL-safe
              characters only ([a-zA-Z0-9_-]), max 64 chars. Write-once: cannot be changed
              after creation.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          policy_ids: An optional list of up to one policy ID to enforce on the wallet.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"privy-idempotency-key": privy_idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/v1/wallets",
            body=await async_maybe_transform(
                {
                    "chain_type": chain_type,
                    "additional_signers": additional_signers,
                    "display_name": display_name,
                    "entity": entity,
                    "external_id": external_id,
                    "owner": owner,
                    "owner_id": owner_id,
                    "policy_ids": policy_ids,
                },
                wallet_create_params.WalletCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    def list(
        self,
        *,
        address: Address | Omit = omit,
        authorization_key: str | Omit = omit,
        chain_type: WalletChainType | Omit = omit,
        cursor: str | Omit = omit,
        entity_id: str | Omit = omit,
        external_id: str | Omit = omit,
        include_archived: bool | Omit = omit,
        limit: Optional[float] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Wallet, AsyncCursor[Wallet]]:
        """Get all wallets in your app.

        Args:
          address: A blockchain wallet address.

        Ethereum addresses are normalized to EIP-55
              checksum format. Solana addresses are validated as base58. All other chain
              addresses (Stellar, Tron, Sui, Aptos, etc.) are accepted as-is.

          authorization_key: Filter wallets by authorization public key. Returns wallets owned by key quorums
              that include the specified P-256 public key (base64-encoded DER format). Cannot
              be used together with user_id.

          chain_type: The wallet chain types.

          entity_id: Filter wallets by the entity ID the wallet is attributed to.

          external_id: Filter wallets by external ID.

          include_archived: Include archived wallets in lookup. Defaults to false.

          user_id: Filter wallets by user ID. Cannot be used together with authorization_key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/wallets",
            page=AsyncCursor[Wallet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "address": address,
                        "authorization_key": authorization_key,
                        "chain_type": chain_type,
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "external_id": external_id,
                        "include_archived": include_archived,
                        "limit": limit,
                        "user_id": user_id,
                    },
                    wallet_list_params.WalletListParams,
                ),
            ),
            model=Wallet,
        )

    async def _export(
        self,
        wallet_id: str,
        *,
        encryption_type: HpkeEncryption,
        recipient_public_key: str,
        export_seed_phrase: bool | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletExportResponseBody:
        """
        Export a wallet's private key

        Args:
          wallet_id: ID of the wallet.

          encryption_type: The encryption type of the wallet to import. Currently only supports `HPKE`.

          recipient_public_key: The base64-encoded encryption public key to encrypt the wallet private key with.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v1/wallets/{wallet_id}/export", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "encryption_type": encryption_type,
                    "recipient_public_key": recipient_public_key,
                    "export_seed_phrase": export_seed_phrase,
                },
                wallet_export_params.WalletExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletExportResponseBody,
        )

    @overload
    async def _init_import(
        self,
        *,
        address: str,
        chain_type: WalletImportSupportedChains,
        encryption_type: HpkeEncryption,
        entropy_type: Literal["hd"],
        index: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletInitImportResponse:
        """Initialize a wallet import.

        Complete by submitting the import.

        Args:
          address: The address of the wallet to import.

          chain_type: The chain type of the wallet to import. Supports `ethereum`, `solana`,
              `stellar`, `tron`, `sui`, `aptos`, and `xrpl`.

          encryption_type: The encryption type of the wallet to import. Currently only supports `HPKE`.

          entropy_type: The entropy type of the wallet to import.

          index: The index of the wallet to import.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _init_import(
        self,
        *,
        address: str,
        chain_type: WalletImportSupportedChains,
        encryption_type: HpkeEncryption,
        entropy_type: Literal["private-key"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletInitImportResponse:
        """Initialize a wallet import.

        Complete by submitting the import.

        Args:
          address: The address of the wallet to import.

          chain_type: The chain type of the wallet to import. Supports `ethereum`, `solana`,
              `stellar`, `tron`, `sui`, `aptos`, and `xrpl`.

          encryption_type: The encryption type of the wallet to import. Currently only supports `HPKE`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["address", "chain_type", "encryption_type", "entropy_type", "index"],
        ["address", "chain_type", "encryption_type", "entropy_type"],
    )
    async def _init_import(
        self,
        *,
        address: str,
        chain_type: WalletImportSupportedChains,
        encryption_type: HpkeEncryption,
        entropy_type: Literal["hd"] | Literal["private-key"],
        index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletInitImportResponse:
        return await self._post(
            "/v1/wallets/import/init",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "chain_type": chain_type,
                    "encryption_type": encryption_type,
                    "entropy_type": entropy_type,
                    "index": index,
                },
                wallet_init_import_params.WalletInitImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletInitImportResponse,
        )

    async def _raw_sign(
        self,
        wallet_id: str,
        *,
        params: RawSignInputParams,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RawSignResponse:
        """
        Sign a message with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          params: Parameters for the `raw_sign` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v1/wallets/{wallet_id}/raw_sign", wallet_id=wallet_id),
            body=await async_maybe_transform({"params": params}, wallet_raw_sign_params.WalletRawSignParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RawSignResponse,
        )

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signTransaction"],
        params: EthereumSignTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signTransaction` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        caip2: Caip2,
        method: Literal["eth_sendTransaction"],
        params: EthereumSendTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        experimental_data_suffix: Hex | Omit = omit,
        reference_id: str | Omit = omit,
        sponsor: bool | Omit = omit,
        sponsor_options: RpcSponsorOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the EVM `eth_sendTransaction` RPC.

          experimental_data_suffix: A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
              bytes).

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["personal_sign"],
        params: EthereumPersonalSignRpcInputParamsParam,
        address: str | Omit = omit,
        caip2: Caip2 | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        signature_options: SignatureOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `personal_sign` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          signature_options: Options controlling signature production for personal_sign and
              eth_signTypedData_v4.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signTypedData_v4"],
        params: EthereumSignTypedDataRpcInputParamsParam,
        address: str | Omit = omit,
        caip2: Caip2 | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        signature_options: SignatureOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signTypedData_v4` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          signature_options: Options controlling signature production for personal_sign and
              eth_signTypedData_v4.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["secp256k1_sign"],
        params: EthereumSecp256k1SignRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `secp256k1_sign` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_sign7702Authorization"],
        params: EthereumSign7702AuthorizationRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_sign7702Authorization` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signUserOperation"],
        params: EthereumSignUserOperationRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signUserOperation` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        caip2: Caip2,
        method: Literal["wallet_sendCalls"],
        params: EthereumSendCallsRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        experimental_data_suffix: Hex | Omit = omit,
        sponsor: bool | Omit = omit,
        sponsor_options: RpcSponsorOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the `wallet_sendCalls` RPC.

          experimental_data_suffix: A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
              bytes).

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signTransaction"],
        params: SolanaSignTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the SVM `signTransaction` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        caip2: Caip2,
        method: Literal["signAndSendTransaction"],
        params: SolanaSignAndSendTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        optimistic_broadcast: bool | Omit = omit,
        reference_id: str | Omit = omit,
        sponsor: bool | Omit = omit,
        sponsor_options: RpcSponsorOptionsParam | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the SVM `signAndSendTransaction` RPC.

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signMessage"],
        params: SolanaSignMessageRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the SVM `signMessage` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["transfer"],
        params: SparkTransferRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `transfer` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getBalance"],
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["transferTokens"],
        params: SparkTransferTokensRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `transferTokens` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getStaticDepositAddress"],
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getClaimStaticDepositQuote"],
        params: SparkGetClaimStaticDepositQuoteRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `getClaimStaticDepositQuote` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["claimStaticDeposit"],
        params: SparkClaimStaticDepositRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `claimStaticDeposit` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["createLightningInvoice"],
        params: SparkCreateLightningInvoiceRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `createLightningInvoice` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["payLightningInvoice"],
        params: SparkPayLightningInvoiceRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `payLightningInvoice` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signMessageWithIdentityKey"],
        params: SparkSignMessageWithIdentityKeyRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `signMessageWithIdentityKey` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["withdraw"],
        params: SparkWithdrawRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `withdraw` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getWithdrawalFeeQuote"],
        params: SparkGetWithdrawalFeeQuoteRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `getWithdrawalFeeQuote` RPC.

          network: The Spark network.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["tron_signTransaction"],
        params: TronSignTransactionRpcInputParamsParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Tron `tron_signTransaction` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["tron_sendTransaction"],
        params: TronSendTransactionRpcInputParamsParam,
        caip2: Caip2 | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Tron `tron_sendTransaction` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["xrpl_signTransaction"],
        params: XrplSignTransactionRpcInputParamsParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the XRPL `xrpl_signTransaction` RPC.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        address: str,
        method: Literal["exportPrivateKey"],
        params: PrivateKeyExportInputParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Input for exporting a wallet (private key or seed phrase) with HPKE encryption.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        address: str,
        method: Literal["exportSeedPhrase"],
        params: SeedPhraseExportInputParam,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          path_wallet_id: ID of the wallet.

          params: Input for exporting a wallet (private key or seed phrase) with HPKE encryption.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["method", "params"], ["caip2", "method", "params"], ["method"], ["address", "method", "params"])
    async def _rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signTransaction"]
        | Literal["eth_sendTransaction"]
        | Literal["personal_sign"]
        | Literal["eth_signTypedData_v4"]
        | Literal["secp256k1_sign"]
        | Literal["eth_sign7702Authorization"]
        | Literal["eth_signUserOperation"]
        | Literal["wallet_sendCalls"]
        | Literal["signTransaction"]
        | Literal["signAndSendTransaction"]
        | Literal["signMessage"]
        | Literal["transfer"]
        | Literal["getBalance"]
        | Literal["transferTokens"]
        | Literal["getStaticDepositAddress"]
        | Literal["getClaimStaticDepositQuote"]
        | Literal["claimStaticDeposit"]
        | Literal["createLightningInvoice"]
        | Literal["payLightningInvoice"]
        | Literal["signMessageWithIdentityKey"]
        | Literal["withdraw"]
        | Literal["getWithdrawalFeeQuote"]
        | Literal["tron_signTransaction"]
        | Literal["tron_sendTransaction"]
        | Literal["xrpl_signTransaction"]
        | Literal["exportPrivateKey"]
        | Literal["exportSeedPhrase"],
        params: EthereumSignTransactionRpcInputParamsParam
        | EthereumSendTransactionRpcInputParamsParam
        | EthereumPersonalSignRpcInputParamsParam
        | EthereumSignTypedDataRpcInputParamsParam
        | EthereumSecp256k1SignRpcInputParamsParam
        | EthereumSign7702AuthorizationRpcInputParamsParam
        | EthereumSignUserOperationRpcInputParamsParam
        | EthereumSendCallsRpcInputParamsParam
        | SolanaSignTransactionRpcInputParamsParam
        | SolanaSignAndSendTransactionRpcInputParamsParam
        | SolanaSignMessageRpcInputParamsParam
        | SparkTransferRpcInputParamsParam
        | SparkTransferTokensRpcInputParamsParam
        | SparkGetClaimStaticDepositQuoteRpcInputParamsParam
        | SparkClaimStaticDepositRpcInputParamsParam
        | SparkCreateLightningInvoiceRpcInputParamsParam
        | SparkPayLightningInvoiceRpcInputParamsParam
        | SparkSignMessageWithIdentityKeyRpcInputParamsParam
        | SparkWithdrawRpcInputParamsParam
        | SparkGetWithdrawalFeeQuoteRpcInputParamsParam
        | TronSignTransactionRpcInputParamsParam
        | TronSendTransactionRpcInputParamsParam
        | XrplSignTransactionRpcInputParamsParam
        | PrivateKeyExportInputParam
        | SeedPhraseExportInputParam
        | Omit = omit,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        caip2: Caip2 | Omit = omit,
        experimental_data_suffix: Hex | Omit = omit,
        reference_id: str | Omit = omit,
        sponsor: bool | Omit = omit,
        sponsor_options: RpcSponsorOptionsParam | Omit = omit,
        signature_options: SignatureOptionsParam | Omit = omit,
        optimistic_broadcast: bool | Omit = omit,
        network: SparkNetwork | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRpcResponse:
        if not path_wallet_id:
            raise ValueError(f"Expected a non-empty value for `path_wallet_id` but received {path_wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            WalletRpcResponse,
            await self._post(
                path_template("/v1/wallets/{path_wallet_id}/rpc", path_wallet_id=path_wallet_id),
                body=await async_maybe_transform(
                    {
                        "method": method,
                        "params": params,
                        "address": address,
                        "chain_type": chain_type,
                        "body_wallet_id": body_wallet_id,
                        "caip2": caip2,
                        "experimental_data_suffix": experimental_data_suffix,
                        "reference_id": reference_id,
                        "sponsor": sponsor,
                        "sponsor_options": sponsor_options,
                        "signature_options": signature_options,
                        "optimistic_broadcast": optimistic_broadcast,
                        "network": network,
                    },
                    wallet_rpc_params.WalletRpcParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, WalletRpcResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def _submit_import(
        self,
        *,
        wallet: wallet_submit_import_params.Wallet,
        additional_signers: AdditionalSignerInputParam | Omit = omit,
        display_name: str | Omit = omit,
        external_id: str | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        policy_ids: PolicyInputParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Submit a wallet import request.

        Args:
          wallet: The submission input for importing an HD wallet.

          additional_signers: Additional signers for the wallet.

          display_name: A human-readable label for the wallet.

          external_id: A customer-provided identifier for mapping to external systems. URL-safe
              characters only ([a-zA-Z0-9_-]), max 64 chars. Write-once: cannot be changed
              after creation.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          policy_ids: An optional list of up to one policy ID to enforce on the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/wallets/import/submit",
            body=await async_maybe_transform(
                {
                    "wallet": wallet,
                    "additional_signers": additional_signers,
                    "display_name": display_name,
                    "external_id": external_id,
                    "owner": owner,
                    "owner_id": owner_id,
                    "policy_ids": policy_ids,
                },
                wallet_submit_import_params.WalletSubmitImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    async def _transfer(
        self,
        wallet_id: str,
        *,
        destination: TokenTransferDestinationParam,
        source: TokenTransferSourceParam,
        amount: str | Omit = omit,
        amount_type: AmountType | Omit = omit,
        fee_configuration: FeeConfigurationParam | Omit = omit,
        nonce: WalletActionNonce | Omit = omit,
        slippage_bps: int | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_idempotency_key: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferActionResponse:
        """
        Transfer tokens from a wallet to a destination address.

        Args:
          wallet_id: ID of the wallet.

          destination: The destination address for a token transfer. Optionally specify a different
              asset or chain for cross-asset or cross-chain transfers.

          source: The source asset, amount, and chain for a token transfer. Specify either `asset`
              (named) or `asset_address` (custom), not both.

          amount: Amount as a decimal string in the token's standard unit (e.g. "1.5" for 1.5
              USDC). For exact_input, the amount to send. For exact_output, the exact amount
              to receive. Takes precedence over source.amount when both are provided.

          amount_type: Whether the amount refers to the input token or output token.

          fee_configuration: Total fees assessed on a transfer, in BPS

          nonce: Unique caller-generated nonce used to prevent replaying a signed wallet action
              request. Must be at least 24 characters (e.g. a cuid2 or UUID).

          slippage_bps: Maximum allowed slippage in basis points (1 bps = 0.01%). Only applicable for
              cross-chain or cross-asset transfers; omit to use the provider default.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v1/wallets/{wallet_id}/transfer", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                    "amount": amount,
                    "amount_type": amount_type,
                    "fee_configuration": fee_configuration,
                    "nonce": nonce,
                    "slippage_bps": slippage_bps,
                },
                wallet_transfer_params.WalletTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferActionResponse,
        )

    async def _update(
        self,
        wallet_id: str,
        *,
        additional_signers: AdditionalSignerInputParam | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        privy_authorization_signature: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Update a wallet's policies or authorization key configuration.

        Args:
          wallet_id: ID of the wallet.

          additional_signers: Additional signers for the wallet.

          display_name: A human-readable label for the wallet. Set to null to clear.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          policy_ids: New policy IDs to enforce on the wallet. Currently, only one policy is supported
              per wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-request-expiry": privy_request_expiry,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/v1/wallets/{wallet_id}", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "additional_signers": additional_signers,
                    "display_name": display_name,
                    "owner": owner,
                    "owner_id": owner_id,
                    "policy_ids": policy_ids,
                },
                wallet_update_params.WalletUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    async def archive(
        self,
        wallet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Archives a wallet, preventing it from being used in any write or signing
        operations. Archived wallets are hidden from list endpoints by default. Returns
        404 if the wallet does not exist or is already archived.

        Args:
          wallet_id: ID of the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._post(
            path_template("/v1/wallets/{wallet_id}/archive", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    async def assign_entity(
        self,
        wallet_id: str,
        *,
        id: EntityID,
        type: WalletEntityType,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletEntityAssignmentResponse:
        """
        Assign a user or organization to a wallet.

        Args:
          wallet_id: ID of the wallet.

          id: A Privy entity ID.

          type: The type of entity a wallet is attributed to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._post(
            path_template("/v1/wallets/{wallet_id}/entity", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "type": type,
                },
                wallet_assign_entity_params.WalletAssignEntityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletEntityAssignmentResponse,
        )

    async def authenticate_with_jwt(
        self,
        *,
        encryption_type: Literal["HPKE"],
        recipient_public_key: str,
        user_jwt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletAuthenticateWithJwtResponse:
        """
        Exchange a user JWT for a session key authorized to act on the user's wallets.
        Returns the encrypted authorization key and the list of wallets it can access.

        Args:
          encryption_type: The encryption type for the authentication response. Currently only supports
              HPKE.

          recipient_public_key: The public key of your ECDH keypair, in base64-encoded, SPKI-format, whose
              private key will be able to decrypt the session key.

          user_jwt: The user's JWT, to be used to authenticate the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            WalletAuthenticateWithJwtResponse,
            await self._post(
                "/v1/wallets/authenticate",
                body=await async_maybe_transform(
                    {
                        "encryption_type": encryption_type,
                        "recipient_public_key": recipient_public_key,
                        "user_jwt": user_jwt,
                    },
                    wallet_authenticate_with_jwt_params.WalletAuthenticateWithJwtParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, WalletAuthenticateWithJwtResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def create_batch(
        self,
        *,
        wallets: Iterable[WalletBatchItemInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletBatchCreateResponse:
        """Creates multiple wallets in a single request.

        Each wallet creation is
        independent; failures for one wallet do not affect others. Maximum batch size is
        100 wallets.

        Args:
          wallets: Array of wallet creation requests. Minimum 1, maximum 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/wallets/batch",
            body=await async_maybe_transform({"wallets": wallets}, wallet_create_batch_params.WalletCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletBatchCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def create_wallets_with_recovery(
        self,
        *,
        primary_signer: wallet_create_wallets_with_recovery_params.PrimarySigner,
        recovery_user: wallet_create_wallets_with_recovery_params.RecoveryUser,
        wallets: Iterable[wallet_create_wallets_with_recovery_params.Wallet],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletCreateWalletsWithRecoveryResponse:
        """
        Create one or more wallets associated with a recovery user, so the user can
        later regain wallet access via the linked accounts. Deprecated; prefer the
        standard wallet creation flow combined with a separate recovery setup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/wallets_with_recovery",
            body=await async_maybe_transform(
                {
                    "primary_signer": primary_signer,
                    "recovery_user": recovery_user,
                    "wallets": wallets,
                },
                wallet_create_wallets_with_recovery_params.WalletCreateWalletsWithRecoveryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletCreateWalletsWithRecoveryResponse,
        )

    async def get(
        self,
        wallet_id: str,
        *,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """
        Get a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          include_archived: Include archived wallets in lookup. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            path_template("/v1/wallets/{wallet_id}", wallet_id=wallet_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_archived": include_archived}, wallet_get_params.WalletGetParams
                ),
            ),
            cast_to=Wallet,
        )

    async def get_wallet_by_address(
        self,
        *,
        address: Address,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Wallet:
        """Look up a wallet by its blockchain address.

        Returns the wallet object if found.

        Args:
          address: A blockchain wallet address. Ethereum addresses are normalized to EIP-55
              checksum format. Solana addresses are validated as base58. All other chain
              addresses (Stellar, Tron, Sui, Aptos, etc.) are accepted as-is.

          include_archived: Include archived wallets in lookup. Defaults to false (archived wallets return
              404).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/wallets/address",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "include_archived": include_archived,
                },
                wallet_get_wallet_by_address_params.WalletGetWalletByAddressParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )


class WalletsResourceWithRawResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.create = to_raw_response_wrapper(
            wallets.create,
        )
        self.list = to_raw_response_wrapper(
            wallets.list,
        )
        self._export = to_raw_response_wrapper(
            wallets._export,
        )
        self._init_import = to_raw_response_wrapper(
            wallets._init_import,
        )
        self._raw_sign = to_raw_response_wrapper(
            wallets._raw_sign,
        )
        self._rpc = to_raw_response_wrapper(
            wallets._rpc,
        )
        self._submit_import = to_raw_response_wrapper(
            wallets._submit_import,
        )
        self._transfer = to_raw_response_wrapper(
            wallets._transfer,
        )
        self._update = to_raw_response_wrapper(
            wallets._update,
        )
        self.archive = to_raw_response_wrapper(
            wallets.archive,
        )
        self.assign_entity = to_raw_response_wrapper(
            wallets.assign_entity,
        )
        self.authenticate_with_jwt = to_raw_response_wrapper(
            wallets.authenticate_with_jwt,
        )
        self.create_batch = to_raw_response_wrapper(
            wallets.create_batch,
        )
        self.create_wallets_with_recovery = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                wallets.create_wallets_with_recovery,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = to_raw_response_wrapper(
            wallets.get,
        )
        self.get_wallet_by_address = to_raw_response_wrapper(
            wallets.get_wallet_by_address,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """Operations related to wallet actions"""
        return ActionsResourceWithRawResponse(self._wallets.actions)

    @cached_property
    def earn(self) -> EarnResourceWithRawResponse:
        return EarnResourceWithRawResponse(self._wallets.earn)

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        """Operations related to wallets"""
        return TransactionsResourceWithRawResponse(self._wallets.transactions)

    @cached_property
    def balance(self) -> BalanceResourceWithRawResponse:
        """Operations related to wallets"""
        return BalanceResourceWithRawResponse(self._wallets.balance)

    @cached_property
    def swap(self) -> SwapResourceWithRawResponse:
        """Operations for swapping tokens within wallets"""
        return SwapResourceWithRawResponse(self._wallets.swap)


class AsyncWalletsResourceWithRawResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.create = async_to_raw_response_wrapper(
            wallets.create,
        )
        self.list = async_to_raw_response_wrapper(
            wallets.list,
        )
        self._export = async_to_raw_response_wrapper(
            wallets._export,
        )
        self._init_import = async_to_raw_response_wrapper(
            wallets._init_import,
        )
        self._raw_sign = async_to_raw_response_wrapper(
            wallets._raw_sign,
        )
        self._rpc = async_to_raw_response_wrapper(
            wallets._rpc,
        )
        self._submit_import = async_to_raw_response_wrapper(
            wallets._submit_import,
        )
        self._transfer = async_to_raw_response_wrapper(
            wallets._transfer,
        )
        self._update = async_to_raw_response_wrapper(
            wallets._update,
        )
        self.archive = async_to_raw_response_wrapper(
            wallets.archive,
        )
        self.assign_entity = async_to_raw_response_wrapper(
            wallets.assign_entity,
        )
        self.authenticate_with_jwt = async_to_raw_response_wrapper(
            wallets.authenticate_with_jwt,
        )
        self.create_batch = async_to_raw_response_wrapper(
            wallets.create_batch,
        )
        self.create_wallets_with_recovery = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                wallets.create_wallets_with_recovery,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = async_to_raw_response_wrapper(
            wallets.get,
        )
        self.get_wallet_by_address = async_to_raw_response_wrapper(
            wallets.get_wallet_by_address,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """Operations related to wallet actions"""
        return AsyncActionsResourceWithRawResponse(self._wallets.actions)

    @cached_property
    def earn(self) -> AsyncEarnResourceWithRawResponse:
        return AsyncEarnResourceWithRawResponse(self._wallets.earn)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        """Operations related to wallets"""
        return AsyncTransactionsResourceWithRawResponse(self._wallets.transactions)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithRawResponse:
        """Operations related to wallets"""
        return AsyncBalanceResourceWithRawResponse(self._wallets.balance)

    @cached_property
    def swap(self) -> AsyncSwapResourceWithRawResponse:
        """Operations for swapping tokens within wallets"""
        return AsyncSwapResourceWithRawResponse(self._wallets.swap)


class WalletsResourceWithStreamingResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.create = to_streamed_response_wrapper(
            wallets.create,
        )
        self.list = to_streamed_response_wrapper(
            wallets.list,
        )
        self._export = to_streamed_response_wrapper(
            wallets._export,
        )
        self._init_import = to_streamed_response_wrapper(
            wallets._init_import,
        )
        self._raw_sign = to_streamed_response_wrapper(
            wallets._raw_sign,
        )
        self._rpc = to_streamed_response_wrapper(
            wallets._rpc,
        )
        self._submit_import = to_streamed_response_wrapper(
            wallets._submit_import,
        )
        self._transfer = to_streamed_response_wrapper(
            wallets._transfer,
        )
        self._update = to_streamed_response_wrapper(
            wallets._update,
        )
        self.archive = to_streamed_response_wrapper(
            wallets.archive,
        )
        self.assign_entity = to_streamed_response_wrapper(
            wallets.assign_entity,
        )
        self.authenticate_with_jwt = to_streamed_response_wrapper(
            wallets.authenticate_with_jwt,
        )
        self.create_batch = to_streamed_response_wrapper(
            wallets.create_batch,
        )
        self.create_wallets_with_recovery = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                wallets.create_wallets_with_recovery,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = to_streamed_response_wrapper(
            wallets.get,
        )
        self.get_wallet_by_address = to_streamed_response_wrapper(
            wallets.get_wallet_by_address,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """Operations related to wallet actions"""
        return ActionsResourceWithStreamingResponse(self._wallets.actions)

    @cached_property
    def earn(self) -> EarnResourceWithStreamingResponse:
        return EarnResourceWithStreamingResponse(self._wallets.earn)

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        """Operations related to wallets"""
        return TransactionsResourceWithStreamingResponse(self._wallets.transactions)

    @cached_property
    def balance(self) -> BalanceResourceWithStreamingResponse:
        """Operations related to wallets"""
        return BalanceResourceWithStreamingResponse(self._wallets.balance)

    @cached_property
    def swap(self) -> SwapResourceWithStreamingResponse:
        """Operations for swapping tokens within wallets"""
        return SwapResourceWithStreamingResponse(self._wallets.swap)


class AsyncWalletsResourceWithStreamingResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.create = async_to_streamed_response_wrapper(
            wallets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            wallets.list,
        )
        self._export = async_to_streamed_response_wrapper(
            wallets._export,
        )
        self._init_import = async_to_streamed_response_wrapper(
            wallets._init_import,
        )
        self._raw_sign = async_to_streamed_response_wrapper(
            wallets._raw_sign,
        )
        self._rpc = async_to_streamed_response_wrapper(
            wallets._rpc,
        )
        self._submit_import = async_to_streamed_response_wrapper(
            wallets._submit_import,
        )
        self._transfer = async_to_streamed_response_wrapper(
            wallets._transfer,
        )
        self._update = async_to_streamed_response_wrapper(
            wallets._update,
        )
        self.archive = async_to_streamed_response_wrapper(
            wallets.archive,
        )
        self.assign_entity = async_to_streamed_response_wrapper(
            wallets.assign_entity,
        )
        self.authenticate_with_jwt = async_to_streamed_response_wrapper(
            wallets.authenticate_with_jwt,
        )
        self.create_batch = async_to_streamed_response_wrapper(
            wallets.create_batch,
        )
        self.create_wallets_with_recovery = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                wallets.create_wallets_with_recovery,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = async_to_streamed_response_wrapper(
            wallets.get,
        )
        self.get_wallet_by_address = async_to_streamed_response_wrapper(
            wallets.get_wallet_by_address,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """Operations related to wallet actions"""
        return AsyncActionsResourceWithStreamingResponse(self._wallets.actions)

    @cached_property
    def earn(self) -> AsyncEarnResourceWithStreamingResponse:
        return AsyncEarnResourceWithStreamingResponse(self._wallets.earn)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """Operations related to wallets"""
        return AsyncTransactionsResourceWithStreamingResponse(self._wallets.transactions)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithStreamingResponse:
        """Operations related to wallets"""
        return AsyncBalanceResourceWithStreamingResponse(self._wallets.balance)

    @cached_property
    def swap(self) -> AsyncSwapResourceWithStreamingResponse:
        """Operations for swapping tokens within wallets"""
        return AsyncSwapResourceWithStreamingResponse(self._wallets.swap)
