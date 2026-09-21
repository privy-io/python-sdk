# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .transfer_initiation_channel_param import TransferInitiationChannelParam
from .transfer_initiation_subchannel_param import TransferInitiationSubchannelParam
from .transfer_initiation_attestations_param import TransferInitiationAttestationsParam

__all__ = ["TransferInitiationParam"]


class TransferInitiationParam(TypedDict, total=False):
    """
    Payment initiation context for transfers sourced from wallets that require initiation data. Captures how the payment was initiated (channel and subchannel) and whether Strong Customer Authentication was applied or which SCA exemption was used.
    """

    attestations: Required[TransferInitiationAttestationsParam]
    """Payment initiation attestations for a transfer."""

    channel: Required[TransferInitiationChannelParam]
    """How the payment was initiated.

    Use `p2p_mobile_payment` for peer-to-peer transfers initiated on a mobile
    device; `other_mobile_payment` for non-P2P mobile-initiated payments (e.g. a
    merchant payment via a mobile app); `other` for payments not relying on a mobile
    device.
    """

    subchannel: Required[TransferInitiationSubchannelParam]
    """Whether the payment was made remotely or in person.

    Use `remote` for payments initiated from a distance (mobile app, online banking,
    or e-commerce checkout); `non_remote` for payments made in person (physical
    card, payment terminal, or contactless tap).
    """
