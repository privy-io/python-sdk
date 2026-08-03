# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CrossAppEmbeddedWallet"]


class CrossAppEmbeddedWallet(BaseModel):
    """An embedded wallet associated with a cross-app account."""

    address: str
