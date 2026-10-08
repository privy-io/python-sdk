# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalFiatAccountIndividualOwnerParam"]


class ExternalFiatAccountIndividualOwnerParam(TypedDict, total=False):
    """An individual who owns an external fiat account."""

    first_name: Required[str]

    last_name: Required[str]

    type: Required[Literal["individual"]]
