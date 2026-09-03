# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...payout_source_param import PayoutSourceParam
from ...payout_destination_param import PayoutDestinationParam

__all__ = ["FiatCreateParams"]


class FiatCreateParams(TypedDict, total=False):
    destination: Required[PayoutDestinationParam]
    """The destination bank account for a payout."""

    source: Required[PayoutSourceParam]
    """The source crypto asset, chain, and amount for a payout."""

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
