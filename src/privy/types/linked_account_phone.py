# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LinkedAccountPhone"]


class LinkedAccountPhone(BaseModel):
    """A phone number account linked to the user."""

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    phone_number: str = FieldInfo(alias="phoneNumber")

    type: Literal["phone"]

    verified_at: float

    number: Optional[str] = None
