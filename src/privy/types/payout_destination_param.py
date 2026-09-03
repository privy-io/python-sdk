# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PayoutDestinationParam"]


class PayoutDestinationParam(TypedDict, total=False):
    """The destination bank account for a payout."""

    fiat_account_id: Required[str]
    """The ID of a previously registered external fiat account to pay out to."""
