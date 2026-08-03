# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .onramp_transfer_status import OnrampTransferStatus
from .onramp_deposit_instructions import OnrampDepositInstructions
from .offramp_deposit_instructions import OfframpDepositInstructions

__all__ = [
    "FiatGetStatusResponse",
    "Transaction",
    "TransactionUnionMember0",
    "TransactionUnionMember0Destination",
    "TransactionUnionMember0Receipt",
    "TransactionUnionMember1",
    "TransactionUnionMember1Destination",
    "TransactionUnionMember1Receipt",
]


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

    deposit_instructions: OnrampDepositInstructions
    """Bank deposit instructions for an onramp transfer."""

    destination: TransactionUnionMember0Destination

    is_sandbox: bool

    status: OnrampTransferStatus
    """Status of an onramp or offramp transfer."""

    type: Literal["onramp"]

    receipt: Optional[TransactionUnionMember0Receipt] = None


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

    deposit_instructions: OfframpDepositInstructions
    """Deposit instructions for an offramp transfer."""

    destination: TransactionUnionMember1Destination

    is_sandbox: bool

    status: OnrampTransferStatus
    """Status of an onramp or offramp transfer."""

    type: Literal["offramp"]

    receipt: Optional[TransactionUnionMember1Receipt] = None


Transaction: TypeAlias = Union[TransactionUnionMember0, TransactionUnionMember1]


class FiatGetStatusResponse(BaseModel):
    transactions: List[Transaction]
