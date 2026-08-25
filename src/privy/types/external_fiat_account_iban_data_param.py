# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalFiatAccountIbanDataParam"]


class ExternalFiatAccountIbanDataParam(TypedDict, total=False):
    """IBAN bank account data for an external fiat account. Pays out over SEPA."""

    account_number: Required[str]
    """The IBAN. Up to 34 characters, per ISO 13616."""

    bic: Required[str]
    """The BIC/SWIFT code of the beneficiary bank."""

    country: Required[str]
    """Country the account is held in, as an ISO 3166-1 alpha-3 code."""

    type: Required[Literal["iban"]]
