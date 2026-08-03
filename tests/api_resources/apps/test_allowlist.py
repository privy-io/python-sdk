# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import AllowlistEntry, AllowlistDeletionResponse
from tests.utils import assert_matches_type
from privy.types.apps import AllowlistListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAllowlist:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: PrivyAPI) -> None:
        allowlist = client.apps.allowlist.create(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        )
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: PrivyAPI) -> None:
        response = client.apps.allowlist.with_raw_response.create(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = response.parse()
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: PrivyAPI) -> None:
        with client.apps.allowlist.with_streaming_response.create(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = response.parse()
            assert_matches_type(AllowlistEntry, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.allowlist.with_raw_response.create(
                app_id="",
                type="email",
                value="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: PrivyAPI) -> None:
        allowlist = client.apps.allowlist.create(
            app_id="app_id",
            type="emailDomain",
            value="string",
        )
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: PrivyAPI) -> None:
        response = client.apps.allowlist.with_raw_response.create(
            app_id="app_id",
            type="emailDomain",
            value="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = response.parse()
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: PrivyAPI) -> None:
        with client.apps.allowlist.with_streaming_response.create(
            app_id="app_id",
            type="emailDomain",
            value="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = response.parse()
            assert_matches_type(AllowlistEntry, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.allowlist.with_raw_response.create(
                app_id="",
                type="emailDomain",
                value="string",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: PrivyAPI) -> None:
        allowlist = client.apps.allowlist.create(
            app_id="app_id",
            type="wallet",
            value="value",
        )
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: PrivyAPI) -> None:
        response = client.apps.allowlist.with_raw_response.create(
            app_id="app_id",
            type="wallet",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = response.parse()
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: PrivyAPI) -> None:
        with client.apps.allowlist.with_streaming_response.create(
            app_id="app_id",
            type="wallet",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = response.parse()
            assert_matches_type(AllowlistEntry, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_3(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.allowlist.with_raw_response.create(
                app_id="",
                type="wallet",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: PrivyAPI) -> None:
        allowlist = client.apps.allowlist.create(
            app_id="app_id",
            type="phone",
            value="value",
        )
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: PrivyAPI) -> None:
        response = client.apps.allowlist.with_raw_response.create(
            app_id="app_id",
            type="phone",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = response.parse()
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: PrivyAPI) -> None:
        with client.apps.allowlist.with_streaming_response.create(
            app_id="app_id",
            type="phone",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = response.parse()
            assert_matches_type(AllowlistEntry, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_4(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.allowlist.with_raw_response.create(
                app_id="",
                type="phone",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        allowlist = client.apps.allowlist.list(
            "app_id",
        )
        assert_matches_type(AllowlistListResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.apps.allowlist.with_raw_response.list(
            "app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = response.parse()
        assert_matches_type(AllowlistListResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.apps.allowlist.with_streaming_response.list(
            "app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = response.parse()
            assert_matches_type(AllowlistListResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.allowlist.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_overload_1(self, client: PrivyAPI) -> None:
        allowlist = client.apps.allowlist.delete(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        )
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_overload_1(self, client: PrivyAPI) -> None:
        response = client.apps.allowlist.with_raw_response.delete(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = response.parse()
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_overload_1(self, client: PrivyAPI) -> None:
        with client.apps.allowlist.with_streaming_response.delete(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = response.parse()
            assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_overload_1(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.allowlist.with_raw_response.delete(
                app_id="",
                type="email",
                value="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_overload_2(self, client: PrivyAPI) -> None:
        allowlist = client.apps.allowlist.delete(
            app_id="app_id",
            type="emailDomain",
            value="string",
        )
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_overload_2(self, client: PrivyAPI) -> None:
        response = client.apps.allowlist.with_raw_response.delete(
            app_id="app_id",
            type="emailDomain",
            value="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = response.parse()
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_overload_2(self, client: PrivyAPI) -> None:
        with client.apps.allowlist.with_streaming_response.delete(
            app_id="app_id",
            type="emailDomain",
            value="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = response.parse()
            assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_overload_2(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.allowlist.with_raw_response.delete(
                app_id="",
                type="emailDomain",
                value="string",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_overload_3(self, client: PrivyAPI) -> None:
        allowlist = client.apps.allowlist.delete(
            app_id="app_id",
            type="wallet",
            value="value",
        )
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_overload_3(self, client: PrivyAPI) -> None:
        response = client.apps.allowlist.with_raw_response.delete(
            app_id="app_id",
            type="wallet",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = response.parse()
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_overload_3(self, client: PrivyAPI) -> None:
        with client.apps.allowlist.with_streaming_response.delete(
            app_id="app_id",
            type="wallet",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = response.parse()
            assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_overload_3(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.allowlist.with_raw_response.delete(
                app_id="",
                type="wallet",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_overload_4(self, client: PrivyAPI) -> None:
        allowlist = client.apps.allowlist.delete(
            app_id="app_id",
            type="phone",
            value="value",
        )
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_overload_4(self, client: PrivyAPI) -> None:
        response = client.apps.allowlist.with_raw_response.delete(
            app_id="app_id",
            type="phone",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = response.parse()
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_overload_4(self, client: PrivyAPI) -> None:
        with client.apps.allowlist.with_streaming_response.delete(
            app_id="app_id",
            type="phone",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = response.parse()
            assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_overload_4(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.allowlist.with_raw_response.delete(
                app_id="",
                type="phone",
                value="value",
            )


class TestAsyncAllowlist:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        allowlist = await async_client.apps.allowlist.create(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        )
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.apps.allowlist.with_raw_response.create(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = await response.parse()
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.apps.allowlist.with_streaming_response.create(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = await response.parse()
            assert_matches_type(AllowlistEntry, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.allowlist.with_raw_response.create(
                app_id="",
                type="email",
                value="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        allowlist = await async_client.apps.allowlist.create(
            app_id="app_id",
            type="emailDomain",
            value="string",
        )
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.apps.allowlist.with_raw_response.create(
            app_id="app_id",
            type="emailDomain",
            value="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = await response.parse()
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.apps.allowlist.with_streaming_response.create(
            app_id="app_id",
            type="emailDomain",
            value="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = await response.parse()
            assert_matches_type(AllowlistEntry, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.allowlist.with_raw_response.create(
                app_id="",
                type="emailDomain",
                value="string",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        allowlist = await async_client.apps.allowlist.create(
            app_id="app_id",
            type="wallet",
            value="value",
        )
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.apps.allowlist.with_raw_response.create(
            app_id="app_id",
            type="wallet",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = await response.parse()
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.apps.allowlist.with_streaming_response.create(
            app_id="app_id",
            type="wallet",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = await response.parse()
            assert_matches_type(AllowlistEntry, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.allowlist.with_raw_response.create(
                app_id="",
                type="wallet",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        allowlist = await async_client.apps.allowlist.create(
            app_id="app_id",
            type="phone",
            value="value",
        )
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.apps.allowlist.with_raw_response.create(
            app_id="app_id",
            type="phone",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = await response.parse()
        assert_matches_type(AllowlistEntry, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.apps.allowlist.with_streaming_response.create(
            app_id="app_id",
            type="phone",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = await response.parse()
            assert_matches_type(AllowlistEntry, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.allowlist.with_raw_response.create(
                app_id="",
                type="phone",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        allowlist = await async_client.apps.allowlist.list(
            "app_id",
        )
        assert_matches_type(AllowlistListResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.apps.allowlist.with_raw_response.list(
            "app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = await response.parse()
        assert_matches_type(AllowlistListResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.apps.allowlist.with_streaming_response.list(
            "app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = await response.parse()
            assert_matches_type(AllowlistListResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.allowlist.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        allowlist = await async_client.apps.allowlist.delete(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        )
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.apps.allowlist.with_raw_response.delete(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = await response.parse()
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.apps.allowlist.with_streaming_response.delete(
            app_id="app_id",
            type="email",
            value="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = await response.parse()
            assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.allowlist.with_raw_response.delete(
                app_id="",
                type="email",
                value="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        allowlist = await async_client.apps.allowlist.delete(
            app_id="app_id",
            type="emailDomain",
            value="string",
        )
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.apps.allowlist.with_raw_response.delete(
            app_id="app_id",
            type="emailDomain",
            value="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = await response.parse()
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.apps.allowlist.with_streaming_response.delete(
            app_id="app_id",
            type="emailDomain",
            value="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = await response.parse()
            assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.allowlist.with_raw_response.delete(
                app_id="",
                type="emailDomain",
                value="string",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        allowlist = await async_client.apps.allowlist.delete(
            app_id="app_id",
            type="wallet",
            value="value",
        )
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.apps.allowlist.with_raw_response.delete(
            app_id="app_id",
            type="wallet",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = await response.parse()
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.apps.allowlist.with_streaming_response.delete(
            app_id="app_id",
            type="wallet",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = await response.parse()
            assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.allowlist.with_raw_response.delete(
                app_id="",
                type="wallet",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        allowlist = await async_client.apps.allowlist.delete(
            app_id="app_id",
            type="phone",
            value="value",
        )
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.apps.allowlist.with_raw_response.delete(
            app_id="app_id",
            type="phone",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowlist = await response.parse()
        assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.apps.allowlist.with_streaming_response.delete(
            app_id="app_id",
            type="phone",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowlist = await response.parse()
            assert_matches_type(AllowlistDeletionResponse, allowlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.allowlist.with_raw_response.delete(
                app_id="",
                type="phone",
                value="value",
            )
