# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..types import (
    Hex,
    Caip2,
    AmountType,
    IntentType,
    IntentStatus,
    OwnerIDInput,
    PolicyAction,
    PolicyMethod,
    SparkNetwork,
    intent_rpc_params,
    intent_list_params,
    intent_transfer_params,
    intent_update_policy_params,
    intent_update_wallet_params,
    intent_update_key_quorum_params,
    intent_create_policy_rule_params,
    intent_update_policy_rule_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.hex import Hex
from ..pagination import SyncCursor, AsyncCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.caip_2 import Caip2
from ..types.amount_type import AmountType
from ..types.intent_type import IntentType
from ..types.intent_status import IntentStatus
from ..types.policy_action import PolicyAction
from ..types.policy_method import PolicyMethod
from ..types.spark_network import SparkNetwork
from ..types.owner_id_input import OwnerIDInput
from ..types.intent_response import IntentResponse
from ..types.owner_input_param import OwnerInputParam
from ..types.rpc_intent_response import RpcIntentResponse
from ..types.policy_condition_param import PolicyConditionParam
from ..types.policy_intent_response import PolicyIntentResponse
from ..types.wallet_intent_response import WalletIntentResponse
from ..types.fee_configuration_param import FeeConfigurationParam
from ..types.signature_options_param import SignatureOptionsParam
from ..types.transfer_intent_response import TransferIntentResponse
from ..types.rpc_sponsor_options_param import RpcSponsorOptionsParam
from ..types.key_quorum_intent_response import KeyQuorumIntentResponse
from ..types.rule_delete_intent_response import RuleDeleteIntentResponse
from ..types.rule_mutate_intent_response import RuleMutateIntentResponse
from ..types.token_transfer_source_param import TokenTransferSourceParam
from ..types.additional_signer_input_param import AdditionalSignerInputParam
from ..types.policy_rule_request_body_param import PolicyRuleRequestBodyParam
from ..types.private_key_export_input_param import PrivateKeyExportInputParam
from ..types.seed_phrase_export_input_param import SeedPhraseExportInputParam
from ..types.token_transfer_destination_param import TokenTransferDestinationParam
from ..types.spark_transfer_rpc_input_params_param import SparkTransferRpcInputParamsParam
from ..types.spark_withdraw_rpc_input_params_param import SparkWithdrawRpcInputParamsParam
from ..types.ethereum_send_calls_rpc_input_params_param import EthereumSendCallsRpcInputParamsParam
from ..types.solana_sign_message_rpc_input_params_param import SolanaSignMessageRpcInputParamsParam
from ..types.spark_transfer_tokens_rpc_input_params_param import SparkTransferTokensRpcInputParamsParam
from ..types.tron_send_transaction_rpc_input_params_param import TronSendTransactionRpcInputParamsParam
from ..types.tron_sign_transaction_rpc_input_params_param import TronSignTransactionRpcInputParamsParam
from ..types.ethereum_personal_sign_rpc_input_params_param import EthereumPersonalSignRpcInputParamsParam
from ..types.solana_sign_transaction_rpc_input_params_param import SolanaSignTransactionRpcInputParamsParam
from ..types.ethereum_sign_typed_data_rpc_input_params_param import EthereumSignTypedDataRpcInputParamsParam
from ..types.ethereum_secp_256k_1_sign_rpc_input_params_param import EthereumSecp256k1SignRpcInputParamsParam
from ..types.ethereum_send_transaction_rpc_input_params_param import EthereumSendTransactionRpcInputParamsParam
from ..types.ethereum_sign_transaction_rpc_input_params_param import EthereumSignTransactionRpcInputParamsParam
from ..types.spark_claim_static_deposit_rpc_input_params_param import SparkClaimStaticDepositRpcInputParamsParam
from ..types.spark_pay_lightning_invoice_rpc_input_params_param import SparkPayLightningInvoiceRpcInputParamsParam
from ..types.ethereum_sign_user_operation_rpc_input_params_param import EthereumSignUserOperationRpcInputParamsParam
from ..types.spark_create_lightning_invoice_rpc_input_params_param import SparkCreateLightningInvoiceRpcInputParamsParam
from ..types.spark_get_withdrawal_fee_quote_rpc_input_params_param import SparkGetWithdrawalFeeQuoteRpcInputParamsParam
from ..types.ethereum_sign_7702_authorization_rpc_input_params_param import (
    EthereumSign7702AuthorizationRpcInputParamsParam,
)
from ..types.solana_sign_and_send_transaction_rpc_input_params_param import (
    SolanaSignAndSendTransactionRpcInputParamsParam,
)
from ..types.spark_get_claim_static_deposit_quote_rpc_input_params_param import (
    SparkGetClaimStaticDepositQuoteRpcInputParamsParam,
)
from ..types.spark_sign_message_with_identity_key_rpc_input_params_param import (
    SparkSignMessageWithIdentityKeyRpcInputParamsParam,
)

__all__ = ["IntentsResource", "AsyncIntentsResource"]


class IntentsResource(SyncAPIResource):
    """Operations related to authorization intents for wallet actions"""

    @cached_property
    def with_raw_response(self) -> IntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return IntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return IntentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        created_by_id: str | Omit = omit,
        current_user_has_signed: Literal["true", "false"] | Omit = omit,
        cursor: str | Omit = omit,
        intent_type: IntentType | Omit = omit,
        limit: Optional[float] | Omit = omit,
        pending_member_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        sort_by: Literal["created_at_desc", "expires_at_asc", "updated_at_desc"] | Omit = omit,
        status: IntentStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[IntentResponse]:
        """List intents for an app.

        Returns a paginated list of intents with their current
        status and details.

        Args:
          intent_type: Type of intent.

          status: Current status of an intent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/intents",
            page=SyncCursor[IntentResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_by_id": created_by_id,
                        "current_user_has_signed": current_user_has_signed,
                        "cursor": cursor,
                        "intent_type": intent_type,
                        "limit": limit,
                        "pending_member_id": pending_member_id,
                        "resource_id": resource_id,
                        "sort_by": sort_by,
                        "status": status,
                    },
                    intent_list_params.IntentListParams,
                ),
            ),
            model=cast(Any, IntentResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def create_policy_rule(
        self,
        policy_id: str,
        *,
        action: PolicyAction,
        conditions: Iterable[PolicyConditionParam],
        method: PolicyMethod,
        name: str,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleMutateIntentResponse:
        """Create an intent to add a rule to a policy.

        The intent must be authorized by the
        policy owner before it can be executed.

        Args:
          policy_id: ID of the policy.

          action: The action to take when a policy rule matches.

          method: Method the rule applies to.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/intents/policies/{policy_id}/rules", policy_id=policy_id),
            body=maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "method": method,
                    "name": name,
                },
                intent_create_policy_rule_params.IntentCreatePolicyRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleMutateIntentResponse,
        )

    def delete_policy_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteIntentResponse:
        """Create an intent to delete a rule from a policy.

        The intent must be authorized
        by the policy owner before it can be executed.

        Args:
          policy_id: ID of the policy.

          rule_id: ID of the rule.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return self._delete(
            path_template("/v1/intents/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleDeleteIntentResponse,
        )

    def get(
        self,
        intent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntentResponse:
        """Retrieve an intent by ID.

        Returns the intent details including its current
        status, authorization details, and execution result if applicable.

        Args:
          intent_id: ID of the intent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not intent_id:
            raise ValueError(f"Expected a non-empty value for `intent_id` but received {intent_id!r}")
        return cast(
            IntentResponse,
            self._get(
                path_template("/v1/intents/{intent_id}", intent_id=intent_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, IntentResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def reject(
        self,
        intent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntentResponse:
        """Reject a pending intent, preventing it from being executed.

        Can be called by the
        intent creator (via user token) or with the app secret.

        Args:
          intent_id: ID of the intent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not intent_id:
            raise ValueError(f"Expected a non-empty value for `intent_id` but received {intent_id!r}")
        return cast(
            IntentResponse,
            self._post(
                path_template("/v1/intents/{intent_id}/reject", intent_id=intent_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, IntentResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signTransaction"],
        params: EthereumSignTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signTransaction` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the EVM `eth_sendTransaction` RPC.

          experimental_data_suffix: A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
              bytes).

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `personal_sign` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          signature_options: Options controlling signature production for personal_sign and
              eth_signTypedData_v4.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signTypedData_v4` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          signature_options: Options controlling signature production for personal_sign and
              eth_signTypedData_v4.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["secp256k1_sign"],
        params: EthereumSecp256k1SignRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `secp256k1_sign` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_sign7702Authorization"],
        params: EthereumSign7702AuthorizationRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_sign7702Authorization` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signUserOperation"],
        params: EthereumSignUserOperationRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signUserOperation` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the `wallet_sendCalls` RPC.

          experimental_data_suffix: A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
              bytes).

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signTransaction"],
        params: SolanaSignTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the SVM `signTransaction` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the SVM `signAndSendTransaction` RPC.

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signMessage"],
        params: SolanaSignMessageRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the SVM `signMessage` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["transfer"],
        params: SparkTransferRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `transfer` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getBalance"],
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["transferTokens"],
        params: SparkTransferTokensRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `transferTokens` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getStaticDepositAddress"],
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getClaimStaticDepositQuote"],
        params: SparkGetClaimStaticDepositQuoteRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `getClaimStaticDepositQuote` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["claimStaticDeposit"],
        params: SparkClaimStaticDepositRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `claimStaticDeposit` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["createLightningInvoice"],
        params: SparkCreateLightningInvoiceRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `createLightningInvoice` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["payLightningInvoice"],
        params: SparkPayLightningInvoiceRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `payLightningInvoice` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signMessageWithIdentityKey"],
        params: SparkSignMessageWithIdentityKeyRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `signMessageWithIdentityKey` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["withdraw"],
        params: SparkWithdrawRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `withdraw` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getWithdrawalFeeQuote"],
        params: SparkGetWithdrawalFeeQuoteRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `getWithdrawalFeeQuote` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["tron_signTransaction"],
        params: TronSignTransactionRpcInputParamsParam,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Tron `tron_signTransaction` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["tron_sendTransaction"],
        params: TronSendTransactionRpcInputParamsParam,
        caip2: Caip2 | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Tron `tron_sendTransaction` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        address: str,
        method: Literal["exportPrivateKey"],
        params: PrivateKeyExportInputParam,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Input for exporting a wallet (private key or seed phrase) with HPKE encryption.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def rpc(
        self,
        path_wallet_id: str,
        *,
        address: str,
        method: Literal["exportSeedPhrase"],
        params: SeedPhraseExportInputParam,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Input for exporting a wallet (private key or seed phrase) with HPKE encryption.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["method", "params"], ["caip2", "method", "params"], ["method"], ["address", "method", "params"])
    def rpc(
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
        | PrivateKeyExportInputParam
        | SeedPhraseExportInputParam
        | Omit = omit,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
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
    ) -> RpcIntentResponse:
        if not path_wallet_id:
            raise ValueError(f"Expected a non-empty value for `path_wallet_id` but received {path_wallet_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/intents/wallets/{path_wallet_id}/rpc", path_wallet_id=path_wallet_id),
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
                intent_rpc_params.IntentRpcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RpcIntentResponse,
        )

    def transfer(
        self,
        wallet_id: str,
        *,
        destination: TokenTransferDestinationParam,
        source: TokenTransferSourceParam,
        amount: str | Omit = omit,
        amount_type: AmountType | Omit = omit,
        fee_configuration: FeeConfigurationParam | Omit = omit,
        slippage_bps: int | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferIntentResponse:
        """Create an intent to execute a token transfer via a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

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

          slippage_bps: Maximum allowed slippage in basis points (1 bps = 0.01%). Only applicable for
              cross-chain or cross-asset transfers; omit to use the provider default.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/intents/wallets/{wallet_id}/transfer", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                    "amount": amount,
                    "amount_type": amount_type,
                    "fee_configuration": fee_configuration,
                    "slippage_bps": slippage_bps,
                },
                intent_transfer_params.IntentTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferIntentResponse,
        )

    def update_key_quorum(
        self,
        key_quorum_id: str,
        *,
        authorization_threshold: float | Omit = omit,
        display_name: str | Omit = omit,
        key_quorum_ids: SequenceNotStr[str] | Omit = omit,
        public_keys: SequenceNotStr[str] | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyQuorumIntentResponse:
        """Create an intent to update a key quorum.

        The intent must be authorized by the
        key quorum members before it can be executed.

        Args:
          key_quorum_id: ID of the key quorum.

          authorization_threshold: The number of keys that must sign for an action to be valid. Must be less than
              or equal to total number of key quorum members.

          key_quorum_ids: List of key quorum IDs that should be members of this key quorum. Key quorums
              can only be nested 1 level deep.

          public_keys: List of P-256 public keys of the keys that should be authorized to sign on the
              key quorum, in base64-encoded DER format.

          user_ids: List of user IDs of the users that should be authorized to sign on the key
              quorum.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return self._patch(
            path_template("/v1/intents/key_quorums/{key_quorum_id}", key_quorum_id=key_quorum_id),
            body=maybe_transform(
                {
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                    "key_quorum_ids": key_quorum_ids,
                    "public_keys": public_keys,
                    "user_ids": user_ids,
                },
                intent_update_key_quorum_params.IntentUpdateKeyQuorumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorumIntentResponse,
        )

    def update_policy(
        self,
        policy_id: str,
        *,
        name: str | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        rules: Iterable[PolicyRuleRequestBodyParam] | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyIntentResponse:
        """Create an intent to update a policy.

        The intent must be authorized by the policy
        owner before it can be executed.

        Args:
          policy_id: ID of the policy.

          name: Name to assign to policy.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return self._patch(
            path_template("/v1/intents/policies/{policy_id}", policy_id=policy_id),
            body=maybe_transform(
                {
                    "name": name,
                    "owner": owner,
                    "owner_id": owner_id,
                    "rules": rules,
                },
                intent_update_policy_params.IntentUpdatePolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyIntentResponse,
        )

    def update_policy_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        action: PolicyAction,
        conditions: Iterable[PolicyConditionParam],
        method: PolicyMethod,
        name: str,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleMutateIntentResponse:
        """Create an intent to update a rule on a policy.

        The intent must be authorized by
        the policy owner before it can be executed.

        Args:
          policy_id: ID of the policy.

          rule_id: ID of the rule.

          action: The action to take when a policy rule matches.

          method: Method the rule applies to.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return self._patch(
            path_template("/v1/intents/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            body=maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "method": method,
                    "name": name,
                },
                intent_update_policy_rule_params.IntentUpdatePolicyRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleMutateIntentResponse,
        )

    def update_wallet(
        self,
        wallet_id: str,
        *,
        additional_signers: AdditionalSignerInputParam | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletIntentResponse:
        """Create an intent to update a wallet.

        The intent must be authorized by the wallet
        owner before it can be executed.

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

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return self._patch(
            path_template("/v1/intents/wallets/{wallet_id}", wallet_id=wallet_id),
            body=maybe_transform(
                {
                    "additional_signers": additional_signers,
                    "display_name": display_name,
                    "owner": owner,
                    "owner_id": owner_id,
                    "policy_ids": policy_ids,
                },
                intent_update_wallet_params.IntentUpdateWalletParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletIntentResponse,
        )


class AsyncIntentsResource(AsyncAPIResource):
    """Operations related to authorization intents for wallet actions"""

    @cached_property
    def with_raw_response(self) -> AsyncIntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncIntentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        created_by_id: str | Omit = omit,
        current_user_has_signed: Literal["true", "false"] | Omit = omit,
        cursor: str | Omit = omit,
        intent_type: IntentType | Omit = omit,
        limit: Optional[float] | Omit = omit,
        pending_member_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        sort_by: Literal["created_at_desc", "expires_at_asc", "updated_at_desc"] | Omit = omit,
        status: IntentStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[IntentResponse, AsyncCursor[IntentResponse]]:
        """List intents for an app.

        Returns a paginated list of intents with their current
        status and details.

        Args:
          intent_type: Type of intent.

          status: Current status of an intent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/intents",
            page=AsyncCursor[IntentResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_by_id": created_by_id,
                        "current_user_has_signed": current_user_has_signed,
                        "cursor": cursor,
                        "intent_type": intent_type,
                        "limit": limit,
                        "pending_member_id": pending_member_id,
                        "resource_id": resource_id,
                        "sort_by": sort_by,
                        "status": status,
                    },
                    intent_list_params.IntentListParams,
                ),
            ),
            model=cast(Any, IntentResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def create_policy_rule(
        self,
        policy_id: str,
        *,
        action: PolicyAction,
        conditions: Iterable[PolicyConditionParam],
        method: PolicyMethod,
        name: str,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleMutateIntentResponse:
        """Create an intent to add a rule to a policy.

        The intent must be authorized by the
        policy owner before it can be executed.

        Args:
          policy_id: ID of the policy.

          action: The action to take when a policy rule matches.

          method: Method the rule applies to.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/intents/policies/{policy_id}/rules", policy_id=policy_id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "method": method,
                    "name": name,
                },
                intent_create_policy_rule_params.IntentCreatePolicyRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleMutateIntentResponse,
        )

    async def delete_policy_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteIntentResponse:
        """Create an intent to delete a rule from a policy.

        The intent must be authorized
        by the policy owner before it can be executed.

        Args:
          policy_id: ID of the policy.

          rule_id: ID of the rule.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/intents/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleDeleteIntentResponse,
        )

    async def get(
        self,
        intent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntentResponse:
        """Retrieve an intent by ID.

        Returns the intent details including its current
        status, authorization details, and execution result if applicable.

        Args:
          intent_id: ID of the intent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not intent_id:
            raise ValueError(f"Expected a non-empty value for `intent_id` but received {intent_id!r}")
        return cast(
            IntentResponse,
            await self._get(
                path_template("/v1/intents/{intent_id}", intent_id=intent_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, IntentResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def reject(
        self,
        intent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntentResponse:
        """Reject a pending intent, preventing it from being executed.

        Can be called by the
        intent creator (via user token) or with the app secret.

        Args:
          intent_id: ID of the intent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not intent_id:
            raise ValueError(f"Expected a non-empty value for `intent_id` but received {intent_id!r}")
        return cast(
            IntentResponse,
            await self._post(
                path_template("/v1/intents/{intent_id}/reject", intent_id=intent_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, IntentResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signTransaction"],
        params: EthereumSignTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signTransaction` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the EVM `eth_sendTransaction` RPC.

          experimental_data_suffix: A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
              bytes).

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `personal_sign` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          signature_options: Options controlling signature production for personal_sign and
              eth_signTypedData_v4.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signTypedData_v4` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          signature_options: Options controlling signature production for personal_sign and
              eth_signTypedData_v4.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["secp256k1_sign"],
        params: EthereumSecp256k1SignRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `secp256k1_sign` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_sign7702Authorization"],
        params: EthereumSign7702AuthorizationRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_sign7702Authorization` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["eth_signUserOperation"],
        params: EthereumSignUserOperationRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the EVM `eth_signUserOperation` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the `wallet_sendCalls` RPC.

          experimental_data_suffix: A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
              bytes).

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signTransaction"],
        params: SolanaSignTransactionRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the SVM `signTransaction` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
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
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          params: Parameters for the SVM `signAndSendTransaction` RPC.

          sponsor_options: Options for user-pays gas sponsorship on the RPC endpoint. When provided
              alongside `sponsor: true`, controls which token asset the user pays gas with.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signMessage"],
        params: SolanaSignMessageRpcInputParamsParam,
        address: str | Omit = omit,
        chain_type: Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the SVM `signMessage` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["transfer"],
        params: SparkTransferRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `transfer` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getBalance"],
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["transferTokens"],
        params: SparkTransferTokensRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `transferTokens` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getStaticDepositAddress"],
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getClaimStaticDepositQuote"],
        params: SparkGetClaimStaticDepositQuoteRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `getClaimStaticDepositQuote` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["claimStaticDeposit"],
        params: SparkClaimStaticDepositRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `claimStaticDeposit` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["createLightningInvoice"],
        params: SparkCreateLightningInvoiceRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `createLightningInvoice` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["payLightningInvoice"],
        params: SparkPayLightningInvoiceRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `payLightningInvoice` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["signMessageWithIdentityKey"],
        params: SparkSignMessageWithIdentityKeyRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `signMessageWithIdentityKey` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["withdraw"],
        params: SparkWithdrawRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `withdraw` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["getWithdrawalFeeQuote"],
        params: SparkGetWithdrawalFeeQuoteRpcInputParamsParam,
        network: SparkNetwork | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Spark `getWithdrawalFeeQuote` RPC.

          network: The Spark network.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["tron_signTransaction"],
        params: TronSignTransactionRpcInputParamsParam,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Tron `tron_signTransaction` RPC.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        method: Literal["tron_sendTransaction"],
        params: TronSendTransactionRpcInputParamsParam,
        caip2: Caip2 | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Parameters for the Tron `tron_sendTransaction` RPC.

          caip2: A valid CAIP-2 chain ID (e.g. 'eip155:4217' for Tempo, 'eip155:1' for Ethereum).

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        address: str,
        method: Literal["exportPrivateKey"],
        params: PrivateKeyExportInputParam,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Input for exporting a wallet (private key or seed phrase) with HPKE encryption.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def rpc(
        self,
        path_wallet_id: str,
        *,
        address: str,
        method: Literal["exportSeedPhrase"],
        params: SeedPhraseExportInputParam,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcIntentResponse:
        """Create an intent to execute an RPC method on a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

        Args:
          path_wallet_id: ID of the wallet.

          params: Input for exporting a wallet (private key or seed phrase) with HPKE encryption.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["method", "params"], ["caip2", "method", "params"], ["method"], ["address", "method", "params"])
    async def rpc(
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
        | PrivateKeyExportInputParam
        | SeedPhraseExportInputParam
        | Omit = omit,
        address: str | Omit = omit,
        chain_type: Literal["ethereum"] | Literal["solana"] | Omit = omit,
        body_wallet_id: str | Omit = omit,
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
    ) -> RpcIntentResponse:
        if not path_wallet_id:
            raise ValueError(f"Expected a non-empty value for `path_wallet_id` but received {path_wallet_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/intents/wallets/{path_wallet_id}/rpc", path_wallet_id=path_wallet_id),
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
                intent_rpc_params.IntentRpcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RpcIntentResponse,
        )

    async def transfer(
        self,
        wallet_id: str,
        *,
        destination: TokenTransferDestinationParam,
        source: TokenTransferSourceParam,
        amount: str | Omit = omit,
        amount_type: AmountType | Omit = omit,
        fee_configuration: FeeConfigurationParam | Omit = omit,
        slippage_bps: int | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferIntentResponse:
        """Create an intent to execute a token transfer via a wallet.

        The intent must be
        authorized by either the wallet owner or signers before it can be executed.

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

          slippage_bps: Maximum allowed slippage in basis points (1 bps = 0.01%). Only applicable for
              cross-chain or cross-asset transfers; omit to use the provider default.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/intents/wallets/{wallet_id}/transfer", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                    "amount": amount,
                    "amount_type": amount_type,
                    "fee_configuration": fee_configuration,
                    "slippage_bps": slippage_bps,
                },
                intent_transfer_params.IntentTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferIntentResponse,
        )

    async def update_key_quorum(
        self,
        key_quorum_id: str,
        *,
        authorization_threshold: float | Omit = omit,
        display_name: str | Omit = omit,
        key_quorum_ids: SequenceNotStr[str] | Omit = omit,
        public_keys: SequenceNotStr[str] | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyQuorumIntentResponse:
        """Create an intent to update a key quorum.

        The intent must be authorized by the
        key quorum members before it can be executed.

        Args:
          key_quorum_id: ID of the key quorum.

          authorization_threshold: The number of keys that must sign for an action to be valid. Must be less than
              or equal to total number of key quorum members.

          key_quorum_ids: List of key quorum IDs that should be members of this key quorum. Key quorums
              can only be nested 1 level deep.

          public_keys: List of P-256 public keys of the keys that should be authorized to sign on the
              key quorum, in base64-encoded DER format.

          user_ids: List of user IDs of the users that should be authorized to sign on the key
              quorum.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_quorum_id:
            raise ValueError(f"Expected a non-empty value for `key_quorum_id` but received {key_quorum_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return await self._patch(
            path_template("/v1/intents/key_quorums/{key_quorum_id}", key_quorum_id=key_quorum_id),
            body=await async_maybe_transform(
                {
                    "authorization_threshold": authorization_threshold,
                    "display_name": display_name,
                    "key_quorum_ids": key_quorum_ids,
                    "public_keys": public_keys,
                    "user_ids": user_ids,
                },
                intent_update_key_quorum_params.IntentUpdateKeyQuorumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyQuorumIntentResponse,
        )

    async def update_policy(
        self,
        policy_id: str,
        *,
        name: str | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        rules: Iterable[PolicyRuleRequestBodyParam] | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyIntentResponse:
        """Create an intent to update a policy.

        The intent must be authorized by the policy
        owner before it can be executed.

        Args:
          policy_id: ID of the policy.

          name: Name to assign to policy.

          owner: The owner of the resource, specified as a Privy user ID, a P-256 public key, or
              null to remove the current owner.

          owner_id: The key quorum ID to set as the owner of the resource. If you provide this, do
              not specify an owner.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return await self._patch(
            path_template("/v1/intents/policies/{policy_id}", policy_id=policy_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "owner": owner,
                    "owner_id": owner_id,
                    "rules": rules,
                },
                intent_update_policy_params.IntentUpdatePolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyIntentResponse,
        )

    async def update_policy_rule(
        self,
        rule_id: str,
        *,
        policy_id: str,
        action: PolicyAction,
        conditions: Iterable[PolicyConditionParam],
        method: PolicyMethod,
        name: str,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleMutateIntentResponse:
        """Create an intent to update a rule on a policy.

        The intent must be authorized by
        the policy owner before it can be executed.

        Args:
          policy_id: ID of the policy.

          rule_id: ID of the rule.

          action: The action to take when a policy rule matches.

          method: Method the rule applies to.

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return await self._patch(
            path_template("/v1/intents/policies/{policy_id}/rules/{rule_id}", policy_id=policy_id, rule_id=rule_id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "method": method,
                    "name": name,
                },
                intent_update_policy_rule_params.IntentUpdatePolicyRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleMutateIntentResponse,
        )

    async def update_wallet(
        self,
        wallet_id: str,
        *,
        additional_signers: AdditionalSignerInputParam | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        owner: Optional[OwnerInputParam] | Omit = omit,
        owner_id: Optional[OwnerIDInput] | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        privy_request_expiry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletIntentResponse:
        """Create an intent to update a wallet.

        The intent must be authorized by the wallet
        owner before it can be executed.

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

          privy_request_expiry: Request expiry. Value is a Unix timestamp in milliseconds representing the
              deadline by which the request must be processed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        extra_headers = {**strip_not_given({"privy-request-expiry": privy_request_expiry}), **(extra_headers or {})}
        return await self._patch(
            path_template("/v1/intents/wallets/{wallet_id}", wallet_id=wallet_id),
            body=await async_maybe_transform(
                {
                    "additional_signers": additional_signers,
                    "display_name": display_name,
                    "owner": owner,
                    "owner_id": owner_id,
                    "policy_ids": policy_ids,
                },
                intent_update_wallet_params.IntentUpdateWalletParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletIntentResponse,
        )


class IntentsResourceWithRawResponse:
    def __init__(self, intents: IntentsResource) -> None:
        self._intents = intents

        self.list = to_raw_response_wrapper(
            intents.list,
        )
        self.create_policy_rule = to_raw_response_wrapper(
            intents.create_policy_rule,
        )
        self.delete_policy_rule = to_raw_response_wrapper(
            intents.delete_policy_rule,
        )
        self.get = to_raw_response_wrapper(
            intents.get,
        )
        self.reject = to_raw_response_wrapper(
            intents.reject,
        )
        self.rpc = to_raw_response_wrapper(
            intents.rpc,
        )
        self.transfer = to_raw_response_wrapper(
            intents.transfer,
        )
        self.update_key_quorum = to_raw_response_wrapper(
            intents.update_key_quorum,
        )
        self.update_policy = to_raw_response_wrapper(
            intents.update_policy,
        )
        self.update_policy_rule = to_raw_response_wrapper(
            intents.update_policy_rule,
        )
        self.update_wallet = to_raw_response_wrapper(
            intents.update_wallet,
        )


class AsyncIntentsResourceWithRawResponse:
    def __init__(self, intents: AsyncIntentsResource) -> None:
        self._intents = intents

        self.list = async_to_raw_response_wrapper(
            intents.list,
        )
        self.create_policy_rule = async_to_raw_response_wrapper(
            intents.create_policy_rule,
        )
        self.delete_policy_rule = async_to_raw_response_wrapper(
            intents.delete_policy_rule,
        )
        self.get = async_to_raw_response_wrapper(
            intents.get,
        )
        self.reject = async_to_raw_response_wrapper(
            intents.reject,
        )
        self.rpc = async_to_raw_response_wrapper(
            intents.rpc,
        )
        self.transfer = async_to_raw_response_wrapper(
            intents.transfer,
        )
        self.update_key_quorum = async_to_raw_response_wrapper(
            intents.update_key_quorum,
        )
        self.update_policy = async_to_raw_response_wrapper(
            intents.update_policy,
        )
        self.update_policy_rule = async_to_raw_response_wrapper(
            intents.update_policy_rule,
        )
        self.update_wallet = async_to_raw_response_wrapper(
            intents.update_wallet,
        )


class IntentsResourceWithStreamingResponse:
    def __init__(self, intents: IntentsResource) -> None:
        self._intents = intents

        self.list = to_streamed_response_wrapper(
            intents.list,
        )
        self.create_policy_rule = to_streamed_response_wrapper(
            intents.create_policy_rule,
        )
        self.delete_policy_rule = to_streamed_response_wrapper(
            intents.delete_policy_rule,
        )
        self.get = to_streamed_response_wrapper(
            intents.get,
        )
        self.reject = to_streamed_response_wrapper(
            intents.reject,
        )
        self.rpc = to_streamed_response_wrapper(
            intents.rpc,
        )
        self.transfer = to_streamed_response_wrapper(
            intents.transfer,
        )
        self.update_key_quorum = to_streamed_response_wrapper(
            intents.update_key_quorum,
        )
        self.update_policy = to_streamed_response_wrapper(
            intents.update_policy,
        )
        self.update_policy_rule = to_streamed_response_wrapper(
            intents.update_policy_rule,
        )
        self.update_wallet = to_streamed_response_wrapper(
            intents.update_wallet,
        )


class AsyncIntentsResourceWithStreamingResponse:
    def __init__(self, intents: AsyncIntentsResource) -> None:
        self._intents = intents

        self.list = async_to_streamed_response_wrapper(
            intents.list,
        )
        self.create_policy_rule = async_to_streamed_response_wrapper(
            intents.create_policy_rule,
        )
        self.delete_policy_rule = async_to_streamed_response_wrapper(
            intents.delete_policy_rule,
        )
        self.get = async_to_streamed_response_wrapper(
            intents.get,
        )
        self.reject = async_to_streamed_response_wrapper(
            intents.reject,
        )
        self.rpc = async_to_streamed_response_wrapper(
            intents.rpc,
        )
        self.transfer = async_to_streamed_response_wrapper(
            intents.transfer,
        )
        self.update_key_quorum = async_to_streamed_response_wrapper(
            intents.update_key_quorum,
        )
        self.update_policy = async_to_streamed_response_wrapper(
            intents.update_policy,
        )
        self.update_policy_rule = async_to_streamed_response_wrapper(
            intents.update_policy_rule,
        )
        self.update_wallet = async_to_streamed_response_wrapper(
            intents.update_wallet,
        )
