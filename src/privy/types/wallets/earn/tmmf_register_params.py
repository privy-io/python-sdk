# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..tmmf_chain import TmmfChain
from ..tmmf_provider_param import TmmfProviderParam

__all__ = ["TmmfRegisterParams"]


class TmmfRegisterParams(TypedDict, total=False):
    chain: Required[TmmfChain]
    """Chain the fund is held on, e.g. "ethereum_sepolia"."""

    provider: Required[TmmfProviderParam]
    """The fund provider."""
