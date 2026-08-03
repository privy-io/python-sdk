# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CrossAppSmartWallet"]


class CrossAppSmartWallet(BaseModel):
    """A smart wallet associated with a cross-app account."""

    address: str
