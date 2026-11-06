# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["TmmfRegistrationStatus"]

TmmfRegistrationStatus: TypeAlias = Union[
    Literal["pending", "action_required", "approved", "rejected", "suspended"], str
]
