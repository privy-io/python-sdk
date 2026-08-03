# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AlchemyPaymasterContext"]


class AlchemyPaymasterContext(BaseModel):
    """The Alchemy paymaster context for a smart wallet network configuration."""

    policy_id: str
