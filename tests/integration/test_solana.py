from __future__ import annotations

import base64

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from privy import PrivyClient
from privy.types.wallet import Wallet

pytestmark = pytest.mark.integration


def _base58_decode(value: str) -> bytes:
    number = 0
    for character in value:
        number = number * 58 + "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz".index(character)
    decoded = number.to_bytes((number.bit_length() + 7) // 8, "big")
    return b"\0" * (len(value) - len(value.lstrip("1"))) + decoded


@pytest.fixture(scope="module")
def solana_wallet(privy_client: PrivyClient) -> Wallet:
    wallet = privy_client.wallets.create(chain_type="solana")
    assert wallet.id
    assert wallet.address
    assert wallet.chain_type == "solana"
    return wallet


@pytest.mark.parametrize("message", [b"Hello, world!", base64.b64encode(b"Hello, world!").decode("ascii")])
def test_sign_message(privy_client: PrivyClient, solana_wallet: Wallet, message: str | bytes) -> None:
    response = privy_client.wallets.solana.sign_message(solana_wallet.id, message)

    assert response.encoding == "base64"
    Ed25519PublicKey.from_public_bytes(_base58_decode(solana_wallet.address)).verify(
        base64.b64decode(response.signature),
        base64.b64decode(message) if isinstance(message, str) else message,
    )
