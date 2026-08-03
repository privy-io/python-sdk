# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .hpke_aead_algorithm import HpkeAeadAlgorithm

__all__ = ["HpkeImportConfigParam"]


class HpkeImportConfigParam(TypedDict, total=False):
    """Optional HPKE configuration for wallet import decryption.

    These parameters allow importing wallets encrypted by external providers that use different HPKE configurations.
    """

    aad: str
    """Additional Authenticated Data (AAD) used during encryption.

    Should be base64-encoded bytes.
    """

    aead_algorithm: HpkeAeadAlgorithm
    """The AEAD algorithm used for HPKE encryption."""

    info: str
    """Application-specific context information (INFO) used during HPKE encryption.

    Should be base64-encoded bytes.
    """
