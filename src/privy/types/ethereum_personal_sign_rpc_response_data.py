# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EthereumPersonalSignRpcResponseData"]


class EthereumPersonalSignRpcResponseData(BaseModel):
    """Data returned by the EVM `personal_sign` RPC."""

    encoding: Literal["hex"]

    signature: str
