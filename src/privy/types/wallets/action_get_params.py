# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .wallet_action_include import WalletActionInclude

__all__ = ["ActionGetParams"]


class ActionGetParams(TypedDict, total=False):
    wallet_id: Required[str]
    """ID of the wallet."""

    include: WalletActionInclude
    """Expandable relations to include on a wallet action response."""

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """
