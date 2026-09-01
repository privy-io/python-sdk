"""Request-expiry configuration and resolution helpers."""

from __future__ import annotations

from typing import Callable, Optional
from dataclasses import dataclass

__all__ = [
    "DEFAULT_REQUEST_EXPIRY_MS",
    "PrivyRequestExpiryOptions",
    "RequestExpiryProvider",
    "resolve_request_expiry",
]


# 15 minutes
DEFAULT_REQUEST_EXPIRY_MS = 15 * 60 * 1000

RequestExpiryProvider = Callable[[], Optional[int]]


@dataclass(frozen=True)
class PrivyRequestExpiryOptions:
    """Client-level configuration for automatic request expiry.

    ``default_ms`` is a duration from now. Per-request expiry values are absolute
    Unix timestamps in milliseconds.
    """

    disabled: bool = False
    default_ms: int | None = None


def resolve_request_expiry(
    request_expiry: int | None,
    request_expiry_provider: RequestExpiryProvider | None,
) -> int | None:
    """Return an explicit expiry or ask the client for its default."""

    if request_expiry is not None:
        return request_expiry
    if request_expiry_provider is None:
        return None
    return request_expiry_provider()
