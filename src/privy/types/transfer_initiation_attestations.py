# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .transfer_sca_attestation import TransferScaAttestation

__all__ = ["TransferInitiationAttestations"]


class TransferInitiationAttestations(BaseModel):
    """Payment initiation attestations for a transfer."""

    sca: TransferScaAttestation
    """Strong Customer Authentication attestation for a transfer."""
