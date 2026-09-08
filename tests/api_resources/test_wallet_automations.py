# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import WalletAutomationReindexResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWalletAutomations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            caip2="eip155:321669910225",
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
            caip2="eip155:321669910225",
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
