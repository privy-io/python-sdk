# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalFiatAccountPixDataParam"]


class ExternalFiatAccountPixDataParam(TypedDict, total=False):
    """Brazilian Pix account data for an external fiat account.

    Provide exactly one of `pix_key` or `br_code`.
    """

    type: Required[Literal["pix"]]

    br_code: str
    """The Pix "copia e cola" (copy and paste) BR Code."""

    document_number: str
    """Optional CPF/CNPJ associated with the account, digits only."""

    pix_key: str
    """
    The Pix key: an EVP (UUID), CPF, CNPJ, Brazilian phone number (+55…), or email
    address.
    """
