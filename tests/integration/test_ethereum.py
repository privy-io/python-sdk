from __future__ import annotations

import pytest

from privy import PrivyClient
from privy.types.wallet import Wallet

pytestmark = pytest.mark.integration


@pytest.fixture(scope="module")
def ethereum_wallet(privy_client: PrivyClient) -> Wallet:
    wallet = privy_client.wallets.create(chain_type="ethereum")
    assert wallet.id
    assert wallet.chain_type == "ethereum"
    return wallet


@pytest.mark.parametrize("message", ["Hello, world!", "0x48656c6c6f", b"Hello, world!"])
def test_sign_message(privy_client: PrivyClient, ethereum_wallet: Wallet, message: str | bytes) -> None:
    response = privy_client.wallets.ethereum.sign_message(ethereum_wallet.id, message)

    assert response.encoding == "hex"
    assert response.signature.startswith("0x")


def test_sign_secp256k1(privy_client: PrivyClient, ethereum_wallet: Wallet) -> None:
    response = privy_client.wallets.ethereum.sign_secp256k1(
        ethereum_wallet.id,
        params={"hash": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"},
    )

    assert response.encoding == "hex"
    assert response.signature.startswith("0x")


def test_sign_7702_authorization(privy_client: PrivyClient, ethereum_wallet: Wallet) -> None:
    response = privy_client.wallets.ethereum.sign_7702_authorization(
        ethereum_wallet.id,
        params={
            "chain_id": 11155111,
            "contract": "0x1234567890123456789012345678901234567890",
        },
    )

    assert response.authorization.contract == "0x1234567890123456789012345678901234567890"
    assert response.authorization.r.startswith("0x")
    assert response.authorization.s.startswith("0x")
    assert response.authorization.y_parity in {0, 1}


def test_sign_transaction(privy_client: PrivyClient, ethereum_wallet: Wallet) -> None:
    response = privy_client.wallets.ethereum.sign_transaction(
        ethereum_wallet.id,
        params={
            "transaction": {
                "type": 2,
                "chain_id": 1,
                "to": "0x1234567890123456789012345678901234567890",
                "value": "0x1",
                "gas_limit": "0x5208",
                "data": "0x",
            }
        },
    )

    assert response.encoding == "rlp"
    assert response.signed_transaction.startswith("0x")
