# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .fiat import (
    FiatResource,
    AsyncFiatResource,
    FiatResourceWithRawResponse,
    AsyncFiatResourceWithRawResponse,
    FiatResourceWithStreamingResponse,
    AsyncFiatResourceWithStreamingResponse,
)
from .crypto import (
    CryptoResource,
    AsyncCryptoResource,
    CryptoResourceWithRawResponse,
    AsyncCryptoResourceWithRawResponse,
    CryptoResourceWithStreamingResponse,
    AsyncCryptoResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DepositAccountsResource", "AsyncDepositAccountsResource"]


class DepositAccountsResource(SyncAPIResource):
    @cached_property
    def crypto(self) -> CryptoResource:
        """Operations related to wallets"""
        return CryptoResource(self._client)

    @cached_property
    def fiat(self) -> FiatResource:
        """Operations related to fiat onramping and offramping"""
        return FiatResource(self._client)

    @cached_property
    def with_raw_response(self) -> DepositAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return DepositAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DepositAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return DepositAccountsResourceWithStreamingResponse(self)


class AsyncDepositAccountsResource(AsyncAPIResource):
    @cached_property
    def crypto(self) -> AsyncCryptoResource:
        """Operations related to wallets"""
        return AsyncCryptoResource(self._client)

    @cached_property
    def fiat(self) -> AsyncFiatResource:
        """Operations related to fiat onramping and offramping"""
        return AsyncFiatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDepositAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/privy-io/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDepositAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDepositAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/privy-io/python-sdk#with_streaming_response
        """
        return AsyncDepositAccountsResourceWithStreamingResponse(self)


class DepositAccountsResourceWithRawResponse:
    def __init__(self, deposit_accounts: DepositAccountsResource) -> None:
        self._deposit_accounts = deposit_accounts

    @cached_property
    def crypto(self) -> CryptoResourceWithRawResponse:
        """Operations related to wallets"""
        return CryptoResourceWithRawResponse(self._deposit_accounts.crypto)

    @cached_property
    def fiat(self) -> FiatResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return FiatResourceWithRawResponse(self._deposit_accounts.fiat)


class AsyncDepositAccountsResourceWithRawResponse:
    def __init__(self, deposit_accounts: AsyncDepositAccountsResource) -> None:
        self._deposit_accounts = deposit_accounts

    @cached_property
    def crypto(self) -> AsyncCryptoResourceWithRawResponse:
        """Operations related to wallets"""
        return AsyncCryptoResourceWithRawResponse(self._deposit_accounts.crypto)

    @cached_property
    def fiat(self) -> AsyncFiatResourceWithRawResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncFiatResourceWithRawResponse(self._deposit_accounts.fiat)


class DepositAccountsResourceWithStreamingResponse:
    def __init__(self, deposit_accounts: DepositAccountsResource) -> None:
        self._deposit_accounts = deposit_accounts

    @cached_property
    def crypto(self) -> CryptoResourceWithStreamingResponse:
        """Operations related to wallets"""
        return CryptoResourceWithStreamingResponse(self._deposit_accounts.crypto)

    @cached_property
    def fiat(self) -> FiatResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return FiatResourceWithStreamingResponse(self._deposit_accounts.fiat)


class AsyncDepositAccountsResourceWithStreamingResponse:
    def __init__(self, deposit_accounts: AsyncDepositAccountsResource) -> None:
        self._deposit_accounts = deposit_accounts

    @cached_property
    def crypto(self) -> AsyncCryptoResourceWithStreamingResponse:
        """Operations related to wallets"""
        return AsyncCryptoResourceWithStreamingResponse(self._deposit_accounts.crypto)

    @cached_property
    def fiat(self) -> AsyncFiatResourceWithStreamingResponse:
        """Operations related to fiat onramping and offramping"""
        return AsyncFiatResourceWithStreamingResponse(self._deposit_accounts.fiat)
