# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AttachedWalletAutomation"]


class AttachedWalletAutomation(BaseModel):
    """A summary of an automation attached to a wallet."""

    id: str
    """ID of the automation."""

    enabled: bool
    """
    Whether this attachment is currently active — true only if both the attachment
    and the underlying automation are enabled.
    """
