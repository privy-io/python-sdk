# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    User,
)
from tests.utils import assert_matches_type
from privy.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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
                    "chain_type": "ethereum",
                    "additional_signers": [
                        {
                            "signer_id": "string",
                            "override_policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                        }
                    ],
                    "create_smart_wallet": True,
                    "policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                }
            ],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        user = client.users.list()
        assert_matches_type(SyncCursor[User], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PrivyAPI) -> None:
        user = client.users.list(
            cursor="x",
            limit=100,
        )
        assert_matches_type(SyncCursor[User], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncCursor[User], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncCursor[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: PrivyAPI) -> None:
        user = client.users.delete(
            "user_id",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        user = client.users.get(
            "user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_custom_auth_id(self, client: PrivyAPI) -> None:
        user = client.users.get_by_custom_auth_id(
            custom_user_id="custom_user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_custom_auth_id(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_custom_auth_id(
            custom_user_id="custom_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_custom_auth_id(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_custom_auth_id(
            custom_user_id="custom_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_discord_username(self, client: PrivyAPI) -> None:
        user = client.users.get_by_discord_username(
            username="username",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_discord_username(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_discord_username(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_discord_username(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_discord_username(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_email_address(self, client: PrivyAPI) -> None:
        user = client.users.get_by_email_address(
            address="dev@stainless.com",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_email_address(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_email_address(
            address="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_farcaster_id(self, client: PrivyAPI) -> None:
        user = client.users.get_by_farcaster_id(
            fid=0,
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_farcaster_id(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_farcaster_id(
            fid=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_farcaster_id(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_farcaster_id(
            fid=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_github_username(self, client: PrivyAPI) -> None:
        user = client.users.get_by_github_username(
            username="username",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_github_username(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_github_username(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_github_username(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_github_username(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_phone_number(self, client: PrivyAPI) -> None:
        user = client.users.get_by_phone_number(
            number="number",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_phone_number(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_phone_number(
            number="number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_phone_number(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_phone_number(
            number="number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_smart_wallet_address(self, client: PrivyAPI) -> None:
        user = client.users.get_by_smart_wallet_address(
            address="address",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_smart_wallet_address(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_smart_wallet_address(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_smart_wallet_address(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_smart_wallet_address(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_telegram_user_id(self, client: PrivyAPI) -> None:
        user = client.users.get_by_telegram_user_id(
            telegram_user_id="telegram_user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_telegram_user_id(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_telegram_user_id(
            telegram_user_id="telegram_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_telegram_user_id(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_telegram_user_id(
            telegram_user_id="telegram_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_telegram_username(self, client: PrivyAPI) -> None:
        user = client.users.get_by_telegram_username(
            username="username",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_telegram_username(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_telegram_username(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_telegram_username(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_telegram_username(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_twitter_subject(self, client: PrivyAPI) -> None:
        user = client.users.get_by_twitter_subject(
            subject="subject",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_twitter_subject(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_twitter_subject(
            subject="subject",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_twitter_subject(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_twitter_subject(
            subject="subject",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_twitter_username(self, client: PrivyAPI) -> None:
        user = client.users.get_by_twitter_username(
            username="username",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_twitter_username(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_twitter_username(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_twitter_username(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.get_by_twitter_username(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_wallet_address(self, client: PrivyAPI) -> None:
        user = client.users.get_by_wallet_address(
            address="address",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_wallet_address(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.get_by_wallet_address(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pregenerate_wallets(self, client: PrivyAPI) -> None:
        user = client.users.pregenerate_wallets(
            user_id="user_id",
            wallets=[{"chain_type": "ethereum"}],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pregenerate_wallets(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.pregenerate_wallets(
            user_id="user_id",
            wallets=[{"chain_type": "ethereum"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pregenerate_wallets(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.pregenerate_wallets(
            user_id="user_id",
            wallets=[{"chain_type": "ethereum"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pregenerate_wallets(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.pregenerate_wallets(
                user_id="",
                wallets=[{"chain_type": "ethereum"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_overload_1(self, client: PrivyAPI) -> None:
        user = client.users.search(
            search_term="searchTerm",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_overload_1(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.search(
            search_term="searchTerm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_overload_1(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.search(
            search_term="searchTerm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_overload_2(self, client: PrivyAPI) -> None:
        user = client.users.search(
            emails=["dev@stainless.com"],
            phone_numbers=["string"],
            wallet_addresses=["string"],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_overload_2(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.search(
            emails=["dev@stainless.com"],
            phone_numbers=["string"],
            wallet_addresses=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_overload_2(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.search(
            emails=["dev@stainless.com"],
            phone_numbers=["string"],
            wallet_addresses=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_custom_metadata(self, client: PrivyAPI) -> None:
        user = client.users.set_custom_metadata(
            user_id="user_id",
            custom_metadata={"key": "value"},
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_custom_metadata(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.set_custom_metadata(
            user_id="user_id",
            custom_metadata={"key": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_custom_metadata(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.set_custom_metadata(
            user_id="user_id",
            custom_metadata={"key": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_custom_metadata(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.set_custom_metadata(
                user_id="",
                custom_metadata={"key": "value"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unlink_linked_account(self, client: PrivyAPI) -> None:
        user = client.users.unlink_linked_account(
            user_id="user_id",
            handle="test@test.com",
            type="email",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unlink_linked_account_with_all_params(self, client: PrivyAPI) -> None:
        user = client.users.unlink_linked_account(
            user_id="user_id",
            handle="test@test.com",
            type="email",
            provider="provider",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unlink_linked_account(self, client: PrivyAPI) -> None:
        response = client.users.with_raw_response.unlink_linked_account(
            user_id="user_id",
            handle="test@test.com",
            type="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unlink_linked_account(self, client: PrivyAPI) -> None:
        with client.users.with_streaming_response.unlink_linked_account(
            user_id="user_id",
            handle="test@test.com",
            type="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unlink_linked_account(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.unlink_linked_account(
                user_id="",
                handle="test@test.com",
                type="email",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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
                    "chain_type": "ethereum",
                    "additional_signers": [
                        {
                            "signer_id": "string",
                            "override_policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                        }
                    ],
                    "create_smart_wallet": True,
                    "policy_ids": ["xxxxxxxxxxxxxxxxxxxxxxxx"],
                }
            ],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.list()
        assert_matches_type(AsyncCursor[User], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.list(
            cursor="x",
            limit=100,
        )
        assert_matches_type(AsyncCursor[User], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncCursor[User], user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncCursor[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.delete(
            "user_id",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get(
            "user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_custom_auth_id(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_custom_auth_id(
            custom_user_id="custom_user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_custom_auth_id(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_custom_auth_id(
            custom_user_id="custom_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_custom_auth_id(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_custom_auth_id(
            custom_user_id="custom_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_discord_username(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_discord_username(
            username="username",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_discord_username(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_discord_username(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_discord_username(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_discord_username(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_email_address(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_email_address(
            address="dev@stainless.com",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_email_address(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_email_address(
            address="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_farcaster_id(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_farcaster_id(
            fid=0,
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_farcaster_id(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_farcaster_id(
            fid=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_farcaster_id(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_farcaster_id(
            fid=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_github_username(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_github_username(
            username="username",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_github_username(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_github_username(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_github_username(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_github_username(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_phone_number(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_phone_number(
            number="number",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_phone_number(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_phone_number(
            number="number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_phone_number(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_phone_number(
            number="number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_smart_wallet_address(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_smart_wallet_address(
            address="address",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_smart_wallet_address(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_smart_wallet_address(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_smart_wallet_address(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_smart_wallet_address(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_telegram_user_id(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_telegram_user_id(
            telegram_user_id="telegram_user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_telegram_user_id(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_telegram_user_id(
            telegram_user_id="telegram_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_telegram_user_id(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_telegram_user_id(
            telegram_user_id="telegram_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_telegram_username(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_telegram_username(
            username="username",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_telegram_username(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_telegram_username(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_telegram_username(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_telegram_username(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_twitter_subject(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_twitter_subject(
            subject="subject",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_twitter_subject(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_twitter_subject(
            subject="subject",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_twitter_subject(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_twitter_subject(
            subject="subject",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_twitter_username(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_twitter_username(
            username="username",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_twitter_username(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_twitter_username(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_twitter_username(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.get_by_twitter_username(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_wallet_address(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.get_by_wallet_address(
            address="address",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_wallet_address(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.get_by_wallet_address(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pregenerate_wallets(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.pregenerate_wallets(
            user_id="user_id",
            wallets=[{"chain_type": "ethereum"}],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pregenerate_wallets(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.pregenerate_wallets(
            user_id="user_id",
            wallets=[{"chain_type": "ethereum"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pregenerate_wallets(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.pregenerate_wallets(
            user_id="user_id",
            wallets=[{"chain_type": "ethereum"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pregenerate_wallets(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.pregenerate_wallets(
                user_id="",
                wallets=[{"chain_type": "ethereum"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.search(
            search_term="searchTerm",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.search(
            search_term="searchTerm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.search(
            search_term="searchTerm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.search(
            emails=["dev@stainless.com"],
            phone_numbers=["string"],
            wallet_addresses=["string"],
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.search(
            emails=["dev@stainless.com"],
            phone_numbers=["string"],
            wallet_addresses=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.search(
            emails=["dev@stainless.com"],
            phone_numbers=["string"],
            wallet_addresses=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_custom_metadata(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.set_custom_metadata(
            user_id="user_id",
            custom_metadata={"key": "value"},
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_custom_metadata(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.set_custom_metadata(
            user_id="user_id",
            custom_metadata={"key": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_custom_metadata(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.set_custom_metadata(
            user_id="user_id",
            custom_metadata={"key": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_custom_metadata(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.set_custom_metadata(
                user_id="",
                custom_metadata={"key": "value"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unlink_linked_account(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.unlink_linked_account(
            user_id="user_id",
            handle="test@test.com",
            type="email",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unlink_linked_account_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        user = await async_client.users.unlink_linked_account(
            user_id="user_id",
            handle="test@test.com",
            type="email",
            provider="provider",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unlink_linked_account(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.users.with_raw_response.unlink_linked_account(
            user_id="user_id",
            handle="test@test.com",
            type="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unlink_linked_account(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.users.with_streaming_response.unlink_linked_account(
            user_id="user_id",
            handle="test@test.com",
            type="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unlink_linked_account(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.unlink_linked_account(
                user_id="",
                handle="test@test.com",
                type="email",
            )
