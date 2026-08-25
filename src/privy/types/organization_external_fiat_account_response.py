# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .organization_external_fiat_account import OrganizationExternalFiatAccount

__all__ = ["OrganizationExternalFiatAccountResponse"]


class OrganizationExternalFiatAccountResponse(BaseModel):
    """Response containing a single organization external fiat account."""

    external_fiat_account: OrganizationExternalFiatAccount
    """A Bridge external fiat account linked to an organization."""
