# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .named_token_transfer_source import NamedTokenTransferSource
from .custom_token_transfer_source import CustomTokenTransferSource

__all__ = ["TokenTransferSource"]

TokenTransferSource: TypeAlias = Union[NamedTokenTransferSource, CustomTokenTransferSource]
