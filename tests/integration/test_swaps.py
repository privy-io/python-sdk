from __future__ import annotations

import uuid

import pytest

from privy import PrivyClient, PrivySwapsService, PrivyRequestOptions, AuthorizationContext, generate_p256_key_pair
from privy.types.wallets import SwapExecuteParams

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skip(reason="Requires a funded wallet"),
]

BASE_CAIP2 = "eip155:8453"
TEST_TOKEN = "0x0000000000000000000000000000000000000001"


def test_authorized_swap_quote(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(
        chain_type="ethereum",
        owner={"public_key": key_pair.public_key},
    )

    quote = privy_client.wallets.swaps.quote(
        wallet.id,
        swap_quote_params={
            "base_amount": "1000000000000000000",
            "source": {
                "asset_address": "native",
                "caip2": BASE_CAIP2,
            },
            "destination": {
                "asset_address": TEST_TOKEN,
                "caip2": BASE_CAIP2,
            },
            "amount_type": "exact_input",
        },
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    assert isinstance(privy_client.wallets.swaps, PrivySwapsService)
    assert quote.input_amount
    assert quote.est_output_amount
    assert quote.input_token == "native"
    assert quote.output_token == TEST_TOKEN
    assert quote.minimum_output_amount


def test_authorized_swap_execution_with_idempotency(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(
        chain_type="ethereum",
        owner={"public_key": key_pair.public_key},
    )
    swap_params: SwapExecuteParams = {
        "base_amount": "1000000000000000000",
        "source": {
            "asset_address": "native",
            "caip2": BASE_CAIP2,
        },
        "destination": {
            "asset_address": TEST_TOKEN,
            "caip2": BASE_CAIP2,
        },
        "amount_type": "exact_input",
        "slippage_bps": 50,
    }
    idempotency_key = f"swap-{uuid.uuid4()}"

    action = privy_client.wallets.swaps.execute(
        wallet.id,
        swap_execute_params=swap_params,
        idempotency_key=idempotency_key,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    duplicate_action = privy_client.wallets.swaps.execute(
        wallet.id,
        swap_execute_params=swap_params,
        idempotency_key=idempotency_key,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    assert action.id
    assert action.type == "swap"
    assert action.wallet_id == wallet.id
    assert action.status
    assert duplicate_action.id == action.id
