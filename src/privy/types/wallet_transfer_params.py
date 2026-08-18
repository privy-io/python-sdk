# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .amount_type import AmountType
from .wallet_action_nonce import WalletActionNonce
from .fee_configuration_param import FeeConfigurationParam
from .token_transfer_source_param import TokenTransferSourceParam
from .token_transfer_destination_param import TokenTransferDestinationParam

__all__ = ["WalletTransferParams"]


class WalletTransferParams(TypedDict, total=False):
    destination: Required[TokenTransferDestinationParam]
    """The destination address for a token transfer.

    Optionally specify a different asset or chain for cross-asset or cross-chain
    transfers.
    """

    source: Required[TokenTransferSourceParam]
    """The source asset, amount, and chain for a token transfer.

    Specify either `asset` (named) or `asset_address` (custom), not both.
    """

    amount: str
    """Amount as a decimal string in the token's standard unit (e.g.

    "1.5" for 1.5 USDC). For exact_input, the amount to send. For exact_output, the
    exact amount to receive. Takes precedence over source.amount when both are
    provided.
    """

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
    """Maximum allowed slippage in basis points (1 bps = 0.01%).

    Only applicable for cross-chain or cross-asset transfers; omit to use the
    provider default.
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
