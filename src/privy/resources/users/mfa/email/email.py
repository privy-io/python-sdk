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

__all__ = ["EmailResource", "AsyncEmailResource"]


class EmailResource(SyncAPIResource):
    @cached_property
    def enrollment(self) -> EnrollmentResource:
        """Operations related to user MFA"""
        return EnrollmentResource(self._client)

    @cached_property
    def verification(self) -> VerificationResource:
        """Operations related to user MFA"""
        return VerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return EmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return EmailResourceWithStreamingResponse(self)


class AsyncEmailResource(AsyncAPIResource):
    @cached_property
    def enrollment(self) -> AsyncEnrollmentResource:
        """Operations related to user MFA"""
        return AsyncEnrollmentResource(self._client)

    @cached_property
    def verification(self) -> AsyncVerificationResource:
        """Operations related to user MFA"""
        return AsyncVerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncEmailResourceWithStreamingResponse(self)


class EmailResourceWithRawResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

    @cached_property
    def enrollment(self) -> EnrollmentResourceWithRawResponse:
        """Operations related to user MFA"""
        return EnrollmentResourceWithRawResponse(self._email.enrollment)

    @cached_property
    def verification(self) -> VerificationResourceWithRawResponse:
        """Operations related to user MFA"""
        return VerificationResourceWithRawResponse(self._email.verification)


class AsyncEmailResourceWithRawResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

    @cached_property
    def enrollment(self) -> AsyncEnrollmentResourceWithRawResponse:
        """Operations related to user MFA"""
        return AsyncEnrollmentResourceWithRawResponse(self._email.enrollment)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithRawResponse:
        """Operations related to user MFA"""
        return AsyncVerificationResourceWithRawResponse(self._email.verification)


class EmailResourceWithStreamingResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

    @cached_property
    def enrollment(self) -> EnrollmentResourceWithStreamingResponse:
        """Operations related to user MFA"""
        return EnrollmentResourceWithStreamingResponse(self._email.enrollment)

    @cached_property
    def verification(self) -> VerificationResourceWithStreamingResponse:
        """Operations related to user MFA"""
        return VerificationResourceWithStreamingResponse(self._email.verification)


class AsyncEmailResourceWithStreamingResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

    @cached_property
    def enrollment(self) -> AsyncEnrollmentResourceWithStreamingResponse:
        """Operations related to user MFA"""
        return AsyncEnrollmentResourceWithStreamingResponse(self._email.enrollment)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithStreamingResponse:
        """Operations related to user MFA"""
        return AsyncVerificationResourceWithStreamingResponse(self._email.verification)
