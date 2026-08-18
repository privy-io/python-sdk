# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .amount_type import AmountType
from .fee_configuration import FeeConfiguration
from .wallet_action_nonce import WalletActionNonce
from .token_transfer_source import TokenTransferSource
from .token_transfer_destination import TokenTransferDestination

__all__ = ["TransferRequestBody"]


class TransferRequestBody(BaseModel):
    """Request body for initiating a sponsored token transfer from an embedded wallet."""

    destination: TokenTransferDestination
    """The destination address for a token transfer.

    Optionally specify a different asset or chain for cross-asset or cross-chain
    transfers.
    """

    source: TokenTransferSource
    """The source asset, amount, and chain for a token transfer.

    Specify either `asset` (named) or `asset_address` (custom), not both.
    """

    amount: Optional[str] = None
    """Amount as a decimal string in the token's standard unit (e.g.

    "1.5" for 1.5 USDC). For exact_input, the amount to send. For exact_output, the
    exact amount to receive. Takes precedence over source.amount when both are
    provided.
    """

    amount_type: Optional[AmountType] = None
    """Whether the amount refers to the input token or output token."""

    fee_configuration: Optional[FeeConfiguration] = None
    """Total fees assessed on a transfer, in BPS"""

    nonce: Optional[WalletActionNonce] = None
    """
    Unique caller-generated nonce used to prevent replaying a signed wallet action
    request. Must be at least 24 characters (e.g. a cuid2 or UUID).
    """

    slippage_bps: Optional[int] = None
    """Maximum allowed slippage in basis points (1 bps = 0.01%).

    Only applicable for cross-chain or cross-asset transfers; omit to use the
    provider default.
    """
