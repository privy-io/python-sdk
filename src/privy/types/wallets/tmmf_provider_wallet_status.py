# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["TmmfProviderWalletStatus"]

TmmfProviderWalletStatus: TypeAlias = Union[Literal["created", "approved", "rejected", "deactivated"], str]
