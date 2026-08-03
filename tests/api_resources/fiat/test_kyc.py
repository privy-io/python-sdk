# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import OnrampKYCResponse
from tests.utils import assert_matches_type
from privy.types.fiat import KYCGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKYC:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: PrivyAPI) -> None:
        kyc = client.fiat.kyc.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: PrivyAPI) -> None:
        kyc = client.fiat.kyc.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
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
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "type": "individual",
                "account_purpose": "account_purpose",
                "account_purpose_other": "account_purpose_other",
                "acting_as_intermediary": "acting_as_intermediary",
                "completed_customer_safety_check_at": "completed_customer_safety_check_at",
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["x"],
                        "description": "x",
                    }
                ],
                "employment_status": "employment_status",
                "endorsements": ["string"],
                "expected_monthly_payments_usd": "expected_monthly_payments_usd",
                "has_accepted_terms_of_service": True,
                "has_signed_terms_of_service": True,
                "kyc_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "middle_name": "x",
                "most_recent_occupation": "most_recent_occupation",
                "nationality": "xxx",
                "ofac_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "phone": "xx",
                "signed_agreement_id": "x",
                "source_of_funds": "source_of_funds",
                "transliterated_first_name": "x",
                "transliterated_last_name": "x",
                "transliterated_middle_name": "x",
                "transliterated_residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "verified_selfie_at": "verified_selfie_at",
            },
            provider="bridge",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: PrivyAPI) -> None:
        response = client.fiat.kyc.with_raw_response.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: PrivyAPI) -> None:
        with client.fiat.kyc.with_streaming_response.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.kyc.with_raw_response.create(
                user_id="",
                data={
                    "birth_date": "xxxxxxxxxx",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "identifying_information": [
                        {
                            "issuing_country": "xxx",
                            "type": "type",
                        }
                    ],
                    "last_name": "x",
                    "residential_address": {
                        "city": "x",
                        "country": "xxx",
                        "street_line_1": "x",
                        "subdivision": "x",
                    },
                    "type": "individual",
                },
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: PrivyAPI) -> None:
        kyc = client.fiat.kyc.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: PrivyAPI) -> None:
        kyc = client.fiat.kyc.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
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
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "type": "individual",
                "account_purpose": "account_purpose",
                "account_purpose_other": "account_purpose_other",
                "acting_as_intermediary": "acting_as_intermediary",
                "completed_customer_safety_check_at": "completed_customer_safety_check_at",
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["x"],
                        "description": "x",
                    }
                ],
                "employment_status": "employment_status",
                "endorsements": ["string"],
                "expected_monthly_payments_usd": "expected_monthly_payments_usd",
                "has_accepted_terms_of_service": True,
                "has_signed_terms_of_service": True,
                "kyc_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "middle_name": "x",
                "most_recent_occupation": "most_recent_occupation",
                "nationality": "xxx",
                "ofac_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "phone": "xx",
                "signed_agreement_id": "x",
                "source_of_funds": "source_of_funds",
                "transliterated_first_name": "x",
                "transliterated_last_name": "x",
                "transliterated_middle_name": "x",
                "transliterated_residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "verified_selfie_at": "verified_selfie_at",
            },
            provider="bridge-sandbox",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: PrivyAPI) -> None:
        response = client.fiat.kyc.with_raw_response.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: PrivyAPI) -> None:
        with client.fiat.kyc.with_streaming_response.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.kyc.with_raw_response.create(
                user_id="",
                data={
                    "birth_date": "xxxxxxxxxx",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "identifying_information": [
                        {
                            "issuing_country": "xxx",
                            "type": "type",
                        }
                    ],
                    "last_name": "x",
                    "residential_address": {
                        "city": "x",
                        "country": "xxx",
                        "street_line_1": "x",
                        "subdivision": "x",
                    },
                    "type": "individual",
                },
                provider="bridge-sandbox",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: PrivyAPI) -> None:
        kyc = client.fiat.kyc.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: PrivyAPI) -> None:
        kyc = client.fiat.kyc.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
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
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "type": "individual",
                "account_purpose": "account_purpose",
                "account_purpose_other": "account_purpose_other",
                "acting_as_intermediary": "acting_as_intermediary",
                "completed_customer_safety_check_at": "completed_customer_safety_check_at",
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["x"],
                        "description": "x",
                    }
                ],
                "employment_status": "employment_status",
                "endorsements": ["string"],
                "expected_monthly_payments_usd": "expected_monthly_payments_usd",
                "has_accepted_terms_of_service": True,
                "has_signed_terms_of_service": True,
                "kyc_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "middle_name": "x",
                "most_recent_occupation": "most_recent_occupation",
                "nationality": "xxx",
                "ofac_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "phone": "xx",
                "signed_agreement_id": "x",
                "source_of_funds": "source_of_funds",
                "transliterated_first_name": "x",
                "transliterated_last_name": "x",
                "transliterated_middle_name": "x",
                "transliterated_residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "verified_selfie_at": "verified_selfie_at",
            },
            provider="bridge",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: PrivyAPI) -> None:
        response = client.fiat.kyc.with_raw_response.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: PrivyAPI) -> None:
        with client.fiat.kyc.with_streaming_response.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.kyc.with_raw_response.update(
                user_id="",
                data={
                    "birth_date": "xxxxxxxxxx",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "identifying_information": [
                        {
                            "issuing_country": "xxx",
                            "type": "type",
                        }
                    ],
                    "last_name": "x",
                    "residential_address": {
                        "city": "x",
                        "country": "xxx",
                        "street_line_1": "x",
                        "subdivision": "x",
                    },
                    "type": "individual",
                },
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: PrivyAPI) -> None:
        kyc = client.fiat.kyc.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: PrivyAPI) -> None:
        kyc = client.fiat.kyc.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
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
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "type": "individual",
                "account_purpose": "account_purpose",
                "account_purpose_other": "account_purpose_other",
                "acting_as_intermediary": "acting_as_intermediary",
                "completed_customer_safety_check_at": "completed_customer_safety_check_at",
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["x"],
                        "description": "x",
                    }
                ],
                "employment_status": "employment_status",
                "endorsements": ["string"],
                "expected_monthly_payments_usd": "expected_monthly_payments_usd",
                "has_accepted_terms_of_service": True,
                "has_signed_terms_of_service": True,
                "kyc_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "middle_name": "x",
                "most_recent_occupation": "most_recent_occupation",
                "nationality": "xxx",
                "ofac_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "phone": "xx",
                "signed_agreement_id": "x",
                "source_of_funds": "source_of_funds",
                "transliterated_first_name": "x",
                "transliterated_last_name": "x",
                "transliterated_middle_name": "x",
                "transliterated_residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "verified_selfie_at": "verified_selfie_at",
            },
            provider="bridge-sandbox",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: PrivyAPI) -> None:
        response = client.fiat.kyc.with_raw_response.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: PrivyAPI) -> None:
        with client.fiat.kyc.with_streaming_response.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.kyc.with_raw_response.update(
                user_id="",
                data={
                    "birth_date": "xxxxxxxxxx",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "identifying_information": [
                        {
                            "issuing_country": "xxx",
                            "type": "type",
                        }
                    ],
                    "last_name": "x",
                    "residential_address": {
                        "city": "x",
                        "country": "xxx",
                        "street_line_1": "x",
                        "subdivision": "x",
                    },
                    "type": "individual",
                },
                provider="bridge-sandbox",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        kyc = client.fiat.kyc.get(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(KYCGetResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.fiat.kyc.with_raw_response.get(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KYCGetResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.fiat.kyc.with_streaming_response.get(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KYCGetResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fiat.kyc.with_raw_response.get(
                user_id="",
                provider="bridge",
            )


class TestAsyncKYC:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.fiat.kyc.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.fiat.kyc.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
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
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "type": "individual",
                "account_purpose": "account_purpose",
                "account_purpose_other": "account_purpose_other",
                "acting_as_intermediary": "acting_as_intermediary",
                "completed_customer_safety_check_at": "completed_customer_safety_check_at",
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["x"],
                        "description": "x",
                    }
                ],
                "employment_status": "employment_status",
                "endorsements": ["string"],
                "expected_monthly_payments_usd": "expected_monthly_payments_usd",
                "has_accepted_terms_of_service": True,
                "has_signed_terms_of_service": True,
                "kyc_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "middle_name": "x",
                "most_recent_occupation": "most_recent_occupation",
                "nationality": "xxx",
                "ofac_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "phone": "xx",
                "signed_agreement_id": "x",
                "source_of_funds": "source_of_funds",
                "transliterated_first_name": "x",
                "transliterated_last_name": "x",
                "transliterated_middle_name": "x",
                "transliterated_residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "verified_selfie_at": "verified_selfie_at",
            },
            provider="bridge",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.kyc.with_raw_response.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.kyc.with_streaming_response.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.kyc.with_raw_response.create(
                user_id="",
                data={
                    "birth_date": "xxxxxxxxxx",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "identifying_information": [
                        {
                            "issuing_country": "xxx",
                            "type": "type",
                        }
                    ],
                    "last_name": "x",
                    "residential_address": {
                        "city": "x",
                        "country": "xxx",
                        "street_line_1": "x",
                        "subdivision": "x",
                    },
                    "type": "individual",
                },
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.fiat.kyc.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.fiat.kyc.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
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
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "type": "individual",
                "account_purpose": "account_purpose",
                "account_purpose_other": "account_purpose_other",
                "acting_as_intermediary": "acting_as_intermediary",
                "completed_customer_safety_check_at": "completed_customer_safety_check_at",
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["x"],
                        "description": "x",
                    }
                ],
                "employment_status": "employment_status",
                "endorsements": ["string"],
                "expected_monthly_payments_usd": "expected_monthly_payments_usd",
                "has_accepted_terms_of_service": True,
                "has_signed_terms_of_service": True,
                "kyc_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "middle_name": "x",
                "most_recent_occupation": "most_recent_occupation",
                "nationality": "xxx",
                "ofac_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "phone": "xx",
                "signed_agreement_id": "x",
                "source_of_funds": "source_of_funds",
                "transliterated_first_name": "x",
                "transliterated_last_name": "x",
                "transliterated_middle_name": "x",
                "transliterated_residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "verified_selfie_at": "verified_selfie_at",
            },
            provider="bridge-sandbox",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.kyc.with_raw_response.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.kyc.with_streaming_response.create(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.kyc.with_raw_response.create(
                user_id="",
                data={
                    "birth_date": "xxxxxxxxxx",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "identifying_information": [
                        {
                            "issuing_country": "xxx",
                            "type": "type",
                        }
                    ],
                    "last_name": "x",
                    "residential_address": {
                        "city": "x",
                        "country": "xxx",
                        "street_line_1": "x",
                        "subdivision": "x",
                    },
                    "type": "individual",
                },
                provider="bridge-sandbox",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.fiat.kyc.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.fiat.kyc.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
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
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "type": "individual",
                "account_purpose": "account_purpose",
                "account_purpose_other": "account_purpose_other",
                "acting_as_intermediary": "acting_as_intermediary",
                "completed_customer_safety_check_at": "completed_customer_safety_check_at",
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["x"],
                        "description": "x",
                    }
                ],
                "employment_status": "employment_status",
                "endorsements": ["string"],
                "expected_monthly_payments_usd": "expected_monthly_payments_usd",
                "has_accepted_terms_of_service": True,
                "has_signed_terms_of_service": True,
                "kyc_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "middle_name": "x",
                "most_recent_occupation": "most_recent_occupation",
                "nationality": "xxx",
                "ofac_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "phone": "xx",
                "signed_agreement_id": "x",
                "source_of_funds": "source_of_funds",
                "transliterated_first_name": "x",
                "transliterated_last_name": "x",
                "transliterated_middle_name": "x",
                "transliterated_residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "verified_selfie_at": "verified_selfie_at",
            },
            provider="bridge",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.kyc.with_raw_response.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.kyc.with_streaming_response.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.kyc.with_raw_response.update(
                user_id="",
                data={
                    "birth_date": "xxxxxxxxxx",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "identifying_information": [
                        {
                            "issuing_country": "xxx",
                            "type": "type",
                        }
                    ],
                    "last_name": "x",
                    "residential_address": {
                        "city": "x",
                        "country": "xxx",
                        "street_line_1": "x",
                        "subdivision": "x",
                    },
                    "type": "individual",
                },
                provider="bridge",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.fiat.kyc.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.fiat.kyc.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
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
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "type": "individual",
                "account_purpose": "account_purpose",
                "account_purpose_other": "account_purpose_other",
                "acting_as_intermediary": "acting_as_intermediary",
                "completed_customer_safety_check_at": "completed_customer_safety_check_at",
                "documents": [
                    {
                        "file": "x",
                        "purposes": ["x"],
                        "description": "x",
                    }
                ],
                "employment_status": "employment_status",
                "endorsements": ["string"],
                "expected_monthly_payments_usd": "expected_monthly_payments_usd",
                "has_accepted_terms_of_service": True,
                "has_signed_terms_of_service": True,
                "kyc_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "middle_name": "x",
                "most_recent_occupation": "most_recent_occupation",
                "nationality": "xxx",
                "ofac_screen": {
                    "result": "passed",
                    "screened_at": "7321-69-10",
                },
                "phone": "xx",
                "signed_agreement_id": "x",
                "source_of_funds": "source_of_funds",
                "transliterated_first_name": "x",
                "transliterated_last_name": "x",
                "transliterated_middle_name": "x",
                "transliterated_residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                    "postal_code": "x",
                    "street_line_2": "x",
                },
                "verified_selfie_at": "verified_selfie_at",
            },
            provider="bridge-sandbox",
        )
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.kyc.with_raw_response.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.kyc.with_streaming_response.update(
            user_id="user_id",
            data={
                "birth_date": "xxxxxxxxxx",
                "email": "dev@stainless.com",
                "first_name": "x",
                "identifying_information": [
                    {
                        "issuing_country": "xxx",
                        "type": "type",
                    }
                ],
                "last_name": "x",
                "residential_address": {
                    "city": "x",
                    "country": "xxx",
                    "street_line_1": "x",
                    "subdivision": "x",
                },
                "type": "individual",
            },
            provider="bridge-sandbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(OnrampKYCResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.kyc.with_raw_response.update(
                user_id="",
                data={
                    "birth_date": "xxxxxxxxxx",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "identifying_information": [
                        {
                            "issuing_country": "xxx",
                            "type": "type",
                        }
                    ],
                    "last_name": "x",
                    "residential_address": {
                        "city": "x",
                        "country": "xxx",
                        "street_line_1": "x",
                        "subdivision": "x",
                    },
                    "type": "individual",
                },
                provider="bridge-sandbox",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        kyc = await async_client.fiat.kyc.get(
            user_id="user_id",
            provider="bridge",
        )
        assert_matches_type(KYCGetResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.fiat.kyc.with_raw_response.get(
            user_id="user_id",
            provider="bridge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KYCGetResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.fiat.kyc.with_streaming_response.get(
            user_id="user_id",
            provider="bridge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KYCGetResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fiat.kyc.with_raw_response.get(
                user_id="",
                provider="bridge",
            )
