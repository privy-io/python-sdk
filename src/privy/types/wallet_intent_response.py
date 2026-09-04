# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .wallet import Wallet
from .._models import BaseModel
from .owner_input import OwnerInput
from .policy_input import PolicyInput
from .owner_id_input import OwnerIDInput
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .additional_signer_input import AdditionalSignerInput

__all__ = ["WalletIntentResponse", "WalletIntentResponseRequestDetails", "WalletIntentResponseRequestDetailsBody"]


class WalletIntentResponseRequestDetailsBody(BaseModel):
    additional_signers: Optional[AdditionalSignerInput] = None
    """Additional signers for the wallet."""

    authorization_key_ids: Optional[List[str]] = None

    authorization_threshold: Optional[float] = None

    display_name: Optional[str] = None

    external_id: Optional[str] = None

    owner: Optional[OwnerInput] = None
    """
    The owner of the resource, specified as a Privy user ID, a P-256 public key, or
    null to remove the current owner.
    """

    owner_id: Optional[OwnerIDInput] = None
    """The key quorum ID to set as the owner of the resource.

    If you provide this, do not specify an owner.
    """

    policy_ids: Optional[PolicyInput] = None
    """An optional list of up to one policy ID to enforce on the wallet."""


class WalletIntentResponseRequestDetails(BaseModel):
    """The original wallet update request that would be sent to the wallet endpoint"""

    body: WalletIntentResponseRequestDetailsBody

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
