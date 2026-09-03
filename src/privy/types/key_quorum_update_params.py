# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["KeyQuorumUpdateParams"]


class KeyQuorumUpdateParams(TypedDict, total=False):
    public_keys: Required[List[str]]

    authorization_threshold: float

    display_name: str

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """
