# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AllowlistEntry"]


class AllowlistEntry(BaseModel):
    """An allowlist entry for an app."""

    id: str

    accepted_at: Optional[float] = FieldInfo(alias="acceptedAt", default=None)

    app_id: str = FieldInfo(alias="appId")

    type: str

    value: str
