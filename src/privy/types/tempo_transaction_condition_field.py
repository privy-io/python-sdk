# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TempoTransactionConditionField"]

TempoTransactionConditionField: TypeAlias = Literal[
    "fee_token", "fee_payer_signature", "nonce_key", "valid_before", "valid_after"
]
