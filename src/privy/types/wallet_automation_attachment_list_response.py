# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .wallet_automation_attachment_response import WalletAutomationAttachmentResponse

__all__ = ["WalletAutomationAttachmentListResponse"]


class WalletAutomationAttachmentListResponse(BaseModel):
    """List of wallet automation attachments."""

    data: List[WalletAutomationAttachmentResponse]
