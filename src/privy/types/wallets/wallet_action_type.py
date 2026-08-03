# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WalletActionType"]

WalletActionType: TypeAlias = Literal[
    "swap", "transfer", "earn_deposit", "earn_withdraw", "earn_incentive_claim", "earn_fee_collect"
]
