# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import KyxTosResponse, KYBStatusResponse, KYBStatusListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKYB:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        kyb = client.organizations.kyb.list(
            "organization_id",
        )
        assert_matches_type(KYBStatusListResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.organizations.kyb.with_raw_response.list(
            "organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyb = response.parse()
        assert_matches_type(KYBStatusListResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.organizations.kyb.with_streaming_response.list(
            "organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyb = response.parse()
            assert_matches_type(KYBStatusListResponse, kyb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.kyb.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_links(self, client: PrivyAPI) -> None:
        kyb = client.organizations.kyb.initiate_links(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        )
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_links_with_all_params(self, client: PrivyAPI) -> None:
        kyb = client.organizations.kyb.initiate_links(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
            business_name="x",
            client_agreement_id="client_agreement_id",
            endorsements=["sepa"],
            environment="production",
            redirect_uri="https://example.com",
        )
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_links(self, client: PrivyAPI) -> None:
        response = client.organizations.kyb.with_raw_response.initiate_links(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyb = response.parse()
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_links(self, client: PrivyAPI) -> None:
        with client.organizations.kyb.with_streaming_response.initiate_links(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyb = response.parse()
            assert_matches_type(KYBStatusResponse, kyb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_initiate_links(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.kyb.with_raw_response.initiate_links(
                organization_id="",
                email="dev@stainless.com",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_tos(self, client: PrivyAPI) -> None:
        kyb = client.organizations.kyb.initiate_tos(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        )
        assert_matches_type(KyxTosResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_tos_with_all_params(self, client: PrivyAPI) -> None:
        kyb = client.organizations.kyb.initiate_tos(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
            business_name="x",
            environment="production",
        )
        assert_matches_type(KyxTosResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_tos(self, client: PrivyAPI) -> None:
        response = client.organizations.kyb.with_raw_response.initiate_tos(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyb = response.parse()
        assert_matches_type(KyxTosResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_tos(self, client: PrivyAPI) -> None:
        with client.organizations.kyb.with_streaming_response.initiate_tos(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyb = response.parse()
            assert_matches_type(KyxTosResponse, kyb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_initiate_tos(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.kyb.with_raw_response.initiate_tos(
                organization_id="",
                email="dev@stainless.com",
                provider="bridge",
            )


class TestAsyncKYB:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        kyb = await async_client.organizations.kyb.list(
            "organization_id",
        )
        assert_matches_type(KYBStatusListResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.organizations.kyb.with_raw_response.list(
            "organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyb = await response.parse()
        assert_matches_type(KYBStatusListResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.organizations.kyb.with_streaming_response.list(
            "organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyb = await response.parse()
            assert_matches_type(KYBStatusListResponse, kyb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.kyb.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_links(self, async_client: AsyncPrivyAPI) -> None:
        kyb = await async_client.organizations.kyb.initiate_links(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        )
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_links_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        kyb = await async_client.organizations.kyb.initiate_links(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
            business_name="x",
            client_agreement_id="client_agreement_id",
            endorsements=["sepa"],
            environment="production",
            redirect_uri="https://example.com",
        )
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_links(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.organizations.kyb.with_raw_response.initiate_links(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyb = await response.parse()
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_links(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.organizations.kyb.with_streaming_response.initiate_links(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyb = await response.parse()
            assert_matches_type(KYBStatusResponse, kyb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_initiate_links(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.kyb.with_raw_response.initiate_links(
                organization_id="",
                email="dev@stainless.com",
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_tos(self, async_client: AsyncPrivyAPI) -> None:
        kyb = await async_client.organizations.kyb.initiate_tos(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        )
        assert_matches_type(KyxTosResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_tos_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        kyb = await async_client.organizations.kyb.initiate_tos(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
            business_name="x",
            environment="production",
        )
        assert_matches_type(KyxTosResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_tos(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.organizations.kyb.with_raw_response.initiate_tos(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyb = await response.parse()
        assert_matches_type(KyxTosResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_tos(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.organizations.kyb.with_streaming_response.initiate_tos(
            organization_id="organization_id",
            email="dev@stainless.com",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyb = await response.parse()
            assert_matches_type(KyxTosResponse, kyb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_initiate_tos(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.kyb.with_raw_response.initiate_tos(
                organization_id="",
                email="dev@stainless.com",
                provider="bridge",
            )
