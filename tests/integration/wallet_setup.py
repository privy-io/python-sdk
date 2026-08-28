from __future__ import annotations

import json
import time
import uuid
import base64
from typing import Literal
from dataclasses import dataclass

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

from privy import P256KeyPair, PrivyClient, PrivyRequestOptions, AuthorizationContext, generate_p256_key_pair
from privy.types import Wallet, WalletChainType

WalletOwnership = Literal["ownerless", "key-owned", "user-owned", "quorum-owned"]

WALLET_CASES: tuple[WalletOwnership, ...] = (
    "ownerless",
    "key-owned",
    "user-owned",
    "quorum-owned",
)


@dataclass(frozen=True)
class TestWalletResources:
    client: PrivyClient
    p256_key_pair: P256KeyPair
    quorum_key_pair: P256KeyPair
    user_id: str
    custom_user_id: str
    quorum_id: str


@dataclass(frozen=True)
class TestWallet:
    ownership: WalletOwnership
    wallet: Wallet
    request_options: PrivyRequestOptions | None


def generate_test_jwt(private_key_pem: str, subject: str) -> str:
    """Create the RS256 custom-auth JWT used to authorize user-owned wallets."""

    private_key = serialization.load_pem_private_key(private_key_pem.encode("utf-8"), password=None)
    if not isinstance(private_key, rsa.RSAPrivateKey):
        raise ValueError("JWT_AUTH_SK must be a PEM-encoded RSA private key")

    header = _base64url_json({"alg": "RS256", "typ": "JWT"})
    payload = _base64url_json({"sub": subject, "exp": int(time.time()) + 60 * 60})
    signing_input = f"{header}.{payload}".encode("ascii")
    signature = private_key.sign(signing_input, padding.PKCS1v15(), hashes.SHA256())
    return f"{header}.{payload}.{_base64url(signature)}"


def setup_test_wallet_resources(client: PrivyClient) -> TestWalletResources:
    """Create fresh authorization resources shared by a test module's wallets."""

    p256_key_pair = generate_p256_key_pair()
    quorum_key_pair = generate_p256_key_pair()
    custom_user_id = f"test-user-{uuid.uuid4()}"

    # PrivyClient adds authorization-aware wallet helpers on top of this generated API client.
    api = client._client  # pyright: ignore[reportPrivateUsage]
    user = api.users.create(linked_accounts=[{"type": "custom_auth", "custom_user_id": custom_user_id}])
    quorum = api.key_quorums.create(
        public_keys=[quorum_key_pair.public_key],
        user_ids=[user.id],
        display_name="Python SDK Test Quorum",
        authorization_threshold=1,
    )

    return TestWalletResources(
        client=client,
        p256_key_pair=p256_key_pair,
        quorum_key_pair=quorum_key_pair,
        user_id=user.id,
        custom_user_id=custom_user_id,
        quorum_id=quorum.id,
    )


def create_test_wallets(
    resources: TestWalletResources,
    chain_type: WalletChainType,
    jwt_auth_private_key: str,
) -> dict[WalletOwnership, TestWallet]:
    """Create one on-demand wallet for every supported ownership configuration."""

    user_jwt = generate_test_jwt(jwt_auth_private_key, resources.custom_user_id)
    quorum_jwt = generate_test_jwt(jwt_auth_private_key, resources.custom_user_id)
    wallets: dict[WalletOwnership, TestWallet] = {}

    for ownership in WALLET_CASES:
        authorization_context: AuthorizationContext | None = None

        if ownership == "ownerless":
            wallet = resources.client.wallets.create(chain_type=chain_type)
        elif ownership == "key-owned":
            wallet = resources.client.wallets.create(
                chain_type=chain_type,
                owner={"public_key": resources.p256_key_pair.public_key},
            )
            authorization_context = AuthorizationContext(
                authorization_private_keys=[resources.p256_key_pair.private_key]
            )
        elif ownership == "user-owned":
            wallet = resources.client.wallets.create(
                chain_type=chain_type,
                owner={"user_id": resources.user_id},
            )
            authorization_context = AuthorizationContext(user_jwts=[user_jwt])
        else:
            wallet = resources.client.wallets.create(chain_type=chain_type, owner_id=resources.quorum_id)
            authorization_context = AuthorizationContext(
                authorization_private_keys=[resources.quorum_key_pair.private_key],
                user_jwts=[quorum_jwt],
            )

        request_options = (
            PrivyRequestOptions(authorization_context=authorization_context)
            if authorization_context is not None
            else None
        )
        wallets[ownership] = TestWallet(
            ownership=ownership,
            wallet=wallet,
            request_options=request_options,
        )

    return wallets


def _base64url_json(value: object) -> str:
    return _base64url(json.dumps(value, separators=(",", ":")).encode("utf-8"))


def _base64url(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).rstrip(b"=").decode("ascii")
