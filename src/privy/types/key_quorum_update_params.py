# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["KeyQuorumUpdateParams"]


class KeyQuorumUpdateParams(TypedDict, total=False):
    authorization_threshold: float
    """The number of keys that must sign for an action to be valid.

    Must be less than or equal to total number of key quorum members.
    """

    display_name: str

    key_quorum_ids: SequenceNotStr[str]
    """List of key quorum IDs that should be members of this key quorum.

    Key quorums can only be nested 1 level deep.
    """

    public_keys: SequenceNotStr[str]
    """
    List of P-256 public keys of the keys that should be authorized to sign on the
    key quorum, in base64-encoded DER format.
    """

    user_ids: SequenceNotStr[str]
    """
    List of user IDs of the users that should be authorized to sign on the key
    quorum.
    """

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """
