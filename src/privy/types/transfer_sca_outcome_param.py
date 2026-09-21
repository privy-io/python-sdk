# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["TransferScaOutcomeParam"]

TransferScaOutcomeParam: TypeAlias = Union[
    Literal[
        "sca_used",
        "payment_to_self",
        "trusted_beneficiaries",
        "recurring_transaction",
        "contactless_low_value",
        "unattended_terminal_for_transport",
        "low_value",
        "secure_corporate_payment",
        "transaction_risk_analysis",
        "merchant_initiated_transaction",
        "not_applicable",
        "other",
    ],
    str,
]
