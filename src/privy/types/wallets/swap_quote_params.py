# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..amount_type import AmountType
from ..swap_source_param import SwapSourceParam
from ..fee_configuration_param import FeeConfigurationParam
from ..swap_quote_destination_param import SwapQuoteDestinationParam

__all__ = ["SwapQuoteParams"]


class SwapQuoteParams(TypedDict, total=False):
    base_amount: Required[str]
    """Amount in base units (e.g., wei for ETH).

    Must be a non-negative integer string.
    """

    destination: Required[SwapQuoteDestinationParam]
    """The output side of a swap quote request."""

    source: Required[SwapSourceParam]
    """The input side of a swap request, including token and chain."""

    amount_type: AmountType
    """Whether the amount refers to the input token or output token."""

    fee_configuration: FeeConfigurationParam
    """Total fees assessed on a transfer, in BPS"""

    slippage_bps: int
    """Maximum slippage tolerance in basis points (e.g., 50 for 0.5%).

    If omitted, auto-slippage is used.
    """

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """
