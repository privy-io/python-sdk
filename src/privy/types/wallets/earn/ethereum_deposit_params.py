# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...wallet_action_nonce import WalletActionNonce

__all__ = ["EthereumDepositParams"]


class EthereumDepositParams(TypedDict, total=False):
    vault_id: Required[str]
    """The ID of the vault to deposit into."""

    amount: str
    """Human-readable decimal amount to deposit (e.g.

    "1.5" for 1.5 USDC). Exactly one of `amount` or `raw_amount` must be provided.
    """

    nonce: WalletActionNonce
    """
    Unique caller-generated nonce used to prevent replaying a signed wallet action
    request. Must be at least 24 characters (e.g. a cuid2 or UUID).
    """

    raw_amount: str
    """Amount in smallest unit to deposit (e.g.

    "1500000" for 1.5 USDC with 6 decimals). Exactly one of `amount` or `raw_amount`
    must be provided.
    """

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """

    privy_idempotency_key: Annotated[str, PropertyInfo(alias="privy-idempotency-key")]
    """
    Idempotency keys ensure API requests are executed only once within a 24-hour
    window.
    """

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """
