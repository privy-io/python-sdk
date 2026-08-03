# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .rpc_sponsor_asset import RpcSponsorAsset

__all__ = ["RpcSponsorOptions"]


class RpcSponsorOptions(BaseModel):
    """Options for user-pays gas sponsorship on the RPC endpoint.

    When provided alongside `sponsor: true`, controls which token asset the user pays gas with.
    """

    asset: RpcSponsorAsset
    """Token asset identifier for user-pays gas sponsorship.

    Common values: 'usdc', 'usdt', 'eurc', 'usdg', 'usdc_e'. Available tokens vary
    by chain.
    """
