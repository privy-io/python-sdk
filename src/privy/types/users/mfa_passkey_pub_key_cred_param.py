# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MfaPasskeyPubKeyCredParam"]


class MfaPasskeyPubKeyCredParam(BaseModel):
    """A public key credential parameter specifying the algorithm and credential type."""

    alg: float

    type: Literal["public-key"]
