# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..email_domain import EmailDomain

__all__ = [
    "AllowlistDeleteParams",
    "EmailInviteInput",
    "EmailDomainInviteInput",
    "WalletInviteInput",
    "PhoneInviteInput",
]


class EmailInviteInput(TypedDict, total=False):
    type: Required[Literal["email"]]

    value: Required[str]


class EmailDomainInviteInput(TypedDict, total=False):
    type: Required[Literal["emailDomain"]]

    value: Required[EmailDomain]
    """An email domain."""


class WalletInviteInput(TypedDict, total=False):
    type: Required[Literal["wallet"]]

    value: Required[str]


class PhoneInviteInput(TypedDict, total=False):
    type: Required[Literal["phone"]]

    value: Required[str]


AllowlistDeleteParams: TypeAlias = Union[EmailInviteInput, EmailDomainInviteInput, WalletInviteInput, PhoneInviteInput]
