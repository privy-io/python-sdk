# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Any, List, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ...types import (
    wallet_rpc_params,
    wallet_list_params,
    wallet_create_params,
    wallet_update_params,
    wallet_authenticate_with_jwt_params,
    wallet_create_wallets_with_recovery_params,
)
from .balance import (
    BalanceResource,
    AsyncBalanceResource,
    BalanceResourceWithRawResponse,
    AsyncBalanceResourceWithRawResponse,
    BalanceResourceWithStreamingResponse,
    AsyncBalanceResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
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
from ...types.wallet import Wallet
from ...types.wallet_rpc_response import WalletRpcResponse
from ...types.wallet_authenticate_with_jwt_response import WalletAuthenticateWithJwtResponse
from ...types.wallet_create_wallets_with_recovery_response import WalletCreateWalletsWithRecoveryResponse

__all__ = ["WalletsResource", "AsyncWalletsResource"]


class WalletsResource(SyncAPIResource):
    @cached_property
    def transactions(self) -> TransactionsResource:
        return TransactionsResource(self._client)

    @cached_property
    def balance(self) -> BalanceResource:
        return BalanceResource(self._client)

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
        chain_type: Literal["solana", "ethereum", "cosmos", "stellar", "sui", "tron"],
        additional_signers: Iterable[wallet_create_params.AdditionalSigner] | NotGiven = NOT_GIVEN,
        owner: Optional[wallet_create_params.Owner] | NotGiven = NOT_GIVEN,
        owner_id: Optional[str] | NotGiven = NOT_GIVEN,
        policy_ids: List[str] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Wallet:
        """Create a new wallet.

        Args:
          chain_type: Chain type of the wallet.

        "ethereum" supports any EVM-compatible network.

          additional_signers: Additional signers for the wallet.

          owner: The P-256 public key of the owner of the wallet. If you provide this, do not
              specify an owner_id as it will be generated automatically.

          owner_id: The key quorum ID to set as the owner of the wallet. If you provide this, do not
              specify an owner.

          policy_ids: List of policy IDs for policies that should be enforced on the wallet.
              Currently, only one policy is supported per wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/wallets",
            body=maybe_transform(
                {
                    "chain_type": chain_type,
                    "additional_signers": additional_signers,
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

    def update(
        self,
        wallet_id: str,
        *,
        additional_signers: Iterable[wallet_update_params.AdditionalSigner] | NotGiven = NOT_GIVEN,
        owner: Optional[wallet_update_params.Owner] | NotGiven = NOT_GIVEN,
        owner_id: Optional[str] | NotGiven = NOT_GIVEN,
        policy_ids: List[str] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Wallet:
        """
        Update a wallet's policies or authorization key configuration.

        Args:
          wallet_id: ID of the wallet.

          additional_signers: Additional signers for the wallet.

          owner: The P-256 public key of the owner of the wallet. If you provide this, do not
              specify an owner_id as it will be generated automatically.

          owner_id: The key quorum ID to set as the owner of the wallet. If you provide this, do not
              specify an owner.

          policy_ids: New policy IDs to enforce on the wallet. Currently, only one policy is supported
              per wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return self._patch(
            f"/v1/wallets/{wallet_id}",
            body=maybe_transform(
                {
                    "additional_signers": additional_signers,
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

    def list(
        self,
        *,
        chain_type: Literal["solana", "ethereum", "cosmos", "stellar", "sui", "tron"] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursor[Wallet]:
        """Get all wallets in your app.

        Args:
          chain_type: Chain type of the wallet.

        'Ethereum' supports any EVM-compatible network.

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
                        "chain_type": chain_type,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    wallet_list_params.WalletListParams,
                ),
            ),
            model=Wallet,
        )

    @typing_extensions.deprecated("deprecated")
    def authenticate_with_jwt(
        self,
        *,
        user_jwt: str,
        encryption_type: Literal["HPKE"] | NotGiven = NOT_GIVEN,
        recipient_public_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletAuthenticateWithJwtResponse:
        """
        Obtain a user session signer to enable wallet access.

        Args:
          user_jwt: The user's JWT, to be used to authenticate the user.

          encryption_type: The encryption type for the authentication response. Currently only supports
              HPKE.

          recipient_public_key: The public key of your ECDH keypair, in base64-encoded, SPKI-format, whose
              private key will be able to decrypt the session key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            WalletAuthenticateWithJwtResponse,
            self._post(
                "/v1/user_signers/authenticate",
                body=maybe_transform(
                    {
                        "user_jwt": user_jwt,
                        "encryption_type": encryption_type,
                        "recipient_public_key": recipient_public_key,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletCreateWalletsWithRecoveryResponse:
        """
        Create wallets with an associated recovery user.

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Wallet:
        """
        Get a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            f"/v1/wallets/{wallet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    @overload
    def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["eth_signTransaction"],
        params: wallet_rpc_params.EthSignTransactionParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        wallet_id: str,
        *,
        caip2: str,
        method: Literal["eth_sendTransaction"],
        params: wallet_rpc_params.EthSendTransactionParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["personal_sign"],
        params: wallet_rpc_params.PersonalSignParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["eth_signTypedData_v4"],
        params: wallet_rpc_params.EthSignTypedDataV4Params,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["eth_sign7702Authorization"],
        params: wallet_rpc_params.EthSign7702AuthorizationParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["secp256k1_sign"],
        params: wallet_rpc_params.Secp256k1SignParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["signTransaction"],
        params: wallet_rpc_params.SignTransactionParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["solana"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        wallet_id: str,
        *,
        caip2: str,
        method: Literal["signAndSendTransaction"],
        params: wallet_rpc_params.SignAndSendTransactionParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["solana"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["signMessage"],
        params: wallet_rpc_params.SignMessageParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["solana"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["method", "params"], ["caip2", "method", "params"])
    def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["eth_signTransaction"]
        | Literal["eth_sendTransaction"]
        | Literal["personal_sign"]
        | Literal["eth_signTypedData_v4"]
        | Literal["eth_sign7702Authorization"]
        | Literal["secp256k1_sign"]
        | Literal["signTransaction"]
        | Literal["signAndSendTransaction"]
        | Literal["signMessage"],
        params: wallet_rpc_params.EthSignTransactionParams
        | wallet_rpc_params.PersonalSignParams
        | wallet_rpc_params.EthSignTypedDataV4Params
        | wallet_rpc_params.EthSign7702AuthorizationParams
        | wallet_rpc_params.Secp256k1SignParams
        | wallet_rpc_params.SignTransactionParams
        | wallet_rpc_params.SignMessageParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | Literal["solana"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        caip2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            WalletRpcResponse,
            self._post(
                f"/v1/wallets/{wallet_id}/rpc",
                body=maybe_transform(
                    {
                        "method": method,
                        "params": params,
                        "address": address,
                        "chain_type": chain_type,
                        "caip2": caip2,
                    },
                    wallet_rpc_params.WalletRpcParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, WalletRpcResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncWalletsResource(AsyncAPIResource):
    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        return AsyncTransactionsResource(self._client)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        return AsyncBalanceResource(self._client)

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
        chain_type: Literal["solana", "ethereum", "cosmos", "stellar", "sui", "tron"],
        additional_signers: Iterable[wallet_create_params.AdditionalSigner] | NotGiven = NOT_GIVEN,
        owner: Optional[wallet_create_params.Owner] | NotGiven = NOT_GIVEN,
        owner_id: Optional[str] | NotGiven = NOT_GIVEN,
        policy_ids: List[str] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Wallet:
        """Create a new wallet.

        Args:
          chain_type: Chain type of the wallet.

        "ethereum" supports any EVM-compatible network.

          additional_signers: Additional signers for the wallet.

          owner: The P-256 public key of the owner of the wallet. If you provide this, do not
              specify an owner_id as it will be generated automatically.

          owner_id: The key quorum ID to set as the owner of the wallet. If you provide this, do not
              specify an owner.

          policy_ids: List of policy IDs for policies that should be enforced on the wallet.
              Currently, only one policy is supported per wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/wallets",
            body=await async_maybe_transform(
                {
                    "chain_type": chain_type,
                    "additional_signers": additional_signers,
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

    async def update(
        self,
        wallet_id: str,
        *,
        additional_signers: Iterable[wallet_update_params.AdditionalSigner] | NotGiven = NOT_GIVEN,
        owner: Optional[wallet_update_params.Owner] | NotGiven = NOT_GIVEN,
        owner_id: Optional[str] | NotGiven = NOT_GIVEN,
        policy_ids: List[str] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Wallet:
        """
        Update a wallet's policies or authorization key configuration.

        Args:
          wallet_id: ID of the wallet.

          additional_signers: Additional signers for the wallet.

          owner: The P-256 public key of the owner of the wallet. If you provide this, do not
              specify an owner_id as it will be generated automatically.

          owner_id: The key quorum ID to set as the owner of the wallet. If you provide this, do not
              specify an owner.

          policy_ids: New policy IDs to enforce on the wallet. Currently, only one policy is supported
              per wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given({"privy-authorization-signature": privy_authorization_signature}),
            **(extra_headers or {}),
        }
        return await self._patch(
            f"/v1/wallets/{wallet_id}",
            body=await async_maybe_transform(
                {
                    "additional_signers": additional_signers,
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

    def list(
        self,
        *,
        chain_type: Literal["solana", "ethereum", "cosmos", "stellar", "sui", "tron"] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Wallet, AsyncCursor[Wallet]]:
        """Get all wallets in your app.

        Args:
          chain_type: Chain type of the wallet.

        'Ethereum' supports any EVM-compatible network.

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
                        "chain_type": chain_type,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    wallet_list_params.WalletListParams,
                ),
            ),
            model=Wallet,
        )

    @typing_extensions.deprecated("deprecated")
    async def authenticate_with_jwt(
        self,
        *,
        user_jwt: str,
        encryption_type: Literal["HPKE"] | NotGiven = NOT_GIVEN,
        recipient_public_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletAuthenticateWithJwtResponse:
        """
        Obtain a user session signer to enable wallet access.

        Args:
          user_jwt: The user's JWT, to be used to authenticate the user.

          encryption_type: The encryption type for the authentication response. Currently only supports
              HPKE.

          recipient_public_key: The public key of your ECDH keypair, in base64-encoded, SPKI-format, whose
              private key will be able to decrypt the session key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            WalletAuthenticateWithJwtResponse,
            await self._post(
                "/v1/user_signers/authenticate",
                body=await async_maybe_transform(
                    {
                        "user_jwt": user_jwt,
                        "encryption_type": encryption_type,
                        "recipient_public_key": recipient_public_key,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletCreateWalletsWithRecoveryResponse:
        """
        Create wallets with an associated recovery user.

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Wallet:
        """
        Get a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            f"/v1/wallets/{wallet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Wallet,
        )

    @overload
    async def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["eth_signTransaction"],
        params: wallet_rpc_params.EthSignTransactionParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        wallet_id: str,
        *,
        caip2: str,
        method: Literal["eth_sendTransaction"],
        params: wallet_rpc_params.EthSendTransactionParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["personal_sign"],
        params: wallet_rpc_params.PersonalSignParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["eth_signTypedData_v4"],
        params: wallet_rpc_params.EthSignTypedDataV4Params,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["eth_sign7702Authorization"],
        params: wallet_rpc_params.EthSign7702AuthorizationParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["secp256k1_sign"],
        params: wallet_rpc_params.Secp256k1SignParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["signTransaction"],
        params: wallet_rpc_params.SignTransactionParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["solana"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        wallet_id: str,
        *,
        caip2: str,
        method: Literal["signAndSendTransaction"],
        params: wallet_rpc_params.SignAndSendTransactionParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["solana"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["signMessage"],
        params: wallet_rpc_params.SignMessageParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["solana"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        """
        Sign a message or transaction with a wallet by wallet ID.

        Args:
          wallet_id: ID of the wallet.

          privy_authorization_signature: Request authorization signature. If multiple signatures are required, they
              should be comma separated.

          privy_idempotency_key: Idempotency keys ensure API requests are executed only once within a 24-hour
              window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["method", "params"], ["caip2", "method", "params"])
    async def rpc(
        self,
        wallet_id: str,
        *,
        method: Literal["eth_signTransaction"]
        | Literal["eth_sendTransaction"]
        | Literal["personal_sign"]
        | Literal["eth_signTypedData_v4"]
        | Literal["eth_sign7702Authorization"]
        | Literal["secp256k1_sign"]
        | Literal["signTransaction"]
        | Literal["signAndSendTransaction"]
        | Literal["signMessage"],
        params: wallet_rpc_params.EthSignTransactionParams
        | wallet_rpc_params.PersonalSignParams
        | wallet_rpc_params.EthSignTypedDataV4Params
        | wallet_rpc_params.EthSign7702AuthorizationParams
        | wallet_rpc_params.Secp256k1SignParams
        | wallet_rpc_params.SignTransactionParams
        | wallet_rpc_params.SignMessageParams,
        address: str | NotGiven = NOT_GIVEN,
        chain_type: Literal["ethereum"] | Literal["solana"] | NotGiven = NOT_GIVEN,
        privy_authorization_signature: str | NotGiven = NOT_GIVEN,
        privy_idempotency_key: str | NotGiven = NOT_GIVEN,
        caip2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletRpcResponse:
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-authorization-signature": privy_authorization_signature,
                    "privy-idempotency-key": privy_idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            WalletRpcResponse,
            await self._post(
                f"/v1/wallets/{wallet_id}/rpc",
                body=await async_maybe_transform(
                    {
                        "method": method,
                        "params": params,
                        "address": address,
                        "chain_type": chain_type,
                        "caip2": caip2,
                    },
                    wallet_rpc_params.WalletRpcParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, WalletRpcResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class WalletsResourceWithRawResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.create = to_raw_response_wrapper(
            wallets.create,
        )
        self.update = to_raw_response_wrapper(
            wallets.update,
        )
        self.list = to_raw_response_wrapper(
            wallets.list,
        )
        self.authenticate_with_jwt = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                wallets.authenticate_with_jwt  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_wallets_with_recovery = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                wallets.create_wallets_with_recovery  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = to_raw_response_wrapper(
            wallets.get,
        )
        self.rpc = to_raw_response_wrapper(
            wallets.rpc,
        )

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self._wallets.transactions)

    @cached_property
    def balance(self) -> BalanceResourceWithRawResponse:
        return BalanceResourceWithRawResponse(self._wallets.balance)


class AsyncWalletsResourceWithRawResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.create = async_to_raw_response_wrapper(
            wallets.create,
        )
        self.update = async_to_raw_response_wrapper(
            wallets.update,
        )
        self.list = async_to_raw_response_wrapper(
            wallets.list,
        )
        self.authenticate_with_jwt = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                wallets.authenticate_with_jwt  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_wallets_with_recovery = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                wallets.create_wallets_with_recovery  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = async_to_raw_response_wrapper(
            wallets.get,
        )
        self.rpc = async_to_raw_response_wrapper(
            wallets.rpc,
        )

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self._wallets.transactions)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithRawResponse:
        return AsyncBalanceResourceWithRawResponse(self._wallets.balance)


class WalletsResourceWithStreamingResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.create = to_streamed_response_wrapper(
            wallets.create,
        )
        self.update = to_streamed_response_wrapper(
            wallets.update,
        )
        self.list = to_streamed_response_wrapper(
            wallets.list,
        )
        self.authenticate_with_jwt = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                wallets.authenticate_with_jwt  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_wallets_with_recovery = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                wallets.create_wallets_with_recovery  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = to_streamed_response_wrapper(
            wallets.get,
        )
        self.rpc = to_streamed_response_wrapper(
            wallets.rpc,
        )

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self._wallets.transactions)

    @cached_property
    def balance(self) -> BalanceResourceWithStreamingResponse:
        return BalanceResourceWithStreamingResponse(self._wallets.balance)


class AsyncWalletsResourceWithStreamingResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.create = async_to_streamed_response_wrapper(
            wallets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            wallets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            wallets.list,
        )
        self.authenticate_with_jwt = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                wallets.authenticate_with_jwt  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_wallets_with_recovery = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                wallets.create_wallets_with_recovery  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = async_to_streamed_response_wrapper(
            wallets.get,
        )
        self.rpc = async_to_streamed_response_wrapper(
            wallets.rpc,
        )

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self._wallets.transactions)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithStreamingResponse:
        return AsyncBalanceResourceWithStreamingResponse(self._wallets.balance)
