# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .raw_sign_input_params_param import RawSignInputParamsParam

__all__ = ["IntentRawSignParams"]


class IntentRawSignParams(TypedDict, total=False):
    params: Required[RawSignInputParamsParam]
    """Parameters for the `raw_sign` RPC."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """
