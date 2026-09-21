# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    WalletAutomationResponse,
    WalletAutomationReindexResponse,
    WalletAutomationSuccessResponse,
    WalletAutomationExecutionResponse,
)
from tests.utils import assert_matches_type
from privy.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWalletAutomations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.create(
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            owner_id="x",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.create(
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                        "asset": "x",
                        "chain": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            owner_id="x",
            name="x",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.wallet_automations.with_raw_response.create(
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            owner_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = response.parse()
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.wallet_automations.with_streaming_response.create(
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            owner_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = response.parse()
            assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.update(
            automation_id="automation_id",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.update(
            automation_id="automation_id",
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                        "asset": "x",
                        "chain": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            enabled=True,
            name="x",
            owner_id="string",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PrivyAPI) -> None:
        response = client.wallet_automations.with_raw_response.update(
            automation_id="automation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = response.parse()
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PrivyAPI) -> None:
        with client.wallet_automations.with_streaming_response.update(
            automation_id="automation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = response.parse()
            assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            client.wallet_automations.with_raw_response.update(
                automation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.list()
        assert_matches_type(SyncCursor[WalletAutomationResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.list(
            cursor="cursor",
            limit=1,
            wallet_id="x",
        )
        assert_matches_type(SyncCursor[WalletAutomationResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.wallet_automations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = response.parse()
        assert_matches_type(SyncCursor[WalletAutomationResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.wallet_automations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = response.parse()
            assert_matches_type(SyncCursor[WalletAutomationResponse], wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.delete(
            "automation_id",
        )
        assert_matches_type(WalletAutomationSuccessResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PrivyAPI) -> None:
        response = client.wallet_automations.with_raw_response.delete(
            "automation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = response.parse()
        assert_matches_type(WalletAutomationSuccessResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PrivyAPI) -> None:
        with client.wallet_automations.with_streaming_response.delete(
            "automation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = response.parse()
            assert_matches_type(WalletAutomationSuccessResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            client.wallet_automations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.get(
            "automation_id",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.wallet_automations.with_raw_response.get(
            "automation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = response.parse()
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.wallet_automations.with_streaming_response.get(
            "automation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = response.parse()
            assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            client.wallet_automations.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_executions(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.list_executions()
        assert_matches_type(SyncCursor[WalletAutomationExecutionResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_executions_with_all_params(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.list_executions(
            cursor="cursor",
            limit=1,
            wallet_id="x",
        )
        assert_matches_type(SyncCursor[WalletAutomationExecutionResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_executions(self, client: PrivyAPI) -> None:
        response = client.wallet_automations.with_raw_response.list_executions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = response.parse()
        assert_matches_type(SyncCursor[WalletAutomationExecutionResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_executions(self, client: PrivyAPI) -> None:
        with client.wallet_automations.with_streaming_response.list_executions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = response.parse()
            assert_matches_type(SyncCursor[WalletAutomationExecutionResponse], wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reindex(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.reindex(
            asset_address="x",
        )
        assert_matches_type(WalletAutomationReindexResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reindex_with_all_params(self, client: PrivyAPI) -> None:
        wallet_automation = client.wallet_automations.reindex(
            asset_address="x",
            caip2="tron:mainnet",
            chain="x",
            deposit_address="x",
            wallet_id="x",
        )
        assert_matches_type(WalletAutomationReindexResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reindex(self, client: PrivyAPI) -> None:
        response = client.wallet_automations.with_raw_response.reindex(
            asset_address="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = response.parse()
        assert_matches_type(WalletAutomationReindexResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reindex(self, client: PrivyAPI) -> None:
        with client.wallet_automations.with_streaming_response.reindex(
            asset_address="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = response.parse()
            assert_matches_type(WalletAutomationReindexResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWalletAutomations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.create(
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            owner_id="x",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.create(
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                        "asset": "x",
                        "chain": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            owner_id="x",
            name="x",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallet_automations.with_raw_response.create(
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            owner_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = await response.parse()
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallet_automations.with_streaming_response.create(
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            owner_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = await response.parse()
            assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.update(
            automation_id="automation_id",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.update(
            automation_id="automation_id",
            config={
                "action": {
                    "destination_chain_asset": {
                        "asset_address": "x",
                        "caip2": "x",
                        "asset": "x",
                        "chain": "x",
                    },
                    "type": "swap",
                },
                "trigger": {
                    "assets": {"mode": "all"},
                    "type": "deposit",
                },
            },
            enabled=True,
            name="x",
            owner_id="string",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallet_automations.with_raw_response.update(
            automation_id="automation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = await response.parse()
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallet_automations.with_streaming_response.update(
            automation_id="automation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = await response.parse()
            assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            await async_client.wallet_automations.with_raw_response.update(
                automation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.list()
        assert_matches_type(AsyncCursor[WalletAutomationResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.list(
            cursor="cursor",
            limit=1,
            wallet_id="x",
        )
        assert_matches_type(AsyncCursor[WalletAutomationResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallet_automations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = await response.parse()
        assert_matches_type(AsyncCursor[WalletAutomationResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallet_automations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = await response.parse()
            assert_matches_type(AsyncCursor[WalletAutomationResponse], wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.delete(
            "automation_id",
        )
        assert_matches_type(WalletAutomationSuccessResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallet_automations.with_raw_response.delete(
            "automation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = await response.parse()
        assert_matches_type(WalletAutomationSuccessResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallet_automations.with_streaming_response.delete(
            "automation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = await response.parse()
            assert_matches_type(WalletAutomationSuccessResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            await async_client.wallet_automations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.get(
            "automation_id",
        )
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallet_automations.with_raw_response.get(
            "automation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = await response.parse()
        assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallet_automations.with_streaming_response.get(
            "automation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = await response.parse()
            assert_matches_type(WalletAutomationResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            await async_client.wallet_automations.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_executions(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.list_executions()
        assert_matches_type(AsyncCursor[WalletAutomationExecutionResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_executions_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.list_executions(
            cursor="cursor",
            limit=1,
            wallet_id="x",
        )
        assert_matches_type(AsyncCursor[WalletAutomationExecutionResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_executions(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallet_automations.with_raw_response.list_executions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = await response.parse()
        assert_matches_type(AsyncCursor[WalletAutomationExecutionResponse], wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_executions(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallet_automations.with_streaming_response.list_executions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = await response.parse()
            assert_matches_type(AsyncCursor[WalletAutomationExecutionResponse], wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reindex(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.reindex(
            asset_address="x",
        )
        assert_matches_type(WalletAutomationReindexResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reindex_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        wallet_automation = await async_client.wallet_automations.reindex(
            asset_address="x",
            caip2="tron:mainnet",
            chain="x",
            deposit_address="x",
            wallet_id="x",
        )
        assert_matches_type(WalletAutomationReindexResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reindex(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallet_automations.with_raw_response.reindex(
            asset_address="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet_automation = await response.parse()
        assert_matches_type(WalletAutomationReindexResponse, wallet_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reindex(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallet_automations.with_streaming_response.reindex(
            asset_address="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet_automation = await response.parse()
            assert_matches_type(WalletAutomationReindexResponse, wallet_automation, path=["response"])

        assert cast(Any, response.is_closed) is True
