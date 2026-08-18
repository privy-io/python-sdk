# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..amount_type import AmountType
from ..swap_source_param import SwapSourceParam
from ..wallet_action_nonce import WalletActionNonce
from ..swap_destination_param import SwapDestinationParam
from ..fee_configuration_param import FeeConfigurationParam

__all__ = ["SwapExecuteParams"]


class SwapExecuteParams(TypedDict, total=False):
    base_amount: Required[str]
    """Amount in base units (e.g., wei for ETH).

    Must be a non-negative integer string.
    """

    destination: Required[SwapDestinationParam]
    """The output side of a swap execution request."""

    source: Required[SwapSourceParam]
    """The input side of a swap request, including token and chain."""

    amount_type: AmountType
    """Whether the amount refers to the input token or output token."""

    fee_configuration: FeeConfigurationParam
    """Total fees assessed on a transfer, in BPS"""

    nonce: WalletActionNonce
    """
    Unique caller-generated nonce used to prevent replaying a signed wallet action
    request. Must be at least 24 characters (e.g. a cuid2 or UUID).
    """

    slippage_bps: int
    """Maximum slippage tolerance in basis points (e.g., 50 for 0.5%)."""

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
