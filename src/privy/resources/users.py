# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import overload

import httpx

from ..types import (
    user_list_params,
    user_create_params,
    user_search_params,
    user_get_by_farcaster_id_params,
    user_get_by_phone_number_params,
    user_pregenerate_wallets_params,
    user_set_custom_metadata_params,
    user_get_by_email_address_params,
    user_get_by_custom_auth_id_params,
    user_get_by_wallet_address_params,
    user_unlink_linked_account_params,
    user_get_by_github_username_params,
    user_get_by_twitter_subject_params,
    user_get_by_discord_username_params,
    user_get_by_telegram_user_id_params,
    user_get_by_twitter_username_params,
    user_get_by_telegram_username_params,
    user_get_by_smart_wallet_address_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursor, AsyncCursor
from ..types.user import User
from .._base_client import AsyncPaginator, make_request_options
from ..types.custom_metadata_param import CustomMetadataParam
from ..types.linked_account_type_param import LinkedAccountTypeParam
from ..types.linked_account_input_param import LinkedAccountInputParam
from ..types.wallet_creation_input_param import WalletCreationInputParam

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    """Operations related to users"""

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        linked_accounts: Iterable[LinkedAccountInputParam],
        custom_metadata: CustomMetadataParam | Omit = omit,
        wallets: Iterable[user_create_params.Wallet] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """Create a new user with linked accounts.

        Optionally pre-generate embedded wallets
        for the user.

        Args:
          custom_metadata: Custom metadata associated with the user.

          wallets: Wallets to create for the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users",
            body=maybe_transform(
                {
                    "linked_accounts": linked_accounts,
                    "custom_metadata": custom_metadata,
                    "wallets": wallets,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[User]:
        """
        Get all users in your app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/users",
            page=SyncCursor[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=User,
        )

    def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a user by user ID.

        Args:
          user_id: ID of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/users/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Get a user by user ID.

        Args:
          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_custom_auth_id(
        self,
        *,
        custom_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their custom auth ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/custom_auth/id",
            body=maybe_transform(
                {"custom_user_id": custom_user_id}, user_get_by_custom_auth_id_params.UserGetByCustomAuthIDParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_discord_username(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Discord username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/discord/username",
            body=maybe_transform(
                {"username": username}, user_get_by_discord_username_params.UserGetByDiscordUsernameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_email_address(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/email/address",
            body=maybe_transform({"address": address}, user_get_by_email_address_params.UserGetByEmailAddressParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_farcaster_id(
        self,
        *,
        fid: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Farcaster ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/farcaster/fid",
            body=maybe_transform({"fid": fid}, user_get_by_farcaster_id_params.UserGetByFarcasterIDParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_github_username(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Github username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/github/username",
            body=maybe_transform(
                {"username": username}, user_get_by_github_username_params.UserGetByGitHubUsernameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_phone_number(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/phone/number",
            body=maybe_transform({"number": number}, user_get_by_phone_number_params.UserGetByPhoneNumberParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_smart_wallet_address(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their smart wallet address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/smart_wallet/address",
            body=maybe_transform(
                {"address": address}, user_get_by_smart_wallet_address_params.UserGetBySmartWalletAddressParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_telegram_user_id(
        self,
        *,
        telegram_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Telegram user ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/telegram/telegram_user_id",
            body=maybe_transform(
                {"telegram_user_id": telegram_user_id},
                user_get_by_telegram_user_id_params.UserGetByTelegramUserIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_telegram_username(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Telegram username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/telegram/username",
            body=maybe_transform(
                {"username": username}, user_get_by_telegram_username_params.UserGetByTelegramUsernameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_twitter_subject(
        self,
        *,
        subject: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Twitter subject.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/twitter/subject",
            body=maybe_transform(
                {"subject": subject}, user_get_by_twitter_subject_params.UserGetByTwitterSubjectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_twitter_username(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Twitter username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/twitter/username",
            body=maybe_transform(
                {"username": username}, user_get_by_twitter_username_params.UserGetByTwitterUsernameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_by_wallet_address(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their wallet address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/wallet/address",
            body=maybe_transform({"address": address}, user_get_by_wallet_address_params.UserGetByWalletAddressParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def pregenerate_wallets(
        self,
        user_id: str,
        *,
        wallets: Iterable[WalletCreationInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Creates an embedded wallet for an existing user.

        Args:
          user_id: ID of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/wallets", user_id=user_id),
            body=maybe_transform({"wallets": wallets}, user_pregenerate_wallets_params.UserPregenerateWalletsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    @overload
    def search(
        self,
        *,
        search_term: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Search users by search term, emails, phone numbers, or wallet addresses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def search(
        self,
        *,
        emails: SequenceNotStr[str],
        phone_numbers: SequenceNotStr[str],
        wallet_addresses: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Search users by search term, emails, phone numbers, or wallet addresses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["search_term"], ["emails", "phone_numbers", "wallet_addresses"])
    def search(
        self,
        *,
        search_term: str | Omit = omit,
        emails: SequenceNotStr[str] | Omit = omit,
        phone_numbers: SequenceNotStr[str] | Omit = omit,
        wallet_addresses: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        return self._post(
            "/v1/users/search",
            body=maybe_transform(
                {
                    "search_term": search_term,
                    "emails": emails,
                    "phone_numbers": phone_numbers,
                    "wallet_addresses": wallet_addresses,
                },
                user_search_params.UserSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def set_custom_metadata(
        self,
        user_id: str,
        *,
        custom_metadata: CustomMetadataParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Adds custom metadata to a user by user ID.

        Args:
          user_id: ID of the user.

          custom_metadata: Custom metadata associated with the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/custom_metadata", user_id=user_id),
            body=maybe_transform(
                {"custom_metadata": custom_metadata}, user_set_custom_metadata_params.UserSetCustomMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def unlink_linked_account(
        self,
        user_id: str,
        *,
        handle: str,
        type: LinkedAccountTypeParam,
        provider: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Unlinks a user linked account.

        Args:
          user_id: ID of the user.

          type: The possible types of linked accounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/accounts/unlink", user_id=user_id),
            body=maybe_transform(
                {
                    "handle": handle,
                    "type": type,
                    "provider": provider,
                },
                user_unlink_linked_account_params.UserUnlinkLinkedAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class AsyncUsersResource(AsyncAPIResource):
    """Operations related to users"""

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        linked_accounts: Iterable[LinkedAccountInputParam],
        custom_metadata: CustomMetadataParam | Omit = omit,
        wallets: Iterable[user_create_params.Wallet] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """Create a new user with linked accounts.

        Optionally pre-generate embedded wallets
        for the user.

        Args:
          custom_metadata: Custom metadata associated with the user.

          wallets: Wallets to create for the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users",
            body=await async_maybe_transform(
                {
                    "linked_accounts": linked_accounts,
                    "custom_metadata": custom_metadata,
                    "wallets": wallets,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[User, AsyncCursor[User]]:
        """
        Get all users in your app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/users",
            page=AsyncCursor[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=User,
        )

    async def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a user by user ID.

        Args:
          user_id: ID of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/users/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Get a user by user ID.

        Args:
          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_custom_auth_id(
        self,
        *,
        custom_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their custom auth ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/custom_auth/id",
            body=await async_maybe_transform(
                {"custom_user_id": custom_user_id}, user_get_by_custom_auth_id_params.UserGetByCustomAuthIDParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_discord_username(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Discord username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/discord/username",
            body=await async_maybe_transform(
                {"username": username}, user_get_by_discord_username_params.UserGetByDiscordUsernameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_email_address(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/email/address",
            body=await async_maybe_transform(
                {"address": address}, user_get_by_email_address_params.UserGetByEmailAddressParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_farcaster_id(
        self,
        *,
        fid: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Farcaster ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/farcaster/fid",
            body=await async_maybe_transform({"fid": fid}, user_get_by_farcaster_id_params.UserGetByFarcasterIDParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_github_username(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Github username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/github/username",
            body=await async_maybe_transform(
                {"username": username}, user_get_by_github_username_params.UserGetByGitHubUsernameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_phone_number(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/phone/number",
            body=await async_maybe_transform(
                {"number": number}, user_get_by_phone_number_params.UserGetByPhoneNumberParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_smart_wallet_address(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their smart wallet address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/smart_wallet/address",
            body=await async_maybe_transform(
                {"address": address}, user_get_by_smart_wallet_address_params.UserGetBySmartWalletAddressParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_telegram_user_id(
        self,
        *,
        telegram_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Telegram user ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/telegram/telegram_user_id",
            body=await async_maybe_transform(
                {"telegram_user_id": telegram_user_id},
                user_get_by_telegram_user_id_params.UserGetByTelegramUserIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_telegram_username(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Telegram username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/telegram/username",
            body=await async_maybe_transform(
                {"username": username}, user_get_by_telegram_username_params.UserGetByTelegramUsernameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_twitter_subject(
        self,
        *,
        subject: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Twitter subject.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/twitter/subject",
            body=await async_maybe_transform(
                {"subject": subject}, user_get_by_twitter_subject_params.UserGetByTwitterSubjectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_twitter_username(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their Twitter username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/twitter/username",
            body=await async_maybe_transform(
                {"username": username}, user_get_by_twitter_username_params.UserGetByTwitterUsernameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_by_wallet_address(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Looks up a user by their wallet address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/wallet/address",
            body=await async_maybe_transform(
                {"address": address}, user_get_by_wallet_address_params.UserGetByWalletAddressParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def pregenerate_wallets(
        self,
        user_id: str,
        *,
        wallets: Iterable[WalletCreationInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Creates an embedded wallet for an existing user.

        Args:
          user_id: ID of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/wallets", user_id=user_id),
            body=await async_maybe_transform(
                {"wallets": wallets}, user_pregenerate_wallets_params.UserPregenerateWalletsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    @overload
    async def search(
        self,
        *,
        search_term: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Search users by search term, emails, phone numbers, or wallet addresses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def search(
        self,
        *,
        emails: SequenceNotStr[str],
        phone_numbers: SequenceNotStr[str],
        wallet_addresses: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Search users by search term, emails, phone numbers, or wallet addresses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["search_term"], ["emails", "phone_numbers", "wallet_addresses"])
    async def search(
        self,
        *,
        search_term: str | Omit = omit,
        emails: SequenceNotStr[str] | Omit = omit,
        phone_numbers: SequenceNotStr[str] | Omit = omit,
        wallet_addresses: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        return await self._post(
            "/v1/users/search",
            body=await async_maybe_transform(
                {
                    "search_term": search_term,
                    "emails": emails,
                    "phone_numbers": phone_numbers,
                    "wallet_addresses": wallet_addresses,
                },
                user_search_params.UserSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def set_custom_metadata(
        self,
        user_id: str,
        *,
        custom_metadata: CustomMetadataParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Adds custom metadata to a user by user ID.

        Args:
          user_id: ID of the user.

          custom_metadata: Custom metadata associated with the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/custom_metadata", user_id=user_id),
            body=await async_maybe_transform(
                {"custom_metadata": custom_metadata}, user_set_custom_metadata_params.UserSetCustomMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def unlink_linked_account(
        self,
        user_id: str,
        *,
        handle: str,
        type: LinkedAccountTypeParam,
        provider: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Unlinks a user linked account.

        Args:
          user_id: ID of the user.

          type: The possible types of linked accounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/accounts/unlink", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "handle": handle,
                    "type": type,
                    "provider": provider,
                },
                user_unlink_linked_account_params.UserUnlinkLinkedAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.get = to_raw_response_wrapper(
            users.get,
        )
        self.get_by_custom_auth_id = to_raw_response_wrapper(
            users.get_by_custom_auth_id,
        )
        self.get_by_discord_username = to_raw_response_wrapper(
            users.get_by_discord_username,
        )
        self.get_by_email_address = to_raw_response_wrapper(
            users.get_by_email_address,
        )
        self.get_by_farcaster_id = to_raw_response_wrapper(
            users.get_by_farcaster_id,
        )
        self.get_by_github_username = to_raw_response_wrapper(
            users.get_by_github_username,
        )
        self.get_by_phone_number = to_raw_response_wrapper(
            users.get_by_phone_number,
        )
        self.get_by_smart_wallet_address = to_raw_response_wrapper(
            users.get_by_smart_wallet_address,
        )
        self.get_by_telegram_user_id = to_raw_response_wrapper(
            users.get_by_telegram_user_id,
        )
        self.get_by_telegram_username = to_raw_response_wrapper(
            users.get_by_telegram_username,
        )
        self.get_by_twitter_subject = to_raw_response_wrapper(
            users.get_by_twitter_subject,
        )
        self.get_by_twitter_username = to_raw_response_wrapper(
            users.get_by_twitter_username,
        )
        self.get_by_wallet_address = to_raw_response_wrapper(
            users.get_by_wallet_address,
        )
        self.pregenerate_wallets = to_raw_response_wrapper(
            users.pregenerate_wallets,
        )
        self.search = to_raw_response_wrapper(
            users.search,
        )
        self.set_custom_metadata = to_raw_response_wrapper(
            users.set_custom_metadata,
        )
        self.unlink_linked_account = to_raw_response_wrapper(
            users.unlink_linked_account,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.get = async_to_raw_response_wrapper(
            users.get,
        )
        self.get_by_custom_auth_id = async_to_raw_response_wrapper(
            users.get_by_custom_auth_id,
        )
        self.get_by_discord_username = async_to_raw_response_wrapper(
            users.get_by_discord_username,
        )
        self.get_by_email_address = async_to_raw_response_wrapper(
            users.get_by_email_address,
        )
        self.get_by_farcaster_id = async_to_raw_response_wrapper(
            users.get_by_farcaster_id,
        )
        self.get_by_github_username = async_to_raw_response_wrapper(
            users.get_by_github_username,
        )
        self.get_by_phone_number = async_to_raw_response_wrapper(
            users.get_by_phone_number,
        )
        self.get_by_smart_wallet_address = async_to_raw_response_wrapper(
            users.get_by_smart_wallet_address,
        )
        self.get_by_telegram_user_id = async_to_raw_response_wrapper(
            users.get_by_telegram_user_id,
        )
        self.get_by_telegram_username = async_to_raw_response_wrapper(
            users.get_by_telegram_username,
        )
        self.get_by_twitter_subject = async_to_raw_response_wrapper(
            users.get_by_twitter_subject,
        )
        self.get_by_twitter_username = async_to_raw_response_wrapper(
            users.get_by_twitter_username,
        )
        self.get_by_wallet_address = async_to_raw_response_wrapper(
            users.get_by_wallet_address,
        )
        self.pregenerate_wallets = async_to_raw_response_wrapper(
            users.pregenerate_wallets,
        )
        self.search = async_to_raw_response_wrapper(
            users.search,
        )
        self.set_custom_metadata = async_to_raw_response_wrapper(
            users.set_custom_metadata,
        )
        self.unlink_linked_account = async_to_raw_response_wrapper(
            users.unlink_linked_account,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.get = to_streamed_response_wrapper(
            users.get,
        )
        self.get_by_custom_auth_id = to_streamed_response_wrapper(
            users.get_by_custom_auth_id,
        )
        self.get_by_discord_username = to_streamed_response_wrapper(
            users.get_by_discord_username,
        )
        self.get_by_email_address = to_streamed_response_wrapper(
            users.get_by_email_address,
        )
        self.get_by_farcaster_id = to_streamed_response_wrapper(
            users.get_by_farcaster_id,
        )
        self.get_by_github_username = to_streamed_response_wrapper(
            users.get_by_github_username,
        )
        self.get_by_phone_number = to_streamed_response_wrapper(
            users.get_by_phone_number,
        )
        self.get_by_smart_wallet_address = to_streamed_response_wrapper(
            users.get_by_smart_wallet_address,
        )
        self.get_by_telegram_user_id = to_streamed_response_wrapper(
            users.get_by_telegram_user_id,
        )
        self.get_by_telegram_username = to_streamed_response_wrapper(
            users.get_by_telegram_username,
        )
        self.get_by_twitter_subject = to_streamed_response_wrapper(
            users.get_by_twitter_subject,
        )
        self.get_by_twitter_username = to_streamed_response_wrapper(
            users.get_by_twitter_username,
        )
        self.get_by_wallet_address = to_streamed_response_wrapper(
            users.get_by_wallet_address,
        )
        self.pregenerate_wallets = to_streamed_response_wrapper(
            users.pregenerate_wallets,
        )
        self.search = to_streamed_response_wrapper(
            users.search,
        )
        self.set_custom_metadata = to_streamed_response_wrapper(
            users.set_custom_metadata,
        )
        self.unlink_linked_account = to_streamed_response_wrapper(
            users.unlink_linked_account,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            users.get,
        )
        self.get_by_custom_auth_id = async_to_streamed_response_wrapper(
            users.get_by_custom_auth_id,
        )
        self.get_by_discord_username = async_to_streamed_response_wrapper(
            users.get_by_discord_username,
        )
        self.get_by_email_address = async_to_streamed_response_wrapper(
            users.get_by_email_address,
        )
        self.get_by_farcaster_id = async_to_streamed_response_wrapper(
            users.get_by_farcaster_id,
        )
        self.get_by_github_username = async_to_streamed_response_wrapper(
            users.get_by_github_username,
        )
        self.get_by_phone_number = async_to_streamed_response_wrapper(
            users.get_by_phone_number,
        )
        self.get_by_smart_wallet_address = async_to_streamed_response_wrapper(
            users.get_by_smart_wallet_address,
        )
        self.get_by_telegram_user_id = async_to_streamed_response_wrapper(
            users.get_by_telegram_user_id,
        )
        self.get_by_telegram_username = async_to_streamed_response_wrapper(
            users.get_by_telegram_username,
        )
        self.get_by_twitter_subject = async_to_streamed_response_wrapper(
            users.get_by_twitter_subject,
        )
        self.get_by_twitter_username = async_to_streamed_response_wrapper(
            users.get_by_twitter_username,
        )
        self.get_by_wallet_address = async_to_streamed_response_wrapper(
            users.get_by_wallet_address,
        )
        self.pregenerate_wallets = async_to_streamed_response_wrapper(
            users.pregenerate_wallets,
        )
        self.search = async_to_streamed_response_wrapper(
            users.search,
        )
        self.set_custom_metadata = async_to_streamed_response_wrapper(
            users.set_custom_metadata,
        )
        self.unlink_linked_account = async_to_streamed_response_wrapper(
            users.unlink_linked_account,
        )
