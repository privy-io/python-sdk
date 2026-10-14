# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .denylist_rule_type import DenylistRuleType

__all__ = ["DenylistEntry"]


class DenylistEntry(BaseModel):
    """A denylist entry for an app."""

    id: str
    """The ID of the denylist entry."""

    rule_type: DenylistRuleType
    """The type of identifier a denylist rule blocks."""

    value: str
    """The blocked identifier."""
