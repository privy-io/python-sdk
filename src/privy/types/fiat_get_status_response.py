# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "FiatGetStatusResponse",
    "Transaction",
    "TransactionUnionMember0",
    "TransactionUnionMember0DepositInstructions",
    "TransactionUnionMember0Destination",
    "TransactionUnionMember0Receipt",
    "TransactionUnionMember1",
    "TransactionUnionMember1DepositInstructions",
    "TransactionUnionMember1Destination",
    "TransactionUnionMember1Receipt",
]


class TransactionUnionMember0DepositInstructions(BaseModel):
    amount: str

    currency: Literal["usd", "eur"]

    payment_rail: Literal["sepa", "ach_push", "wire"]

    account_holder_name: Optional[str] = None

    bank_account_number: Optional[str] = None

    bank_address: Optional[str] = None

    bank_beneficiary_address: Optional[str] = None

    bank_beneficiary_name: Optional[str] = None

    bank_name: Optional[str] = None

    bank_routing_number: Optional[str] = None

    bic: Optional[str] = None

    deposit_message: Optional[str] = None

    iban: Optional[str] = None


class TransactionUnionMember0Destination(BaseModel):
    address: str

    chain: str

    currency: str

    privy_user_id: Optional[str] = None


class TransactionUnionMember0Receipt(BaseModel):
    final_amount: str

    transaction_hash: Optional[str] = None


class TransactionUnionMember0(BaseModel):
    id: str

    created_at: str

    deposit_instructions: TransactionUnionMember0DepositInstructions

    destination: TransactionUnionMember0Destination

    is_sandbox: bool

    status: Literal[
        "awaiting_funds",
        "in_review",
        "funds_received",
        "payment_submitted",
        "payment_processed",
        "canceled",
        "error",
        "undeliverable",
        "returned",
        "refunded",
    ]

    type: Literal["onramp"]

    receipt: Optional[TransactionUnionMember0Receipt] = None


class TransactionUnionMember1DepositInstructions(BaseModel):
    amount: str

    chain: Literal["ethereum", "base", "arbitrum", "polygon", "optimism"]

    currency: Literal["usdc"]

    from_address: str

    to_address: str


class TransactionUnionMember1Destination(BaseModel):
    currency: str

    external_account_id: str

    payment_rail: str


class TransactionUnionMember1Receipt(BaseModel):
    final_amount: str

    transaction_hash: Optional[str] = None


class TransactionUnionMember1(BaseModel):
    id: str

    created_at: str

    deposit_instructions: TransactionUnionMember1DepositInstructions

    destination: TransactionUnionMember1Destination

    is_sandbox: bool

    status: Literal[
        "awaiting_funds",
        "in_review",
        "funds_received",
        "payment_submitted",
        "payment_processed",
        "canceled",
        "error",
        "undeliverable",
        "returned",
        "refunded",
    ]

    type: Literal["offramp"]

    receipt: Optional[TransactionUnionMember1Receipt] = None


Transaction: TypeAlias = Union[TransactionUnionMember0, TransactionUnionMember1]


class FiatGetStatusResponse(BaseModel):
    transactions: List[Transaction]
