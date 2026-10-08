# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .external_fiat_account_business_owner_param import ExternalFiatAccountBusinessOwnerParam
from .external_fiat_account_individual_owner_param import ExternalFiatAccountIndividualOwnerParam

__all__ = ["ExternalFiatAccountOwnerParam"]

ExternalFiatAccountOwnerParam: TypeAlias = Union[
    ExternalFiatAccountIndividualOwnerParam, ExternalFiatAccountBusinessOwnerParam
]
