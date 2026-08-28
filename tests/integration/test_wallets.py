from __future__ import annotations

import os
import base64
from typing import cast
from collections.abc import Mapping

import pytest
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

from privy import (
    PrivyClient,
    PrivyRequestOptions,
    AuthorizationContext,
    WalletAPIRequestSignatureInput,
    generate_p256_key_pair,
    format_request_for_authorization_signature,
)
from privy.types.wallet_raw_sign_params import WalletRawSignParams

from .wallet_setup import (
    WALLET_CASES,
    TestWallet as WalletUnderTest,
    WalletOwnership,
    TestWalletResources as WalletResources,
    create_test_wallets,
    setup_test_wallet_resources,
)

pytestmark = pytest.mark.integration

RAW_SIGN_HASH = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
RAW_SIGN_PARAMS: WalletRawSignParams = {"params": {"hash": RAW_SIGN_HASH}}


@pytest.fixture(scope="module")
def wallet_resources(privy_client: PrivyClient) -> WalletResources:
    return setup_test_wallet_resources(privy_client)


@pytest.fixture(scope="module")
def tron_wallets(
    wallet_resources: WalletResources, jwt_auth_private_key: str
) -> Mapping[WalletOwnership, WalletUnderTest]:
    return create_test_wallets(wallet_resources, "tron", jwt_auth_private_key)


@pytest.fixture(scope="module", params=WALLET_CASES, ids=WALLET_CASES)
def tron_wallet(
    request: pytest.FixtureRequest, tron_wallets: Mapping[WalletOwnership, WalletUnderTest]
) -> WalletUnderTest:
    return tron_wallets[cast(WalletOwnership, request.param)]


def encoded_public_key(private_key: ec.EllipticCurvePrivateKey) -> str:
    public_key = private_key.public_key().public_bytes(
        serialization.Encoding.DER,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return base64.b64encode(public_key).decode("ascii")


def authorization_payload(wallet_id: str) -> bytes:
    api_url = (os.environ.get("TEST_API_URL") or "https://api.staging.privy.io").rstrip("/")
    return format_request_for_authorization_signature(
        WalletAPIRequestSignatureInput(
            method="POST",
            url=f"{api_url}/v1/wallets/{wallet_id}/raw_sign",
            body=RAW_SIGN_PARAMS,
            headers={"privy-app-id": os.environ["TEST_APP_ID"]},
        )
    )


def test_raw_sign(privy_client: PrivyClient, tron_wallet: WalletUnderTest) -> None:
    wallet = tron_wallet.wallet
    assert wallet.id, f"expected created wallet to have an ID, got {wallet.to_dict()!r}"
    assert wallet.address
    assert wallet.chain_type == "tron"
    assert wallet.public_key

    response = privy_client.wallets.raw_sign(
        wallet.id,
        wallet_raw_sign_params=RAW_SIGN_PARAMS,
        request_options=tron_wallet.request_options,
    )

    assert response.method == "raw_sign"
    assert response.data.encoding == "hex"
    assert response.data.signature.startswith("0x")


def test_update_with_authorization_private_key(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(
        chain_type="ethereum",
        owner={"public_key": key_pair.public_key},
    )

    updated = privy_client.wallets.update(
        wallet.id,
        wallet_update_params={"display_name": "Updated wallet"},
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    assert updated.id == wallet.id
    assert updated.display_name == "Updated wallet"


def test_raw_sign_with_authorization_signer(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    private_key = serialization.load_der_private_key(
        base64.b64decode(key_pair.private_key),
        password=None,
    )
    assert isinstance(private_key, ec.EllipticCurvePrivateKey)
    wallet = privy_client.wallets.create(
        chain_type="tron",
        owner={"public_key": key_pair.public_key},
    )
    assert wallet.id
    assert wallet.chain_type == "tron"

    response = privy_client.wallets.raw_sign(
        wallet.id,
        wallet_raw_sign_params=RAW_SIGN_PARAMS,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                signers=[
                    lambda payload: base64.b64encode(private_key.sign(payload, ec.ECDSA(hashes.SHA256()))).decode(
                        "ascii"
                    )
                ],
            )
        ),
    )

    assert response.method == "raw_sign"
    assert response.data.encoding == "hex"
    assert response.data.signature.startswith("0x")


def test_raw_sign_with_precomputed_authorization_signature(privy_client: PrivyClient) -> None:
    private_key = ec.generate_private_key(ec.SECP256R1())
    wallet = privy_client.wallets.create(
        chain_type="tron",
        owner={"public_key": encoded_public_key(private_key)},
    )
    assert wallet.id
    assert wallet.chain_type == "tron"

    signature = private_key.sign(authorization_payload(wallet.id), ec.ECDSA(hashes.SHA256()))
    response = privy_client.wallets.raw_sign(
        wallet.id,
        wallet_raw_sign_params=RAW_SIGN_PARAMS,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                signatures=[base64.b64encode(signature).decode("ascii")],
            )
        ),
    )

    assert response.method == "raw_sign"
    assert response.data.encoding == "hex"
    assert response.data.signature.startswith("0x")


def test_raw_sign_with_authorization_private_key(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(
        chain_type="tron",
        owner={"public_key": key_pair.public_key},
    )
    assert wallet.id
    assert wallet.chain_type == "tron"

    response = privy_client.wallets.raw_sign(
        wallet.id,
        wallet_raw_sign_params=RAW_SIGN_PARAMS,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    assert response.method == "raw_sign"
    assert response.data.encoding == "hex"
    assert response.data.signature.startswith("0x")


def test_rpc_with_authorization_private_key(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(
        chain_type="ethereum",
        owner={"public_key": key_pair.public_key},
    )
    assert wallet.id
    assert wallet.chain_type == "ethereum"

    response = privy_client.wallets.rpc(
        wallet.id,
        wallet_rpc_request_body={
            "method": "personal_sign",
            "chain_type": "ethereum",
            "params": {"message": "Hello, world!", "encoding": "utf-8"},
        },
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    assert response.method == "personal_sign"
    assert response.data.encoding == "hex"
    assert response.data.signature.startswith("0x")
