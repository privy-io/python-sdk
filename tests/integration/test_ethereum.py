from __future__ import annotations

from typing import cast
from collections.abc import Mapping

import pytest

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


@pytest.fixture(scope="module")
def wallet_resources(privy_client: PrivyClient) -> WalletResources:
    return setup_test_wallet_resources(privy_client)


@pytest.fixture(scope="module")
def ethereum_wallets(
    wallet_resources: WalletResources, jwt_auth_private_key: str
) -> Mapping[WalletOwnership, WalletUnderTest]:
    return create_test_wallets(wallet_resources, "ethereum", jwt_auth_private_key)


@pytest.fixture(scope="module", params=WALLET_CASES, ids=WALLET_CASES)
def ethereum_wallet(
    request: pytest.FixtureRequest, ethereum_wallets: Mapping[WalletOwnership, WalletUnderTest]
) -> WalletUnderTest:
    ownership = cast(WalletOwnership, request.param)
    test_wallet = ethereum_wallets[ownership]
    assert test_wallet.wallet.id
    assert test_wallet.wallet.chain_type == "ethereum"
    return test_wallet


@pytest.mark.parametrize("message", ["Hello, world!", "0x48656c6c6f", b"Hello, world!"])
def test_sign_message(privy_client: PrivyClient, ethereum_wallet: WalletUnderTest, message: str | bytes) -> None:
    response = privy_client.wallets.ethereum.sign_message(
        ethereum_wallet.wallet.id,
        message,
        request_options=ethereum_wallet.request_options,
    )

    assert response.encoding == "hex"
    assert response.signature.startswith("0x")


def test_sign_secp256k1(privy_client: PrivyClient, ethereum_wallet: WalletUnderTest) -> None:
    response = privy_client.wallets.ethereum.sign_secp256k1(
        ethereum_wallet.wallet.id,
        params={"hash": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"},
        request_options=ethereum_wallet.request_options,
    )

    assert response.encoding == "hex"
    assert response.signature.startswith("0x")


def test_sign_7702_authorization(privy_client: PrivyClient, ethereum_wallet: WalletUnderTest) -> None:
    response = privy_client.wallets.ethereum.sign_7702_authorization(
        ethereum_wallet.wallet.id,
        params={
            "chain_id": 11155111,
            "contract": "0x1234567890123456789012345678901234567890",
        },
        request_options=ethereum_wallet.request_options,
    )

    assert response.authorization.contract == "0x1234567890123456789012345678901234567890"
    assert response.authorization.r.startswith("0x")
    assert response.authorization.s.startswith("0x")
    assert response.authorization.y_parity in {0, 1}


def test_sign_transaction(privy_client: PrivyClient, ethereum_wallet: WalletUnderTest) -> None:
    response = privy_client.wallets.ethereum.sign_transaction(
        ethereum_wallet.wallet.id,
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
        request_options=ethereum_wallet.request_options,
    )

    assert response.encoding == "rlp"
    assert response.signed_transaction.startswith("0x")


def test_sign_typed_data(privy_client: PrivyClient, ethereum_wallet: WalletUnderTest) -> None:
    response = privy_client.wallets.ethereum.sign_typed_data(
        ethereum_wallet.wallet.id,
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
        request_options=ethereum_wallet.request_options,
    )

    assert response.encoding == "hex"
    assert response.signature.startswith("0x")


@pytest.mark.skip(reason="Requires a funded wallet")
def test_sign_user_operation(privy_client: PrivyClient, ethereum_wallet: WalletUnderTest) -> None:
    response = privy_client.wallets.ethereum.sign_user_operation(
        ethereum_wallet.wallet.id,
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
        request_options=ethereum_wallet.request_options,
    )

    assert response.encoding == "hex"
    assert response.signature.startswith("0x")


@pytest.mark.skip(reason="Requires a funded wallet")
def test_send_transaction(privy_client: PrivyClient, ethereum_wallet: WalletUnderTest) -> None:
    response = privy_client.wallets.ethereum.send_transaction(
        ethereum_wallet.wallet.id,
        caip2="eip155:11155111",
        params={
            "transaction": {
                "to": ethereum_wallet.wallet.address,
                "value": "0x1",
            }
        },
        request_options=ethereum_wallet.request_options,
    )

    assert response.caip2 == "eip155:11155111"
    assert response.hash.startswith("0x")


@pytest.mark.skip(reason="Requires a funded wallet")
def test_send_calls(privy_client: PrivyClient, ethereum_wallet: WalletUnderTest) -> None:
    response = privy_client.wallets.ethereum.send_calls(
        ethereum_wallet.wallet.id,
        caip2="eip155:11155111",
        params={
            "calls": [
                {
                    "to": ethereum_wallet.wallet.address,
                    "value": "0x1",
                }
            ]
        },
        request_options=ethereum_wallet.request_options,
    )

    assert response.caip2 == "eip155:11155111"
    assert response.transaction_id
