# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Wallet", "AdditionalSigner"]


class AdditionalSigner(BaseModel):
    signer_id: str


class Wallet(BaseModel):
    id: str
    """Unique ID of the wallet.

    This will be the primary identifier when using the wallet in the future.
    """

    additional_signers: List[AdditionalSigner]
    """Additional signers for the wallet."""

    address: str
    """Address of the wallet."""

    chain_type: Literal["solana", "ethereum", "cosmos", "stellar", "sui", "tron"]
    """Chain type of the wallet. 'Ethereum' supports any EVM-compatible network."""

    created_at: float
    """Unix timestamp of when the wallet was created in milliseconds."""

    policy_ids: List[str]
    """List of policy IDs for policies that are enforced on the wallet."""

    exported_at: Optional[float] = None
    """
    Unix timestamp of when the wallet was exported in milliseconds, if the wallet
    was exported.
    """

    owner_id: Optional[str] = None
    """The key quorum ID of the owner of the wallet."""

    public_key: Optional[str] = None
    """
    The compressed, raw public key for the wallet along the chain cryptographic
    curve.
    """
