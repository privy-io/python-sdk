from __future__ import annotations

import os
import re
import hmac
import base64
import hashlib
import unicodedata
from typing import cast
from collections.abc import Mapping

import pytest
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519

from privy import (
    PrivyClient,
    PrivyRequestOptions,
    AuthorizationContext,
    WalletAPIRequestSignatureInput,
    generate_p256_key_pair,
    format_request_for_authorization_signature,
)
from privy.types.wallet_raw_sign_params import WalletRawSignParams
from privy.types.wallet_transfer_params import WalletTransferParams

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
TRANSFER_PARAMS: WalletTransferParams = {
    "source": {"asset": "usdc", "amount": "0.01", "chain": "base"},
    "destination": {"address": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"},
}


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


@pytest.fixture(scope="module")
def ethereum_wallets(
    wallet_resources: WalletResources, jwt_auth_private_key: str
) -> Mapping[WalletOwnership, WalletUnderTest]:
    return create_test_wallets(wallet_resources, "ethereum", jwt_auth_private_key)


@pytest.fixture(scope="module", params=WALLET_CASES, ids=WALLET_CASES)
def ethereum_wallet(
    request: pytest.FixtureRequest, ethereum_wallets: Mapping[WalletOwnership, WalletUnderTest]
) -> WalletUnderTest:
    return ethereum_wallets[cast(WalletOwnership, request.param)]


def encoded_public_key(private_key: ec.EllipticCurvePrivateKey) -> str:
    public_key = private_key.public_key().public_bytes(
        serialization.Encoding.DER,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return base64.b64encode(public_key).decode("ascii")


def authorization_payload(wallet_id: str, request_expiry: int) -> bytes:
    api_url = (os.environ.get("TEST_API_URL") or "https://api.staging.privy.io").rstrip("/")
    return format_request_for_authorization_signature(
        WalletAPIRequestSignatureInput(
            method="POST",
            url=f"{api_url}/v1/wallets/{wallet_id}/raw_sign",
            body=RAW_SIGN_PARAMS,
            headers={
                "privy-app-id": os.environ["TEST_APP_ID"],
                "privy-request-expiry": str(request_expiry),
            },
        )
    )


def compressed_secp256k1_public_key(private_key: str) -> str:
    key = ec.derive_private_key(int(private_key, 16), ec.SECP256K1())
    return (
        key.public_key()
        .public_bytes(
            serialization.Encoding.X962,
            serialization.PublicFormat.CompressedPoint,
        )
        .hex()
    )


def solana_address_from_seed_phrase(seed_phrase: str) -> str:
    mnemonic = unicodedata.normalize("NFKD", seed_phrase).encode("utf-8")
    seed = hashlib.pbkdf2_hmac("sha512", mnemonic, b"mnemonic", 2048)
    digest = hmac.new(b"ed25519 seed", seed, hashlib.sha512).digest()
    private_key, chain_code = digest[:32], digest[32:]

    for index in (44, 501, 0, 0):
        hardened_index = index + 2**31
        digest = hmac.new(
            chain_code,
            b"\x00" + private_key + hardened_index.to_bytes(4, "big"),
            hashlib.sha512,
        ).digest()
        private_key, chain_code = digest[:32], digest[32:]

    public_key = (
        ed25519.Ed25519PrivateKey.from_private_bytes(private_key)
        .public_key()
        .public_bytes(
            serialization.Encoding.Raw,
            serialization.PublicFormat.Raw,
        )
    )
    return base58_encode(public_key)


def base58_encode(value: bytes) -> str:
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    encoded = ""
    number = int.from_bytes(value, "big")
    while number:
        number, remainder = divmod(number, 58)
        encoded = alphabet[remainder] + encoded
    return alphabet[0] * (len(value) - len(value.lstrip(b"\x00"))) + encoded


def test_export_private_key(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(
        chain_type="tron",
        owner={"public_key": key_pair.public_key},
    )
    assert wallet.public_key

    exported = privy_client.wallets.export_private_key(
        wallet.id,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    assert re.fullmatch(r"[0-9a-f]{64}", exported["private_key"])
    assert compressed_secp256k1_public_key(exported["private_key"]) == wallet.public_key


def test_export_seed_phrase(privy_client: PrivyClient) -> None:
    key_pair = generate_p256_key_pair()
    wallet = privy_client.wallets.create(
        chain_type="solana",
        owner={"public_key": key_pair.public_key},
    )

    exported = privy_client.wallets.export_seed_phrase(
        wallet.id,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                authorization_private_keys=[key_pair.private_key],
            )
        ),
    )

    words = exported["seed_phrase"].split()
    assert 12 <= len(words) <= 24
    assert all(re.fullmatch(r"[a-z]+", word) for word in words)
    assert solana_address_from_seed_phrase(exported["seed_phrase"]) == wallet.address


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


@pytest.mark.skip(reason="Requires funded wallets and transfers real funds")
def test_transfer(privy_client: PrivyClient, ethereum_wallet: WalletUnderTest) -> None:
    wallet = ethereum_wallet.wallet
    response = privy_client.wallets.transfer(
        wallet.id,
        wallet_transfer_params=TRANSFER_PARAMS,
        request_options=ethereum_wallet.request_options,
    )

    assert response.id
    assert response.wallet_id == wallet.id
    assert response.type == "transfer"
    assert response.destination_address == TRANSFER_PARAMS["destination"]["address"]
    assert response.source_chain == TRANSFER_PARAMS["source"]["chain"]


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

    request_expiry = privy_client.get_request_expiry()
    assert request_expiry is not None
    signature = private_key.sign(authorization_payload(wallet.id, request_expiry), ec.ECDSA(hashes.SHA256()))
    response = privy_client.wallets.raw_sign(
        wallet.id,
        wallet_raw_sign_params=RAW_SIGN_PARAMS,
        request_options=PrivyRequestOptions(
            authorization_context=AuthorizationContext(
                signatures=[base64.b64encode(signature).decode("ascii")],
            ),
            request_expiry=request_expiry,
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
