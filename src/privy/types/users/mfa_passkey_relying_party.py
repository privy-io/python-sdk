# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MfaPasskeyRelyingParty"]


class MfaPasskeyRelyingParty(BaseModel):
    """Relying party information for a WebAuthn ceremony."""

    name: str

    id: Optional[str] = None
