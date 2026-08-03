# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FiatOnrampProvider"]

FiatOnrampProvider: TypeAlias = Literal[
    "meld", "meld-sandbox", "moonpay", "moonpay-sandbox", "coinbase", "coinbase-sandbox", "stripe", "stripe-sandbox"
]
