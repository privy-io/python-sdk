# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .failure_reason import FailureReason
from .evm_wallet_action_step_status import EvmWalletActionStepStatus
from .evm_user_operation_entrypoint_version import EvmUserOperationEntrypointVersion

__all__ = ["EvmUserOperationWalletActionStep"]


class EvmUserOperationWalletActionStep(BaseModel):
    """A wallet action step consisting of an EVM user operation."""

    bundle_transaction_hash: Optional[str] = None
    """Transaction hash of the bundle in which this user operation was included.

    Null until included by a bundler.
    """

    caip2: str
    """CAIP-2 network identifier, containing the chain ID of the user operation."""

    entrypoint_version: EvmUserOperationEntrypointVersion
    """The ERC-4337 entrypoint contract version used by the user operation."""

    status: EvmWalletActionStepStatus
    """Status of an EVM step in a wallet action."""

    type: Literal["evm_user_operation"]

    user_operation_hash: Optional[str] = None
    """The user operation hash for this step.

    May change while the step status is non-terminal.
    """

    failure_reason: Optional[FailureReason] = None
    """A description of why a wallet action (or a step within a wallet action) failed."""

    finalized: Optional[bool] = None
    """Whether this step has reached on-chain finality.

    Absent until finality is confirmed.
    """

    gas_credits_charged_usd: Optional[str] = None
    """Amount charged in USD for gas sponsorship on this step."""
