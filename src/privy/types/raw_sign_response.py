# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .raw_sign_response_data import RawSignResponseData

__all__ = ["RawSignResponse"]


class RawSignResponse(BaseModel):
    """Response to the `raw_sign` RPC."""

    data: RawSignResponseData
    """Data returned by the `raw_sign` RPC."""

    method: Literal["raw_sign"]
