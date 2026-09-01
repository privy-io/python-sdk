# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo
from ...crypto_deposit_asset_param import CryptoDepositAssetParam
from ...crypto_deposit_asset_filter_param import CryptoDepositAssetFilterParam

__all__ = [
    "CryptoCreateParams",
    "CreateCryptoDepositAccountWithConfigRequestBody",
    "CreateCryptoDepositAccountWithRouteRequestBody",
]


class CreateCryptoDepositAccountWithConfigRequestBody(TypedDict, total=False):
    deposit_config_id: Required[str]

    type: Required[Literal["deposit_config"]]

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """

    privy_idempotency_key: Annotated[str, PropertyInfo(alias="privy-idempotency-key")]
    """
    Idempotency keys ensure API requests are executed only once within a 24-hour
    window.
    """

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class CreateCryptoDepositAccountWithRouteRequestBody(TypedDict, total=False):
    destination: Required[CryptoDepositAssetParam]
    """An asset on a chain.

    Uses a human-readable alias (usdc, base) when one is on file, otherwise the raw
    asset address and CAIP-2.
    """

    source: Required[CryptoDepositAssetFilterParam]
    """Which assets a deposit address accepts.

    Asset and chain use human-readable aliases when known.
    """

    type: Required[Literal["inline_route"]]

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """

    privy_idempotency_key: Annotated[str, PropertyInfo(alias="privy-idempotency-key")]
    """
    Idempotency keys ensure API requests are executed only once within a 24-hour
    window.
    """

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


CryptoCreateParams: TypeAlias = Union[
    CreateCryptoDepositAccountWithConfigRequestBody, CreateCryptoDepositAccountWithRouteRequestBody
]
