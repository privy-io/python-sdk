# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PolicyDeleteResponse"]


class PolicyDeleteResponse(BaseModel):
    success: bool
    """Whether the policy was deleted successfully."""
