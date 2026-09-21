# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .transfer_initiation_param import TransferInitiationParam

__all__ = ["TransferCustodyOptionsParam"]


class TransferCustodyOptionsParam(TypedDict, total=False):
    """Options for a transfer from a custodial wallet."""

    initiation: Required[TransferInitiationParam]
    """
    Payment initiation context for transfers sourced from wallets that require
    initiation data. Captures how the payment was initiated (channel and subchannel)
    and whether Strong Customer Authentication was applied or which SCA exemption
    was used.
    """
