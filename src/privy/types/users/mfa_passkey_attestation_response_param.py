# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MfaPasskeyAttestationResponseParam"]


class MfaPasskeyAttestationResponseParam(TypedDict, total=False):
    """The authenticator attestation response from a WebAuthn registration ceremony."""

    attestation_object: Required[str]

    client_data_json: Required[str]

    authenticator_data: str

    public_key: str

    public_key_algorithm: float

    transports: SequenceNotStr[str]
