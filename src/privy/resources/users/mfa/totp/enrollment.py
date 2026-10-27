# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.users.mfa.totp import enrollment_verify_params
from .....types.users.mfa_verification_response import MfaVerificationResponse
from .....types.users.totp_mfa_enrollment_init_response import TotpMfaEnrollmentInitResponse

__all__ = ["EnrollmentResource", "AsyncEnrollmentResource"]


class EnrollmentResource(SyncAPIResource):
    """Operations related to user MFA"""

    @cached_property
    def with_raw_response(self) -> EnrollmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return EnrollmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnrollmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return EnrollmentResourceWithStreamingResponse(self)

    def init(
        self,
        user_id: str,
        *,
        privy_user_token: str,
        privy_mfa_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TotpMfaEnrollmentInitResponse:
        """
        Creates a TOTP secret for the user to add to an authenticator app.

        Args:
          privy_user_token: Access token or custom authentication JWT for the user the request acts on.

          privy_mfa_token: MFA token from a completed MFA verification, required on MFA-protected requests
              for users with MFA enrolled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-user-token": privy_user_token,
                    "privy-mfa-token": privy_mfa_token,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v1/users/{user_id}/mfa/totp/enrollment/init", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TotpMfaEnrollmentInitResponse,
        )

    def verify(
        self,
        user_id: str,
        *,
        code: str,
        privy_user_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MfaVerificationResponse:
        """
        Enrolls the authenticator from init using a code it generated.

        Args:
          privy_user_token: Access token or custom authentication JWT for the user the request acts on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"privy-user-token": privy_user_token, **(extra_headers or {})}
        return self._post(
            path_template("/v1/users/{user_id}/mfa/totp/enrollment/verify", user_id=user_id),
            body=maybe_transform({"code": code}, enrollment_verify_params.EnrollmentVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MfaVerificationResponse,
        )


class AsyncEnrollmentResource(AsyncAPIResource):
    """Operations related to user MFA"""

    @cached_property
    def with_raw_response(self) -> AsyncEnrollmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEnrollmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnrollmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncEnrollmentResourceWithStreamingResponse(self)

    async def init(
        self,
        user_id: str,
        *,
        privy_user_token: str,
        privy_mfa_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TotpMfaEnrollmentInitResponse:
        """
        Creates a TOTP secret for the user to add to an authenticator app.

        Args:
          privy_user_token: Access token or custom authentication JWT for the user the request acts on.

          privy_mfa_token: MFA token from a completed MFA verification, required on MFA-protected requests
              for users with MFA enrolled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "privy-user-token": privy_user_token,
                    "privy-mfa-token": privy_mfa_token,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v1/users/{user_id}/mfa/totp/enrollment/init", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TotpMfaEnrollmentInitResponse,
        )

    async def verify(
        self,
        user_id: str,
        *,
        code: str,
        privy_user_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MfaVerificationResponse:
        """
        Enrolls the authenticator from init using a code it generated.

        Args:
          privy_user_token: Access token or custom authentication JWT for the user the request acts on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"privy-user-token": privy_user_token, **(extra_headers or {})}
        return await self._post(
            path_template("/v1/users/{user_id}/mfa/totp/enrollment/verify", user_id=user_id),
            body=await async_maybe_transform({"code": code}, enrollment_verify_params.EnrollmentVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MfaVerificationResponse,
        )


class EnrollmentResourceWithRawResponse:
    def __init__(self, enrollment: EnrollmentResource) -> None:
        self._enrollment = enrollment

        self.init = to_raw_response_wrapper(
            enrollment.init,
        )
        self.verify = to_raw_response_wrapper(
            enrollment.verify,
        )


class AsyncEnrollmentResourceWithRawResponse:
    def __init__(self, enrollment: AsyncEnrollmentResource) -> None:
        self._enrollment = enrollment

        self.init = async_to_raw_response_wrapper(
            enrollment.init,
        )
        self.verify = async_to_raw_response_wrapper(
            enrollment.verify,
        )


class EnrollmentResourceWithStreamingResponse:
    def __init__(self, enrollment: EnrollmentResource) -> None:
        self._enrollment = enrollment

        self.init = to_streamed_response_wrapper(
            enrollment.init,
        )
        self.verify = to_streamed_response_wrapper(
            enrollment.verify,
        )


class AsyncEnrollmentResourceWithStreamingResponse:
    def __init__(self, enrollment: AsyncEnrollmentResource) -> None:
        self._enrollment = enrollment

        self.init = async_to_streamed_response_wrapper(
            enrollment.init,
        )
        self.verify = async_to_streamed_response_wrapper(
            enrollment.verify,
        )
