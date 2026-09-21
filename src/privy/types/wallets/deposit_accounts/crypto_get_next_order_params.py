# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CryptoGetNextOrderParams"]


class CryptoGetNextOrderParams(TypedDict, total=False):
    after: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Return the earliest sweep strictly after this timestamp."""
