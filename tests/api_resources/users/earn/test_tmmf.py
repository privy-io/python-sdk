# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from tests.utils import assert_matches_type
from privy.types.wallets import TmmfUserResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTmmf:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        tmmf = client.users.earn.tmmf.get(
            user_id="x",
        )
        assert_matches_type(TmmfUserResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: PrivyAPI) -> None:
        tmmf = client.users.earn.tmmf.get(
            user_id="x",
            provider="wisdomtree",
            wallet_id="x",
            wallets_cursor="x",
            wallets_limit=1,
        )
        assert_matches_type(TmmfUserResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.users.earn.tmmf.with_raw_response.get(
            user_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = response.parse()
        assert_matches_type(TmmfUserResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.users.earn.tmmf.with_streaming_response.get(
            user_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = response.parse()
            assert_matches_type(TmmfUserResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.earn.tmmf.with_raw_response.get(
                user_id="",
            )


class TestAsyncTmmf:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        tmmf = await async_client.users.earn.tmmf.get(
            user_id="x",
        )
        assert_matches_type(TmmfUserResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        tmmf = await async_client.users.earn.tmmf.get(
            user_id="x",
            provider="wisdomtree",
            wallet_id="x",
            wallets_cursor="x",
            wallets_limit=1,
        )
        assert_matches_type(TmmfUserResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.earn.tmmf.with_raw_response.get(
            user_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = await response.parse()
        assert_matches_type(TmmfUserResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.earn.tmmf.with_streaming_response.get(
            user_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = await response.parse()
            assert_matches_type(TmmfUserResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.earn.tmmf.with_raw_response.get(
                user_id="",
            )
