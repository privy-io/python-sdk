# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .wallet import Wallet
from .._models import BaseModel
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .transfer_request_body import TransferRequestBody

__all__ = ["TransferIntentResponse", "TransferIntentResponseRequestDetails"]


class TransferIntentResponseRequestDetails(BaseModel):
    """
    The original transfer request that would be sent to the wallet transfer endpoint
    """

    body: TransferRequestBody
    """Request body for initiating a sponsored token transfer from an embedded wallet."""

    method: Literal["POST"]

    url: str


class TransferIntentResponse(BaseIntentResponse):
    """Response for a transfer intent"""

    intent_type: Literal["TRANSFER"]

    request_details: TransferIntentResponseRequestDetails
    """
    The original transfer request that would be sent to the wallet transfer endpoint
    """

    action_result: Optional[BaseActionResult] = None
    """
    Result of transfer execution (only present if intent status is 'executed' or
    'failed')
    """

    current_resource_data: Optional[Wallet] = None
    """A wallet managed by Privy's wallet infrastructure."""
