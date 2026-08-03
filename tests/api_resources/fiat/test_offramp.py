# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import OfframpResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOfframp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        offramp = client.fiat.offramp.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "currency": "usd",
                "external_account_id": "a068d2dd-743a-4011-9b62-8ad33cc7a7be",
                "payment_rail": "ach_push",
            },
            provider="bridge-sandbox",
            source={
                "chain": "base",
                "currency": "usdc",
                "from_address": "0xc24272abc794b973b896715db40a72714a030323",
            },
        )
        assert_matches_type(OfframpResponse, offramp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.fiat.offramp.with_raw_response.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "currency": "usd",
                "external_account_id": "a068d2dd-743a-4011-9b62-8ad33cc7a7be",
                "payment_rail": "ach_push",
            },
            provider="bridge-sandbox",
            source={
                "chain": "base",
                "currency": "usdc",
                "from_address": "0xc24272abc794b973b896715db40a72714a030323",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offramp = response.parse()
        assert_matches_type(OfframpResponse, offramp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.fiat.offramp.with_streaming_response.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "currency": "usd",
                "external_account_id": "a068d2dd-743a-4011-9b62-8ad33cc7a7be",
                "payment_rail": "ach_push",
            },
            provider="bridge-sandbox",
            source={
                "chain": "base",
                "currency": "usdc",
                "from_address": "0xc24272abc794b973b896715db40a72714a030323",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offramp = response.parse()
            assert_matches_type(OfframpResponse, offramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.offramp.with_raw_response.create(
                user_id="",
                amount="100.00",
                destination={
                    "currency": "usd",
                    "external_account_id": "a068d2dd-743a-4011-9b62-8ad33cc7a7be",
                    "payment_rail": "ach_push",
                },
                provider="bridge-sandbox",
                source={
                    "chain": "base",
                    "currency": "usdc",
                    "from_address": "0xc24272abc794b973b896715db40a72714a030323",
                },
            )


class TestAsyncOfframp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        offramp = await async_client.fiat.offramp.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "currency": "usd",
                "external_account_id": "a068d2dd-743a-4011-9b62-8ad33cc7a7be",
                "payment_rail": "ach_push",
            },
            provider="bridge-sandbox",
            source={
                "chain": "base",
                "currency": "usdc",
                "from_address": "0xc24272abc794b973b896715db40a72714a030323",
            },
        )
        assert_matches_type(OfframpResponse, offramp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.offramp.with_raw_response.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "currency": "usd",
                "external_account_id": "a068d2dd-743a-4011-9b62-8ad33cc7a7be",
                "payment_rail": "ach_push",
            },
            provider="bridge-sandbox",
            source={
                "chain": "base",
                "currency": "usdc",
                "from_address": "0xc24272abc794b973b896715db40a72714a030323",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offramp = await response.parse()
        assert_matches_type(OfframpResponse, offramp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.offramp.with_streaming_response.create(
            user_id="user_id",
            amount="100.00",
            destination={
                "currency": "usd",
                "external_account_id": "a068d2dd-743a-4011-9b62-8ad33cc7a7be",
                "payment_rail": "ach_push",
            },
            provider="bridge-sandbox",
            source={
                "chain": "base",
                "currency": "usdc",
                "from_address": "0xc24272abc794b973b896715db40a72714a030323",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offramp = await response.parse()
            assert_matches_type(OfframpResponse, offramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.offramp.with_raw_response.create(
                user_id="",
                amount="100.00",
                destination={
                    "currency": "usd",
                    "external_account_id": "a068d2dd-743a-4011-9b62-8ad33cc7a7be",
                    "payment_rail": "ach_push",
                },
                provider="bridge-sandbox",
                source={
                    "chain": "base",
                    "currency": "usdc",
                    "from_address": "0xc24272abc794b973b896715db40a72714a030323",
                },
            )
