# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from tests.utils import assert_matches_type
from privy.types.fiat import AccountGetResponse, AccountCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        account = client.fiat.accounts.create(
            user_id="user_id",
            account_owner_name="John Doe",
            currency="usd",
            provider="bridge-sandbox",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        account = client.fiat.accounts.create(
            user_id="user_id",
            account_owner_name="John Doe",
            currency="usd",
            provider="bridge-sandbox",
            account={
                "account_number": "1234567899",
                "routing_number": "121212121",
                "checking_or_savings": "checking",
            },
            address={
                "city": "New York",
                "country": "USA",
                "street_line_1": "123 Washington St",
                "postal_code": "10001",
                "state": "NY",
                "street_line_2": "Apt 2F",
            },
            bank_name="Chase",
            first_name="John",
            iban={
                "account_number": "x",
                "bic": "x",
                "country": "xxx",
            },
            last_name="Doe",
            swift={
                "account": {
                    "account_number": "x",
                    "bic": "x",
                    "country": "xxx",
                },
                "address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "postal_code": "x",
                    "state": "x",
                    "street_line_2": "x",
                },
                "category": "client",
                "purpose_of_funds": ["intra_group_transfer"],
                "short_business_description": "x",
            },
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.fiat.accounts.with_raw_response.create(
            user_id="user_id",
            account_owner_name="John Doe",
            currency="usd",
            provider="bridge-sandbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.fiat.accounts.with_streaming_response.create(
            user_id="user_id",
            account_owner_name="John Doe",
            currency="usd",
            provider="bridge-sandbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.accounts.with_raw_response.create(
                user_id="",
                account_owner_name="John Doe",
                currency="usd",
                provider="bridge-sandbox",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        account = client.fiat.accounts.get(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(AccountGetResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.fiat.accounts.with_raw_response.get(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountGetResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.fiat.accounts.with_streaming_response.get(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountGetResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.accounts.with_raw_response.get(
                user_id="",
                provider="bridge",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        account = await async_client.fiat.accounts.create(
            user_id="user_id",
            account_owner_name="John Doe",
            currency="usd",
            provider="bridge-sandbox",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        account = await async_client.fiat.accounts.create(
            user_id="user_id",
            account_owner_name="John Doe",
            currency="usd",
            provider="bridge-sandbox",
            account={
                "account_number": "1234567899",
                "routing_number": "121212121",
                "checking_or_savings": "checking",
            },
            address={
                "city": "New York",
                "country": "USA",
                "street_line_1": "123 Washington St",
                "postal_code": "10001",
                "state": "NY",
                "street_line_2": "Apt 2F",
            },
            bank_name="Chase",
            first_name="John",
            iban={
                "account_number": "x",
                "bic": "x",
                "country": "xxx",
            },
            last_name="Doe",
            swift={
                "account": {
                    "account_number": "x",
                    "bic": "x",
                    "country": "xxx",
                },
                "address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "postal_code": "x",
                    "state": "x",
                    "street_line_2": "x",
                },
                "category": "client",
                "purpose_of_funds": ["intra_group_transfer"],
                "short_business_description": "x",
            },
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.accounts.with_raw_response.create(
            user_id="user_id",
            account_owner_name="John Doe",
            currency="usd",
            provider="bridge-sandbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.accounts.with_streaming_response.create(
            user_id="user_id",
            account_owner_name="John Doe",
            currency="usd",
            provider="bridge-sandbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.accounts.with_raw_response.create(
                user_id="",
                account_owner_name="John Doe",
                currency="usd",
                provider="bridge-sandbox",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        account = await async_client.fiat.accounts.get(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(AccountGetResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.accounts.with_raw_response.get(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountGetResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.accounts.with_streaming_response.get(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountGetResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.accounts.with_raw_response.get(
                user_id="",
                provider="bridge",
            )
