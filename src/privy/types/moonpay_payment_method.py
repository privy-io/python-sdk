# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["MoonpayPaymentMethod"]

MoonpayPaymentMethod: TypeAlias = Literal[
    "ach_bank_transfer",
    "credit_debit_card",
    "gbp_bank_transfer",
    "gbp_open_banking_payment",
    "mobile_wallet",
    "sepa_bank_transfer",
    "sepa_open_banking_payment",
    "pix_instant_payment",
    "yellow_card_bank_transfer",
]
