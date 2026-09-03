# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FiatConfigureAppParams"]


class FiatConfigureAppParams(TypedDict, total=False):
    api_key: Required[str]

    provider: Required[Literal["bridge", "bridge-sandbox"]]
