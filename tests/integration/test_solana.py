from __future__ import annotations

import base64
import struct
from typing import cast
from collections.abc import Mapping

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from privy import PrivyClient

from .wallet_setup import (
    WALLET_CASES,
    TestWallet as WalletUnderTest,
    WalletOwnership,
    TestWalletResources as WalletResources,
    create_test_wallets,
    setup_test_wallet_resources,
)

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
def wallet_resources(privy_client: PrivyClient) -> WalletResources:
    return setup_test_wallet_resources(privy_client)


@pytest.fixture(scope="module")
def solana_wallets(
    wallet_resources: WalletResources, jwt_auth_private_key: str
) -> Mapping[WalletOwnership, WalletUnderTest]:
    return create_test_wallets(wallet_resources, "solana", jwt_auth_private_key)


@pytest.fixture(scope="module", params=WALLET_CASES, ids=WALLET_CASES)
def solana_wallet(
    request: pytest.FixtureRequest, solana_wallets: Mapping[WalletOwnership, WalletUnderTest]
) -> WalletUnderTest:
    test_wallet = solana_wallets[cast(WalletOwnership, request.param)]
    assert test_wallet.wallet.id
    assert test_wallet.wallet.address
    assert test_wallet.wallet.chain_type == "solana"
    return test_wallet


@pytest.mark.parametrize("message", [b"Hello, world!", base64.b64encode(b"Hello, world!").decode("ascii")])
def test_sign_message(privy_client: PrivyClient, solana_wallet: WalletUnderTest, message: str | bytes) -> None:
    response = privy_client.wallets.solana.sign_message(
        solana_wallet.wallet.id,
        message,
        request_options=solana_wallet.request_options,
    )

    assert response.encoding == "base64"
    Ed25519PublicKey.from_public_bytes(_base58_decode(solana_wallet.wallet.address)).verify(
        base64.b64decode(response.signature),
        base64.b64decode(message) if isinstance(message, str) else message,
    )


def test_sign_transaction(privy_client: PrivyClient, solana_wallet: WalletUnderTest) -> None:
    response = privy_client.wallets.solana.sign_transaction(
        solana_wallet.wallet.id,
        _create_transfer_transaction(solana_wallet.wallet.address),
        request_options=solana_wallet.request_options,
    )

    assert response.encoding == "base64"
    assert base64.b64decode(response.signed_transaction)


@pytest.mark.skip(reason="skipped to avoid spending funds")
def test_sign_and_send_transaction(privy_client: PrivyClient, solana_wallet: WalletUnderTest) -> None:
    caip2 = "solana:EtWTRABZaYq6iMfeYKouRu166VU2xqa1"
    response = privy_client.wallets.solana.sign_and_send_transaction(
        solana_wallet.wallet.id,
        _create_transfer_transaction(solana_wallet.wallet.address),
        caip2=caip2,
        request_options=solana_wallet.request_options,
    )

    assert response.caip2 == caip2
    assert response.hash
