# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .wallet_entity import WalletEntity
from .wallet_custodian import WalletCustodian
from .wallet_chain_type import WalletChainType
from .wallet_additional_signer import WalletAdditionalSigner

__all__ = ["Wallet"]


class Wallet(BaseModel):
    """A wallet managed by Privy's wallet infrastructure."""

    id: str
    """Unique ID of the wallet.

    This will be the primary identifier when using the wallet in the future.
    """

    additional_signers: WalletAdditionalSigner
    """Additional signers for the wallet."""

    address: str
    """Address of the wallet."""

    chain_type: WalletChainType
    """The wallet chain types."""

    created_at: float
    """Unix timestamp of when the wallet was created in milliseconds."""

    exported_at: Optional[float] = None
    """
    Unix timestamp of when the wallet was exported in milliseconds, if the wallet
    was exported.
    """

    imported_at: Optional[float] = None
    """
    Unix timestamp of when the wallet was imported in milliseconds, if the wallet
    was imported.
    """

    owner_id: Optional[str] = None
    """The key quorum ID of the owner of the wallet."""

    policy_ids: List[str]
    """List of policy IDs for policies that are enforced on the wallet."""

    archived_at: Optional[float] = None
    """
    Unix timestamp of when the wallet was archived in milliseconds, or null if the
    wallet is active.
    """

    authorization_threshold: Optional[float] = None
    """The number of keys that must sign for an action to be valid."""

    custody: Optional[WalletCustodian] = None
    """Information about the custodian managing this wallet."""

    display_name: Optional[str] = None
    """A human-readable label for the wallet."""

    entity: Optional[WalletEntity] = None
    """The entity a wallet is attributed to."""

    external_id: Optional[str] = None
    """A customer-provided identifier for mapping to external systems.

    Write-once, set only at creation.
    """

    public_key: Optional[str] = None
    """
    The compressed, raw public key for the wallet along the chain cryptographic
    curve.
    """
