"""Public webhook operations."""

from __future__ import annotations

from collections.abc import Mapping

from svix.webhooks import Webhook

from .._client import PrivyAPI
from .._exceptions import PrivyAPIError
from ..resources.webhooks import WebhooksResource
from ..types.unsafe_unwrap_webhook_event import UnsafeUnwrapWebhookEvent

__all__ = ["InvalidWebhookError", "PrivyWebhooksService", "WebhookPayload"]

WebhookPayload = UnsafeUnwrapWebhookEvent


class InvalidWebhookError(PrivyAPIError):
    """Raised when a webhook request cannot be verified."""


class PrivyWebhooksService(WebhooksResource):
    """Webhook operations with Svix signature verification."""

    def __init__(self, client: PrivyAPI, webhook_signing_secret: str | None = None) -> None:
        super().__init__(client)
        self._webhook_signing_secret = webhook_signing_secret

    def verify(
        self,
        *,
        payload: bytes | str,
        headers: Mapping[str, str],
        signing_secret: str | None = None,
    ) -> WebhookPayload:
        """Verify and deserialize a signed webhook request.

        Pass the raw, unmodified request body and its ``svix-id``,
        ``svix-timestamp``, and ``svix-signature`` headers. Svix rejects invalid
        signatures and timestamps outside its tolerance window to prevent replay
        attacks. A per-call signing secret takes precedence over the client-level
        secret.
        """
        secret = signing_secret or self._webhook_signing_secret
        if not secret:
            raise InvalidWebhookError("Webhook signing secret is required. Pass it to PrivyClient or to verify().")

        try:
            Webhook(secret).verify(payload, dict(headers))
        except Exception as exc:
            raise InvalidWebhookError(f"Webhook verification failed: {exc}") from exc

        body = payload.decode("utf-8") if isinstance(payload, bytes) else payload
        return self.unsafe_unwrap(body)
