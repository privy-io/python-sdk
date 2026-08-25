# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo
from ...automation_asset_filter_input_param import AutomationAssetFilterInputParam
from ...automation_destination_asset_input_param import AutomationDestinationAssetInputParam

__all__ = [
    "CryptoCreateParams",
    "CreateCryptoDepositAccountWithConfigRequestBody",
    "CreateCryptoDepositAccountWithRouteRequestBody",
]


class CreateCryptoDepositAccountWithConfigRequestBody(TypedDict, total=False):
    deposit_config_id: Required[str]

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
    destination: Required[AutomationDestinationAssetInputParam]
    """
    A destination asset spec accepting either raw identifiers (asset_address, caip2)
    or human-readable aliases (asset, chain). Exactly one of asset_address or asset
    must be provided; exactly one of caip2 or chain must be provided.
    """

    source: Required[AutomationAssetFilterInputParam]
    """
    Which assets to include/exclude for an automation trigger (input form with alias
    support).
    """

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
