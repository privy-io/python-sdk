from __future__ import annotations

import time

import pytest

from privy import (
    PrivyClient,
    APIStatusError,
    PrivyRequestOptions,
    AuthorizationContext,
    generate_p256_key_pair,
)
from privy.types.wallets.payout import FiatCreateParams

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skip(reason="Requires a registered fiat account, which the API checks before the request expiry"),
]

FIAT_PAYOUT: FiatCreateParams = {
    "destination": {"fiat_account_id": "fiat-account-id"},
    "source": {"amount": "1.00", "asset": "usdc", "chain": "base"},
}
# Rejections must come from the request expiry check, not from another validation error.
EXPIRY_ERROR = r"(?i)expir"


def test_fiat_payout_rejects_an_expired_request_expiry(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(chain_type="ethereum", owner={"public_key": key_pair.public_key})

    with pytest.raises(APIStatusError, match=EXPIRY_ERROR):
        privy_client.wallets.payout.fiat.create(
            wallet.id,
            fiat_create_params=FIAT_PAYOUT,
            request_options=PrivyRequestOptions(
                authorization_context=AuthorizationContext(authorization_private_keys=[key_pair.private_key]),
                request_expiry=time.time_ns() // 1_000_000 - 60_000,
            ),
        )


def test_fiat_payout_with_a_per_call_request_expiry(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(chain_type="ethereum", owner={"public_key": key_pair.public_key})

    response = privy_client.wallets.payout.fiat.create(
        wallet.id,
        fiat_create_params=FIAT_PAYOUT,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(authorization_private_keys=[key_pair.private_key]),
            request_expiry=privy_client.get_request_expiry(20 * 60 * 1000),
        ),
    )

    assert response.wallet_id == wallet.id
