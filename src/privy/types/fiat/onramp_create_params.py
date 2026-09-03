# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OnrampCreateParams", "Destination", "Source"]


class OnrampCreateParams(TypedDict, total=False):
    amount: Required[str]

    destination: Required[Destination]

    provider: Required[Literal["bridge", "bridge-sandbox"]]

    source: Required[Source]


class Destination(TypedDict, total=False):
    chain: Required[Literal["ethereum", "base", "arbitrum", "polygon", "optimism"]]

    currency: Required[Literal["usdc"]]

    to_address: Required[str]


class Source(TypedDict, total=False):
    currency: Required[Literal["usd", "eur"]]

    payment_rail: Required[Literal["sepa", "ach_push", "wire"]]
