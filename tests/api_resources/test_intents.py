# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    IntentResponse,
    RpcIntentResponse,
    PolicyIntentResponse,
    WalletIntentResponse,
    TransferIntentResponse,
    KeyQuorumIntentResponse,
    RuleDeleteIntentResponse,
    RuleMutateIntentResponse,
)
from tests.utils import assert_matches_type
from privy.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        intent = client.intents.list()
        assert_matches_type(SyncCursor[IntentResponse], intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PrivyAPI) -> None:
        intent = client.intents.list(
            created_by_id="created_by_id",
            current_user_has_signed="true",
            cursor="x",
            intent_type="KEY_QUORUM",
            limit=100,
            pending_member_id="pending_member_id",
            resource_id="resource_id",
            sort_by="created_at_desc",
            status="pending",
        )
        assert_matches_type(SyncCursor[IntentResponse], intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(SyncCursor[IntentResponse], intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(SyncCursor[IntentResponse], intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_policy_rule(self, client: PrivyAPI) -> None:
        intent = client.intents.create_policy_rule(
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        )
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_policy_rule_with_all_params(self, client: PrivyAPI) -> None:
        intent = client.intents.create_policy_rule(
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_policy_rule(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.create_policy_rule(
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_policy_rule(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.create_policy_rule(
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_policy_rule(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.intents.with_raw_response.create_policy_rule(
                policy_id="",
                action="ALLOW",
                conditions=[
                    {
                        "field": "to",
                        "field_source": "ethereum_transaction",
                        "operator": "eq",
                        "value": "string",
                    }
                ],
                method="eth_sendTransaction",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_policy_rule(self, client: PrivyAPI) -> None:
        intent = client.intents.delete_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
        )
        assert_matches_type(RuleDeleteIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_policy_rule_with_all_params(self, client: PrivyAPI) -> None:
        intent = client.intents.delete_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RuleDeleteIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_policy_rule(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.delete_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RuleDeleteIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_policy_rule(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.delete_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RuleDeleteIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_policy_rule(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.intents.with_raw_response.delete_policy_rule(
                rule_id="rule_id",
                policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.intents.with_raw_response.delete_policy_rule(
                rule_id="",
                policy_id="policy_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        intent = client.intents.get(
            "intent_id",
        )
        assert_matches_type(IntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.get(
            "intent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(IntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.get(
            "intent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(IntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `intent_id` but received ''"):
            client.intents.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reject(self, client: PrivyAPI) -> None:
        intent = client.intents.reject(
            "intent_id",
        )
        assert_matches_type(IntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reject(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.reject(
            "intent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(IntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reject(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.reject(
            "intent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(IntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reject(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `intent_id` but received ''"):
            client.intents.with_raw_response.reject(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_1(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_1(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTransaction",
            params={
                "transaction": {
                    "authorization_list": [
                        {
                            "chain_id": "string",
                            "contract": "contract",
                            "nonce": "string",
                            "r": "string",
                            "s": "string",
                            "y_parity": 0,
                        }
                    ],
                    "chain_id": "string",
                    "data": "string",
                    "from": "from",
                    "gas_limit": "string",
                    "gas_price": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "to": "to",
                    "type": 0,
                    "value": "string",
                }
            },
            address="address",
            chain_type="ethereum",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_1(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_1(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_1(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="eth_signTransaction",
                params={"transaction": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_2(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_2(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={
                "transaction": {
                    "authorization_list": [
                        {
                            "chain_id": "string",
                            "contract": "contract",
                            "nonce": "string",
                            "r": "string",
                            "s": "string",
                            "y_parity": 0,
                        }
                    ],
                    "chain_id": "string",
                    "data": "string",
                    "from": "from",
                    "gas_limit": "string",
                    "gas_price": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "to": "to",
                    "type": 0,
                    "value": "string",
                }
            },
            address="address",
            chain_type="ethereum",
            experimental_data_suffix="string",
            reference_id="x",
            sponsor=True,
            sponsor_options={"asset": "string"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_2(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_2(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_2(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="eth_sendTransaction",
                params={"transaction": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_3(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_3(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
            address="address",
            caip2="-l-f12-k:_--l__36_",
            chain_type="ethereum",
            signature_options={"type": "ecdsa"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_3(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_3(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_3(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="personal_sign",
                params={
                    "encoding": "utf-8",
                    "message": "message",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_4(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_4(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
            address="address",
            caip2="-l-f12-k:_--l__36_",
            chain_type="ethereum",
            signature_options={"type": "ecdsa"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_4(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_4(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_4(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="eth_signTypedData_v4",
                params={
                    "typed_data": {
                        "domain": {"foo": "bar"},
                        "message": {"foo": "bar"},
                        "primary_type": "primary_type",
                        "types": {
                            "foo": [
                                {
                                    "name": "name",
                                    "type": "type",
                                }
                            ]
                        },
                    }
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_5(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "string"},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_5(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "string"},
            address="address",
            chain_type="ethereum",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_5(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_5(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_5(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="secp256k1_sign",
                params={"hash": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_6(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_6(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
                "executor": "self",
                "nonce": "string",
            },
            address="address",
            chain_type="ethereum",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_6(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_6(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_6(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="eth_sign7702Authorization",
                params={
                    "chain_id": "string",
                    "contract": "contract",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_7(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signUserOperation",
            params={
                "chain_id": "string",
                "contract": "contract",
                "user_operation": {
                    "call_data": "string",
                    "call_gas_limit": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "pre_verification_gas": "string",
                    "sender": "sender",
                    "verification_gas_limit": "string",
                },
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_7(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signUserOperation",
            params={
                "chain_id": "string",
                "contract": "contract",
                "user_operation": {
                    "call_data": "string",
                    "call_gas_limit": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "pre_verification_gas": "string",
                    "sender": "sender",
                    "verification_gas_limit": "string",
                    "factory": "factory",
                    "factory_data": "string",
                    "paymaster": "paymaster",
                    "paymaster_data": "string",
                    "paymaster_post_op_gas_limit": "string",
                    "paymaster_verification_gas_limit": "string",
                },
            },
            address="address",
            chain_type="ethereum",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_7(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signUserOperation",
            params={
                "chain_id": "string",
                "contract": "contract",
                "user_operation": {
                    "call_data": "string",
                    "call_gas_limit": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "pre_verification_gas": "string",
                    "sender": "sender",
                    "verification_gas_limit": "string",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_7(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signUserOperation",
            params={
                "chain_id": "string",
                "contract": "contract",
                "user_operation": {
                    "call_data": "string",
                    "call_gas_limit": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "pre_verification_gas": "string",
                    "sender": "sender",
                    "verification_gas_limit": "string",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_7(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="eth_signUserOperation",
                params={
                    "chain_id": "string",
                    "contract": "contract",
                    "user_operation": {
                        "call_data": "string",
                        "call_gas_limit": "string",
                        "max_fee_per_gas": "string",
                        "max_priority_fee_per_gas": "string",
                        "nonce": "string",
                        "pre_verification_gas": "string",
                        "sender": "sender",
                        "verification_gas_limit": "string",
                    },
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_8(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="wallet_sendCalls",
            params={"calls": [{"to": "to"}]},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_8(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="wallet_sendCalls",
            params={
                "calls": [
                    {
                        "to": "to",
                        "data": "string",
                        "value": "string",
                    }
                ]
            },
            address="address",
            chain_type="ethereum",
            experimental_data_suffix="string",
            sponsor=True,
            sponsor_options={"asset": "string"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_8(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="wallet_sendCalls",
            params={"calls": [{"to": "to"}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_8(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="wallet_sendCalls",
            params={"calls": [{"to": "to"}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_8(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="wallet_sendCalls",
                params={"calls": [{"to": "to"}]},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_9(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="aptos_signTransaction",
            params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_9(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="aptos_signTransaction",
            params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_9(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="aptos_signTransaction",
            params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_9(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="aptos_signTransaction",
            params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_9(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="aptos_signTransaction",
                params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_10(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_10(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
            address="address",
            chain_type="solana",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_10(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_10(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_10(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="signTransaction",
                params={
                    "encoding": "base64",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_11(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_11(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
            address="address",
            chain_type="solana",
            optimistic_broadcast=True,
            reference_id="x",
            sponsor=True,
            sponsor_options={"asset": "string"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_11(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_11(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_11(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="signAndSendTransaction",
                params={
                    "encoding": "base64",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_12(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_12(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
            address="address",
            chain_type="solana",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_12(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_12(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_12(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="signMessage",
                params={
                    "encoding": "base64",
                    "message": "message",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_13(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="transfer",
            params={
                "amount_sats": 0,
                "receiver_spark_address": "receiver_spark_address",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_13(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="transfer",
            params={
                "amount_sats": 0,
                "receiver_spark_address": "receiver_spark_address",
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_13(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="transfer",
            params={
                "amount_sats": 0,
                "receiver_spark_address": "receiver_spark_address",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_13(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="transfer",
            params={
                "amount_sats": 0,
                "receiver_spark_address": "receiver_spark_address",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_13(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="transfer",
                params={
                    "amount_sats": 0,
                    "receiver_spark_address": "receiver_spark_address",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_14(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getBalance",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_14(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getBalance",
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_14(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="getBalance",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_14(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="getBalance",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_14(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="getBalance",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_15(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="transferTokens",
            params={
                "receiver_spark_address": "receiver_spark_address",
                "token_amount": 0,
                "token_identifier": "token_identifier",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_15(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="transferTokens",
            params={
                "receiver_spark_address": "receiver_spark_address",
                "token_amount": 0,
                "token_identifier": "token_identifier",
                "output_selection_strategy": "SMALL_FIRST",
                "selected_outputs": [
                    {
                        "previous_transaction_hash": "previous_transaction_hash",
                        "previous_transaction_vout": 0,
                        "output": {
                            "owner_public_key": "owner_public_key",
                            "token_amount": "token_amount",
                            "id": "id",
                            "revocation_commitment": "revocation_commitment",
                            "token_identifier": "token_identifier",
                            "token_public_key": "token_public_key",
                            "withdraw_bond_sats": 0,
                            "withdraw_relative_block_locktime": 0,
                        },
                    }
                ],
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_15(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="transferTokens",
            params={
                "receiver_spark_address": "receiver_spark_address",
                "token_amount": 0,
                "token_identifier": "token_identifier",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_15(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="transferTokens",
            params={
                "receiver_spark_address": "receiver_spark_address",
                "token_amount": 0,
                "token_identifier": "token_identifier",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_15(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="transferTokens",
                params={
                    "receiver_spark_address": "receiver_spark_address",
                    "token_amount": 0,
                    "token_identifier": "token_identifier",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_16(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getStaticDepositAddress",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_16(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getStaticDepositAddress",
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_16(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="getStaticDepositAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_16(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="getStaticDepositAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_16(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="getStaticDepositAddress",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_17(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getClaimStaticDepositQuote",
            params={"transaction_id": "transaction_id"},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_17(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getClaimStaticDepositQuote",
            params={
                "transaction_id": "transaction_id",
                "output_index": 0,
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_17(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="getClaimStaticDepositQuote",
            params={"transaction_id": "transaction_id"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_17(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="getClaimStaticDepositQuote",
            params={"transaction_id": "transaction_id"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_17(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="getClaimStaticDepositQuote",
                params={"transaction_id": "transaction_id"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_18(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="claimStaticDeposit",
            params={
                "credit_amount_sats": 0,
                "signature": "signature",
                "transaction_id": "transaction_id",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_18(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="claimStaticDeposit",
            params={
                "credit_amount_sats": 0,
                "signature": "signature",
                "transaction_id": "transaction_id",
                "output_index": 0,
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_18(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="claimStaticDeposit",
            params={
                "credit_amount_sats": 0,
                "signature": "signature",
                "transaction_id": "transaction_id",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_18(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="claimStaticDeposit",
            params={
                "credit_amount_sats": 0,
                "signature": "signature",
                "transaction_id": "transaction_id",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_18(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="claimStaticDeposit",
                params={
                    "credit_amount_sats": 0,
                    "signature": "signature",
                    "transaction_id": "transaction_id",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_19(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="createLightningInvoice",
            params={"amount_sats": 0},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_19(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="createLightningInvoice",
            params={
                "amount_sats": 0,
                "description_hash": "description_hash",
                "expiry_seconds": 0,
                "include_spark_address": True,
                "memo": "memo",
                "receiver_identity_pubkey": "receiver_identity_pubkey",
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_19(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="createLightningInvoice",
            params={"amount_sats": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_19(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="createLightningInvoice",
            params={"amount_sats": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_19(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="createLightningInvoice",
                params={"amount_sats": 0},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_20(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="payLightningInvoice",
            params={
                "invoice": "invoice",
                "max_fee_sats": 0,
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_20(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="payLightningInvoice",
            params={
                "invoice": "invoice",
                "max_fee_sats": 0,
                "amount_sats_to_send": 0,
                "prefer_spark": True,
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_20(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="payLightningInvoice",
            params={
                "invoice": "invoice",
                "max_fee_sats": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_20(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="payLightningInvoice",
            params={
                "invoice": "invoice",
                "max_fee_sats": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_20(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="payLightningInvoice",
                params={
                    "invoice": "invoice",
                    "max_fee_sats": 0,
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_21(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signMessageWithIdentityKey",
            params={"message": "message"},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_21(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signMessageWithIdentityKey",
            params={
                "message": "message",
                "compact": True,
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_21(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="signMessageWithIdentityKey",
            params={"message": "message"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_21(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="signMessageWithIdentityKey",
            params={"message": "message"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_21(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="signMessageWithIdentityKey",
                params={"message": "message"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_22(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="withdraw",
            params={
                "exit_speed": "FAST",
                "onchain_address": "onchain_address",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_22(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="withdraw",
            params={
                "exit_speed": "FAST",
                "onchain_address": "onchain_address",
                "amount_sats": 0,
                "deduct_fee_from_withdrawal_amount": True,
                "fee_amount_sats": 0,
                "fee_quote_id": "fee_quote_id",
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_22(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="withdraw",
            params={
                "exit_speed": "FAST",
                "onchain_address": "onchain_address",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_22(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="withdraw",
            params={
                "exit_speed": "FAST",
                "onchain_address": "onchain_address",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_22(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="withdraw",
                params={
                    "exit_speed": "FAST",
                    "onchain_address": "onchain_address",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_23(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getWithdrawalFeeQuote",
            params={
                "amount_sats": 0,
                "onchain_address": "onchain_address",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_23(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getWithdrawalFeeQuote",
            params={
                "amount_sats": 0,
                "onchain_address": "onchain_address",
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_23(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="getWithdrawalFeeQuote",
            params={
                "amount_sats": 0,
                "onchain_address": "onchain_address",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_23(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="getWithdrawalFeeQuote",
            params={
                "amount_sats": 0,
                "onchain_address": "onchain_address",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_23(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="getWithdrawalFeeQuote",
                params={
                    "amount_sats": 0,
                    "onchain_address": "onchain_address",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_24(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="tron_signTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "expiration": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                }
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_24(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="tron_signTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "expiration": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                    "data": "d6BC",
                    "fee_limit": 0,
                    "timestamp": 0,
                }
            },
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_24(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="tron_signTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "expiration": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_24(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="tron_signTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "expiration": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_24(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="tron_signTransaction",
                params={
                    "raw_data": {
                        "contract": [
                            {
                                "amount": 1,
                                "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                                "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                                "type": "TransferContract",
                            }
                        ],
                        "expiration": 0,
                        "ref_block_bytes": "E1CB",
                        "ref_block_hash": "E1CB97d8EBbDbaAa",
                    }
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_25(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="tron_sendTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ]
                }
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_25(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="tron_sendTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "data": "d6BC",
                    "expiration": 0,
                    "fee_limit": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                    "timestamp": 0,
                },
                "reference_id": "reference_id",
            },
            caip2="-l-f12-k:_--l__36_",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_25(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="tron_sendTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ]
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_25(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="tron_sendTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ]
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_25(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="tron_sendTransaction",
                params={
                    "raw_data": {
                        "contract": [
                            {
                                "amount": 1,
                                "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                                "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                                "type": "TransferContract",
                            }
                        ]
                    }
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_26(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="xrpl_signTransaction",
            params={
                "encoding": "hex",
                "transaction": "transaction",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_26(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            method="xrpl_signTransaction",
            params={
                "encoding": "hex",
                "transaction": "transaction",
            },
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_26(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="xrpl_signTransaction",
            params={
                "encoding": "hex",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_26(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="xrpl_signTransaction",
            params={
                "encoding": "hex",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_26(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="xrpl_signTransaction",
                params={
                    "encoding": "hex",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_27(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportPrivateKey",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_27(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportPrivateKey",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
                "export_seed_phrase": True,
                "export_type": "display",
            },
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_27(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportPrivateKey",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_27(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportPrivateKey",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_27(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                address="address",
                method="exportPrivateKey",
                params={
                    "encryption_type": "HPKE",
                    "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_overload_28(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportSeedPhrase",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rpc_with_all_params_overload_28(self, client: PrivyAPI) -> None:
        intent = client.intents.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportSeedPhrase",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
                "export_seed_phrase": True,
                "export_type": "display",
            },
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rpc_overload_28(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportSeedPhrase",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rpc_overload_28(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportSeedPhrase",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rpc_overload_28(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            client.intents.with_raw_response.rpc(
                path_wallet_id="",
                address="address",
                method="exportSeedPhrase",
                params={
                    "encryption_type": "HPKE",
                    "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transfer(self, client: PrivyAPI) -> None:
        intent = client.intents.transfer(
            wallet_id="wallet_id",
            destination={"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
            source={
                "asset": "usdc",
                "chain": "base",
            },
        )
        assert_matches_type(TransferIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transfer_with_all_params(self, client: PrivyAPI) -> None:
        intent = client.intents.transfer(
            wallet_id="wallet_id",
            destination={
                "address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2",
                "asset": "asset",
                "chain": "chain",
            },
            source={
                "asset": "usdc",
                "chain": "base",
                "amount": "10.5",
            },
            amount="10.5",
            amount_type="exact_input",
            fee_configuration={
                "type": "total_fee_bps",
                "value": 50,
            },
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            reference_id="x",
            slippage_bps=0,
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(TransferIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_transfer(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.transfer(
            wallet_id="wallet_id",
            destination={"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
            source={
                "asset": "usdc",
                "chain": "base",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(TransferIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_transfer(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.transfer(
            wallet_id="wallet_id",
            destination={"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
            source={
                "asset": "usdc",
                "chain": "base",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(TransferIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_transfer(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.intents.with_raw_response.transfer(
                wallet_id="",
                destination={"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
                source={
                    "asset": "usdc",
                    "chain": "base",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_key_quorum(self, client: PrivyAPI) -> None:
        intent = client.intents.update_key_quorum(
            key_quorum_id="key_quorum_id",
        )
        assert_matches_type(KeyQuorumIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_key_quorum_with_all_params(self, client: PrivyAPI) -> None:
        intent = client.intents.update_key_quorum(
            key_quorum_id="key_quorum_id",
            authorization_threshold=0,
            display_name="display_name",
            key_quorum_ids=["string"],
            public_keys=["string"],
            user_ids=["string"],
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(KeyQuorumIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_key_quorum(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.update_key_quorum(
            key_quorum_id="key_quorum_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(KeyQuorumIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_key_quorum(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.update_key_quorum(
            key_quorum_id="key_quorum_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(KeyQuorumIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_key_quorum(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_quorum_id` but received ''"):
            client.intents.with_raw_response.update_key_quorum(
                key_quorum_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_policy(self, client: PrivyAPI) -> None:
        intent = client.intents.update_policy(
            policy_id="policy_id",
        )
        assert_matches_type(PolicyIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_policy_with_all_params(self, client: PrivyAPI) -> None:
        intent = client.intents.update_policy(
            policy_id="policy_id",
            name="x",
            owner={"user_id": "user_id"},
            owner_id="string",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "string",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "x",
                }
            ],
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(PolicyIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_policy(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.update_policy(
            policy_id="policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(PolicyIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_policy(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.update_policy(
            policy_id="policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(PolicyIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_policy(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.intents.with_raw_response.update_policy(
                policy_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_policy_rule(self, client: PrivyAPI) -> None:
        intent = client.intents.update_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        )
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_policy_rule_with_all_params(self, client: PrivyAPI) -> None:
        intent = client.intents.update_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_policy_rule(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.update_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_policy_rule(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.update_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_policy_rule(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.intents.with_raw_response.update_policy_rule(
                rule_id="rule_id",
                policy_id="",
                action="ALLOW",
                conditions=[
                    {
                        "field": "to",
                        "field_source": "ethereum_transaction",
                        "operator": "eq",
                        "value": "string",
                    }
                ],
                method="eth_sendTransaction",
                name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.intents.with_raw_response.update_policy_rule(
                rule_id="",
                policy_id="policy_id",
                action="ALLOW",
                conditions=[
                    {
                        "field": "to",
                        "field_source": "ethereum_transaction",
                        "operator": "eq",
                        "value": "string",
                    }
                ],
                method="eth_sendTransaction",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_wallet(self, client: PrivyAPI) -> None:
        intent = client.intents.update_wallet(
            wallet_id="wallet_id",
        )
        assert_matches_type(WalletIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_wallet_with_all_params(self, client: PrivyAPI) -> None:
        intent = client.intents.update_wallet(
            wallet_id="wallet_id",
            additional_signers=[
                {
                    "signer_id": "string",
                    "override_policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                }
            ],
            display_name="display_name",
            owner={"user_id": "user_id"},
            owner_id="string",
            policy_ids=["xxxxxxxxxxxxxxxxxxxxxxxx"],
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(WalletIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_wallet(self, client: PrivyAPI) -> None:
        response = client.intents.with_raw_response.update_wallet(
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = response.parse()
        assert_matches_type(WalletIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_wallet(self, client: PrivyAPI) -> None:
        with client.intents.with_streaming_response.update_wallet(
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = response.parse()
            assert_matches_type(WalletIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_wallet(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.intents.with_raw_response.update_wallet(
                wallet_id="",
            )


class TestAsyncIntents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.list()
        assert_matches_type(AsyncCursor[IntentResponse], intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.list(
            created_by_id="created_by_id",
            current_user_has_signed="true",
            cursor="x",
            intent_type="KEY_QUORUM",
            limit=100,
            pending_member_id="pending_member_id",
            resource_id="resource_id",
            sort_by="created_at_desc",
            status="pending",
        )
        assert_matches_type(AsyncCursor[IntentResponse], intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(AsyncCursor[IntentResponse], intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(AsyncCursor[IntentResponse], intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.create_policy_rule(
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        )
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_policy_rule_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.create_policy_rule(
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.create_policy_rule(
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.create_policy_rule(
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.intents.with_raw_response.create_policy_rule(
                policy_id="",
                action="ALLOW",
                conditions=[
                    {
                        "field": "to",
                        "field_source": "ethereum_transaction",
                        "operator": "eq",
                        "value": "string",
                    }
                ],
                method="eth_sendTransaction",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.delete_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
        )
        assert_matches_type(RuleDeleteIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_policy_rule_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.delete_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RuleDeleteIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.delete_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RuleDeleteIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.delete_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RuleDeleteIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.intents.with_raw_response.delete_policy_rule(
                rule_id="rule_id",
                policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.intents.with_raw_response.delete_policy_rule(
                rule_id="",
                policy_id="policy_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.get(
            "intent_id",
        )
        assert_matches_type(IntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.get(
            "intent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(IntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.get(
            "intent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(IntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `intent_id` but received ''"):
            await async_client.intents.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reject(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.reject(
            "intent_id",
        )
        assert_matches_type(IntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reject(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.reject(
            "intent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(IntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reject(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.reject(
            "intent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(IntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reject(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `intent_id` but received ''"):
            await async_client.intents.with_raw_response.reject(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTransaction",
            params={
                "transaction": {
                    "authorization_list": [
                        {
                            "chain_id": "string",
                            "contract": "contract",
                            "nonce": "string",
                            "r": "string",
                            "s": "string",
                            "y_parity": 0,
                        }
                    ],
                    "chain_id": "string",
                    "data": "string",
                    "from": "from",
                    "gas_limit": "string",
                    "gas_price": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "to": "to",
                    "type": 0,
                    "value": "string",
                }
            },
            address="address",
            chain_type="ethereum",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="eth_signTransaction",
                params={"transaction": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={
                "transaction": {
                    "authorization_list": [
                        {
                            "chain_id": "string",
                            "contract": "contract",
                            "nonce": "string",
                            "r": "string",
                            "s": "string",
                            "y_parity": 0,
                        }
                    ],
                    "chain_id": "string",
                    "data": "string",
                    "from": "from",
                    "gas_limit": "string",
                    "gas_price": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "to": "to",
                    "type": 0,
                    "value": "string",
                }
            },
            address="address",
            chain_type="ethereum",
            experimental_data_suffix="string",
            reference_id="x",
            sponsor=True,
            sponsor_options={"asset": "string"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="eth_sendTransaction",
                params={"transaction": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
            address="address",
            caip2="-l-f12-k:_--l__36_",
            chain_type="ethereum",
            signature_options={"type": "ecdsa"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="personal_sign",
                params={
                    "encoding": "utf-8",
                    "message": "message",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
            address="address",
            caip2="-l-f12-k:_--l__36_",
            chain_type="ethereum",
            signature_options={"type": "ecdsa"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="eth_signTypedData_v4",
                params={
                    "typed_data": {
                        "domain": {"foo": "bar"},
                        "message": {"foo": "bar"},
                        "primary_type": "primary_type",
                        "types": {
                            "foo": [
                                {
                                    "name": "name",
                                    "type": "type",
                                }
                            ]
                        },
                    }
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "string"},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "string"},
            address="address",
            chain_type="ethereum",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="secp256k1_sign",
                params={"hash": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
                "executor": "self",
                "nonce": "string",
            },
            address="address",
            chain_type="ethereum",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="eth_sign7702Authorization",
                params={
                    "chain_id": "string",
                    "contract": "contract",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signUserOperation",
            params={
                "chain_id": "string",
                "contract": "contract",
                "user_operation": {
                    "call_data": "string",
                    "call_gas_limit": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "pre_verification_gas": "string",
                    "sender": "sender",
                    "verification_gas_limit": "string",
                },
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="eth_signUserOperation",
            params={
                "chain_id": "string",
                "contract": "contract",
                "user_operation": {
                    "call_data": "string",
                    "call_gas_limit": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "pre_verification_gas": "string",
                    "sender": "sender",
                    "verification_gas_limit": "string",
                    "factory": "factory",
                    "factory_data": "string",
                    "paymaster": "paymaster",
                    "paymaster_data": "string",
                    "paymaster_post_op_gas_limit": "string",
                    "paymaster_verification_gas_limit": "string",
                },
            },
            address="address",
            chain_type="ethereum",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signUserOperation",
            params={
                "chain_id": "string",
                "contract": "contract",
                "user_operation": {
                    "call_data": "string",
                    "call_gas_limit": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "pre_verification_gas": "string",
                    "sender": "sender",
                    "verification_gas_limit": "string",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="eth_signUserOperation",
            params={
                "chain_id": "string",
                "contract": "contract",
                "user_operation": {
                    "call_data": "string",
                    "call_gas_limit": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "pre_verification_gas": "string",
                    "sender": "sender",
                    "verification_gas_limit": "string",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="eth_signUserOperation",
                params={
                    "chain_id": "string",
                    "contract": "contract",
                    "user_operation": {
                        "call_data": "string",
                        "call_gas_limit": "string",
                        "max_fee_per_gas": "string",
                        "max_priority_fee_per_gas": "string",
                        "nonce": "string",
                        "pre_verification_gas": "string",
                        "sender": "sender",
                        "verification_gas_limit": "string",
                    },
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="wallet_sendCalls",
            params={"calls": [{"to": "to"}]},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="wallet_sendCalls",
            params={
                "calls": [
                    {
                        "to": "to",
                        "data": "string",
                        "value": "string",
                    }
                ]
            },
            address="address",
            chain_type="ethereum",
            experimental_data_suffix="string",
            sponsor=True,
            sponsor_options={"asset": "string"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="wallet_sendCalls",
            params={"calls": [{"to": "to"}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="wallet_sendCalls",
            params={"calls": [{"to": "to"}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="wallet_sendCalls",
                params={"calls": [{"to": "to"}]},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="aptos_signTransaction",
            params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="aptos_signTransaction",
            params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="aptos_signTransaction",
            params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="aptos_signTransaction",
            params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="aptos_signTransaction",
                params={"transaction": "0xd6BCe0d7D40E9dF64a2Af4B3"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_10(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_10(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
            address="address",
            chain_type="solana",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_10(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_10(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_10(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="signTransaction",
                params={
                    "encoding": "base64",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_11(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_11(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
            address="address",
            chain_type="solana",
            optimistic_broadcast=True,
            reference_id="x",
            sponsor=True,
            sponsor_options={"asset": "string"},
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_11(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_11(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_11(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="signAndSendTransaction",
                params={
                    "encoding": "base64",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_12(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_12(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
            address="address",
            chain_type="solana",
            body_wallet_id="wallet_id",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_12(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_12(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_12(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="signMessage",
                params={
                    "encoding": "base64",
                    "message": "message",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_13(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="transfer",
            params={
                "amount_sats": 0,
                "receiver_spark_address": "receiver_spark_address",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_13(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="transfer",
            params={
                "amount_sats": 0,
                "receiver_spark_address": "receiver_spark_address",
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_13(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="transfer",
            params={
                "amount_sats": 0,
                "receiver_spark_address": "receiver_spark_address",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_13(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="transfer",
            params={
                "amount_sats": 0,
                "receiver_spark_address": "receiver_spark_address",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_13(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="transfer",
                params={
                    "amount_sats": 0,
                    "receiver_spark_address": "receiver_spark_address",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_14(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getBalance",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_14(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getBalance",
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_14(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="getBalance",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_14(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="getBalance",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_14(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="getBalance",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_15(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="transferTokens",
            params={
                "receiver_spark_address": "receiver_spark_address",
                "token_amount": 0,
                "token_identifier": "token_identifier",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_15(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="transferTokens",
            params={
                "receiver_spark_address": "receiver_spark_address",
                "token_amount": 0,
                "token_identifier": "token_identifier",
                "output_selection_strategy": "SMALL_FIRST",
                "selected_outputs": [
                    {
                        "previous_transaction_hash": "previous_transaction_hash",
                        "previous_transaction_vout": 0,
                        "output": {
                            "owner_public_key": "owner_public_key",
                            "token_amount": "token_amount",
                            "id": "id",
                            "revocation_commitment": "revocation_commitment",
                            "token_identifier": "token_identifier",
                            "token_public_key": "token_public_key",
                            "withdraw_bond_sats": 0,
                            "withdraw_relative_block_locktime": 0,
                        },
                    }
                ],
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_15(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="transferTokens",
            params={
                "receiver_spark_address": "receiver_spark_address",
                "token_amount": 0,
                "token_identifier": "token_identifier",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_15(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="transferTokens",
            params={
                "receiver_spark_address": "receiver_spark_address",
                "token_amount": 0,
                "token_identifier": "token_identifier",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_15(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="transferTokens",
                params={
                    "receiver_spark_address": "receiver_spark_address",
                    "token_amount": 0,
                    "token_identifier": "token_identifier",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_16(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getStaticDepositAddress",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_16(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getStaticDepositAddress",
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_16(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="getStaticDepositAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_16(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="getStaticDepositAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_16(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="getStaticDepositAddress",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_17(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getClaimStaticDepositQuote",
            params={"transaction_id": "transaction_id"},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_17(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getClaimStaticDepositQuote",
            params={
                "transaction_id": "transaction_id",
                "output_index": 0,
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_17(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="getClaimStaticDepositQuote",
            params={"transaction_id": "transaction_id"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_17(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="getClaimStaticDepositQuote",
            params={"transaction_id": "transaction_id"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_17(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="getClaimStaticDepositQuote",
                params={"transaction_id": "transaction_id"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_18(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="claimStaticDeposit",
            params={
                "credit_amount_sats": 0,
                "signature": "signature",
                "transaction_id": "transaction_id",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_18(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="claimStaticDeposit",
            params={
                "credit_amount_sats": 0,
                "signature": "signature",
                "transaction_id": "transaction_id",
                "output_index": 0,
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_18(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="claimStaticDeposit",
            params={
                "credit_amount_sats": 0,
                "signature": "signature",
                "transaction_id": "transaction_id",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_18(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="claimStaticDeposit",
            params={
                "credit_amount_sats": 0,
                "signature": "signature",
                "transaction_id": "transaction_id",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_18(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="claimStaticDeposit",
                params={
                    "credit_amount_sats": 0,
                    "signature": "signature",
                    "transaction_id": "transaction_id",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_19(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="createLightningInvoice",
            params={"amount_sats": 0},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_19(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="createLightningInvoice",
            params={
                "amount_sats": 0,
                "description_hash": "description_hash",
                "expiry_seconds": 0,
                "include_spark_address": True,
                "memo": "memo",
                "receiver_identity_pubkey": "receiver_identity_pubkey",
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_19(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="createLightningInvoice",
            params={"amount_sats": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_19(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="createLightningInvoice",
            params={"amount_sats": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_19(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="createLightningInvoice",
                params={"amount_sats": 0},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_20(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="payLightningInvoice",
            params={
                "invoice": "invoice",
                "max_fee_sats": 0,
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_20(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="payLightningInvoice",
            params={
                "invoice": "invoice",
                "max_fee_sats": 0,
                "amount_sats_to_send": 0,
                "prefer_spark": True,
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_20(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="payLightningInvoice",
            params={
                "invoice": "invoice",
                "max_fee_sats": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_20(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="payLightningInvoice",
            params={
                "invoice": "invoice",
                "max_fee_sats": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_20(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="payLightningInvoice",
                params={
                    "invoice": "invoice",
                    "max_fee_sats": 0,
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_21(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signMessageWithIdentityKey",
            params={"message": "message"},
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_21(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="signMessageWithIdentityKey",
            params={
                "message": "message",
                "compact": True,
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_21(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="signMessageWithIdentityKey",
            params={"message": "message"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_21(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="signMessageWithIdentityKey",
            params={"message": "message"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_21(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="signMessageWithIdentityKey",
                params={"message": "message"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_22(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="withdraw",
            params={
                "exit_speed": "FAST",
                "onchain_address": "onchain_address",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_22(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="withdraw",
            params={
                "exit_speed": "FAST",
                "onchain_address": "onchain_address",
                "amount_sats": 0,
                "deduct_fee_from_withdrawal_amount": True,
                "fee_amount_sats": 0,
                "fee_quote_id": "fee_quote_id",
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_22(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="withdraw",
            params={
                "exit_speed": "FAST",
                "onchain_address": "onchain_address",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_22(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="withdraw",
            params={
                "exit_speed": "FAST",
                "onchain_address": "onchain_address",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_22(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="withdraw",
                params={
                    "exit_speed": "FAST",
                    "onchain_address": "onchain_address",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_23(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getWithdrawalFeeQuote",
            params={
                "amount_sats": 0,
                "onchain_address": "onchain_address",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_23(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="getWithdrawalFeeQuote",
            params={
                "amount_sats": 0,
                "onchain_address": "onchain_address",
            },
            network="MAINNET",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_23(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="getWithdrawalFeeQuote",
            params={
                "amount_sats": 0,
                "onchain_address": "onchain_address",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_23(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="getWithdrawalFeeQuote",
            params={
                "amount_sats": 0,
                "onchain_address": "onchain_address",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_23(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="getWithdrawalFeeQuote",
                params={
                    "amount_sats": 0,
                    "onchain_address": "onchain_address",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_24(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="tron_signTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "expiration": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                }
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_24(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="tron_signTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "expiration": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                    "data": "d6BC",
                    "fee_limit": 0,
                    "timestamp": 0,
                }
            },
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_24(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="tron_signTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "expiration": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_24(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="tron_signTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "expiration": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_24(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="tron_signTransaction",
                params={
                    "raw_data": {
                        "contract": [
                            {
                                "amount": 1,
                                "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                                "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                                "type": "TransferContract",
                            }
                        ],
                        "expiration": 0,
                        "ref_block_bytes": "E1CB",
                        "ref_block_hash": "E1CB97d8EBbDbaAa",
                    }
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_25(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="tron_sendTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ]
                }
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_25(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="tron_sendTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ],
                    "data": "d6BC",
                    "expiration": 0,
                    "fee_limit": 0,
                    "ref_block_bytes": "E1CB",
                    "ref_block_hash": "E1CB97d8EBbDbaAa",
                    "timestamp": 0,
                },
                "reference_id": "reference_id",
            },
            caip2="-l-f12-k:_--l__36_",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_25(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="tron_sendTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ]
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_25(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="tron_sendTransaction",
            params={
                "raw_data": {
                    "contract": [
                        {
                            "amount": 1,
                            "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                            "type": "TransferContract",
                        }
                    ]
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_25(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="tron_sendTransaction",
                params={
                    "raw_data": {
                        "contract": [
                            {
                                "amount": 1,
                                "owner_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                                "to_address": "41E1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
                                "type": "TransferContract",
                            }
                        ]
                    }
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_26(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="xrpl_signTransaction",
            params={
                "encoding": "hex",
                "transaction": "transaction",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_26(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            method="xrpl_signTransaction",
            params={
                "encoding": "hex",
                "transaction": "transaction",
            },
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_26(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            method="xrpl_signTransaction",
            params={
                "encoding": "hex",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_26(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            method="xrpl_signTransaction",
            params={
                "encoding": "hex",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_26(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                method="xrpl_signTransaction",
                params={
                    "encoding": "hex",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_27(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportPrivateKey",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_27(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportPrivateKey",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
                "export_seed_phrase": True,
                "export_type": "display",
            },
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_27(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportPrivateKey",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_27(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportPrivateKey",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_27(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                address="address",
                method="exportPrivateKey",
                params={
                    "encryption_type": "HPKE",
                    "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_overload_28(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportSeedPhrase",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rpc_with_all_params_overload_28(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportSeedPhrase",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
                "export_seed_phrase": True,
                "export_type": "display",
            },
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rpc_overload_28(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportSeedPhrase",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RpcIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rpc_overload_28(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.rpc(
            path_wallet_id="wallet_id",
            address="address",
            method="exportSeedPhrase",
            params={
                "encryption_type": "HPKE",
                "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RpcIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rpc_overload_28(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_wallet_id` but received ''"):
            await async_client.intents.with_raw_response.rpc(
                path_wallet_id="",
                address="address",
                method="exportSeedPhrase",
                params={
                    "encryption_type": "HPKE",
                    "recipient_public_key": "-----BEGIN PUBLIC KEY-----\nSq++/W\nLz/==-----END PUBLIC KEY-----\n",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transfer(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.transfer(
            wallet_id="wallet_id",
            destination={"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
            source={
                "asset": "usdc",
                "chain": "base",
            },
        )
        assert_matches_type(TransferIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transfer_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.transfer(
            wallet_id="wallet_id",
            destination={
                "address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2",
                "asset": "asset",
                "chain": "chain",
            },
            source={
                "asset": "usdc",
                "chain": "base",
                "amount": "10.5",
            },
            amount="10.5",
            amount_type="exact_input",
            fee_configuration={
                "type": "total_fee_bps",
                "value": 50,
            },
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            reference_id="x",
            slippage_bps=0,
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(TransferIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_transfer(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.transfer(
            wallet_id="wallet_id",
            destination={"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
            source={
                "asset": "usdc",
                "chain": "base",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(TransferIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_transfer(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.transfer(
            wallet_id="wallet_id",
            destination={"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
            source={
                "asset": "usdc",
                "chain": "base",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(TransferIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_transfer(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.intents.with_raw_response.transfer(
                wallet_id="",
                destination={"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
                source={
                    "asset": "usdc",
                    "chain": "base",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_key_quorum(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.update_key_quorum(
            key_quorum_id="key_quorum_id",
        )
        assert_matches_type(KeyQuorumIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_key_quorum_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.update_key_quorum(
            key_quorum_id="key_quorum_id",
            authorization_threshold=0,
            display_name="display_name",
            key_quorum_ids=["string"],
            public_keys=["string"],
            user_ids=["string"],
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(KeyQuorumIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_key_quorum(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.update_key_quorum(
            key_quorum_id="key_quorum_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(KeyQuorumIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_key_quorum(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.update_key_quorum(
            key_quorum_id="key_quorum_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(KeyQuorumIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_key_quorum(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_quorum_id` but received ''"):
            await async_client.intents.with_raw_response.update_key_quorum(
                key_quorum_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_policy(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.update_policy(
            policy_id="policy_id",
        )
        assert_matches_type(PolicyIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_policy_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.update_policy(
            policy_id="policy_id",
            name="x",
            owner={"user_id": "user_id"},
            owner_id="string",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "string",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "x",
                }
            ],
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(PolicyIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_policy(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.update_policy(
            policy_id="policy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(PolicyIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_policy(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.update_policy(
            policy_id="policy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(PolicyIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_policy(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.intents.with_raw_response.update_policy(
                policy_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.update_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        )
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_policy_rule_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.update_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.update_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.update_policy_rule(
            rule_id="rule_id",
            policy_id="policy_id",
            action="ALLOW",
            conditions=[
                {
                    "field": "to",
                    "field_source": "ethereum_transaction",
                    "operator": "eq",
                    "value": "string",
                }
            ],
            method="eth_sendTransaction",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(RuleMutateIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_policy_rule(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.intents.with_raw_response.update_policy_rule(
                rule_id="rule_id",
                policy_id="",
                action="ALLOW",
                conditions=[
                    {
                        "field": "to",
                        "field_source": "ethereum_transaction",
                        "operator": "eq",
                        "value": "string",
                    }
                ],
                method="eth_sendTransaction",
                name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.intents.with_raw_response.update_policy_rule(
                rule_id="",
                policy_id="policy_id",
                action="ALLOW",
                conditions=[
                    {
                        "field": "to",
                        "field_source": "ethereum_transaction",
                        "operator": "eq",
                        "value": "string",
                    }
                ],
                method="eth_sendTransaction",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_wallet(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.update_wallet(
            wallet_id="wallet_id",
        )
        assert_matches_type(WalletIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_wallet_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        intent = await async_client.intents.update_wallet(
            wallet_id="wallet_id",
            additional_signers=[
                {
                    "signer_id": "string",
                    "override_policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                }
            ],
            display_name="display_name",
            owner={"user_id": "user_id"},
            owner_id="string",
            policy_ids=["xxxxxxxxxxxxxxxxxxxxxxxx"],
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(WalletIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_wallet(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.intents.with_raw_response.update_wallet(
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intent = await response.parse()
        assert_matches_type(WalletIntentResponse, intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_wallet(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.intents.with_streaming_response.update_wallet(
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intent = await response.parse()
            assert_matches_type(WalletIntentResponse, intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_wallet(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.intents.with_raw_response.update_wallet(
                wallet_id="",
            )
