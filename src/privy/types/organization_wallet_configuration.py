# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .policy_input import PolicyInput
from .additional_signer_input import AdditionalSignerInput

__all__ = ["OrganizationWalletConfiguration"]


class OrganizationWalletConfiguration(BaseModel):
    """Default policies and additional signers for wallets of one chain type."""

    additional_signers: Optional[AdditionalSignerInput] = None
    """Additional signers for the wallet."""

    policy_ids: Optional[PolicyInput] = None
    """An optional list of up to one policy ID to enforce on the wallet."""
