# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreateFiatDepositAccountSourceParam"]


class CreateFiatDepositAccountSourceParam(TypedDict, total=False):
    """The source fiat currency for a fiat deposit account."""

    currency: Required[str]
