# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .owner_id_input import OwnerIDInput
from .owner_input_param import OwnerInputParam
from .additional_signer_input_param import AdditionalSignerInputParam

__all__ = ["WalletUpdateParams"]


class WalletUpdateParams(TypedDict, total=False):
    additional_signers: AdditionalSignerInputParam
    """Additional signers for the wallet."""

    display_name: Optional[str]
    """A human-readable label for the wallet. Set to null to clear."""

    owner: Optional[OwnerInputParam]
    """
    The owner of the resource, specified as a Privy user ID, a P-256 public key, or
    null to remove the current owner.
    """

    owner_id: Optional[OwnerIDInput]
    """The key quorum ID to set as the owner of the resource.

    If you provide this, do not specify an owner.
    """

    policy_ids: SequenceNotStr[str]
    """New policy IDs to enforce on the wallet.

    Currently, only one policy is supported per wallet.
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
