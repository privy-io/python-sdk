# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .raw_sign_hash_params import RawSignHashParams
from .raw_sign_bytes_params import RawSignBytesParams

__all__ = ["RawSignInputParams"]

RawSignInputParams: TypeAlias = Union[RawSignHashParams, RawSignBytesParams]
