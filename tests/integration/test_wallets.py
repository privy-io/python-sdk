from __future__ import annotations

import os
import base64

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

pytestmark = pytest.mark.integration

RAW_SIGN_HASH = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
RAW_SIGN_PARAMS: WalletRawSignParams = {"params": {"hash": RAW_SIGN_HASH}}


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


def test_raw_sign_with_ownerless_tron_wallet(privy_client: PrivyClient) -> None:
    wallet = privy_client.wallets.create(chain_type="tron")
    assert wallet.id, f"expected created wallet to have an ID, got {wallet.to_dict()!r}"
    assert wallet.address
    assert wallet.chain_type == "tron"
    assert wallet.public_key

    response = privy_client.wallets.raw_sign(
        wallet.id,
        wallet_raw_sign_params=RAW_SIGN_PARAMS,
    )

    assert response.method == "raw_sign"
    assert response.data.encoding == "hex"
    assert response.data.signature.startswith("0x")


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
