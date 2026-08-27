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
