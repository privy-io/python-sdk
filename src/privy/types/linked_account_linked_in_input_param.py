# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LinkedAccountLinkedInInputParam"]


class LinkedAccountLinkedInInputParam(TypedDict, total=False):
    """The payload for importing a LinkedIn account."""

    subject: Required[str]

    type: Required[Literal["linkedin_oauth"]]

    email: str

    name: str

    vanity_name: Annotated[str, PropertyInfo(alias="vanityName")]
