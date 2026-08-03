# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FundingOption"]


class FundingOption(BaseModel):
    """A funding option with method and provider."""

    method: str

    provider: str
