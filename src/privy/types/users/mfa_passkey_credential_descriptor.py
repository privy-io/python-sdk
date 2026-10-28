# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MfaPasskeyCredentialDescriptor"]


class MfaPasskeyCredentialDescriptor(BaseModel):
    """A WebAuthn credential descriptor identifying a specific public key credential."""

    id: str

    type: str

    transports: Optional[List[str]] = None
