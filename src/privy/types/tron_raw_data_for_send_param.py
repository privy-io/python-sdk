# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .tron_contract_param import TronContractParam

__all__ = ["TronRawDataForSendParam"]


class TronRawDataForSendParam(TypedDict, total=False):
    """Tron raw_data for tron_sendTransaction.

    Block reference fields are optional; Privy fetches fresh values if omitted.
    """

    contract: Required[Iterable[TronContractParam]]

    data: str

    expiration: int

    fee_limit: int

    ref_block_bytes: str

    ref_block_hash: str

    timestamp: int
