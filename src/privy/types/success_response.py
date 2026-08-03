# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SuccessResponse"]


class SuccessResponse(BaseModel):
    """A simple success response."""

    success: bool
