# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .crypto_deposit_address_strategy import CryptoDepositAddressStrategy

__all__ = ["CreateCryptoDepositAccountWithConfigRequestBodyParam"]


class CreateCryptoDepositAccountWithConfigRequestBodyParam(TypedDict, total=False):
    """Creates a crypto deposit account from an existing deposit configuration."""

    deposit_config_id: Required[str]

    type: Required[Literal["deposit_config"]]

    deposit_address_strategy: CryptoDepositAddressStrategy
    """How deposit source wallets are chosen.

    Omission uses `dedicated`. Destination reuse applies only to the destination's
    own chain type.
    """
