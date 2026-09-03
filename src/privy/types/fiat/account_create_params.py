# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountCreateParams", "Account", "Address", "Iban", "Swift", "SwiftAccount", "SwiftAddress"]


class AccountCreateParams(TypedDict, total=False):
    account_owner_name: Required[str]

    currency: Required[Literal["usd", "eur"]]

    provider: Required[Literal["bridge", "bridge-sandbox"]]

    account: Account

    address: Address

    bank_name: str

    first_name: str

    iban: Iban

    last_name: str

    swift: Swift


class Account(TypedDict, total=False):
    account_number: Required[str]

    routing_number: Required[str]

    checking_or_savings: Literal["checking", "savings"]


class Address(TypedDict, total=False):
    city: Required[str]

    country: Required[str]

    street_line_1: Required[str]

    postal_code: str

    state: str

    street_line_2: str


class Iban(TypedDict, total=False):
    account_number: Required[str]

    bic: Required[str]

    country: Required[str]


class SwiftAccount(TypedDict, total=False):
    account_number: Required[str]

    bic: Required[str]

    country: Required[str]


class SwiftAddress(TypedDict, total=False):
    city: Required[str]

    country: Required[str]

    street_line_1: Required[str]

    postal_code: str

    state: str

    street_line_2: str


class Swift(TypedDict, total=False):
    account: Required[SwiftAccount]

    address: Required[SwiftAddress]

    category: Required[Literal["client", "parent_company", "subsidiary", "supplier"]]

    purpose_of_funds: Required[List[Literal["intra_group_transfer", "invoice_for_goods_and_services"]]]

    short_business_description: Required[str]
