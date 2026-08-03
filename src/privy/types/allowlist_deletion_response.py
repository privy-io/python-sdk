# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AllowlistDeletionResponse"]


class AllowlistDeletionResponse(BaseModel):
    """Confirmation response for deleting an allowlist entry."""

    message: str
