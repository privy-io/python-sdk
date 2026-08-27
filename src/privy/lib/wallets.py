"""Public wallet operations."""

from __future__ import annotations

from typing import Any, Callable, cast

from .._types import omit
from .._client import PrivyAPI
from .ethereum import EthereumWalletService
from .authorization import prepare_request
from .request_options import PrivyRequestOptions
from ..types.raw_sign_response import RawSignResponse
from ..types.wallet_rpc_params import WalletRpcParams
from ..resources.wallets.wallets import WalletsResource
from ..types.wallet_rpc_response import WalletRpcResponse
from ..types.wallet_raw_sign_params import WalletRawSignParams

__all__ = ["WalletsService"]


class WalletsService(WalletsResource):
    def __init__(self, client: PrivyAPI) -> None:
        super().__init__(client)
        self.ethereum = EthereumWalletService(self)

    def rpc(
        self,
        wallet_id: str,
        *,
        wallet_rpc_request_body: WalletRpcParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> WalletRpcResponse:
        options = request_options or PrivyRequestOptions()
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
        )
        signature = prepared.headers.get("privy-authorization-signature")
        generated: Any = self
        rpc = cast(Callable[..., WalletRpcResponse], generated._rpc)
        return rpc(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
        )

    def raw_sign(
        self,
        wallet_id: str,
        *,
        wallet_raw_sign_params: WalletRawSignParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> RawSignResponse:
        options = request_options or PrivyRequestOptions()
        client = self._client
        prepared = prepare_request(
            app_id=client.app_id,
            method="POST",
            url=f"{str(client.base_url).rstrip('/')}/v1/wallets/{wallet_id}/raw_sign",
            body=dict(wallet_raw_sign_params),
            authorization_context=options.authorization_context,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        return self._raw_sign(
            wallet_id,
            params=wallet_raw_sign_params["params"],
            privy_authorization_signature=signature if signature is not None else omit,
        )
