# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .enrollment import (
    EnrollmentResource,
    AsyncEnrollmentResource,
    EnrollmentResourceWithRawResponse,
    AsyncEnrollmentResourceWithRawResponse,
    EnrollmentResourceWithStreamingResponse,
    AsyncEnrollmentResourceWithStreamingResponse,
)
from ....._compat import cached_property
from .verification import (
    VerificationResource,
    AsyncVerificationResource,
    VerificationResourceWithRawResponse,
    AsyncVerificationResourceWithRawResponse,
    VerificationResourceWithStreamingResponse,
    AsyncVerificationResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TotpResource", "AsyncTotpResource"]


class TotpResource(SyncAPIResource):
    @cached_property
    def enrollment(self) -> EnrollmentResource:
        """Operations related to user MFA"""
        return EnrollmentResource(self._client)

    @cached_property
    def verification(self) -> VerificationResource:
        """Operations related to user MFA"""
        return VerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> TotpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TotpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TotpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return TotpResourceWithStreamingResponse(self)


class AsyncTotpResource(AsyncAPIResource):
    @cached_property
    def enrollment(self) -> AsyncEnrollmentResource:
        """Operations related to user MFA"""
        return AsyncEnrollmentResource(self._client)

    @cached_property
    def verification(self) -> AsyncVerificationResource:
        """Operations related to user MFA"""
        return AsyncVerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTotpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTotpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTotpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncTotpResourceWithStreamingResponse(self)


class TotpResourceWithRawResponse:
    def __init__(self, totp: TotpResource) -> None:
        self._totp = totp

    @cached_property
    def enrollment(self) -> EnrollmentResourceWithRawResponse:
        """Operations related to user MFA"""
        return EnrollmentResourceWithRawResponse(self._totp.enrollment)

    @cached_property
    def verification(self) -> VerificationResourceWithRawResponse:
        """Operations related to user MFA"""
        return VerificationResourceWithRawResponse(self._totp.verification)


class AsyncTotpResourceWithRawResponse:
    def __init__(self, totp: AsyncTotpResource) -> None:
        self._totp = totp

    @cached_property
    def enrollment(self) -> AsyncEnrollmentResourceWithRawResponse:
        """Operations related to user MFA"""
        return AsyncEnrollmentResourceWithRawResponse(self._totp.enrollment)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithRawResponse:
        """Operations related to user MFA"""
        return AsyncVerificationResourceWithRawResponse(self._totp.verification)


class TotpResourceWithStreamingResponse:
    def __init__(self, totp: TotpResource) -> None:
        self._totp = totp

    @cached_property
    def enrollment(self) -> EnrollmentResourceWithStreamingResponse:
        """Operations related to user MFA"""
        return EnrollmentResourceWithStreamingResponse(self._totp.enrollment)

    @cached_property
    def verification(self) -> VerificationResourceWithStreamingResponse:
        """Operations related to user MFA"""
        return VerificationResourceWithStreamingResponse(self._totp.verification)


class AsyncTotpResourceWithStreamingResponse:
    def __init__(self, totp: AsyncTotpResource) -> None:
        self._totp = totp

    @cached_property
    def enrollment(self) -> AsyncEnrollmentResourceWithStreamingResponse:
        """Operations related to user MFA"""
        return AsyncEnrollmentResourceWithStreamingResponse(self._totp.enrollment)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithStreamingResponse:
        """Operations related to user MFA"""
        return AsyncVerificationResourceWithStreamingResponse(self._totp.verification)
