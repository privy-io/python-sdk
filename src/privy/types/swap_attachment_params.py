# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SwapAttachmentParams"]


class SwapAttachmentParams(BaseModel):
    """Per-attachment parameters for swap automations."""

    destination_address: str
