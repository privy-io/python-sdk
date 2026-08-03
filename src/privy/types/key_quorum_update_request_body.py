# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["KeyQuorumUpdateRequestBody"]


class KeyQuorumUpdateRequestBody(BaseModel):
    """Request input for updating an existing key quorum.

    At least one field must be provided.
    """

    authorization_threshold: Optional[float] = None
    """The number of keys that must sign for an action to be valid.

    Must be less than or equal to total number of key quorum members.
    """

    display_name: Optional[str] = None

    key_quorum_ids: Optional[List[str]] = None
    """List of key quorum IDs that should be members of this key quorum.

    Key quorums can only be nested 1 level deep.
    """

    public_keys: Optional[List[str]] = None
    """
    List of P-256 public keys of the keys that should be authorized to sign on the
    key quorum, in base64-encoded DER format.
    """

    user_ids: Optional[List[str]] = None
    """
    List of user IDs of the users that should be authorized to sign on the key
    quorum.
    """
