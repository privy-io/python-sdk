# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BridgeFiatDepositMetadata"]


class BridgeFiatDepositMetadata(BaseModel):
    """Bridge metadata for a fiat deposit via virtual account."""

    activity_id: str

    method: Literal["virtual_account"]

    type: Literal["fiat_deposit"]

    virtual_account_id: str
