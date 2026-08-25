# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    SuccessResponse,
    ExternalFiatAccountResponse,
    ListExternalFiatAccountsResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalFiatAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        external_fiat_account = client.users.external_fiat_accounts.create(
            user_id="user_id",
            account={
                "account_number": "x",
                "routing_number": "xxxxxxxxx",
                "type": "us",
            },
            account_owner_name="xxx",
            currency="currency",
            provider="bridge",
        )
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        external_fiat_account = client.users.external_fiat_accounts.create(
            user_id="user_id",
            account={
                "account_number": "x",
                "routing_number": "xxxxxxxxx",
                "type": "us",
                "checking_or_savings": "checking_or_savings",
            },
            account_owner_name="xxx",
            currency="currency",
            provider="bridge",
            address={
                "city": "x",
                "country": "xxx",
                "street_line_1": "x",
                "postal_code": "x",
                "state": "x",
                "street_line_2": "x",
            },
            bank_name="x",
            environment="sandbox",
        )
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.users.external_fiat_accounts.with_raw_response.create(
            user_id="user_id",
            account={
                "account_number": "x",
                "routing_number": "xxxxxxxxx",
                "type": "us",
            },
            account_owner_name="xxx",
            currency="currency",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_fiat_account = response.parse()
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.users.external_fiat_accounts.with_streaming_response.create(
            user_id="user_id",
            account={
                "account_number": "x",
                "routing_number": "xxxxxxxxx",
                "type": "us",
            },
            account_owner_name="xxx",
            currency="currency",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_fiat_account = response.parse()
            assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.external_fiat_accounts.with_raw_response.create(
                user_id="",
                account={
                    "account_number": "x",
                    "routing_number": "xxxxxxxxx",
                    "type": "us",
                },
                account_owner_name="xxx",
                currency="currency",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        external_fiat_account = client.users.external_fiat_accounts.list(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(ListExternalFiatAccountsResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PrivyAPI) -> None:
        external_fiat_account = client.users.external_fiat_accounts.list(
            user_id="user_id",
            provider="bridge",
            environment="sandbox",
        )
        assert_matches_type(ListExternalFiatAccountsResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.users.external_fiat_accounts.with_raw_response.list(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_fiat_account = response.parse()
        assert_matches_type(ListExternalFiatAccountsResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.users.external_fiat_accounts.with_streaming_response.list(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_fiat_account = response.parse()
            assert_matches_type(ListExternalFiatAccountsResponse, external_fiat_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.external_fiat_accounts.with_raw_response.list(
                user_id="",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: PrivyAPI) -> None:
        external_fiat_account = client.users.external_fiat_accounts.delete(
            account_id="account_id",
            user_id="user_id",
        )
        assert_matches_type(SuccessResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PrivyAPI) -> None:
        response = client.users.external_fiat_accounts.with_raw_response.delete(
            account_id="account_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_fiat_account = response.parse()
        assert_matches_type(SuccessResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PrivyAPI) -> None:
        with client.users.external_fiat_accounts.with_streaming_response.delete(
            account_id="account_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_fiat_account = response.parse()
            assert_matches_type(SuccessResponse, external_fiat_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.external_fiat_accounts.with_raw_response.delete(
                account_id="account_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.users.external_fiat_accounts.with_raw_response.delete(
                account_id="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        external_fiat_account = client.users.external_fiat_accounts.get(
            account_id="account_id",
            user_id="user_id",
        )
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.users.external_fiat_accounts.with_raw_response.get(
            account_id="account_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_fiat_account = response.parse()
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.users.external_fiat_accounts.with_streaming_response.get(
            account_id="account_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_fiat_account = response.parse()
            assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.external_fiat_accounts.with_raw_response.get(
                account_id="account_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.users.external_fiat_accounts.with_raw_response.get(
                account_id="",
                user_id="user_id",
            )


class TestAsyncExternalFiatAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        external_fiat_account = await async_client.users.external_fiat_accounts.create(
            user_id="user_id",
            account={
                "account_number": "x",
                "routing_number": "xxxxxxxxx",
                "type": "us",
            },
            account_owner_name="xxx",
            currency="currency",
            provider="bridge",
        )
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        external_fiat_account = await async_client.users.external_fiat_accounts.create(
            user_id="user_id",
            account={
                "account_number": "x",
                "routing_number": "xxxxxxxxx",
                "type": "us",
                "checking_or_savings": "checking_or_savings",
            },
            account_owner_name="xxx",
            currency="currency",
            provider="bridge",
            address={
                "city": "x",
                "country": "xxx",
                "street_line_1": "x",
                "postal_code": "x",
                "state": "x",
                "street_line_2": "x",
            },
            bank_name="x",
            environment="sandbox",
        )
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.external_fiat_accounts.with_raw_response.create(
            user_id="user_id",
            account={
                "account_number": "x",
                "routing_number": "xxxxxxxxx",
                "type": "us",
            },
            account_owner_name="xxx",
            currency="currency",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_fiat_account = await response.parse()
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.external_fiat_accounts.with_streaming_response.create(
            user_id="user_id",
            account={
                "account_number": "x",
                "routing_number": "xxxxxxxxx",
                "type": "us",
            },
            account_owner_name="xxx",
            currency="currency",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_fiat_account = await response.parse()
            assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.external_fiat_accounts.with_raw_response.create(
                user_id="",
                account={
                    "account_number": "x",
                    "routing_number": "xxxxxxxxx",
                    "type": "us",
                },
                account_owner_name="xxx",
                currency="currency",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        external_fiat_account = await async_client.users.external_fiat_accounts.list(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(ListExternalFiatAccountsResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        external_fiat_account = await async_client.users.external_fiat_accounts.list(
            user_id="user_id",
            provider="bridge",
            environment="sandbox",
        )
        assert_matches_type(ListExternalFiatAccountsResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.external_fiat_accounts.with_raw_response.list(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_fiat_account = await response.parse()
        assert_matches_type(ListExternalFiatAccountsResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.external_fiat_accounts.with_streaming_response.list(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_fiat_account = await response.parse()
            assert_matches_type(ListExternalFiatAccountsResponse, external_fiat_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.external_fiat_accounts.with_raw_response.list(
                user_id="",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPrivyAPI) -> None:
        external_fiat_account = await async_client.users.external_fiat_accounts.delete(
            account_id="account_id",
            user_id="user_id",
        )
        assert_matches_type(SuccessResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.external_fiat_accounts.with_raw_response.delete(
            account_id="account_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_fiat_account = await response.parse()
        assert_matches_type(SuccessResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.external_fiat_accounts.with_streaming_response.delete(
            account_id="account_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_fiat_account = await response.parse()
            assert_matches_type(SuccessResponse, external_fiat_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.external_fiat_accounts.with_raw_response.delete(
                account_id="account_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.users.external_fiat_accounts.with_raw_response.delete(
                account_id="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        external_fiat_account = await async_client.users.external_fiat_accounts.get(
            account_id="account_id",
            user_id="user_id",
        )
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.external_fiat_accounts.with_raw_response.get(
            account_id="account_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_fiat_account = await response.parse()
        assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.external_fiat_accounts.with_streaming_response.get(
            account_id="account_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_fiat_account = await response.parse()
            assert_matches_type(ExternalFiatAccountResponse, external_fiat_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.external_fiat_accounts.with_raw_response.get(
                account_id="account_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.users.external_fiat_accounts.with_raw_response.get(
                account_id="",
                user_id="user_id",
            )
