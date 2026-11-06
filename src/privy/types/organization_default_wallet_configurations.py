# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .organization_wallet_configuration import OrganizationWalletConfiguration

__all__ = ["OrganizationDefaultWalletConfigurations"]


class OrganizationDefaultWalletConfigurations(BaseModel):
    """
    Defaults applied to wallets created with the organization as their entity, keyed by chain type.
    """

    ethereum: Optional[OrganizationWalletConfiguration] = None
    """Default policies and additional signers for wallets of one chain type."""

    solana: Optional[OrganizationWalletConfiguration] = None
    """Default policies and additional signers for wallets of one chain type."""

    tron: Optional[OrganizationWalletConfiguration] = None
    """Default policies and additional signers for wallets of one chain type."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, OrganizationWalletConfiguration] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> OrganizationWalletConfiguration: ...
    else:
        __pydantic_extra__: Dict[str, OrganizationWalletConfiguration]
