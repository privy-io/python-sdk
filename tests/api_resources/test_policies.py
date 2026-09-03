# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import Policy, PolicyDeleteResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        policy = client.policies.create(
            chain_type="ethereum",
            name="Allowlisted stablecoins",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                },
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDT contract on Base",
                },
            ],
            version="1.0",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        policy = client.policies.create(
            chain_type="ethereum",
            name="Allowlisted stablecoins",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                },
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDT contract on Base",
                },
            ],
            version="1.0",
            owner={"user_id": "user_id"},
            owner_id="owner_id",
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response.create(
            chain_type="ethereum",
            name="Allowlisted stablecoins",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                },
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDT contract on Base",
                },
            ],
            version="1.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response.create(
            chain_type="ethereum",
            name="Allowlisted stablecoins",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                },
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDT contract on Base",
                },
            ],
            version="1.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: PrivyAPI) -> None:
        policy = client.policies.update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: PrivyAPI) -> None:
        policy = client.policies.update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            name="Allowlisted stablecoins",
            owner={"public_key": "public_key"},
            owner_id="owner_id",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                }
            ],
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response.update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response.update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response.update(
                policy_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: PrivyAPI) -> None:
        policy = client.policies.delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: PrivyAPI) -> None:
        policy = client.policies.delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response.delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: PrivyAPI) -> None:
        with client.policies.with_streaming_response.delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response.delete(
                policy_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        policy = client.policies.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.policies.with_raw_response.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.policies.with_raw_response.get(
                "",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.create(
            chain_type="ethereum",
            name="Allowlisted stablecoins",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                },
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDT contract on Base",
                },
            ],
            version="1.0",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.create(
            chain_type="ethereum",
            name="Allowlisted stablecoins",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                },
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDT contract on Base",
                },
            ],
            version="1.0",
            owner={"user_id": "user_id"},
            owner_id="owner_id",
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response.create(
            chain_type="ethereum",
            name="Allowlisted stablecoins",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                },
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDT contract on Base",
                },
            ],
            version="1.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response.create(
            chain_type="ethereum",
            name="Allowlisted stablecoins",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                },
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDT contract on Base",
                },
            ],
            version="1.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            name="Allowlisted stablecoins",
            owner={"public_key": "public_key"},
            owner_id="owner_id",
            rules=[
                {
                    "action": "ALLOW",
                    "conditions": [
                        {
                            "field": "to",
                            "field_source": "ethereum_transaction",
                            "operator": "eq",
                            "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                        }
                    ],
                    "method": "eth_sendTransaction",
                    "name": "Allowlist USDC contract on Base",
                }
            ],
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response.update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response.update(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Policy, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response.update(
                policy_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response.delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.policies.with_streaming_response.delete(
            policy_id="xxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response.delete(
                policy_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        policy = await async_client.policies.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.policies.with_raw_response.get(
            "xxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Policy, policy, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.policies.with_raw_response.get(
                "",
            )
