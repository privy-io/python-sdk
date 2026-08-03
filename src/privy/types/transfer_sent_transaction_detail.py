# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .wallet_asset_chain_name_input import WalletAssetChainNameInput

__all__ = ["TransferSentTransactionDetail"]


class TransferSentTransactionDetail(BaseModel):
    """Details for a sent transfer transaction."""

    asset: Union[
        Literal["usdc", "usdc.e", "eth", "avax", "pol", "bnb", "usdt", "eurc", "usdb", "pathusd", "sol", "trx"], str
    ]

    chain: WalletAssetChainNameInput
    """Supported blockchain network names for wallet balance and transaction queries."""

    display_values: Dict[str, str]

    raw_value: str

    raw_value_decimals: float

    recipient: str

    recipient_privy_user_id: Optional[str] = None

    sender: str

    sender_privy_user_id: Optional[str] = None

    type: Literal["transfer_sent"]
