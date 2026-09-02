from __future__ import annotations

import time

import pytest

from privy import PrivyClient, PrivyTronService
from privy.types.wallet import Wallet

pytestmark = pytest.mark.integration


def _base58check_to_hex(value: str) -> str:
    number = 0
    for character in value:
        number = number * 58 + "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz".index(character)
    decoded = number.to_bytes((number.bit_length() + 7) // 8, "big")
    decoded = b"\0" * (len(value) - len(value.lstrip("1"))) + decoded
    return decoded[:21].hex()


@pytest.fixture(scope="module")
def tron_wallet(privy_client: PrivyClient) -> Wallet:
    wallet = privy_client.wallets.create(chain_type="tron")
    assert wallet.id
    assert wallet.address
    assert wallet.chain_type == "tron"
    return wallet


def test_tron_service(privy_client: PrivyClient) -> None:
    assert isinstance(privy_client.wallets.tron, PrivyTronService)


def test_sign_transaction(privy_client: PrivyClient, tron_wallet: Wallet) -> None:
    now = int(time.time() * 1000)
    owner_address = _base58check_to_hex(tron_wallet.address)
    response = privy_client.wallets.tron.sign_transaction(
        tron_wallet.id,
        params={
            "raw_data": {
                "contract": [
                    {
                        "type": "TransferContract",
                        "owner_address": owner_address,
                        "to_address": "410000000000000000000000000000000000000000",
                        "amount": 1,
                    }
                ],
                "ref_block_bytes": "1a2b",
                "ref_block_hash": "abc1234567890def",
                "expiration": now + 60_000,
                "timestamp": now,
            }
        },
    )

    assert response.encoding == "hex"
    assert len(response.signed_transaction) >= 130
    assert all(character in "0123456789abcdefABCDEF" for character in response.signed_transaction)


@pytest.mark.skip(reason="skipped to avoid spending funds")
def test_send_transaction(privy_client: PrivyClient, tron_wallet: Wallet) -> None:
    response = privy_client.wallets.tron.send_transaction(
        tron_wallet.id,
        caip2="tron:0xcd8690dc",
        params={
            "raw_data": {
                "contract": [
                    {
                        "type": "TransferContract",
                        "owner_address": _base58check_to_hex(tron_wallet.address),
                        "to_address": "410000000000000000000000000000000000000000",
                        "amount": 1,
                    }
                ]
            }
        },
    )

    assert response.caip2 == "tron:0xcd8690dc"
    assert response.hash
    assert response.transaction_id
