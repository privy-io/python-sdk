# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    Policy,
    SuccessResponse,
    PolicyRuleResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        policy = client.policies.create(
            chain_type="ethereum",
            name="x",
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
            version="1.0",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        policy = client.policies.create(
            chain_type="ethereum",
            name="x",
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
                    "id": "id",
                }
            ],
            version="1.0",
            owner={"user_id": "user_id"},
            owner_id="string",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response.create(
            chain_type="ethereum",
            name="x",
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
            version="1.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response.create(
            chain_type="ethereum",
            name="x",
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
            version="1.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_rule(self, client: PrivyAPI) -> None:
        policy = client.policies._create_rule(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_rule_with_all_params(self, client: PrivyAPI) -> None:
        policy = client.policies._create_rule(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_rule(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response._create_rule(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
        policy = response.parse()
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_rule(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response._create_rule(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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

            policy = response.parse()
            assert_matches_type(PolicyRuleResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_rule(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response._create_rule(
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
    def test_method_delete(self, client: PrivyAPI) -> None:
        policy = client.policies._delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: PrivyAPI) -> None:
        policy = client.policies._delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response._delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response._delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(SuccessResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response._delete(
                policy_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_rule(self, client: PrivyAPI) -> None:
        policy = client.policies._delete_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_rule_with_all_params(self, client: PrivyAPI) -> None:
        policy = client.policies._delete_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_rule(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response._delete_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_rule(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response._delete_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(SuccessResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_rule(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response._delete_rule(
                rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
                policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.policies.with_raw_response._delete_rule(
                rule_id="",
                policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: PrivyAPI) -> None:
        policy = client.policies._update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PrivyAPI) -> None:
        policy = client.policies._update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response._update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response._update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response._update(
                policy_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_rule(self, client: PrivyAPI) -> None:
        policy = client.policies._update_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_rule_with_all_params(self, client: PrivyAPI) -> None:
        policy = client.policies._update_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_rule(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response._update_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
        policy = response.parse()
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_rule(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response._update_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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

            policy = response.parse()
            assert_matches_type(PolicyRuleResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_rule(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response._update_rule(
                rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
            client.policies.with_raw_response._update_rule(
                rule_id="",
                policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
    def test_method_get(self, client: PrivyAPI) -> None:
        policy = client.policies.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_rule(self, client: PrivyAPI) -> None:
        policy = client.policies.get_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_rule(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response.get_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_rule(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response.get_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyRuleResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_rule(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response.get_rule(
                rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
                policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.policies.with_raw_response.get_rule(
                rule_id="",
                policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.create(
            chain_type="ethereum",
            name="x",
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
            version="1.0",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.create(
            chain_type="ethereum",
            name="x",
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
                    "id": "id",
                }
            ],
            version="1.0",
            owner={"user_id": "user_id"},
            owner_id="string",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response.create(
            chain_type="ethereum",
            name="x",
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
            version="1.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response.create(
            chain_type="ethereum",
            name="x",
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
            version="1.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_rule(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._create_rule(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_rule_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._create_rule(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_rule(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response._create_rule(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
        policy = await response.parse()
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_rule(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response._create_rule(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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

            policy = await response.parse()
            assert_matches_type(PolicyRuleResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_rule(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response._create_rule(
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
    async def test_method_delete(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response._delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response._delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(SuccessResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response._delete(
                policy_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_rule(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._delete_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_rule_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._delete_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_rule(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response._delete_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(SuccessResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_rule(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response._delete_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(SuccessResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_rule(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response._delete_rule(
                rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
                policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.policies.with_raw_response._delete_rule(
                rule_id="",
                policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response._update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response._update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response._update(
                policy_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_rule(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._update_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_rule_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies._update_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_rule(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response._update_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
        policy = await response.parse()
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_rule(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response._update_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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

            policy = await response.parse()
            assert_matches_type(PolicyRuleResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_rule(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response._update_rule(
                rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
            await async_client.policies.with_raw_response._update_rule(
                rule_id="",
                policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
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
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_rule(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.get_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_rule(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response.get_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyRuleResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_rule(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response.get_rule(
            rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyRuleResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_rule(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response.get_rule(
                rule_id="xxxxxxxxxxxxxxxxxxxxxxxx",
                policy_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.policies.with_raw_response.get_rule(
                rule_id="",
                policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            )
