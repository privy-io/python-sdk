from __future__ import annotations

import time
from collections import UserList
from collections.abc import Iterator

import pytest

from privy import (
    PrivyClient,
    APIStatusError,
    PrivyRequestOptions,
    AuthorizationContext,
    generate_p256_key_pair,
)
from privy.types import Wallet

pytestmark = pytest.mark.integration

# Rejections must come from the request expiry check, not from another validation error.
EXPIRY_ERROR = r"(?i)expir"


@pytest.fixture(scope="module")
def key_owned_wallet(privy_client: PrivyClient) -> tuple[Wallet, PrivyRequestOptions]:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(chain_type="ethereum", owner={"public_key": key_pair.public_key})
    return wallet, PrivyRequestOptions(
        authorization_context=AuthorizationContext(authorization_private_keys=[key_pair.private_key])
    )


@pytest.fixture(scope="module")
def automation_id(privy_client: PrivyClient) -> Iterator[str]:
    # PrivyClient has no automation service, so create one through the generated API client.
    api = privy_client._client  # pyright: ignore[reportPrivateUsage]
    automation = api.wallet_automations.create(
        config={
            "trigger": {"type": "deposit", "assets": {"mode": "all"}},
            "action": {
                "type": "swap",
                "destination_chain_asset": {"asset_address": "native", "caip2": "eip155:8453"},
            },
        },
        owner_id=None,
        name="Python SDK request expiry test",
    )
    yield automation.id
    api.wallet_automations.delete(automation.id)


def test_attach_and_detach_automations_with_the_default_request_expiry(
    privy_client: PrivyClient, key_owned_wallet: tuple[Wallet, PrivyRequestOptions], automation_id: str
) -> None:
    wallet, request_options = key_owned_wallet

    # UserList checks that non-list sequences are signed as the list the API receives.
    attached = privy_client.wallets.attach_automations(
        wallet.id,
        wallet_attach_automations_params={
            "automation_ids": UserList([automation_id]),
            "params": {"destination_address": wallet.address},
        },
        request_options=request_options,
    )
    detached = privy_client.wallets.detach_automations(
        wallet.id,
        wallet_detach_automations_params={"automation_ids": UserList([automation_id])},
        request_options=request_options,
    )

    assert [attachment.automation_id for attachment in attached.data] == [automation_id]
    assert detached.success is True


def test_attach_automations_rejects_an_expired_request_expiry(
    privy_client: PrivyClient, key_owned_wallet: tuple[Wallet, PrivyRequestOptions], automation_id: str
) -> None:
    wallet, request_options = key_owned_wallet

    with pytest.raises(APIStatusError, match=EXPIRY_ERROR):
        privy_client.wallets.attach_automations(
            wallet.id,
            wallet_attach_automations_params={
                "automation_ids": [automation_id],
                "params": {"destination_address": wallet.address},
            },
            request_options=PrivyRequestOptions(
                authorization_context=request_options.authorization_context,
                request_expiry=time.time_ns() // 1_000_000 - 60_000,
            ),
        )


def test_detach_automations_rejects_an_expired_request_expiry(
    privy_client: PrivyClient, key_owned_wallet: tuple[Wallet, PrivyRequestOptions], automation_id: str
) -> None:
    wallet, request_options = key_owned_wallet

    with pytest.raises(APIStatusError, match=EXPIRY_ERROR):
        privy_client.wallets.detach_automations(
            wallet.id,
            wallet_detach_automations_params={"automation_ids": [automation_id]},
            request_options=PrivyRequestOptions(
                authorization_context=request_options.authorization_context,
                request_expiry=time.time_ns() // 1_000_000 - 60_000,
            ),
        )
