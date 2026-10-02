# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .environment import Environment
from .developer_fee_percent import DeveloperFeePercent
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

    developer_fee_percent: DeveloperFeePercent
    """A developer fee as a percentage string from 0 up to (not including) 100, e.g.

    "1.5" for 1.5%.
    """

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
