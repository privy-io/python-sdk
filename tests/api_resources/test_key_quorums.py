# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import KeyQuorum, SuccessResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeyQuorums:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        key_quorum = client.key_quorums.create()
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        key_quorum = client.key_quorums.create(
            authorization_threshold=1,
            display_name="Prod key quorum",
            key_quorum_ids=["string"],
            public_keys=[
                "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEx4aoeD72yykviK+f/ckqE2CItVIG\n1rCnvC3/XZ1HgpOcMEMialRmTrqIK4oZlYd1RfxU3za/C9yjhboIuoPD3g==",
                "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAErzZtQr/bMIh3Y8f9ZqseB9i/AfjQ\nhu+agbNqXcJy/TfoNqvc/Y3Mh7gIZ8ZLXQEykycx4mYSpqrxp1lBKqsZDQ==",
            ],
            user_ids=["string"],
        )
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.key_quorums.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key_quorum = response.parse()
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.key_quorums.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key_quorum = response.parse()
            assert_matches_type(KeyQuorum, key_quorum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: PrivyAPI) -> None:
        key_quorum = client.key_quorums._delete(
            key_quorum_id="string",
        )
        assert_matches_type(SuccessResponse, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: PrivyAPI) -> None:
        key_quorum = client.key_quorums._delete(
            key_quorum_id="string",
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SuccessResponse, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PrivyAPI) -> None:
        response = client.key_quorums.with_raw_response._delete(
            key_quorum_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key_quorum = response.parse()
        assert_matches_type(SuccessResponse, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PrivyAPI) -> None:
        with client.key_quorums.with_streaming_response._delete(
            key_quorum_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key_quorum = response.parse()
            assert_matches_type(SuccessResponse, key_quorum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_quorum_id` but received ''"):
            client.key_quorums.with_raw_response._delete(
                key_quorum_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: PrivyAPI) -> None:
        key_quorum = client.key_quorums._update(
            key_quorum_id="string",
        )
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PrivyAPI) -> None:
        key_quorum = client.key_quorums._update(
            key_quorum_id="string",
            authorization_threshold=1,
            display_name="Prod key quorum",
            key_quorum_ids=["string"],
            public_keys=[
                "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEx4aoeD72yykviK+f/ckqE2CItVIG\n1rCnvC3/XZ1HgpOcMEMialRmTrqIK4oZlYd1RfxU3za/C9yjhboIuoPD3g=="
            ],
            user_ids=["string"],
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PrivyAPI) -> None:
        response = client.key_quorums.with_raw_response._update(
            key_quorum_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key_quorum = response.parse()
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PrivyAPI) -> None:
        with client.key_quorums.with_streaming_response._update(
            key_quorum_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key_quorum = response.parse()
            assert_matches_type(KeyQuorum, key_quorum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_quorum_id` but received ''"):
            client.key_quorums.with_raw_response._update(
                key_quorum_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        key_quorum = client.key_quorums.get(
            "string",
        )
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.key_quorums.with_raw_response.get(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key_quorum = response.parse()
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.key_quorums.with_streaming_response.get(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key_quorum = response.parse()
            assert_matches_type(KeyQuorum, key_quorum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_quorum_id` but received ''"):
            client.key_quorums.with_raw_response.get(
                "",
            )


class TestAsyncKeyQuorums:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        key_quorum = await async_client.key_quorums.create()
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        key_quorum = await async_client.key_quorums.create(
            authorization_threshold=1,
            display_name="Prod key quorum",
            key_quorum_ids=["string"],
            public_keys=[
                "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEx4aoeD72yykviK+f/ckqE2CItVIG\n1rCnvC3/XZ1HgpOcMEMialRmTrqIK4oZlYd1RfxU3za/C9yjhboIuoPD3g==",
                "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAErzZtQr/bMIh3Y8f9ZqseB9i/AfjQ\nhu+agbNqXcJy/TfoNqvc/Y3Mh7gIZ8ZLXQEykycx4mYSpqrxp1lBKqsZDQ==",
            ],
            user_ids=["string"],
        )
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.key_quorums.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key_quorum = await response.parse()
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.key_quorums.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key_quorum = await response.parse()
            assert_matches_type(KeyQuorum, key_quorum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPrivyAPI) -> None:
        key_quorum = await async_client.key_quorums._delete(
            key_quorum_id="string",
        )
        assert_matches_type(SuccessResponse, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        key_quorum = await async_client.key_quorums._delete(
            key_quorum_id="string",
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(SuccessResponse, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.key_quorums.with_raw_response._delete(
            key_quorum_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key_quorum = await response.parse()
        assert_matches_type(SuccessResponse, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.key_quorums.with_streaming_response._delete(
            key_quorum_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key_quorum = await response.parse()
            assert_matches_type(SuccessResponse, key_quorum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_quorum_id` but received ''"):
            await async_client.key_quorums.with_raw_response._delete(
                key_quorum_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPrivyAPI) -> None:
        key_quorum = await async_client.key_quorums._update(
            key_quorum_id="string",
        )
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        key_quorum = await async_client.key_quorums._update(
            key_quorum_id="string",
            authorization_threshold=1,
            display_name="Prod key quorum",
            key_quorum_ids=["string"],
            public_keys=[
                "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEx4aoeD72yykviK+f/ckqE2CItVIG\n1rCnvC3/XZ1HgpOcMEMialRmTrqIK4oZlYd1RfxU3za/C9yjhboIuoPD3g=="
            ],
            user_ids=["string"],
            privy_authorization_signature="privy-authorization-signature",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.key_quorums.with_raw_response._update(
            key_quorum_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key_quorum = await response.parse()
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.key_quorums.with_streaming_response._update(
            key_quorum_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key_quorum = await response.parse()
            assert_matches_type(KeyQuorum, key_quorum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_quorum_id` but received ''"):
            await async_client.key_quorums.with_raw_response._update(
                key_quorum_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        key_quorum = await async_client.key_quorums.get(
            "string",
        )
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.key_quorums.with_raw_response.get(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key_quorum = await response.parse()
        assert_matches_type(KeyQuorum, key_quorum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.key_quorums.with_streaming_response.get(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key_quorum = await response.parse()
            assert_matches_type(KeyQuorum, key_quorum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_quorum_id` but received ''"):
            await async_client.key_quorums.with_raw_response.get(
                "",
            )
