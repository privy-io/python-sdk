"""Public wallet operations."""

from __future__ import annotations

from .._types import omit
from .authorization import prepare_request
from .request_options import PrivyRequestOptions
from ..types.raw_sign_response import RawSignResponse
from ..resources.wallets.wallets import WalletsResource
from ..types.wallet_raw_sign_params import WalletRawSignParams

__all__ = ["WalletsService"]


class WalletsService(WalletsResource):
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
