from __future__ import annotations

import json

from privy.types import LinkedAccountEthereumEmbeddedWallet
from privy.lib.auth import _parse_user_from_identity_token_payload


def _payload(*accounts: dict[str, object]) -> dict[str, object]:
    return {"sub": "did:privy:user", "cr": "1700000000", "linked_accounts": json.dumps(list(accounts))}


def _embedded_wallet(**extra: object) -> dict[str, object]:
    return {
        "type": "wallet",
        "id": "wallet-id",
        "address": "0x0000000000000000000000000000000000000001",
        "chain_type": "ethereum",
        "wallet_client_type": "privy",
        "lv": 1700000000,
        **extra,
    }


def test_identity_token_embedded_wallet_defaults_user_can_sign_to_true() -> None:
    user = _parse_user_from_identity_token_payload(_payload(_embedded_wallet()))

    account = user.linked_accounts[0]
    assert isinstance(account, LinkedAccountEthereumEmbeddedWallet)
    assert account.user_can_sign is True


def test_identity_token_embedded_wallet_preserves_user_can_sign() -> None:
    user = _parse_user_from_identity_token_payload(_payload(_embedded_wallet(user_can_sign=False)))

    account = user.linked_accounts[0]
    assert isinstance(account, LinkedAccountEthereumEmbeddedWallet)
    assert account.user_can_sign is False
