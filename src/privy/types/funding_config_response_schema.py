# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .currency import Currency
from .funding_option import FundingOption
from .funding_method_enum import FundingMethodEnum

__all__ = ["FundingConfigResponseSchema"]


class FundingConfigResponseSchema(BaseModel):
    """Configuration for funding and on-ramp options."""

    cross_chain_bridging_enabled: bool

    default_recommended_amount: str

    default_recommended_currency: Currency
    """A crypto currency identified by a CAIP-2 chain ID and optional asset."""

    methods: List[FundingMethodEnum]

    options: List[FundingOption]

    prompt_funding_on_wallet_creation: bool
