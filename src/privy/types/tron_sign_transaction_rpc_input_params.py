# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .tron_raw_data_for_sign import TronRawDataForSign

__all__ = ["TronSignTransactionRpcInputParams"]


class TronSignTransactionRpcInputParams(BaseModel):
    """Parameters for the Tron `tron_signTransaction` RPC."""

    raw_data: TronRawDataForSign
    """Tron raw_data for tron_signTransaction.

    Block reference fields are required; caller is responsible for fetching them.
    """
