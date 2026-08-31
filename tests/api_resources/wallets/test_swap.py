# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    SwapQuoteResponse,
)
from tests.utils import assert_matches_type
from privy.types.wallets import SwapActionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSwap:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute(self, client: PrivyAPI) -> None:
        swap = client.wallets.swap.execute(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        )
        assert_matches_type(SwapActionResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: PrivyAPI) -> None:
        swap = client.wallets.swap.execute(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={
                "asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "caip2": "eip155:1",
                "destination_address": "destination_address",
            },
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
            amount_type="exact_input",
            fee_configuration={
                "type": "total_fee_bps",
                "value": 50,
            },
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            reference_id="x",
            slippage_bps=50,
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SwapActionResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: PrivyAPI) -> None:
        response = client.wallets.swap.with_raw_response.execute(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = response.parse()
        assert_matches_type(SwapActionResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: PrivyAPI) -> None:
        with client.wallets.swap.with_streaming_response.execute(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = response.parse()
            assert_matches_type(SwapActionResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.swap.with_raw_response.execute(
                wallet_id="",
                base_amount="1000000000000000000",
                destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
                source={
                    "asset_address": "native",
                    "caip2": "eip155:1",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_quote(self, client: PrivyAPI) -> None:
        swap = client.wallets.swap.quote(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        )
        assert_matches_type(SwapQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_quote_with_all_params(self, client: PrivyAPI) -> None:
        swap = client.wallets.swap.quote(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={
                "asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "caip2": "eip155:1",
                "destination_address": "destination_address",
            },
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
            amount_type="exact_input",
            fee_configuration={
                "type": "total_fee_bps",
                "value": 50,
            },
            slippage_bps=0,
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SwapQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_quote(self, client: PrivyAPI) -> None:
        response = client.wallets.swap.with_raw_response.quote(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = response.parse()
        assert_matches_type(SwapQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_quote(self, client: PrivyAPI) -> None:
        with client.wallets.swap.with_streaming_response.quote(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = response.parse()
            assert_matches_type(SwapQuoteResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_quote(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.swap.with_raw_response.quote(
                wallet_id="",
                base_amount="1000000000000000000",
                destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
                source={
                    "asset_address": "native",
                    "caip2": "eip155:1",
                },
            )


class TestAsyncSwap:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncPrivyAPI) -> None:
        swap = await async_client.wallets.swap.execute(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        )
        assert_matches_type(SwapActionResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        swap = await async_client.wallets.swap.execute(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={
                "asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "caip2": "eip155:1",
                "destination_address": "destination_address",
            },
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
            amount_type="exact_input",
            fee_configuration={
                "type": "total_fee_bps",
                "value": 50,
            },
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            reference_id="x",
            slippage_bps=50,
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SwapActionResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.swap.with_raw_response.execute(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = await response.parse()
        assert_matches_type(SwapActionResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.swap.with_streaming_response.execute(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = await response.parse()
            assert_matches_type(SwapActionResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.swap.with_raw_response.execute(
                wallet_id="",
                base_amount="1000000000000000000",
                destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
                source={
                    "asset_address": "native",
                    "caip2": "eip155:1",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_quote(self, async_client: AsyncPrivyAPI) -> None:
        swap = await async_client.wallets.swap.quote(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        )
        assert_matches_type(SwapQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_quote_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        swap = await async_client.wallets.swap.quote(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={
                "asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "caip2": "eip155:1",
                "destination_address": "destination_address",
            },
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
            amount_type="exact_input",
            fee_configuration={
                "type": "total_fee_bps",
                "value": 50,
            },
            slippage_bps=0,
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SwapQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_quote(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.swap.with_raw_response.quote(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = await response.parse()
        assert_matches_type(SwapQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_quote(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.swap.with_streaming_response.quote(
            wallet_id="wallet_id",
            base_amount="1000000000000000000",
            destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
            source={
                "asset_address": "native",
                "caip2": "eip155:1",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = await response.parse()
            assert_matches_type(SwapQuoteResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_quote(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.swap.with_raw_response.quote(
                wallet_id="",
                base_amount="1000000000000000000",
                destination={"asset_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
                source={
                    "asset_address": "native",
                    "caip2": "eip155:1",
                },
            )
