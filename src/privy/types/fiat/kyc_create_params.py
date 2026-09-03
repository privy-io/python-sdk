# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "KYCCreateParams",
    "Variant0",
    "Variant0Data",
    "Variant0DataIdentifyingInformation",
    "Variant0DataResidentialAddress",
    "Variant0DataDocument",
    "Variant0DataKYCScreen",
    "Variant0DataOfacScreen",
    "Variant0DataTransliteratedResidentialAddress",
    "Variant1",
    "Variant1Data",
    "Variant1DataIdentifyingInformation",
    "Variant1DataResidentialAddress",
    "Variant1DataDocument",
    "Variant1DataKYCScreen",
    "Variant1DataOfacScreen",
    "Variant1DataTransliteratedResidentialAddress",
]


class Variant0(TypedDict, total=False):
    data: Required[Variant0Data]

    provider: Required[Literal["bridge"]]


class Variant0DataIdentifyingInformation(TypedDict, total=False):
    issuing_country: Required[str]

    type: Required[str]

    description: str

    expiration: str

    image_back: str

    image_front: str

    number: str


class Variant0DataResidentialAddress(TypedDict, total=False):
    city: Required[str]

    country: Required[str]

    street_line_1: Required[str]

    subdivision: Required[str]

    postal_code: str

    street_line_2: str


class Variant0DataDocument(TypedDict, total=False):
    file: Required[str]

    purposes: Required[List[str]]

    description: str


class Variant0DataKYCScreen(TypedDict, total=False):
    result: Required[Literal["passed"]]

    screened_at: Required[str]


class Variant0DataOfacScreen(TypedDict, total=False):
    result: Required[Literal["passed"]]

    screened_at: Required[str]


class Variant0DataTransliteratedResidentialAddress(TypedDict, total=False):
    city: Required[str]

    country: Required[str]

    street_line_1: Required[str]

    subdivision: Required[str]

    postal_code: str

    street_line_2: str


class Variant0Data(TypedDict, total=False):
    birth_date: Required[str]

    email: Required[str]

    first_name: Required[str]

    identifying_information: Required[Iterable[Variant0DataIdentifyingInformation]]

    last_name: Required[str]

    residential_address: Required[Variant0DataResidentialAddress]

    type: Required[Literal["individual"]]

    account_purpose: str

    account_purpose_other: str

    acting_as_intermediary: str

    completed_customer_safety_check_at: str

    documents: Iterable[Variant0DataDocument]

    employment_status: str

    endorsements: List[str]

    expected_monthly_payments_usd: str

    has_signed_terms_of_service: bool

    kyc_screen: Variant0DataKYCScreen

    middle_name: str

    most_recent_occupation: str

    nationality: str

    ofac_screen: Variant0DataOfacScreen

    phone: str

    signed_agreement_id: str

    source_of_funds: str

    transliterated_first_name: str

    transliterated_last_name: str

    transliterated_middle_name: str

    transliterated_residential_address: Variant0DataTransliteratedResidentialAddress

    verified_selfie_at: str


class Variant1(TypedDict, total=False):
    data: Required[Variant1Data]

    provider: Required[Literal["bridge-sandbox"]]


class Variant1DataIdentifyingInformation(TypedDict, total=False):
    issuing_country: Required[str]

    type: Required[str]

    description: str

    expiration: str

    image_back: str

    image_front: str

    number: str


class Variant1DataResidentialAddress(TypedDict, total=False):
    city: Required[str]

    country: Required[str]

    street_line_1: Required[str]

    subdivision: Required[str]

    postal_code: str

    street_line_2: str


class Variant1DataDocument(TypedDict, total=False):
    file: Required[str]

    purposes: Required[List[str]]

    description: str


class Variant1DataKYCScreen(TypedDict, total=False):
    result: Required[Literal["passed"]]

    screened_at: Required[str]


class Variant1DataOfacScreen(TypedDict, total=False):
    result: Required[Literal["passed"]]

    screened_at: Required[str]


class Variant1DataTransliteratedResidentialAddress(TypedDict, total=False):
    city: Required[str]

    country: Required[str]

    street_line_1: Required[str]

    subdivision: Required[str]

    postal_code: str

    street_line_2: str


class Variant1Data(TypedDict, total=False):
    birth_date: Required[str]

    email: Required[str]

    first_name: Required[str]

    identifying_information: Required[Iterable[Variant1DataIdentifyingInformation]]

    last_name: Required[str]

    residential_address: Required[Variant1DataResidentialAddress]

    type: Required[Literal["individual"]]

    account_purpose: str

    account_purpose_other: str

    acting_as_intermediary: str

    completed_customer_safety_check_at: str

    documents: Iterable[Variant1DataDocument]

    employment_status: str

    endorsements: List[str]

    expected_monthly_payments_usd: str

    has_signed_terms_of_service: bool

    kyc_screen: Variant1DataKYCScreen

    middle_name: str

    most_recent_occupation: str

    nationality: str

    ofac_screen: Variant1DataOfacScreen

    phone: str

    signed_agreement_id: str

    source_of_funds: str

    transliterated_first_name: str

    transliterated_last_name: str

    transliterated_middle_name: str

    transliterated_residential_address: Variant1DataTransliteratedResidentialAddress

    verified_selfie_at: str


KYCCreateParams: TypeAlias = Union[Variant0, Variant1]
