# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from tests.utils import assert_matches_type
from privy.types.wallets import TransactionGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        transaction = client.wallets.transactions.get(
            wallet_id="wallet_id",
            asset="usdc",
            chain="base",
        )
        assert_matches_type(TransactionGetResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: PrivyAPI) -> None:
        transaction = client.wallets.transactions.get(
            wallet_id="wallet_id",
            asset="usdc",
            chain="base",
            cursor="x",
            limit=100,
        )
        assert_matches_type(TransactionGetResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.wallets.transactions.with_raw_response.get(
            wallet_id="wallet_id",
            asset="usdc",
            chain="base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionGetResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.wallets.transactions.with_streaming_response.get(
            wallet_id="wallet_id",
            asset="usdc",
            chain="base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionGetResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.transactions.with_raw_response.get(
                wallet_id="",
                asset="usdc",
                chain="base",
            )


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        transaction = await async_client.wallets.transactions.get(
            wallet_id="wallet_id",
            asset="usdc",
            chain="base",
        )
        assert_matches_type(TransactionGetResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        transaction = await async_client.wallets.transactions.get(
            wallet_id="wallet_id",
            asset="usdc",
            chain="base",
            cursor="x",
            limit=100,
        )
        assert_matches_type(TransactionGetResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.transactions.with_raw_response.get(
            wallet_id="wallet_id",
            asset="usdc",
            chain="base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionGetResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.transactions.with_streaming_response.get(
            wallet_id="wallet_id",
            asset="usdc",
            chain="base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionGetResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.transactions.with_raw_response.get(
                wallet_id="",
                asset="usdc",
                chain="base",
            )
