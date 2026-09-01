"""Options shared by public client requests."""

from __future__ import annotations

from dataclasses import dataclass

from .authorization import AuthorizationContext

__all__ = ["PrivyRequestOptions"]


@dataclass(frozen=True)
class PrivyRequestOptions:
    authorization_context: AuthorizationContext | None = None
    request_expiry: int | None = None
