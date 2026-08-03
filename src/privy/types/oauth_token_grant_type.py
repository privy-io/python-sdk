# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["OAuthTokenGrantType"]

OAuthTokenGrantType: TypeAlias = Literal[
    "authorization_code", "urn:ietf:params:oauth:grant-type:device_code", "refresh_token"
]
