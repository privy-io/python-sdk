"""Public wallet operations."""

from __future__ import annotations

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
        authorization_context: object | None = None,
    ) -> RawSignResponse:
        # Authorization support will be added with the authorization primitives.
        _ = authorization_context
        return self._raw_sign(wallet_id, **wallet_raw_sign_params)
