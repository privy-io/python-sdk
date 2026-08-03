# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["AuthorizationKeyRole"]

AuthorizationKeyRole: TypeAlias = Optional[Literal["root", "manager", "delegated-actions"]]
