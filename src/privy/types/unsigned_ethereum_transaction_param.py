# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .unsigned_tempo_transaction_param import UnsignedTempoTransactionParam
from .unsigned_standard_ethereum_transaction_param import UnsignedStandardEthereumTransactionParam

__all__ = ["UnsignedEthereumTransactionParam"]

UnsignedEthereumTransactionParam: TypeAlias = Union[
    UnsignedStandardEthereumTransactionParam, UnsignedTempoTransactionParam
]
