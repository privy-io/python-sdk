# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TelegramAuthConfigSchema"]


class TelegramAuthConfigSchema(BaseModel):
    """Configuration for Telegram authentication."""

    bot_id: str

    bot_name: str

    link_enabled: bool

    seamless_auth_enabled: bool
