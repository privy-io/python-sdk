# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkedAccountTelegramInputParam"]


class LinkedAccountTelegramInputParam(TypedDict, total=False):
    """The payload for importing a Telegram account."""

    telegram_user_id: Required[str]

    type: Required[Literal["telegram"]]

    first_name: str

    last_name: str

    photo_url: str

    username: str
