# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .onramp_provider import OnrampProvider

__all__ = ["FiatGetKYCLinkParams"]


class FiatGetKYCLinkParams(TypedDict, total=False):
    email: Required[str]

    provider: Required[OnrampProvider]
    """Valid set of onramp providers"""

    endorsements: List[Literal["sepa"]]

    full_name: str

    redirect_uri: str

    type: Literal["individual", "business"]
