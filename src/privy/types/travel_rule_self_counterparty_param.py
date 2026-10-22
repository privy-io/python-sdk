# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TravelRuleSelfCounterpartyParam"]


class TravelRuleSelfCounterpartyParam(TypedDict, total=False):
    """The bank-side party is the KYC-verified customer.

    Bridge uses the customer's name and address on file.
    """

    type: Required[Literal["self"]]
