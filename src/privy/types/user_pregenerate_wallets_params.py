# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .wallet_creation_input_param import WalletCreationInputParam

__all__ = ["UserPregenerateWalletsParams"]


class UserPregenerateWalletsParams(TypedDict, total=False):
    wallets: Required[Iterable[WalletCreationInputParam]]
