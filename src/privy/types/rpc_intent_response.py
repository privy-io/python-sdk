# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .wallet import Wallet
from .._models import BaseModel
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .wallet_rpc_request_body import WalletRpcRequestBody

__all__ = ["RpcIntentResponse", "RpcIntentResponseRequestDetails"]


class RpcIntentResponseRequestDetails(BaseModel):
    """The original RPC request that would be sent to the wallet endpoint"""

    body: WalletRpcRequestBody
    """Request body for wallet RPC operations, discriminated by method."""

    method: Literal["POST"]

    url: str


class RpcIntentResponse(BaseIntentResponse):
    """Response for an RPC intent"""

    intent_type: Literal["RPC"]

    request_details: RpcIntentResponseRequestDetails
    """The original RPC request that would be sent to the wallet endpoint"""

    action_result: Optional[BaseActionResult] = None
    """Result of RPC execution (only present if status is 'executed' or 'failed')"""

    current_resource_data: Optional[Wallet] = None
    """A wallet managed by Privy's wallet infrastructure."""
