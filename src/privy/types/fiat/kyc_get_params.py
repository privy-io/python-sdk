# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..onramp_provider import OnrampProvider

__all__ = ["KYCGetParams"]


class KYCGetParams(TypedDict, total=False):
    provider: Required[OnrampProvider]
    """Valid set of onramp providers"""
