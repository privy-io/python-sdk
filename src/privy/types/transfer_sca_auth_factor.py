# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .transfer_sca_auth_factor_category import TransferScaAuthFactorCategory

__all__ = ["TransferScaAuthFactor"]


class TransferScaAuthFactor(BaseModel):
    """Authentication factor metadata for a transfer."""

    authenticated_at: datetime
    """The ISO 8601 timestamp when this factor was authenticated."""

    category: TransferScaAuthFactorCategory
    """The type of authentication factor used.

    Known values are: `knowledge` (something only the user knows, e.g. a PIN or
    password), `possession` (something only the user has, e.g. a phone receiving an
    OTP or a hardware token), and `inherence` (something the user is, e.g. a
    fingerprint or face scan). When `outcome` is `sca_used`, the two factors in
    `auth_factors` must belong to two different categories.
    """

    reference: str
    """Your internal identifier for this authentication event (e.g.

    a session ID, transaction ID, or audit log reference). Used for reconciliation.
    """
