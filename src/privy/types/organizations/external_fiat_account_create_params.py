# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..environment import Environment
from ..external_fiat_account_data_param import ExternalFiatAccountDataParam
from ..external_fiat_account_address_param import ExternalFiatAccountAddressParam

__all__ = ["ExternalFiatAccountCreateParams"]


class ExternalFiatAccountCreateParams(TypedDict, total=False):
    account: Required[ExternalFiatAccountDataParam]
    """Bank account details. The `type` field discriminates which shape applies."""

    account_owner_name: Required[str]

    currency: Required[str]

    provider: Required[Literal["bridge"]]
    """Discriminator: the external fiat account is orchestrated via Bridge."""

    address: ExternalFiatAccountAddressParam
    """Physical address associated with an external fiat account."""

    bank_name: str

    environment: Environment
    """The Privy API environment."""
