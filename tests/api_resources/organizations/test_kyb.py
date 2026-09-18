# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    KyxTosResponse,
    KYBStatusResponse,
    KYBStatusListResponse,
)
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
            client_agreement_id="x",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: PrivyAPI) -> None:
        kyb = client.organizations.kyb.submit(
            organization_id="organization_id",
            data={},
            provider="bridge",
        )
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: PrivyAPI) -> None:
        kyb = client.organizations.kyb.submit(
            organization_id="organization_id",
            data={
                "account_purpose": "treasury_management",
                "account_purpose_other": "x",
                "acting_as_intermediary": True,
                "associated_persons": [
                    {
                        "date_of_birth": "7321-69-10",
                        "email": "dev@stainless.com",
                        "first_name": "x",
                        "has_control": True,
                        "has_ownership": True,
                        "identifying_information": [
                            {
                                "issuing_country": "xxx",
                                "type": "type",
                                "description": "description",
                                "expiration": "expiration",
                                "image_back": "image_back",
                                "image_front": "image_front",
                                "number": "number",
                            }
                        ],
                        "is_signer": True,
                        "last_name": "xx",
                        "residential_address": {
                            "city": "x",
                            "country": "xxx",
                            "street_line_1": "xxxx",
                            "postal_code": "x",
                            "street_line_2": "x",
                            "subdivision": "x",
                        },
                        "documents": [
                            {
                                "file": "x",
                                "purposes": ["proof_of_address"],
                                "description": "x",
                            }
                        ],
                        "is_director": True,
                        "middle_name": "x",
                        "nationalities": ["xxx"],
                        "ownership_percentage": 0,
                        "phone": "phone",
                        "place_of_birth": {
                            "country": "xxx",
                            "city": "x",
                        },
                        "relationship_established_at": "7321-69-10",
                        "title": "x",
                        "transliterated_first_name": "x",
                        "transliterated_last_name": "x",
                        "transliterated_middle_name": "x",
                        "transliterated_residential_address": {
                            "city": "x",
                            "country": "xxx",
                            "street_line_1": "xxxx",
                            "postal_code": "x",
                            "street_line_2": "x",
                            "subdivision": "x",
                        },
                    }
                ],
                "business_description": "x",
                "business_industry": ["x"],
                "business_legal_name": "x",
                "business_trade_name": "x",
                "business_type": "llc",
                "compliance_screening_explanation": "x",
                "conducts_money_services": True,
                "conducts_money_services_description": "x",
                "conducts_money_services_using_bridge": True,
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["business_formation"],
                        "description": "x",
                    }
                ],
                "email": "dev@stainless.com",
                "estimated_annual_revenue_usd": "1000000_9999999",
                "expected_monthly_payments_usd": 0,
                "has_foreign_tax_registration": True,
                "has_material_intermediary_ownership": True,
                "high_risk_activities": ["none_of_the_above"],
                "high_risk_activities_explanation": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                        "description": "description",
                        "expiration": "expiration",
                        "image_back": "image_back",
                        "image_front": "image_front",
                        "number": "number",
                    }
                ],
                "incorporation_date": "7321-69-10",
                "is_dao": True,
                "operates_in_prohibited_countries": True,
                "other_websites": ["string"],
                "ownership_threshold": 5,
                "phone": "phone",
                "physical_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "xxxx",
                    "postal_code": "x",
                    "street_line_2": "x",
                    "subdivision": "x",
                },
                "primary_website": "primary_website",
                "publicly_traded_listings": [
                    {
                        "market_identifier_code": "xxxx",
                        "stock_number": "x",
                        "ticker": "x",
                    }
                ],
                "registered_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "xxxx",
                    "postal_code": "x",
                    "street_line_2": "x",
                    "subdivision": "x",
                },
                "regulated_activity": {
                    "license_number": "x",
                    "primary_regulatory_authority_country": "xxx",
                    "primary_regulatory_authority_name": "x",
                    "regulated_activities_description": "x",
                },
                "source_of_funds": "sales_of_goods_and_services",
                "source_of_funds_description": "x",
                "transliterated_business_legal_name": "x",
                "transliterated_business_trade_name": "x",
                "transliterated_physical_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "xxxx",
                    "postal_code": "x",
                    "street_line_2": "x",
                    "subdivision": "x",
                },
                "transliterated_registered_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "xxxx",
                    "postal_code": "x",
                    "street_line_2": "x",
                    "subdivision": "x",
                },
            },
            provider="bridge",
            client_agreement_id="x",
            endorsements=["sepa"],
            environment="production",
        )
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: PrivyAPI) -> None:
        response = client.organizations.kyb.with_raw_response.submit(
            organization_id="organization_id",
            data={},
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyb = response.parse()
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: PrivyAPI) -> None:
        with client.organizations.kyb.with_streaming_response.submit(
            organization_id="organization_id",
            data={},
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyb = response.parse()
            assert_matches_type(KYBStatusResponse, kyb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.kyb.with_raw_response.submit(
                organization_id="",
                data={},
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
            client_agreement_id="x",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncPrivyAPI) -> None:
        kyb = await async_client.organizations.kyb.submit(
            organization_id="organization_id",
            data={},
            provider="bridge",
        )
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        kyb = await async_client.organizations.kyb.submit(
            organization_id="organization_id",
            data={
                "account_purpose": "treasury_management",
                "account_purpose_other": "x",
                "acting_as_intermediary": True,
                "associated_persons": [
                    {
                        "date_of_birth": "7321-69-10",
                        "email": "dev@stainless.com",
                        "first_name": "x",
                        "has_control": True,
                        "has_ownership": True,
                        "identifying_information": [
                            {
                                "issuing_country": "xxx",
                                "type": "type",
                                "description": "description",
                                "expiration": "expiration",
                                "image_back": "image_back",
                                "image_front": "image_front",
                                "number": "number",
                            }
                        ],
                        "is_signer": True,
                        "last_name": "xx",
                        "residential_address": {
                            "city": "x",
                            "country": "xxx",
                            "street_line_1": "xxxx",
                            "postal_code": "x",
                            "street_line_2": "x",
                            "subdivision": "x",
                        },
                        "documents": [
                            {
                                "file": "x",
                                "purposes": ["proof_of_address"],
                                "description": "x",
                            }
                        ],
                        "is_director": True,
                        "middle_name": "x",
                        "nationalities": ["xxx"],
                        "ownership_percentage": 0,
                        "phone": "phone",
                        "place_of_birth": {
                            "country": "xxx",
                            "city": "x",
                        },
                        "relationship_established_at": "7321-69-10",
                        "title": "x",
                        "transliterated_first_name": "x",
                        "transliterated_last_name": "x",
                        "transliterated_middle_name": "x",
                        "transliterated_residential_address": {
                            "city": "x",
                            "country": "xxx",
                            "street_line_1": "xxxx",
                            "postal_code": "x",
                            "street_line_2": "x",
                            "subdivision": "x",
                        },
                    }
                ],
                "business_description": "x",
                "business_industry": ["x"],
                "business_legal_name": "x",
                "business_trade_name": "x",
                "business_type": "llc",
                "compliance_screening_explanation": "x",
                "conducts_money_services": True,
                "conducts_money_services_description": "x",
                "conducts_money_services_using_bridge": True,
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["business_formation"],
                        "description": "x",
                    }
                ],
                "email": "dev@stainless.com",
                "estimated_annual_revenue_usd": "1000000_9999999",
                "expected_monthly_payments_usd": 0,
                "has_foreign_tax_registration": True,
                "has_material_intermediary_ownership": True,
                "high_risk_activities": ["none_of_the_above"],
                "high_risk_activities_explanation": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                        "description": "description",
                        "expiration": "expiration",
                        "image_back": "image_back",
                        "image_front": "image_front",
                        "number": "number",
                    }
                ],
                "incorporation_date": "7321-69-10",
                "is_dao": True,
                "operates_in_prohibited_countries": True,
                "other_websites": ["string"],
                "ownership_threshold": 5,
                "phone": "phone",
                "physical_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "xxxx",
                    "postal_code": "x",
                    "street_line_2": "x",
                    "subdivision": "x",
                },
                "primary_website": "primary_website",
                "publicly_traded_listings": [
                    {
                        "market_identifier_code": "xxxx",
                        "stock_number": "x",
                        "ticker": "x",
                    }
                ],
                "registered_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "xxxx",
                    "postal_code": "x",
                    "street_line_2": "x",
                    "subdivision": "x",
                },
                "regulated_activity": {
                    "license_number": "x",
                    "primary_regulatory_authority_country": "xxx",
                    "primary_regulatory_authority_name": "x",
                    "regulated_activities_description": "x",
                },
                "source_of_funds": "sales_of_goods_and_services",
                "source_of_funds_description": "x",
                "transliterated_business_legal_name": "x",
                "transliterated_business_trade_name": "x",
                "transliterated_physical_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "xxxx",
                    "postal_code": "x",
                    "street_line_2": "x",
                    "subdivision": "x",
                },
                "transliterated_registered_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "xxxx",
                    "postal_code": "x",
                    "street_line_2": "x",
                    "subdivision": "x",
                },
            },
            provider="bridge",
            client_agreement_id="x",
            endorsements=["sepa"],
            environment="production",
        )
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.organizations.kyb.with_raw_response.submit(
            organization_id="organization_id",
            data={},
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyb = await response.parse()
        assert_matches_type(KYBStatusResponse, kyb, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.organizations.kyb.with_streaming_response.submit(
            organization_id="organization_id",
            data={},
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyb = await response.parse()
            assert_matches_type(KYBStatusResponse, kyb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.kyb.with_raw_response.submit(
                organization_id="",
                data={},
                provider="bridge",
            )
