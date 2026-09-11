from __future__ import annotations

import os
import uuid
from dataclasses import dataclass

import pytest

from privy import (
    PrivyClient,
    PrivyEarnService,
    PrivyRequestOptions,
    AuthorizationContext,
    PrivyEarnEthereumService,
    PrivyEarnEthereumIncentiveService,
    generate_p256_key_pair,
)
from privy.types import Wallet
from privy.types.wallets.earn import EthereumDepositParams

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skip(reason="Requires funds and a live earn vault"),
]

EARN_TEST_VAULT_ID_ENV = "EARN_TEST_VAULT_ID"
EARN_TEST_INCENTIVE_CHAIN = "base"


@dataclass(frozen=True)
class OwnedEthereumWallet:
    wallet: Wallet
    request_options: PrivyRequestOptions


@pytest.fixture
def owned_ethereum_wallet(privy_client: PrivyClient) -> OwnedEthereumWallet:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(
        chain_type="ethereum",
        owner={"public_key": key_pair.public_key},
    )
    return OwnedEthereumWallet(
        wallet=wallet,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )


@pytest.fixture
def earn_vault_id() -> str:
    vault_id = os.environ.get(EARN_TEST_VAULT_ID_ENV)
    if not vault_id:
        pytest.skip(f"{EARN_TEST_VAULT_ID_ENV} is required for live earn mutation tests")
    return vault_id


def test_wallets_earn_exposes_authorized_services(privy_client: PrivyClient) -> None:
    assert isinstance(privy_client.wallets.earn, PrivyEarnService)
    assert isinstance(privy_client.wallets.earn.ethereum, PrivyEarnEthereumService)
    assert isinstance(
        privy_client.wallets.earn.ethereum.incentive,
        PrivyEarnEthereumIncentiveService,
    )


def test_deposit_on_owned_wallet(
    privy_client: PrivyClient,
    earn_vault_id: str,
    owned_ethereum_wallet: OwnedEthereumWallet,
) -> None:
    response = privy_client.wallets.earn.ethereum.deposit(
        owned_ethereum_wallet.wallet.id,
        ethereum_deposit_params={
            "vault_id": earn_vault_id,
            "amount": "0.01",
        },
        idempotency_key=str(uuid.uuid4()),
        request_options=owned_ethereum_wallet.request_options,
    )

    assert response.type == "earn_deposit"
    assert response.wallet_id == owned_ethereum_wallet.wallet.id


def test_withdraw_on_owned_wallet(
    privy_client: PrivyClient,
    earn_vault_id: str,
    owned_ethereum_wallet: OwnedEthereumWallet,
) -> None:
    response = privy_client.wallets.earn.ethereum.withdraw(
        owned_ethereum_wallet.wallet.id,
        ethereum_withdraw_params={
            "vault_id": earn_vault_id,
            "raw_amount": "1000000",
        },
        idempotency_key=str(uuid.uuid4()),
        request_options=owned_ethereum_wallet.request_options,
    )

    assert response.type == "earn_withdraw"
    assert response.wallet_id == owned_ethereum_wallet.wallet.id


def test_incentive_claim_on_owned_wallet(
    privy_client: PrivyClient,
    owned_ethereum_wallet: OwnedEthereumWallet,
) -> None:
    response = privy_client.wallets.earn.ethereum.incentive.claim(
        owned_ethereum_wallet.wallet.id,
        incentive_claim_params={"chain": EARN_TEST_INCENTIVE_CHAIN},
        idempotency_key=str(uuid.uuid4()),
        request_options=owned_ethereum_wallet.request_options,
    )

    assert response.type == "earn_incentive_claim"
    assert response.wallet_id == owned_ethereum_wallet.wallet.id


def test_deposit_idempotency(
    privy_client: PrivyClient,
    earn_vault_id: str,
    owned_ethereum_wallet: OwnedEthereumWallet,
) -> None:
    idempotency_key = str(uuid.uuid4())
    params: EthereumDepositParams = {
        "vault_id": earn_vault_id,
        "amount": "0.01",
    }
    first = privy_client.wallets.earn.ethereum.deposit(
        owned_ethereum_wallet.wallet.id,
        ethereum_deposit_params=params,
        idempotency_key=idempotency_key,
        request_options=owned_ethereum_wallet.request_options,
    )
    repeated = privy_client.wallets.earn.ethereum.deposit(
        owned_ethereum_wallet.wallet.id,
        ethereum_deposit_params=params,
        idempotency_key=idempotency_key,
        request_options=owned_ethereum_wallet.request_options,
    )

    assert repeated.id == first.id
