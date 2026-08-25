# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .environment import Environment
from .fiat_deposit_instructions import FiatDepositInstructions
from .fiat_deposit_account_source import FiatDepositAccountSource
from .fiat_deposit_account_status import FiatDepositAccountStatus
from .fiat_deposit_account_destination import FiatDepositAccountDestination

__all__ = ["FiatDepositAccount"]


class FiatDepositAccount(BaseModel):
    """A Bridge fiat deposit account linked to a wallet."""

    id: str

    created_at: str

    deposit_instructions: Optional[FiatDepositInstructions] = None
    """Bank or payment deposit instructions for a fiat deposit account.

    Shape varies by source currency.
    """

    destination: FiatDepositAccountDestination
    """The destination crypto asset and chain for a fiat deposit account."""

    environment: Environment
    """The Privy API environment."""

    provider: Literal["bridge"]
    """Discriminator: the fiat deposit account is orchestrated via Bridge."""

    source: FiatDepositAccountSource
    """
    The source fiat currency and available payment rails for a fiat deposit account.
    """

    status: FiatDepositAccountStatus
    """Activation status of a fiat deposit account."""

    wallet_id: str
