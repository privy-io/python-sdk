# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .raw_sign_input_params import RawSignInputParams

__all__ = ["RawSignInput"]


class RawSignInput(BaseModel):
    """
    Provide either `hash` (to sign a pre-computed hash) OR `bytes`, `encoding`, and `hash_function` (to hash and then sign). These options are mutually exclusive.
    """

    params: RawSignInputParams
    """Parameters for the `raw_sign` RPC."""
