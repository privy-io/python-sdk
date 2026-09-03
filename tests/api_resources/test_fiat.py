# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    FiatGetStatusResponse,
    FiatGetKYCLinkResponse,
    FiatConfigureAppResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_configure_app(self, client: PrivyAPI) -> None:
        fiat = client.fiat.configure_app(
            app_id="app_id",
            api_key="insert-api-key",
            provider="bridge-sandbox",
        )
        assert_matches_type(FiatConfigureAppResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_configure_app(self, client: PrivyAPI) -> None:
        response = client.fiat.with_raw_response.configure_app(
            app_id="app_id",
            api_key="insert-api-key",
            provider="bridge-sandbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = response.parse()
        assert_matches_type(FiatConfigureAppResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_configure_app(self, client: PrivyAPI) -> None:
        with client.fiat.with_streaming_response.configure_app(
            app_id="app_id",
            api_key="insert-api-key",
            provider="bridge-sandbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = response.parse()
            assert_matches_type(FiatConfigureAppResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_configure_app(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.fiat.with_raw_response.configure_app(
                app_id="",
                api_key="insert-api-key",
                provider="bridge-sandbox",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_kyc_link(self, client: PrivyAPI) -> None:
        fiat = client.fiat.get_kyc_link(
            user_id="user_id",
            email="dev@stainless.com",
            provider="bridge",
        )
        assert_matches_type(FiatGetKYCLinkResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_kyc_link_with_all_params(self, client: PrivyAPI) -> None:
        fiat = client.fiat.get_kyc_link(
            user_id="user_id",
            email="dev@stainless.com",
            provider="bridge",
            endorsements=["sepa"],
            full_name="full_name",
            redirect_uri="redirect_uri",
            type="individual",
        )
        assert_matches_type(FiatGetKYCLinkResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_kyc_link(self, client: PrivyAPI) -> None:
        response = client.fiat.with_raw_response.get_kyc_link(
            user_id="user_id",
            email="dev@stainless.com",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = response.parse()
        assert_matches_type(FiatGetKYCLinkResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_kyc_link(self, client: PrivyAPI) -> None:
        with client.fiat.with_streaming_response.get_kyc_link(
            user_id="user_id",
            email="dev@stainless.com",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = response.parse()
            assert_matches_type(FiatGetKYCLinkResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_kyc_link(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.with_raw_response.get_kyc_link(
                user_id="",
                email="dev@stainless.com",
                provider="bridge",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_status(self, client: PrivyAPI) -> None:
        fiat = client.fiat.get_status(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(FiatGetStatusResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_status(self, client: PrivyAPI) -> None:
        response = client.fiat.with_raw_response.get_status(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = response.parse()
        assert_matches_type(FiatGetStatusResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_status(self, client: PrivyAPI) -> None:
        with client.fiat.with_streaming_response.get_status(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = response.parse()
            assert_matches_type(FiatGetStatusResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_status(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.with_raw_response.get_status(
                user_id="",
                provider="bridge",
            )


class TestAsyncFiat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_configure_app(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.fiat.configure_app(
            app_id="app_id",
            api_key="insert-api-key",
            provider="bridge-sandbox",
        )
        assert_matches_type(FiatConfigureAppResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_configure_app(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.with_raw_response.configure_app(
            app_id="app_id",
            api_key="insert-api-key",
            provider="bridge-sandbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = await response.parse()
        assert_matches_type(FiatConfigureAppResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_configure_app(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.with_streaming_response.configure_app(
            app_id="app_id",
            api_key="insert-api-key",
            provider="bridge-sandbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = await response.parse()
            assert_matches_type(FiatConfigureAppResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_configure_app(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.fiat.with_raw_response.configure_app(
                app_id="",
                api_key="insert-api-key",
                provider="bridge-sandbox",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_kyc_link(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.fiat.get_kyc_link(
            user_id="user_id",
            email="dev@stainless.com",
            provider="bridge",
        )
        assert_matches_type(FiatGetKYCLinkResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_kyc_link_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.fiat.get_kyc_link(
            user_id="user_id",
            email="dev@stainless.com",
            provider="bridge",
            endorsements=["sepa"],
            full_name="full_name",
            redirect_uri="redirect_uri",
            type="individual",
        )
        assert_matches_type(FiatGetKYCLinkResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_kyc_link(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.with_raw_response.get_kyc_link(
            user_id="user_id",
            email="dev@stainless.com",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = await response.parse()
        assert_matches_type(FiatGetKYCLinkResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_kyc_link(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.with_streaming_response.get_kyc_link(
            user_id="user_id",
            email="dev@stainless.com",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = await response.parse()
            assert_matches_type(FiatGetKYCLinkResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_kyc_link(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.with_raw_response.get_kyc_link(
                user_id="",
                email="dev@stainless.com",
                provider="bridge",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_status(self, async_client: AsyncPrivyAPI) -> None:
        fiat = await async_client.fiat.get_status(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(FiatGetStatusResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.with_raw_response.get_status(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fiat = await response.parse()
        assert_matches_type(FiatGetStatusResponse, fiat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.with_streaming_response.get_status(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fiat = await response.parse()
            assert_matches_type(FiatGetStatusResponse, fiat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.with_raw_response.get_status(
                user_id="",
                provider="bridge",
            )
