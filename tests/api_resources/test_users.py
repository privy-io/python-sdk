# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    User,
    UserCreateCustomMetadataResponse,
)
from tests.utils import assert_matches_type
from privy.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        user = client.users.create(
            linked_accounts=[
                {
                    "address": "tom.bombadill@privy.io",
                    "type": "email",
                }
            ],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        user = client.users.create(
            linked_accounts=[
                {
                    "address": "tom.bombadill@privy.io",
                    "type": "email",
                }
            ],
            custom_metadata={"foo": "string"},
            wallets=[
                {
                    "chain_type": "solana",
                    "additional_signers": [
                        {
                            "signer_id": "signer_id",
                            "override_policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                        }
                    ],
                    "create_smart_wallet": True,
                    "policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                }
            ],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.create(
            linked_accounts=[
                {
                    "address": "tom.bombadill@privy.io",
                    "type": "email",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.create(
            linked_accounts=[
                {
                    "address": "tom.bombadill@privy.io",
                    "type": "email",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        user = client.users.list()
        assert_matches_type(SyncCursor[User], user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: PrivyAPI) -> None:
        user = client.users.list(
            cursor="x",
            limit=100,
        )
        assert_matches_type(SyncCursor[User], user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncCursor[User], user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncCursor[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: PrivyAPI) -> None:
        user = client.users.delete(
            "user_id",
        )
        assert user is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_custom_metadata(self, client: PrivyAPI) -> None:
        user = client.users.create_custom_metadata(
            "user_id",
        )
        assert_matches_type(UserCreateCustomMetadataResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_custom_metadata(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.create_custom_metadata(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateCustomMetadataResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_custom_metadata(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.create_custom_metadata(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateCustomMetadataResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_custom_metadata(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.create_custom_metadata(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        user = client.users.get(
            "user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_email_address(self, client: PrivyAPI) -> None:
        user = client.users.get_by_email_address(
            address="dev@stainless.com",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_email_address(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_email_address(
            address="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_email_address(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_email_address(
            address="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_jwt_subject_id(self, client: PrivyAPI) -> None:
        user = client.users.get_by_jwt_subject_id(
            custom_user_id="custom_user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_jwt_subject_id(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_jwt_subject_id(
            custom_user_id="custom_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_jwt_subject_id(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_jwt_subject_id(
            custom_user_id="custom_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_wallet_address(self, client: PrivyAPI) -> None:
        user = client.users.get_by_wallet_address(
            address="address",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_wallet_address(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_wallet_address(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_wallet_address(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_wallet_address(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.create(
            linked_accounts=[
                {
                    "address": "tom.bombadill@privy.io",
                    "type": "email",
                }
            ],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.create(
            linked_accounts=[
                {
                    "address": "tom.bombadill@privy.io",
                    "type": "email",
                }
            ],
            custom_metadata={"foo": "string"},
            wallets=[
                {
                    "chain_type": "solana",
                    "additional_signers": [
                        {
                            "signer_id": "signer_id",
                            "override_policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                        }
                    ],
                    "create_smart_wallet": True,
                    "policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                }
            ],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.create(
            linked_accounts=[
                {
                    "address": "tom.bombadill@privy.io",
                    "type": "email",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.create(
            linked_accounts=[
                {
                    "address": "tom.bombadill@privy.io",
                    "type": "email",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.list()
        assert_matches_type(AsyncCursor[User], user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.list(
            cursor="x",
            limit=100,
        )
        assert_matches_type(AsyncCursor[User], user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncCursor[User], user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncCursor[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.delete(
            "user_id",
        )
        assert user is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_custom_metadata(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.create_custom_metadata(
            "user_id",
        )
        assert_matches_type(UserCreateCustomMetadataResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_custom_metadata(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.create_custom_metadata(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateCustomMetadataResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_custom_metadata(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.create_custom_metadata(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateCustomMetadataResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_custom_metadata(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.create_custom_metadata(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get(
            "user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_email_address(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_email_address(
            address="dev@stainless.com",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_email_address(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_email_address(
            address="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_email_address(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_email_address(
            address="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_jwt_subject_id(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_jwt_subject_id(
            custom_user_id="custom_user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_jwt_subject_id(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_jwt_subject_id(
            custom_user_id="custom_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_jwt_subject_id(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_jwt_subject_id(
            custom_user_id="custom_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_wallet_address(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_wallet_address(
            address="address",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_wallet_address(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_wallet_address(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_wallet_address(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_wallet_address(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True
