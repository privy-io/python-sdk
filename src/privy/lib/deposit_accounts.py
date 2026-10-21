"""Authorized wallet deposit-account operations."""

from __future__ import annotations

from typing import Any, Callable, cast
from typing_extensions import override

from .._types import omit
from .._client import PrivyAPI
from .request_url import build_request_url
from .jwt_exchange import JWTExchangeService
from .authorization import prepare_request
from .request_expiry import RequestExpiryProvider, resolve_request_expiry
from .request_options import PrivyRequestOptions
from ..types.create_crypto_deposit_account_response import CreateCryptoDepositAccountResponse
from ..resources.wallets.deposit_accounts.crypto.crypto import CryptoResource
from ..resources.wallets.deposit_accounts.deposit_accounts import DepositAccountsResource
from ..types.wallets.deposit_accounts.crypto_create_params import CryptoCreateParams

__all__ = ["PrivyDepositAccountsService", "PrivyDepositAccountsCryptoService"]


class PrivyDepositAccountsCryptoService(CryptoResource):
    """Crypto deposit-account operations with authorization and request expiry."""

    def __init__(
        self,
        client: PrivyAPI,
        jwt_exchanger: JWTExchangeService | None = None,
        request_expiry_provider: RequestExpiryProvider | None = None,
    ) -> None:
        super().__init__(client)
        self._jwt_exchanger = jwt_exchanger
        self._request_expiry_provider = request_expiry_provider

    def create(
        self,
        wallet_id: str,
        *,
        crypto_create_params: CryptoCreateParams,
        idempotency_key: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> CreateCryptoDepositAccountResponse:
        """Create deposit source wallets that sweep into the wallet."""

        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        body = dict(crypto_create_params)
        prepared = prepare_request(
            app_id=self._client.app_id,
            method="POST",
            url=build_request_url(self._client, f"/v1/wallets/{wallet_id}/deposit_accounts/crypto"),
            body=body,
            idempotency_key=idempotency_key,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        idempotency_header = prepared.headers.get("privy-idempotency-key")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        create = cast(Callable[..., CreateCryptoDepositAccountResponse], generated._create)
        return create(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_idempotency_key=idempotency_header if idempotency_header is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )


class PrivyDepositAccountsService(DepositAccountsResource):
    """Wallet deposit accounts."""

    def __init__(
        self,
        client: PrivyAPI,
        jwt_exchanger: JWTExchangeService | None = None,
        request_expiry_provider: RequestExpiryProvider | None = None,
    ) -> None:
        super().__init__(client)
        self._crypto = PrivyDepositAccountsCryptoService(client, jwt_exchanger, request_expiry_provider)

    @property
    @override
    def crypto(self) -> PrivyDepositAccountsCryptoService:
        return self._crypto
