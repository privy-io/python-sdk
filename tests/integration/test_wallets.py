from __future__ import annotations

import pytest

from privy import PrivyClient

pytestmark = pytest.mark.integration

RAW_SIGN_HASH = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"


def test_raw_sign_with_ownerless_tron_wallet(privy_client: PrivyClient) -> None:
    wallet = privy_client.wallets.create(chain_type="tron")
    assert wallet.id, f"expected created wallet to have an ID, got {wallet.to_dict()!r}"
    assert wallet.address
    assert wallet.chain_type == "tron"
    assert wallet.public_key

    response = privy_client.wallets.raw_sign(
        wallet.id,
        wallet_raw_sign_params={"params": {"hash": RAW_SIGN_HASH}},
    )

    assert response.method == "raw_sign"
    assert response.data.encoding == "hex"
    assert response.data.signature.startswith("0x")
