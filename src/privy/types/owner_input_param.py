# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .owner_input_user_param import OwnerInputUserParam
from .owner_input_public_key_param import OwnerInputPublicKeyParam

__all__ = ["OwnerInputParam"]

OwnerInputParam: TypeAlias = Union[OwnerInputUserParam, OwnerInputPublicKeyParam]
