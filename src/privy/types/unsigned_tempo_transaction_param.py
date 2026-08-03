# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .quantity_param import QuantityParam
from .tempo_call_param import TempoCallParam
from .access_list_entry_param import AccessListEntryParam
from .tempo_aa_authorization_param import TempoAaAuthorizationParam
from .tempo_fee_payer_signature_param import TempoFeePayerSignatureParam

__all__ = ["UnsignedTempoTransactionParam"]

_UnsignedTempoTransactionParamReservedKeywords = TypedDict(
    "_UnsignedTempoTransactionParamReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class UnsignedTempoTransactionParam(_UnsignedTempoTransactionParamReservedKeywords, total=False):
    """An unsigned Tempo transaction (type 118) with batched calls."""

    calls: Required[Iterable[TempoCallParam]]

    type: Required[Literal[118]]

    aa_authorization_list: Iterable[TempoAaAuthorizationParam]

    access_list: Iterable[AccessListEntryParam]

    chain_id: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    fee_payer_signature: TempoFeePayerSignatureParam
    """A fee payer signature for sponsored Tempo transactions (secp256k1 only)."""

    fee_token: str

    gas_limit: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    max_fee_per_gas: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    max_priority_fee_per_gas: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    nonce: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    nonce_key: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    valid_after: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    valid_before: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """
