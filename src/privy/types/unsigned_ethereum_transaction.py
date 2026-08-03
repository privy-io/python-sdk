# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .unsigned_tempo_transaction import UnsignedTempoTransaction
from .unsigned_standard_ethereum_transaction import UnsignedStandardEthereumTransaction

__all__ = ["UnsignedEthereumTransaction"]

UnsignedEthereumTransaction: TypeAlias = Union[UnsignedStandardEthereumTransaction, UnsignedTempoTransaction]
