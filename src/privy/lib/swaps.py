"""Authorized wallet swap operations."""

from __future__ import annotations

from typing import Any, Callable, cast

from .._types import omit
from .._client import PrivyAPI
from .request_url import build_request_url
from .jwt_exchange import JWTExchangeService
from .authorization import prepare_request
from .request_options import PrivyRequestOptions
from ..types.swap_quote_response import SwapQuoteResponse
from ..types.wallets.swap_quote_params import SwapQuoteParams
from ..types.wallets.swap_execute_params import SwapExecuteParams
from ..types.wallets.swap_action_response import SwapActionResponse

__all__ = ["PrivySwapsService"]


class PrivySwapsService:
    """Convenience methods for authorized wallet swaps."""

    def __init__(self, client: PrivyAPI, jwt_exchanger: JWTExchangeService | None = None) -> None:
        self._client = client
        self._swap_resource = client.wallets.swap
        self._jwt_exchanger = jwt_exchanger

    def execute(
        self,
        wallet_id: str,
        *,
        swap_execute_params: SwapExecuteParams,
        idempotency_key: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> SwapActionResponse:
        """Execute a token swap, authorizing and idempotently identifying the request."""

        options = request_options or PrivyRequestOptions()
        body = dict(swap_execute_params)
        prepared = prepare_request(
            app_id=self._client.app_id,
            method="POST",
            url=build_request_url(self._client, f"/v1/wallets/{wallet_id}/swap"),
            body=body,
            idempotency_key=idempotency_key,
            authorization_context=options.authorization_context,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        idempotency_header = prepared.headers.get("privy-idempotency-key")
        generated: Any = self._swap_resource
        execute = cast(Callable[..., SwapActionResponse], generated.execute)
        return execute(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_idempotency_key=idempotency_header if idempotency_header is not None else omit,
        )

    def quote(
        self,
        wallet_id: str,
        *,
        swap_quote_params: SwapQuoteParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> SwapQuoteResponse:
        """Get a token swap quote, authorizing the request when credentials are supplied."""

        options = request_options or PrivyRequestOptions()
        body = dict(swap_quote_params)
        prepared = prepare_request(
            app_id=self._client.app_id,
            method="POST",
            url=build_request_url(self._client, f"/v1/wallets/{wallet_id}/swap/quote"),
            body=body,
            authorization_context=options.authorization_context,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        generated: Any = self._swap_resource
        quote = cast(Callable[..., SwapQuoteResponse], generated.quote)
        return quote(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
        )
