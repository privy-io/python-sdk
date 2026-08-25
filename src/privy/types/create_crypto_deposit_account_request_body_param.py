# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .create_crypto_deposit_account_with_route_request_body_param import (
    CreateCryptoDepositAccountWithRouteRequestBodyParam,
)
from .create_crypto_deposit_account_with_config_request_body_param import (
    CreateCryptoDepositAccountWithConfigRequestBodyParam,
)

__all__ = ["CreateCryptoDepositAccountRequestBodyParam"]

CreateCryptoDepositAccountRequestBodyParam: TypeAlias = Union[
    CreateCryptoDepositAccountWithConfigRequestBodyParam, CreateCryptoDepositAccountWithRouteRequestBodyParam
]
