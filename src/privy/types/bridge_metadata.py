# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .bridge_refund_metadata import BridgeRefundMetadata
from .bridge_fiat_deposit_metadata import BridgeFiatDepositMetadata
from .bridge_fiat_transfer_metadata import BridgeFiatTransferMetadata
from .bridge_crypto_deposit_metadata import BridgeCryptoDepositMetadata
from .bridge_crypto_transfer_metadata import BridgeCryptoTransferMetadata
from .bridge_transfer_refund_metadata import BridgeTransferRefundMetadata
from .bridge_static_memo_deposit_metadata import BridgeStaticMemoDepositMetadata

__all__ = ["BridgeMetadata"]

BridgeMetadata: TypeAlias = Union[
    BridgeCryptoDepositMetadata,
    BridgeRefundMetadata,
    BridgeFiatDepositMetadata,
    BridgeCryptoTransferMetadata,
    BridgeFiatTransferMetadata,
    BridgeTransferRefundMetadata,
    BridgeStaticMemoDepositMetadata,
]
