# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .signature_type import SignatureType

__all__ = ["SignatureOptionsParam"]


class SignatureOptionsParam(TypedDict, total=False):
    """
    Options controlling signature production for personal_sign and eth_signTypedData_v4.
    """

    type: Required[SignatureType]
    """The type of cryptographic signature to produce.

    Use "ecdsa" for standard ECDSA signatures, or "erc1271" for ERC-1271 compliant
    signatures for smart account wallets.
    """
