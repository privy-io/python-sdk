# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .wallet import Wallet
from .._models import BaseModel
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .wallet_update_request_body import WalletUpdateRequestBody

__all__ = ["WalletIntentResponse", "WalletIntentResponseRequestDetails"]


class WalletIntentResponseRequestDetails(BaseModel):
    """The original wallet update request that would be sent to the wallet endpoint"""

    body: WalletUpdateRequestBody
    """Request body for updating a wallet.

    `owner` and `owner_id` are mutually exclusive.
    """

    method: Literal["PATCH"]

    url: str


class WalletIntentResponse(BaseIntentResponse):
    """Response for a wallet intent"""

    intent_type: Literal["WALLET"]

    request_details: WalletIntentResponseRequestDetails
    """The original wallet update request that would be sent to the wallet endpoint"""

    action_result: Optional[BaseActionResult] = None
    """
    Result of wallet update execution (only present if status is 'executed' or
    'failed')
    """

    current_resource_data: Optional[Wallet] = None
    """A wallet managed by Privy's wallet infrastructure."""
