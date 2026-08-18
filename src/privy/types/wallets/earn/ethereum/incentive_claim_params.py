# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ....wallet_action_nonce import WalletActionNonce

__all__ = ["IncentiveClaimParams"]


class IncentiveClaimParams(TypedDict, total=False):
    chain: Required[str]
    """The blockchain network on which to perform the incentive claim.

    Supported chains include: 'tempo', 'ethereum', 'base', 'arbitrum', 'polygon',
    'solana', and more, along with their respective testnets.
    """

    nonce: WalletActionNonce
    """
    Unique caller-generated nonce used to prevent replaying a signed wallet action
    request. Must be at least 24 characters (e.g. a cuid2 or UUID).
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
