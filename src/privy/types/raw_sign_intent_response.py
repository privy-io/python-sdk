# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .wallet import Wallet
from .._models import BaseModel
from .raw_sign_input import RawSignInput
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse

__all__ = ["RawSignIntentResponse", "RawSignIntentResponseRequestDetails"]


class RawSignIntentResponseRequestDetails(BaseModel):
    """The original raw sign request that would be sent to the wallet endpoint"""

    body: RawSignInput
    """
    Provide either `hash` (to sign a pre-computed hash) OR `bytes`, `encoding`, and
    `hash_function` (to hash and then sign). These options are mutually exclusive.
    """

    method: Literal["POST"]

    url: str


class RawSignIntentResponse(BaseIntentResponse):
    """Response for a raw sign intent"""

    intent_type: Literal["RAW_SIGN"]

    request_details: RawSignIntentResponseRequestDetails
    """The original raw sign request that would be sent to the wallet endpoint"""

    action_result: Optional[BaseActionResult] = None
    """Result of raw sign execution (only present if status is 'executed' or 'failed')"""

    current_resource_data: Optional[Wallet] = None
    """A wallet managed by Privy's wallet infrastructure."""
