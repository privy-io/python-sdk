# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .organization_external_fiat_account import OrganizationExternalFiatAccount

__all__ = ["ListOrganizationExternalFiatAccountsResponse"]


class ListOrganizationExternalFiatAccountsResponse(BaseModel):
    """A list of external fiat accounts linked to an organization."""

    accounts: List[OrganizationExternalFiatAccount]

    next_cursor: Optional[str] = None
