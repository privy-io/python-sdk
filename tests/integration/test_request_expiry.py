from __future__ import annotations

import time

import pytest

from privy import (
    P256KeyPair,
    PrivyClient,
    APIStatusError,
    PrivyRequestOptions,
    AuthorizationContext,
    generate_p256_key_pair,
)
from privy.types.wallet_raw_sign_params import WalletRawSignParams

pytestmark = pytest.mark.integration

RAW_SIGN_PARAMS: WalletRawSignParams = {
    "params": {"hash": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"}
}
# Rejections must come from the request expiry check, not from another validation error.
EXPIRY_ERROR = r"(?i)expir"
TWENTY_MINUTES_MS = 20 * 60 * 1000


def now_ms() -> int:
    return time.time_ns() // 1_000_000


@pytest.fixture(scope="module")
def key_pair() -> P256KeyPair:
    return generate_p256_key_pair()


@pytest.fixture(scope="module")
def wallet_id(privy_client: PrivyClient, key_pair: P256KeyPair) -> str:
    # raw_sign does not support ethereum or solana wallets, so use tron (as in test_wallets.py).
    wallet = privy_client.wallets.create(chain_type="tron", owner={"public_key": key_pair.public_key})
    return wallet.id


def signed(key_pair: P256KeyPair, request_expiry: int | None = None) -> PrivyRequestOptions:
    return PrivyRequestOptions(
        authorization_context=AuthorizationContext(authorization_private_keys=[key_pair.private_key]),
        request_expiry=request_expiry,
    )


def test_raw_sign_accepts_the_default_request_expiry(
    privy_client: PrivyClient, wallet_id: str, key_pair: P256KeyPair
) -> None:
    response = privy_client.wallets.raw_sign(
        wallet_id, wallet_raw_sign_params=RAW_SIGN_PARAMS, request_options=signed(key_pair)
    )

    assert response.data.signature.startswith("0x")


def test_raw_sign_accepts_a_per_call_request_expiry(
    privy_client: PrivyClient, wallet_id: str, key_pair: P256KeyPair
) -> None:
    response = privy_client.wallets.raw_sign(
        wallet_id,
        wallet_raw_sign_params=RAW_SIGN_PARAMS,
        request_options=signed(key_pair, privy_client.get_request_expiry(TWENTY_MINUTES_MS)),
    )

    assert response.data.signature.startswith("0x")


def test_raw_sign_rejects_an_expired_request_expiry(
    privy_client: PrivyClient, wallet_id: str, key_pair: P256KeyPair
) -> None:
    with pytest.raises(APIStatusError, match=EXPIRY_ERROR):
        privy_client.wallets.raw_sign(
            wallet_id,
            wallet_raw_sign_params=RAW_SIGN_PARAMS,
            request_options=signed(key_pair, now_ms() - 60_000),
        )


def test_raw_sign_rejects_a_request_expiry_of_0(
    privy_client: PrivyClient, wallet_id: str, key_pair: P256KeyPair
) -> None:
    with pytest.raises(APIStatusError, match=EXPIRY_ERROR):
        privy_client.wallets.raw_sign(
            wallet_id, wallet_raw_sign_params=RAW_SIGN_PARAMS, request_options=signed(key_pair, 0)
        )


def test_update_accepts_the_default_request_expiry(
    privy_client: PrivyClient, wallet_id: str, key_pair: P256KeyPair
) -> None:
    wallet = privy_client.wallets.update(
        wallet_id,
        wallet_update_params={"display_name": "Request expiry default"},
        request_options=signed(key_pair),
    )

    assert wallet.id == wallet_id


def test_update_accepts_a_per_call_request_expiry(
    privy_client: PrivyClient, wallet_id: str, key_pair: P256KeyPair
) -> None:
    wallet = privy_client.wallets.update(
        wallet_id,
        wallet_update_params={"display_name": "Request expiry per-call"},
        request_options=signed(key_pair, privy_client.get_request_expiry(TWENTY_MINUTES_MS)),
    )

    assert wallet.id == wallet_id


def test_update_rejects_an_expired_request_expiry(
    privy_client: PrivyClient, wallet_id: str, key_pair: P256KeyPair
) -> None:
    with pytest.raises(APIStatusError, match=EXPIRY_ERROR):
        privy_client.wallets.update(
            wallet_id,
            wallet_update_params={"display_name": "Request expiry expired"},
            request_options=signed(key_pair, now_ms() - 60_000),
        )


def test_disabled_client_accepts_a_request_without_an_expiry(
    privy_client_without_request_expiry: PrivyClient, wallet_id: str, key_pair: P256KeyPair
) -> None:
    assert privy_client_without_request_expiry.get_request_expiry() is None

    response = privy_client_without_request_expiry.wallets.raw_sign(
        wallet_id, wallet_raw_sign_params=RAW_SIGN_PARAMS, request_options=signed(key_pair)
    )

    assert response.data.signature.startswith("0x")


def test_disabled_client_still_sends_a_per_call_request_expiry_of_0(
    privy_client_without_request_expiry: PrivyClient, wallet_id: str, key_pair: P256KeyPair
) -> None:
    # Without a client default, the request only fails if the per-call 0 is signed and sent.
    with pytest.raises(APIStatusError, match=EXPIRY_ERROR):
        privy_client_without_request_expiry.wallets.raw_sign(
            wallet_id, wallet_raw_sign_params=RAW_SIGN_PARAMS, request_options=signed(key_pair, 0)
        )
