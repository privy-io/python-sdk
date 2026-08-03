# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EthereumPersonalSignRpcInputParams"]


class EthereumPersonalSignRpcInputParams(BaseModel):
    """Parameters for the EVM `personal_sign` RPC."""

    encoding: Literal["utf-8", "hex"]

    message: str
