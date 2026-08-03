# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .tron_contract_param import TronContractParam

__all__ = ["TronRawDataForSignParam"]


class TronRawDataForSignParam(TypedDict, total=False):
    """Tron raw_data for tron_signTransaction.

    Block reference fields are required; caller is responsible for fetching them.
    """

    contract: Required[Iterable[TronContractParam]]

    expiration: Required[int]

    ref_block_bytes: Required[str]

    ref_block_hash: Required[str]

    data: str

    fee_limit: int

    timestamp: int
