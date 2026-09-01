# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CreateCryptoDepositAccountWithConfigRequestBodyParam"]


class CreateCryptoDepositAccountWithConfigRequestBodyParam(TypedDict, total=False):
    """Creates a crypto deposit account from an existing deposit configuration."""

    deposit_config_id: Required[str]

    type: Required[Literal["deposit_config"]]
