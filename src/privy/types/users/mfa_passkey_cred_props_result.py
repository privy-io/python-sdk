# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MfaPasskeyCredPropsResult"]


class MfaPasskeyCredPropsResult(BaseModel):
    """The result of the WebAuthn credProps extension."""

    rk: Optional[bool] = None
