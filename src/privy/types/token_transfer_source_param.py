# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .named_token_transfer_source_param import NamedTokenTransferSourceParam
from .custom_token_transfer_source_param import CustomTokenTransferSourceParam

__all__ = ["TokenTransferSourceParam"]

TokenTransferSourceParam: TypeAlias = Union[NamedTokenTransferSourceParam, CustomTokenTransferSourceParam]
