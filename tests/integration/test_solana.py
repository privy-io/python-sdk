from __future__ import annotations

import base64
import struct

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


def _create_transfer_transaction(source: str) -> bytes:
    destination = _base58_decode("9NvE68JVWHHHGLp5NNELtM5fiBw6SXHrzqQJjUqaykC1")
    message = b"".join(
        (
            b"\x80",  # Versioned message, version 0.
            bytes((1, 0, 1)),  # One signer and one read-only unsigned account.
            b"\x03",
            _base58_decode(source),
            destination,
            bytes(32),  # System program.
            bytes(32),  # Privy replaces this placeholder blockhash before signing.
            b"\x01",  # One instruction.
            b"\x02",  # System program account index.
            b"\x02\x00\x01",  # Source and destination account indices.
            b"\x0c" + struct.pack("<IQ", 2, 100),  # Transfer 100 lamports.
            b"\x00",  # No address lookup tables.
        )
    )
    return b"\x01" + bytes(64) + message


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


def test_sign_transaction(privy_client: PrivyClient, solana_wallet: Wallet) -> None:
    response = privy_client.wallets.solana.sign_transaction(
        solana_wallet.id,
        _create_transfer_transaction(solana_wallet.address),
    )

    assert response.encoding == "base64"
    assert base64.b64decode(response.signed_transaction)
