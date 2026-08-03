# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WalletInviteInputParam"]


class WalletInviteInputParam(TypedDict, total=False):
    """Allowlist invite input for a wallet address."""

    type: Required[Literal["wallet"]]

    value: Required[str]
