# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .kyx_screen_result import KyxScreenResult

__all__ = ["KyxScreenParam"]


class KyxScreenParam(TypedDict, total=False):
    """
    Result of a KYC/AML or OFAC screen you performed and are relying on the provider to accept, honoured only for developers enrolled in reliance.
    """

    result: Required[KyxScreenResult]
    """Outcome of a screen performed under KYC/KYB reliance."""

    screened_at: Required[Annotated[Union[Union[str, datetime], Union[str, date]], PropertyInfo(format="iso8601")]]
    """When the screen was performed (ISO 8601 date or date-time)."""
