# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .tron_raw_data_for_sign_param import TronRawDataForSignParam

__all__ = ["TronSignTransactionRpcInputParamsParam"]


class TronSignTransactionRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Tron `tron_signTransaction` RPC."""

    raw_data: Required[TronRawDataForSignParam]
    """Tron raw_data for tron_signTransaction.

    Block reference fields are required; caller is responsible for fetching them.
    """
