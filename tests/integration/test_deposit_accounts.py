from __future__ import annotations

import time

import pytest

from privy import PrivyClient, APIStatusError, PrivyRequestOptions, AuthorizationContext
from privy.types.wallets.deposit_accounts import CryptoCreateParams

from .wallet_setup import generate_test_jwt, setup_test_wallet_resources

pytestmark = pytest.mark.integration

INLINE_ROUTE: CryptoCreateParams = {
    "type": "inline_route",
    "destination": {"asset": "usdc", "chain": "base"},
    # Only Base: the API rejects source chains that need app-paid gas sponsorship, which staging lacks.
    "source": {"mode": "include", "values": [{"asset": "usdc", "chain": "base"}]},
}
# Rejections must come from the request expiry check, not from another validation error.
EXPIRY_ERROR = r"(?i)expir"


@pytest.fixture
def wallet_and_options(privy_client: PrivyClient, jwt_auth_private_key: str) -> tuple[str, AuthorizationContext]:
    # The destination wallet must be owned by a single user, who authorizes the request.
    resources = setup_test_wallet_resources(privy_client)
    wallet = privy_client.wallets.create(chain_type="ethereum", owner={"user_id": resources.user_id})
    user_jwt = generate_test_jwt(jwt_auth_private_key, resources.custom_user_id)
    return wallet.id, AuthorizationContext(user_jwts=[user_jwt])


def test_create_crypto_deposit_account_with_the_default_request_expiry(
    privy_client: PrivyClient, wallet_and_options: tuple[str, AuthorizationContext]
) -> None:
    wallet_id, authorization_context = wallet_and_options

    response = privy_client.wallets.deposit_accounts.crypto.create(
        wallet_id,
        crypto_create_params=INLINE_ROUTE,
        request_options=PrivyRequestOptions(authorization_context=authorization_context),
    )

    assert response


def test_create_crypto_deposit_account_rejects_an_expired_request_expiry(
    privy_client: PrivyClient, wallet_and_options: tuple[str, AuthorizationContext]
) -> None:
    wallet_id, authorization_context = wallet_and_options

    with pytest.raises(APIStatusError, match=EXPIRY_ERROR):
        privy_client.wallets.deposit_accounts.crypto.create(
            wallet_id,
            crypto_create_params=INLINE_ROUTE,
            request_options=PrivyRequestOptions(
                authorization_context=authorization_context,
                request_expiry=time.time_ns() // 1_000_000 - 60_000,
            ),
        )
