# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .condition_set_items_request_body_param import ConditionSetItemsRequestBodyParam

__all__ = ["IntentUpdateConditionSetItemsParams"]


class IntentUpdateConditionSetItemsParams(TypedDict, total=False):
    condition_set_items_request_body: Required[ConditionSetItemsRequestBodyParam]
    """Array of values to add to the condition set. Maximum 100 items per request."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """
