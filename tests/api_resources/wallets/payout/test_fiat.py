# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from tests.utils import assert_matches_type
from privy.types.wallets import PayoutResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        fiat = client.wallets.payout.fiat._create(
            wallet_id="wallet_id",
            destination={"fiat_account_id": "fiat_account_id"},
            source={
                "amount": "amount",
                "asset": "asset",
                "chain": "chain",
            },
        )
        assert_matches_type(PayoutResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        fiat = client.wallets.payout.fiat._create(
            wallet_id="wallet_id",
            destination={"fiat_account_id": "fiat_account_id"},
            source={
                "amount": "amount",
                "asset": "asset",
                "chain": "chain",
            },
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(PayoutResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.wallets.payout.fiat.with_raw_response._create(
            wallet_id="wallet_id",
            destination={"fiat_account_id": "fiat_account_id"},
            source={
                "amount": "amount",
                "asset": "asset",
                "chain": "chain",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = response.parse()
        assert_matches_type(PayoutResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.wallets.payout.fiat.with_streaming_response._create(
            wallet_id="wallet_id",
            destination={"fiat_account_id": "fiat_account_id"},
            source={
                "amount": "amount",
                "asset": "asset",
                "chain": "chain",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = response.parse()
            assert_matches_type(PayoutResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.payout.fiat.with_raw_response._create(
                wallet_id="",
                destination={"fiat_account_id": "fiat_account_id"},
                source={
                    "amount": "amount",
                    "asset": "asset",
                    "chain": "chain",
                },
            )


class TestAsyncFiat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.wallets.payout.fiat._create(
            wallet_id="wallet_id",
            destination={"fiat_account_id": "fiat_account_id"},
            source={
                "amount": "amount",
                "asset": "asset",
                "chain": "chain",
            },
        )
        assert_matches_type(PayoutResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.wallets.payout.fiat._create(
            wallet_id="wallet_id",
            destination={"fiat_account_id": "fiat_account_id"},
            source={
                "amount": "amount",
                "asset": "asset",
                "chain": "chain",
            },
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(PayoutResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.payout.fiat.with_raw_response._create(
            wallet_id="wallet_id",
            destination={"fiat_account_id": "fiat_account_id"},
            source={
                "amount": "amount",
                "asset": "asset",
                "chain": "chain",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = await response.parse()
        assert_matches_type(PayoutResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.payout.fiat.with_streaming_response._create(
            wallet_id="wallet_id",
            destination={"fiat_account_id": "fiat_account_id"},
            source={
                "amount": "amount",
                "asset": "asset",
                "chain": "chain",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = await response.parse()
            assert_matches_type(PayoutResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.payout.fiat.with_raw_response._create(
                wallet_id="",
                destination={"fiat_account_id": "fiat_account_id"},
                source={
                    "amount": "amount",
                    "asset": "asset",
                    "chain": "chain",
                },
            )
