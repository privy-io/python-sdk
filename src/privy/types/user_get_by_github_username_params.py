# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserGetByGitHubUsernameParams"]


class UserGetByGitHubUsernameParams(TypedDict, total=False):
    username: Required[str]
