# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["OAuthTokenDeviceCodePendingErrorCode"]

OAuthTokenDeviceCodePendingErrorCode: TypeAlias = Literal[
    "authorization_pending", "slow_down", "access_denied", "expired_token"
]
