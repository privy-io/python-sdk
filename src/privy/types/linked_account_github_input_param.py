# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountGitHubInputParam"]


class LinkedAccountGitHubInputParam(TypedDict, total=False):
    """The payload for importing a Github account."""

    subject: Required[str]

    type: Required[Literal["github_oauth"]]

    username: Required[str]

    email: str

    name: str
