# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["SmartWalletType"]

SmartWalletType: TypeAlias = Literal[
    "safe", "kernel", "light_account", "biconomy", "coinbase_smart_wallet", "thirdweb", "nexus"
]
