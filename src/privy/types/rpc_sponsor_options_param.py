# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .rpc_sponsor_asset import RpcSponsorAsset

__all__ = ["RpcSponsorOptionsParam"]


class RpcSponsorOptionsParam(TypedDict, total=False):
    """Options for user-pays gas sponsorship on the RPC endpoint.

    When provided alongside `sponsor: true`, controls which token asset the user pays gas with.
    """

    asset: Required[RpcSponsorAsset]
    """Token asset identifier for user-pays gas sponsorship.

    Common values: 'usdc', 'usdt', 'eurc', 'usdg', 'usdc_e'. Available tokens vary
    by chain.
    """
