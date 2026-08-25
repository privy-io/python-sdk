# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..environment import Environment
from ..orchestration_provider import OrchestrationProvider

__all__ = ["ExternalFiatAccountListParams"]


class ExternalFiatAccountListParams(TypedDict, total=False):
    provider: Required[OrchestrationProvider]
    """Supported fiat orchestration providers."""

    environment: Environment
    """The Privy API environment."""
