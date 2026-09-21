# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .transfer_sca_auth_factor_category_param import TransferScaAuthFactorCategoryParam

__all__ = ["TransferScaAuthFactorParam"]


class TransferScaAuthFactorParam(TypedDict, total=False):
    """Authentication factor metadata for a transfer."""

    authenticated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The ISO 8601 timestamp when this factor was authenticated."""

    category: Required[TransferScaAuthFactorCategoryParam]
    """The type of authentication factor used.

    Known values are: `knowledge` (something only the user knows, e.g. a PIN or
    password), `possession` (something only the user has, e.g. a phone receiving an
    OTP or a hardware token), and `inherence` (something the user is, e.g. a
    fingerprint or face scan). When `outcome` is `sca_used`, the two factors in
    `auth_factors` must belong to two different categories.
    """

    reference: Required[str]
    """Your internal identifier for this authentication event (e.g.

    a session ID, transaction ID, or audit log reference). Used for reconciliation.
    """
