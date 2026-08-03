# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["KeyQuorumCreateParams"]


class KeyQuorumCreateParams(TypedDict, total=False):
    authorization_threshold: float
    """The number of keys that must sign for an action to be valid.

    Must be less than or equal to total number of key quorum members.
    """

    display_name: str

    key_quorum_ids: SequenceNotStr[str]
    """List of key quorum IDs that should be members of this key quorum.

    Key quorums can only be nested 1 level deep. At least one of `user_ids`,
    `public_keys`, or `key_quorum_ids` is required.
    """

    public_keys: SequenceNotStr[str]
    """
    List of P-256 public keys of the keys that should be authorized to sign on the
    key quorum, in base64-encoded DER format. At least one of `user_ids`,
    `public_keys`, or `key_quorum_ids` is required.
    """

    user_ids: SequenceNotStr[str]
    """
    List of user IDs of the users that should be authorized to sign on the key
    quorum. At least one of `user_ids`, `public_keys`, or `key_quorum_ids` is
    required.
    """
