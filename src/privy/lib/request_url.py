"""Helpers for building API request URLs."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .._client import PrivyAPI, AsyncPrivyAPI

__all__ = ["build_request_url"]


def build_request_url(client: PrivyAPI | AsyncPrivyAPI, path: str) -> str:
    """Build an absolute request URL from a client's base URL and a path."""

    return f"{str(client.base_url).rstrip('/')}/{path.lstrip('/')}"
