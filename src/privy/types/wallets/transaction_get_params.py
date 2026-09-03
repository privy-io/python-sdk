# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransactionGetParams"]


class TransactionGetParams(TypedDict, total=False):
    asset: Required[Union[Literal["usdc", "eth", "pol", "sol"], List[Literal["usdc", "eth", "pol", "sol"]]]]

    chain: Required[Literal["base"]]

    cursor: str

    limit: Optional[float]
