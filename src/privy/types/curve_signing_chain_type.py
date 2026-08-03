# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CurveSigningChainType"]

CurveSigningChainType: TypeAlias = Literal[
    "cosmos",
    "stellar",
    "sui",
    "aptos",
    "movement",
    "tron",
    "bitcoin-segwit",
    "bitcoin-taproot",
    "pearl",
    "near",
    "ton",
    "starknet",
]
