# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sms.sms import (
    SMSResource,
    AsyncSMSResource,
    SMSResourceWithRawResponse,
    AsyncSMSResourceWithRawResponse,
    SMSResourceWithStreamingResponse,
    AsyncSMSResourceWithStreamingResponse,
)
from .totp.totp import (
    TotpResource,
    AsyncTotpResource,
    TotpResourceWithRawResponse,
    AsyncTotpResourceWithRawResponse,
    TotpResourceWithStreamingResponse,
    AsyncTotpResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MfaResource", "AsyncMfaResource"]


class MfaResource(SyncAPIResource):
    @cached_property
    def sms(self) -> SMSResource:
        return SMSResource(self._client)

    @cached_property
    def totp(self) -> TotpResource:
        return TotpResource(self._client)

    @cached_property
    def with_raw_response(self) -> MfaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return MfaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MfaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return MfaResourceWithStreamingResponse(self)


class AsyncMfaResource(AsyncAPIResource):
    @cached_property
    def sms(self) -> AsyncSMSResource:
        return AsyncSMSResource(self._client)

    @cached_property
    def totp(self) -> AsyncTotpResource:
        return AsyncTotpResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMfaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMfaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMfaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncMfaResourceWithStreamingResponse(self)


class MfaResourceWithRawResponse:
    def __init__(self, mfa: MfaResource) -> None:
        self._mfa = mfa

    @cached_property
    def sms(self) -> SMSResourceWithRawResponse:
        return SMSResourceWithRawResponse(self._mfa.sms)

    @cached_property
    def totp(self) -> TotpResourceWithRawResponse:
        return TotpResourceWithRawResponse(self._mfa.totp)


class AsyncMfaResourceWithRawResponse:
    def __init__(self, mfa: AsyncMfaResource) -> None:
        self._mfa = mfa

    @cached_property
    def sms(self) -> AsyncSMSResourceWithRawResponse:
        return AsyncSMSResourceWithRawResponse(self._mfa.sms)

    @cached_property
    def totp(self) -> AsyncTotpResourceWithRawResponse:
        return AsyncTotpResourceWithRawResponse(self._mfa.totp)


class MfaResourceWithStreamingResponse:
    def __init__(self, mfa: MfaResource) -> None:
        self._mfa = mfa

    @cached_property
    def sms(self) -> SMSResourceWithStreamingResponse:
        return SMSResourceWithStreamingResponse(self._mfa.sms)

    @cached_property
    def totp(self) -> TotpResourceWithStreamingResponse:
        return TotpResourceWithStreamingResponse(self._mfa.totp)


class AsyncMfaResourceWithStreamingResponse:
    def __init__(self, mfa: AsyncMfaResource) -> None:
        self._mfa = mfa

    @cached_property
    def sms(self) -> AsyncSMSResourceWithStreamingResponse:
        return AsyncSMSResourceWithStreamingResponse(self._mfa.sms)

    @cached_property
    def totp(self) -> AsyncTotpResourceWithStreamingResponse:
        return AsyncTotpResourceWithStreamingResponse(self._mfa.totp)
