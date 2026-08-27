from __future__ import annotations

from privy import PrivyAPI
from privy.lib.request_url import build_request_url


def test_build_request_url_normalizes_separator() -> None:
    with PrivyAPI(
        app_id="app-123",
        app_secret="secret",
        base_url="https://api.staging.privy.io/",
    ) as client:
        url = build_request_url(client, "/v1/wallets/wallet-1/raw_sign")

    assert url == "https://api.staging.privy.io/v1/wallets/wallet-1/raw_sign"
