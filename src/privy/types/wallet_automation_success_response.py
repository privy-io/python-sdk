# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletAutomationSuccessResponse"]


class WalletAutomationSuccessResponse(BaseModel):
    """Confirmation of a successful automation operation."""

    success: Literal[True]
