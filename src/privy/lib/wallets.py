"""Public wallet operations."""

from __future__ import annotations

from typing import Any, Callable, cast

from .tron import PrivyTronService
from .solana import PrivySolanaService
from .._types import omit
from .._client import PrivyAPI
from .ethereum import PrivyEthereumService
from .request_url import build_request_url
from .jwt_exchange import JWTExchangeService
from ..types.wallet import Wallet
from .authorization import prepare_request
from .request_expiry import RequestExpiryProvider, resolve_request_expiry
from .request_options import PrivyRequestOptions
from ..types.raw_sign_response import RawSignResponse
from ..types.wallet_rpc_params import WalletRpcParams
from ..resources.wallets.wallets import WalletsResource
from ..types.wallet_rpc_response import WalletRpcResponse
from ..types.wallet_update_params import WalletUpdateParams
from ..types.wallet_raw_sign_params import WalletRawSignParams

__all__ = ["PrivyWalletsService"]


class PrivyWalletsService(WalletsResource):
    def __init__(
        self,
        client: PrivyAPI,
        jwt_exchanger: JWTExchangeService | None = None,
        request_expiry_provider: RequestExpiryProvider | None = None,
    ) -> None:
        super().__init__(client)
        self._jwt_exchanger = jwt_exchanger
        self._request_expiry_provider = request_expiry_provider
        self.ethereum = PrivyEthereumService(self)
        self.solana = PrivySolanaService(self)
        self.tron = PrivyTronService(self)

    def update(
        self,
        wallet_id: str,
        *,
        wallet_update_params: WalletUpdateParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> Wallet:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        body = dict(wallet_update_params)
        prepared = prepare_request(
            app_id=client.app_id,
            method="PATCH",
            url=build_request_url(client, f"/v1/wallets/{wallet_id}"),
            body=body,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        update = cast(Callable[..., Wallet], generated._update)
        return update(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def rpc(
        self,
        wallet_id: str,
        *,
        wallet_rpc_request_body: WalletRpcParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> WalletRpcResponse:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        body = dict(wallet_rpc_request_body)
        client_values: Any = client
        base_url = client_values.base_url
        prepared = prepare_request(
            app_id=client.app_id,
            method="POST",
            url=f"{str(base_url).rstrip('/')}/v1/wallets/{wallet_id}/rpc",
            body=body,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        rpc = cast(Callable[..., WalletRpcResponse], generated._rpc)
        return rpc(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def raw_sign(
        self,
        wallet_id: str,
        *,
        wallet_raw_sign_params: WalletRawSignParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> RawSignResponse:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        prepared = prepare_request(
            app_id=client.app_id,
            method="POST",
            url=build_request_url(client, f"/v1/wallets/{wallet_id}/raw_sign"),
            body=dict(wallet_raw_sign_params),
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        return self._raw_sign(
            wallet_id,
            params=wallet_raw_sign_params["params"],
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )
