# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .raw_sign_hash_params_param import RawSignHashParamsParam
from .raw_sign_bytes_params_param import RawSignBytesParamsParam

__all__ = ["RawSignInputParamsParam"]

RawSignInputParamsParam: TypeAlias = Union[RawSignHashParamsParam, RawSignBytesParamsParam]
