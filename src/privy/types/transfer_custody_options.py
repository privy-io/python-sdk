# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .transfer_initiation import TransferInitiation

__all__ = ["TransferCustodyOptions"]


class TransferCustodyOptions(BaseModel):
    """Options for a transfer from a custodial wallet."""

    initiation: TransferInitiation
    """
    Payment initiation context for transfers sourced from wallets that require
    initiation data. Captures how the payment was initiated (channel and subchannel)
    and whether Strong Customer Authentication was applied or which SCA exemption
    was used.
    """
