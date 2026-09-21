# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .swap_attachment_params_param import SwapAttachmentParamsParam

__all__ = ["WalletAttachAutomationsParams"]


class WalletAttachAutomationsParams(TypedDict, total=False):
    automation_ids: Required[SequenceNotStr[str]]

    params: SwapAttachmentParamsParam
    """Per-attachment parameters for swap automations."""

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """
