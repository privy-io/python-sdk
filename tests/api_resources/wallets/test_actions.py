# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from tests.utils import assert_matches_type
from privy.types.wallets import WalletActionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        action = client.wallets.actions.get(
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        )
        assert_matches_type(WalletActionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: PrivyAPI) -> None:
        action = client.wallets.actions.get(
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
            include="steps",
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(WalletActionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.wallets.actions.with_raw_response.get(
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(WalletActionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.wallets.actions.with_streaming_response.get(
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(WalletActionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.actions.with_raw_response.get(
                action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                wallet_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            client.wallets.actions.with_raw_response.get(
                action_id="",
                wallet_id="wallet_id",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        action = await async_client.wallets.actions.get(
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        )
        assert_matches_type(WalletActionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        action = await async_client.wallets.actions.get(
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
            include="steps",
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(WalletActionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.actions.with_raw_response.get(
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(WalletActionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.actions.with_streaming_response.get(
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(WalletActionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.actions.with_raw_response.get(
                action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                wallet_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            await async_client.wallets.actions.with_raw_response.get(
                action_id="",
                wallet_id="wallet_id",
            )
