# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import KyxTosResponse, KYCStatusResponse, KYCStatusListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKYC:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        kyc = client.users.kyc.list(
            "user_id",
        )
        assert_matches_type(KYCStatusListResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.users.kyc.with_raw_response.list(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KYCStatusListResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.users.kyc.with_streaming_response.list(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KYCStatusListResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.kyc.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_links(self, client: PrivyAPI) -> None:
        kyc = client.users.kyc.initiate_links(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(KYCStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_links_with_all_params(self, client: PrivyAPI) -> None:
        kyc = client.users.kyc.initiate_links(
            user_id="user_id",
            provider="bridge",
            client_agreement_id="client_agreement_id",
            email="dev@stainless.com",
            endorsements=["sepa"],
            environment="production",
            redirect_uri="https://example.com",
        )
        assert_matches_type(KYCStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_links(self, client: PrivyAPI) -> None:
        response = client.users.kyc.with_raw_response.initiate_links(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KYCStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_links(self, client: PrivyAPI) -> None:
        with client.users.kyc.with_streaming_response.initiate_links(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KYCStatusResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_initiate_links(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.kyc.with_raw_response.initiate_links(
                user_id="",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_tos(self, client: PrivyAPI) -> None:
        kyc = client.users.kyc.initiate_tos(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(KyxTosResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_tos_with_all_params(self, client: PrivyAPI) -> None:
        kyc = client.users.kyc.initiate_tos(
            user_id="user_id",
            provider="bridge",
            email="dev@stainless.com",
            environment="production",
        )
        assert_matches_type(KyxTosResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_tos(self, client: PrivyAPI) -> None:
        response = client.users.kyc.with_raw_response.initiate_tos(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KyxTosResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_tos(self, client: PrivyAPI) -> None:
        with client.users.kyc.with_streaming_response.initiate_tos(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KyxTosResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_initiate_tos(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.kyc.with_raw_response.initiate_tos(
                user_id="",
                provider="bridge",
            )


class TestAsyncKYC:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.users.kyc.list(
            "user_id",
        )
        assert_matches_type(KYCStatusListResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.kyc.with_raw_response.list(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KYCStatusListResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.kyc.with_streaming_response.list(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KYCStatusListResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.kyc.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_links(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.users.kyc.initiate_links(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(KYCStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_links_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.users.kyc.initiate_links(
            user_id="user_id",
            provider="bridge",
            client_agreement_id="client_agreement_id",
            email="dev@stainless.com",
            endorsements=["sepa"],
            environment="production",
            redirect_uri="https://example.com",
        )
        assert_matches_type(KYCStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_links(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.kyc.with_raw_response.initiate_links(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KYCStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_links(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.kyc.with_streaming_response.initiate_links(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KYCStatusResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_initiate_links(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.kyc.with_raw_response.initiate_links(
                user_id="",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_tos(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.users.kyc.initiate_tos(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(KyxTosResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_tos_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.users.kyc.initiate_tos(
            user_id="user_id",
            provider="bridge",
            email="dev@stainless.com",
            environment="production",
        )
        assert_matches_type(KyxTosResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_tos(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.kyc.with_raw_response.initiate_tos(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KyxTosResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_tos(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.kyc.with_streaming_response.initiate_tos(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KyxTosResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_initiate_tos(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.kyc.with_raw_response.initiate_tos(
                user_id="",
                provider="bridge",
            )
