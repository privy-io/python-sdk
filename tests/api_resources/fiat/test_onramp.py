# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from tests.utils import assert_matches_type
from privy.types.fiat import OnrampCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnramp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        onramp = client.fiat.onramp.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "chain": "base",
                "currency": "usdc",
                "to_address": "0x38Bc05d7b69F63D05337829fA5Dc4896F179B5fA",
            },
            provider="bridge-sandbox",
            source={
                "currency": "usd",
                "payment_rail": "ach_push",
            },
        )
        assert_matches_type(OnrampCreateResponse, onramp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.fiat.onramp.with_raw_response.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "chain": "base",
                "currency": "usdc",
                "to_address": "0x38Bc05d7b69F63D05337829fA5Dc4896F179B5fA",
            },
            provider="bridge-sandbox",
            source={
                "currency": "usd",
                "payment_rail": "ach_push",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onramp = response.parse()
        assert_matches_type(OnrampCreateResponse, onramp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.fiat.onramp.with_streaming_response.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "chain": "base",
                "currency": "usdc",
                "to_address": "0x38Bc05d7b69F63D05337829fA5Dc4896F179B5fA",
            },
            provider="bridge-sandbox",
            source={
                "currency": "usd",
                "payment_rail": "ach_push",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onramp = response.parse()
            assert_matches_type(OnrampCreateResponse, onramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.onramp.with_raw_response.create(
                user_id="",
                amount="100.00",
                destination={
                    "chain": "base",
                    "currency": "usdc",
                    "to_address": "0x38Bc05d7b69F63D05337829fA5Dc4896F179B5fA",
                },
                provider="bridge-sandbox",
                source={
                    "currency": "usd",
                    "payment_rail": "ach_push",
                },
            )


class TestAsyncOnramp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        onramp = await async_client.fiat.onramp.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "chain": "base",
                "currency": "usdc",
                "to_address": "0x38Bc05d7b69F63D05337829fA5Dc4896F179B5fA",
            },
            provider="bridge-sandbox",
            source={
                "currency": "usd",
                "payment_rail": "ach_push",
            },
        )
        assert_matches_type(OnrampCreateResponse, onramp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.onramp.with_raw_response.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "chain": "base",
                "currency": "usdc",
                "to_address": "0x38Bc05d7b69F63D05337829fA5Dc4896F179B5fA",
            },
            provider="bridge-sandbox",
            source={
                "currency": "usd",
                "payment_rail": "ach_push",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onramp = await response.parse()
        assert_matches_type(OnrampCreateResponse, onramp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.onramp.with_streaming_response.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "chain": "base",
                "currency": "usdc",
                "to_address": "0x38Bc05d7b69F63D05337829fA5Dc4896F179B5fA",
            },
            provider="bridge-sandbox",
            source={
                "currency": "usd",
                "payment_rail": "ach_push",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onramp = await response.parse()
            assert_matches_type(OnrampCreateResponse, onramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.onramp.with_raw_response.create(
                user_id="",
                amount="100.00",
                destination={
                    "chain": "base",
                    "currency": "usdc",
                    "to_address": "0x38Bc05d7b69F63D05337829fA5Dc4896F179B5fA",
                },
                provider="bridge-sandbox",
                source={
                    "currency": "usd",
                    "payment_rail": "ach_push",
                },
            )
