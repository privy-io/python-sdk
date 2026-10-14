# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..email_domain import EmailDomain

__all__ = [
    "DenylistCreateParams",
    "DenylistEmailInput",
    "DenylistEmailDomainInput",
    "DenylistPhoneInput",
    "DenylistEthereumAddressInput",
    "DenylistSolanaAddressInput",
]


class DenylistEmailInput(TypedDict, total=False):
    type: Required[Literal["email"]]

    value: Required[str]


class DenylistEmailDomainInput(TypedDict, total=False):
    type: Required[Literal["emailDomain"]]

    value: Required[EmailDomain]
    """An email domain."""


class DenylistPhoneInput(TypedDict, total=False):
    type: Required[Literal["phone"]]

    value: Required[str]


class DenylistEthereumAddressInput(TypedDict, total=False):
    type: Required[Literal["ethereumAddress"]]

    value: Required[str]


class DenylistSolanaAddressInput(TypedDict, total=False):
    type: Required[Literal["solanaAddress"]]

    value: Required[str]


DenylistCreateParams: TypeAlias = Union[
    DenylistEmailInput,
    DenylistEmailDomainInput,
    DenylistPhoneInput,
    DenylistEthereumAddressInput,
    DenylistSolanaAddressInput,
]
