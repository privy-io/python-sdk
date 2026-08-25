# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...environment import Environment
from ...fiat_deposit_account_destination_param import FiatDepositAccountDestinationParam
from ...create_fiat_deposit_account_source_param import CreateFiatDepositAccountSourceParam

__all__ = ["FiatCreateParams"]


class FiatCreateParams(TypedDict, total=False):
    destination: Required[FiatDepositAccountDestinationParam]
    """The destination crypto asset and chain for a fiat deposit account."""

    provider: Required[Literal["bridge"]]
    """Discriminator: the fiat deposit account is orchestrated via Bridge."""

    source: Required[CreateFiatDepositAccountSourceParam]
    """The source fiat currency for a fiat deposit account."""

    environment: Environment
    """The Privy API environment."""
