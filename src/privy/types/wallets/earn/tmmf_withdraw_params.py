# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..tmmf_fund import TmmfFund
from ..tmmf_chain import TmmfChain
from ..tmmf_currency import TmmfCurrency
from ..tmmf_order_type import TmmfOrderType
from ..tmmf_decimal_amount import TmmfDecimalAmount
from ...wallet_action_nonce import WalletActionNonce

__all__ = ["TmmfWithdrawParams"]


class TmmfWithdrawParams(TypedDict, total=False):
    chain: Required[TmmfChain]
    """Chain the fund is held on, e.g. "ethereum_sepolia"."""

    fund: Required[TmmfFund]
    """Fund ticker, e.g. "WTGXX". Case-insensitive."""

    order_type: Required[TmmfOrderType]
    """
    How a tMMF order fills: `secondary` from the provider pool in minutes, or
    `primary` at the next NAV strike.
    """

    shares: Required[TmmfDecimalAmount]
    """A positive decimal amount in the asset's standard unit, e.g. "1000.00"."""

    withdraw_asset: Required[TmmfCurrency]
    """Currency symbol, e.g. "USDC". Case-insensitive."""

    nonce: WalletActionNonce
    """
    Unique caller-generated nonce used to prevent replaying a signed wallet action
    request. Must be at least 24 characters (e.g. a cuid2 or UUID).
    """

    reference_id: str
    """Developer-provided identifier for this request. Must be unique per app."""

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
