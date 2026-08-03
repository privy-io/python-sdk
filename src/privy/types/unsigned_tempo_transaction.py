# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .quantity import Quantity
from .tempo_call import TempoCall
from .access_list_entry import AccessListEntry
from .tempo_aa_authorization import TempoAaAuthorization
from .tempo_fee_payer_signature import TempoFeePayerSignature

__all__ = ["UnsignedTempoTransaction"]


class UnsignedTempoTransaction(BaseModel):
    """An unsigned Tempo transaction (type 118) with batched calls."""

    calls: List[TempoCall]

    type: Literal[118]

    aa_authorization_list: Optional[List[TempoAaAuthorization]] = None

    access_list: Optional[List[AccessListEntry]] = None

    chain_id: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    fee_payer_signature: Optional[TempoFeePayerSignature] = None
    """A fee payer signature for sponsored Tempo transactions (secp256k1 only)."""

    fee_token: Optional[str] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    gas_limit: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    max_fee_per_gas: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    max_priority_fee_per_gas: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    nonce: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    nonce_key: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    valid_after: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    valid_before: Optional[Quantity] = None
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """
