from __future__ import annotations

import os
import json
import base64
import secrets
from uuid import uuid4
from datetime import datetime, timezone, timedelta
from collections.abc import Iterator

import pytest
from svix.webhooks import Webhook

from privy import PrivyClient, InvalidWebhookError
from privy.types import User, UserCreatedWebhookPayload

from .conftest import STAGING_API_URL, required_environment

pytestmark = pytest.mark.integration


@pytest.fixture(scope="module")
def staging_user(privy_client: PrivyClient) -> Iterator[User]:
    user = privy_client.users.create(
        linked_accounts=[
            {
                "type": "email",
                "address": f"python-webhook-integration-{uuid4()}@privy.io",
            }
        ]
    )
    try:
        yield user
    finally:
        privy_client.users.delete(user.id)


@pytest.fixture(scope="module")
def webhook_payload(staging_user: User) -> bytes:
    return json.dumps(
        {"type": "user.created", "user": staging_user.to_dict()},
        separators=(",", ":"),
    ).encode()


def signing_secret() -> str:
    return base64.b64encode(secrets.token_bytes(32)).decode()


def signed_headers(secret: str, payload: bytes, timestamp: datetime | None = None) -> dict[str, str]:
    timestamp = timestamp or datetime.now(timezone.utc)
    message_id = f"msg_{uuid4()}"
    signature = Webhook(secret).sign(message_id, timestamp, payload.decode())
    return {
        "svix-id": message_id,
        "svix-timestamp": str(int(timestamp.timestamp())),
        "svix-signature": signature,
    }


def test_verify_with_per_call_signing_secret(
    privy_client: PrivyClient,
    staging_user: User,
    webhook_payload: bytes,
) -> None:
    secret = signing_secret()

    event = privy_client.webhooks.verify(
        payload=webhook_payload,
        headers=signed_headers(secret, webhook_payload),
        signing_secret=secret,
    )

    assert isinstance(event, UserCreatedWebhookPayload)
    assert event.type == "user.created"
    assert event.user.id == staging_user.id


def test_verify_with_client_signing_secret(staging_user: User, webhook_payload: bytes) -> None:
    secret = signing_secret()
    api_url = (os.environ.get("TEST_API_URL") or STAGING_API_URL).rstrip("/")

    with PrivyClient(
        app_id=required_environment("TEST_APP_ID"),
        app_secret=required_environment("TEST_APP_SECRET"),
        base_url=api_url,
        webhook_signing_secret=secret,
    ) as client:
        event = client.webhooks.verify(
            payload=webhook_payload,
            headers=signed_headers(secret, webhook_payload),
        )

    assert isinstance(event, UserCreatedWebhookPayload)
    assert event.user.id == staging_user.id


def test_verify_rejects_invalid_signature(privy_client: PrivyClient, webhook_payload: bytes) -> None:
    secret = signing_secret()
    headers = signed_headers(secret, webhook_payload)
    headers["svix-signature"] = "v1,aW52YWxpZA=="

    with pytest.raises(InvalidWebhookError, match="Webhook verification failed"):
        privy_client.webhooks.verify(
            payload=webhook_payload,
            headers=headers,
            signing_secret=secret,
        )


def test_verify_rejects_stale_replayed_request(privy_client: PrivyClient, webhook_payload: bytes) -> None:
    secret = signing_secret()
    stale_timestamp = datetime.now(timezone.utc) - timedelta(minutes=6)

    with pytest.raises(InvalidWebhookError, match="timestamp too old"):
        privy_client.webhooks.verify(
            payload=webhook_payload,
            headers=signed_headers(secret, webhook_payload, stale_timestamp),
            signing_secret=secret,
        )


def test_verify_requires_signing_secret(privy_client: PrivyClient, webhook_payload: bytes) -> None:
    with pytest.raises(InvalidWebhookError, match="Webhook signing secret is required"):
        privy_client.webhooks.verify(payload=webhook_payload, headers={})
