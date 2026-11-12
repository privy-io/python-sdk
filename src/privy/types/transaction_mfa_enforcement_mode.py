# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["TransactionMfaEnforcementMode"]

TransactionMfaEnforcementMode: TypeAlias = Union[Literal["POLICY_BASED", "ALL_WALLET_OPERATIONS"], str]
