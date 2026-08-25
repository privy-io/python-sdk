# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    FiatDepositAccountResponse,
    ListFiatDepositAccountsResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        fiat = client.wallets.deposit_accounts.fiat.create(
            wallet_id="wallet_id",
            destination={
                "asset": "asset",
                "chain": "chain",
            },
            provider="bridge",
            source={"currency": "currency"},
        )
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        fiat = client.wallets.deposit_accounts.fiat.create(
            wallet_id="wallet_id",
            destination={
                "asset": "asset",
                "chain": "chain",
            },
            provider="bridge",
            source={"currency": "currency"},
            environment="sandbox",
        )
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.wallets.deposit_accounts.fiat.with_raw_response.create(
            wallet_id="wallet_id",
            destination={
                "asset": "asset",
                "chain": "chain",
            },
            provider="bridge",
            source={"currency": "currency"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = response.parse()
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.wallets.deposit_accounts.fiat.with_streaming_response.create(
            wallet_id="wallet_id",
            destination={
                "asset": "asset",
                "chain": "chain",
            },
            provider="bridge",
            source={"currency": "currency"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = response.parse()
            assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.deposit_accounts.fiat.with_raw_response.create(
                wallet_id="",
                destination={
                    "asset": "asset",
                    "chain": "chain",
                },
                provider="bridge",
                source={"currency": "currency"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        fiat = client.wallets.deposit_accounts.fiat.list(
            wallet_id="wallet_id",
            provider="bridge",
        )
        assert_matches_type(ListFiatDepositAccountsResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PrivyAPI) -> None:
        fiat = client.wallets.deposit_accounts.fiat.list(
            wallet_id="wallet_id",
            provider="bridge",
            environment="sandbox",
        )
        assert_matches_type(ListFiatDepositAccountsResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.wallets.deposit_accounts.fiat.with_raw_response.list(
            wallet_id="wallet_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = response.parse()
        assert_matches_type(ListFiatDepositAccountsResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.wallets.deposit_accounts.fiat.with_streaming_response.list(
            wallet_id="wallet_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = response.parse()
            assert_matches_type(ListFiatDepositAccountsResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.deposit_accounts.fiat.with_raw_response.list(
                wallet_id="",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        fiat = client.wallets.deposit_accounts.fiat.get(
            deposit_account_id="deposit_account_id",
            wallet_id="wallet_id",
        )
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.wallets.deposit_accounts.fiat.with_raw_response.get(
            deposit_account_id="deposit_account_id",
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = response.parse()
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.wallets.deposit_accounts.fiat.with_streaming_response.get(
            deposit_account_id="deposit_account_id",
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = response.parse()
            assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.deposit_accounts.fiat.with_raw_response.get(
                deposit_account_id="deposit_account_id",
                wallet_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deposit_account_id` but received ''"):
            client.wallets.deposit_accounts.fiat.with_raw_response.get(
                deposit_account_id="",
                wallet_id="wallet_id",
            )


class TestAsyncFiat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.wallets.deposit_accounts.fiat.create(
            wallet_id="wallet_id",
            destination={
                "asset": "asset",
                "chain": "chain",
            },
            provider="bridge",
            source={"currency": "currency"},
        )
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.wallets.deposit_accounts.fiat.create(
            wallet_id="wallet_id",
            destination={
                "asset": "asset",
                "chain": "chain",
            },
            provider="bridge",
            source={"currency": "currency"},
            environment="sandbox",
        )
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.deposit_accounts.fiat.with_raw_response.create(
            wallet_id="wallet_id",
            destination={
                "asset": "asset",
                "chain": "chain",
            },
            provider="bridge",
            source={"currency": "currency"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = await response.parse()
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.deposit_accounts.fiat.with_streaming_response.create(
            wallet_id="wallet_id",
            destination={
                "asset": "asset",
                "chain": "chain",
            },
            provider="bridge",
            source={"currency": "currency"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = await response.parse()
            assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.deposit_accounts.fiat.with_raw_response.create(
                wallet_id="",
                destination={
                    "asset": "asset",
                    "chain": "chain",
                },
                provider="bridge",
                source={"currency": "currency"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.wallets.deposit_accounts.fiat.list(
            wallet_id="wallet_id",
            provider="bridge",
        )
        assert_matches_type(ListFiatDepositAccountsResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.wallets.deposit_accounts.fiat.list(
            wallet_id="wallet_id",
            provider="bridge",
            environment="sandbox",
        )
        assert_matches_type(ListFiatDepositAccountsResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.deposit_accounts.fiat.with_raw_response.list(
            wallet_id="wallet_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = await response.parse()
        assert_matches_type(ListFiatDepositAccountsResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.deposit_accounts.fiat.with_streaming_response.list(
            wallet_id="wallet_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = await response.parse()
            assert_matches_type(ListFiatDepositAccountsResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.deposit_accounts.fiat.with_raw_response.list(
                wallet_id="",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.wallets.deposit_accounts.fiat.get(
            deposit_account_id="deposit_account_id",
            wallet_id="wallet_id",
        )
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.deposit_accounts.fiat.with_raw_response.get(
            deposit_account_id="deposit_account_id",
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = await response.parse()
        assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.deposit_accounts.fiat.with_streaming_response.get(
            deposit_account_id="deposit_account_id",
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = await response.parse()
            assert_matches_type(FiatDepositAccountResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.deposit_accounts.fiat.with_raw_response.get(
                deposit_account_id="deposit_account_id",
                wallet_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deposit_account_id` but received ''"):
            await async_client.wallets.deposit_accounts.fiat.with_raw_response.get(
                deposit_account_id="",
                wallet_id="wallet_id",
            )
