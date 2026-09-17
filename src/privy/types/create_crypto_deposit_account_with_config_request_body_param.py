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
    """Controls deposit source selection.

    `dedicated` creates or reuses eligible dedicated source wallets, never the
    destination wallet. This is the default when omitted, including for existing
    routes. `prefer_destination` uses the destination wallet when it is eligible and
    its chain family is requested; otherwise it uses dedicated source wallets.
    `require_destination` requires the destination wallet to serve its own chain
    family when that family is requested and fails without fallback if it cannot;
    other requested families still use dedicated source wallets. On destination
    reuse, all strategies remove all existing automation attachments, including
    matching and disabled ones, then attach the requested automation. Exported
    wallets cannot serve as deposit sources.
    """
