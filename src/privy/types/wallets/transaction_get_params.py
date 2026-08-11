# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..wallet_asset import WalletAsset
from ..transaction_token_address_input import TransactionTokenAddressInput
from ..transaction_chain_name_input_param import TransactionChainNameInputParam

__all__ = ["TransactionGetParams"]


class TransactionGetParams(TypedDict, total=False):
    chain: Required[TransactionChainNameInputParam]
    """Chains supported for transaction history queries."""

    token: Union[TransactionTokenAddressInput, SequenceNotStr[TransactionTokenAddressInput]]
    """Exactly one of `token` or `asset` is required.

    Cannot be used together with `asset`.
    """

    asset: Union[
        Literal["usdc", "usdc.e", "eth", "avax", "pol", "bnb", "usdt", "eurc", "usdb", "pathusd", "sol", "trx"],
        List[WalletAsset],
    ]
    """Exactly one of `asset` or `token` is required.

    Cannot be used together with `token`.
    """

    cursor: str

    include_archived: bool
    """Include archived wallets in lookup. Defaults to false."""

    limit: Optional[float]

    tx_hash: str
