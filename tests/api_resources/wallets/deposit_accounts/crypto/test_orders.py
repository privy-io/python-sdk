# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import GetCryptoDepositAccountOrderResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        order = client.wallets.deposit_accounts.crypto.orders.get(
            order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        )
        assert_matches_type(GetCryptoDepositAccountOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.wallets.deposit_accounts.crypto.orders.with_raw_response.get(
            order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(GetCryptoDepositAccountOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.wallets.deposit_accounts.crypto.orders.with_streaming_response.get(
            order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(GetCryptoDepositAccountOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.deposit_accounts.crypto.orders.with_raw_response.get(
                order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                wallet_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.wallets.deposit_accounts.crypto.orders.with_raw_response.get(
                order_id="",
                wallet_id="wallet_id",
            )


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        order = await async_client.wallets.deposit_accounts.crypto.orders.get(
            order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        )
        assert_matches_type(GetCryptoDepositAccountOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.deposit_accounts.crypto.orders.with_raw_response.get(
            order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(GetCryptoDepositAccountOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.deposit_accounts.crypto.orders.with_streaming_response.get(
            order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(GetCryptoDepositAccountOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.deposit_accounts.crypto.orders.with_raw_response.get(
                order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                wallet_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.wallets.deposit_accounts.crypto.orders.with_raw_response.get(
                order_id="",
                wallet_id="wallet_id",
            )
