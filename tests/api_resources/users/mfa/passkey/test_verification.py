# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from tests.utils import assert_matches_type
from privy.types.users import (
    MfaVerificationResponse,
    PasskeyMfaVerificationInitResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_init(self, client: PrivyAPI) -> None:
        verification = client.users.mfa.passkey.verification.init(
            user_id="user_id",
            relying_party="https://example.com",
            privy_user_token="x",
        )
        assert_matches_type(PasskeyMfaVerificationInitResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_init(self, client: PrivyAPI) -> None:
        response = client.users.mfa.passkey.verification.with_raw_response.init(
            user_id="user_id",
            relying_party="https://example.com",
            privy_user_token="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(PasskeyMfaVerificationInitResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_init(self, client: PrivyAPI) -> None:
        with client.users.mfa.passkey.verification.with_streaming_response.init(
            user_id="user_id",
            relying_party="https://example.com",
            privy_user_token="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(PasskeyMfaVerificationInitResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_init(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.mfa.passkey.verification.with_raw_response.init(
                user_id="",
                relying_party="https://example.com",
                privy_user_token="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: PrivyAPI) -> None:
        verification = client.users.mfa.passkey.verification.verify(
            user_id="user_id",
            credential={
                "id": "id",
                "client_extension_results": {},
                "raw_id": "raw_id",
                "response": {
                    "authenticator_data": "authenticator_data",
                    "client_data_json": "client_data_json",
                    "signature": "signature",
                },
                "type": "public-key",
            },
            privy_user_token="x",
        )
        assert_matches_type(MfaVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_with_all_params(self, client: PrivyAPI) -> None:
        verification = client.users.mfa.passkey.verification.verify(
            user_id="user_id",
            credential={
                "id": "id",
                "client_extension_results": {
                    "app_id": True,
                    "cred_props": {"rk": True},
                    "hmac_create_secret": True,
                },
                "raw_id": "raw_id",
                "response": {
                    "authenticator_data": "authenticator_data",
                    "client_data_json": "client_data_json",
                    "signature": "signature",
                    "user_handle": "user_handle",
                },
                "type": "public-key",
                "authenticator_attachment": "authenticator_attachment",
            },
            privy_user_token="x",
        )
        assert_matches_type(MfaVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: PrivyAPI) -> None:
        response = client.users.mfa.passkey.verification.with_raw_response.verify(
            user_id="user_id",
            credential={
                "id": "id",
                "client_extension_results": {},
                "raw_id": "raw_id",
                "response": {
                    "authenticator_data": "authenticator_data",
                    "client_data_json": "client_data_json",
                    "signature": "signature",
                },
                "type": "public-key",
            },
            privy_user_token="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(MfaVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: PrivyAPI) -> None:
        with client.users.mfa.passkey.verification.with_streaming_response.verify(
            user_id="user_id",
            credential={
                "id": "id",
                "client_extension_results": {},
                "raw_id": "raw_id",
                "response": {
                    "authenticator_data": "authenticator_data",
                    "client_data_json": "client_data_json",
                    "signature": "signature",
                },
                "type": "public-key",
            },
            privy_user_token="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(MfaVerificationResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_verify(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.mfa.passkey.verification.with_raw_response.verify(
                user_id="",
                credential={
                    "id": "id",
                    "client_extension_results": {},
                    "raw_id": "raw_id",
                    "response": {
                        "authenticator_data": "authenticator_data",
                        "client_data_json": "client_data_json",
                        "signature": "signature",
                    },
                    "type": "public-key",
                },
                privy_user_token="x",
            )


class TestAsyncVerification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_init(self, async_client: AsyncPrivyAPI) -> None:
        verification = await async_client.users.mfa.passkey.verification.init(
            user_id="user_id",
            relying_party="https://example.com",
            privy_user_token="x",
        )
        assert_matches_type(PasskeyMfaVerificationInitResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_init(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.mfa.passkey.verification.with_raw_response.init(
            user_id="user_id",
            relying_party="https://example.com",
            privy_user_token="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(PasskeyMfaVerificationInitResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_init(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.mfa.passkey.verification.with_streaming_response.init(
            user_id="user_id",
            relying_party="https://example.com",
            privy_user_token="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(PasskeyMfaVerificationInitResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_init(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.mfa.passkey.verification.with_raw_response.init(
                user_id="",
                relying_party="https://example.com",
                privy_user_token="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncPrivyAPI) -> None:
        verification = await async_client.users.mfa.passkey.verification.verify(
            user_id="user_id",
            credential={
                "id": "id",
                "client_extension_results": {},
                "raw_id": "raw_id",
                "response": {
                    "authenticator_data": "authenticator_data",
                    "client_data_json": "client_data_json",
                    "signature": "signature",
                },
                "type": "public-key",
            },
            privy_user_token="x",
        )
        assert_matches_type(MfaVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        verification = await async_client.users.mfa.passkey.verification.verify(
            user_id="user_id",
            credential={
                "id": "id",
                "client_extension_results": {
                    "app_id": True,
                    "cred_props": {"rk": True},
                    "hmac_create_secret": True,
                },
                "raw_id": "raw_id",
                "response": {
                    "authenticator_data": "authenticator_data",
                    "client_data_json": "client_data_json",
                    "signature": "signature",
                    "user_handle": "user_handle",
                },
                "type": "public-key",
                "authenticator_attachment": "authenticator_attachment",
            },
            privy_user_token="x",
        )
        assert_matches_type(MfaVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.mfa.passkey.verification.with_raw_response.verify(
            user_id="user_id",
            credential={
                "id": "id",
                "client_extension_results": {},
                "raw_id": "raw_id",
                "response": {
                    "authenticator_data": "authenticator_data",
                    "client_data_json": "client_data_json",
                    "signature": "signature",
                },
                "type": "public-key",
            },
            privy_user_token="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(MfaVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.mfa.passkey.verification.with_streaming_response.verify(
            user_id="user_id",
            credential={
                "id": "id",
                "client_extension_results": {},
                "raw_id": "raw_id",
                "response": {
                    "authenticator_data": "authenticator_data",
                    "client_data_json": "client_data_json",
                    "signature": "signature",
                },
                "type": "public-key",
            },
            privy_user_token="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(MfaVerificationResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_verify(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.mfa.passkey.verification.with_raw_response.verify(
                user_id="",
                credential={
                    "id": "id",
                    "client_extension_results": {},
                    "raw_id": "raw_id",
                    "response": {
                        "authenticator_data": "authenticator_data",
                        "client_data_json": "client_data_json",
                        "signature": "signature",
                    },
                    "type": "public-key",
                },
                privy_user_token="x",
            )
