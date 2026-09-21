# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .transfer_sca_attestation_param import TransferScaAttestationParam

__all__ = ["TransferInitiationAttestationsParam"]


class TransferInitiationAttestationsParam(TypedDict, total=False):
    """Payment initiation attestations for a transfer."""

    sca: Required[TransferScaAttestationParam]
    """Strong Customer Authentication attestation for a transfer."""
