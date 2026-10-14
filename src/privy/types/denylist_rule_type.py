# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["DenylistRuleType"]

DenylistRuleType: TypeAlias = Union[Literal["email", "emailDomain", "phone", "ethereumAddress", "solanaAddress"], str]
