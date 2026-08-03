# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .owner_input_user import OwnerInputUser
from .owner_input_public_key import OwnerInputPublicKey

__all__ = ["OwnerInput"]

OwnerInput: TypeAlias = Union[OwnerInputUser, OwnerInputPublicKey, None]
