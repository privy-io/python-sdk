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


def test_sign_typed_data(privy_client: PrivyClient, ethereum_wallet: Wallet) -> None:
    response = privy_client.wallets.ethereum.sign_typed_data(
        ethereum_wallet.id,
        params={
            "typed_data": {
                "domain": {
                    "name": "Test",
                    "version": "1",
                    "chainId": 1,
                    "verifyingContract": "0x1234567890123456789012345678901234567890",
                },
                "primary_type": "Message",
                "types": {"Message": [{"name": "content", "type": "string"}]},
                "message": {"content": "Hello world"},
            }
        },
    )

    assert response.encoding == "hex"
    assert response.signature.startswith("0x")


@pytest.mark.skip(reason="Requires a funded wallet")
def test_sign_user_operation(privy_client: PrivyClient, ethereum_wallet: Wallet) -> None:
    response = privy_client.wallets.ethereum.sign_user_operation(
        ethereum_wallet.id,
        params={
            "chain_id": "0x66eee",
            "contract": "0x1234567890123456789012345678901234567890",
            "user_operation": {
                "sender": "0x1234567890123456789012345678901234567890",
                "nonce": "0x0",
                "call_data": "0x",
                "call_gas_limit": "0x1",
                "verification_gas_limit": "0x1",
                "pre_verification_gas": "0x1",
                "max_fee_per_gas": "0x1",
                "max_priority_fee_per_gas": "0x1",
            },
        },
    )

    assert response.encoding == "hex"
    assert response.signature.startswith("0x")
