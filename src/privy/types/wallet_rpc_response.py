# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WalletRpcResponse",
    "SignTransaction",
    "SignTransactionData",
    "SignAndSendTransaction",
    "SignAndSendTransactionData",
    "SignAndSendTransactionError",
    "SignMessage",
    "SignMessageData",
    "EthSignTransaction",
    "EthSignTransactionData",
    "EthSendTransaction",
    "EthSendTransactionData",
    "EthSendTransactionDataTransactionRequest",
    "EthSendTransactionError",
    "PersonalSign",
    "PersonalSignData",
    "EthSignTypedDataV4",
    "EthSignTypedDataV4Data",
    "EthSign7702Authorization",
    "EthSign7702AuthorizationData",
    "EthSign7702AuthorizationDataAuthorization",
    "EthSign7702AuthorizationError",
    "Secp256k1Sign",
    "Secp256k1SignData",
]


class SignTransactionData(BaseModel):
    encoding: Literal["base64"]

    signed_transaction: str


class SignTransaction(BaseModel):
    data: SignTransactionData

    method: Literal["signTransaction"]


class SignAndSendTransactionData(BaseModel):
    caip2: str

    hash: str

    transaction_id: Optional[str] = None


class SignAndSendTransactionError(BaseModel):
    code: str

    message: str


class SignAndSendTransaction(BaseModel):
    method: Literal["signAndSendTransaction"]

    data: Optional[SignAndSendTransactionData] = None

    error: Optional[SignAndSendTransactionError] = None


class SignMessageData(BaseModel):
    encoding: Literal["base64"]

    signature: str


class SignMessage(BaseModel):
    data: SignMessageData

    method: Literal["signMessage"]


class EthSignTransactionData(BaseModel):
    encoding: Literal["rlp"]

    signed_transaction: str


class EthSignTransaction(BaseModel):
    data: EthSignTransactionData

    method: Literal["eth_signTransaction"]


class EthSendTransactionDataTransactionRequest(BaseModel):
    chain_id: Union[str, int, None] = None

    data: Optional[str] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    gas_limit: Union[str, int, None] = None

    gas_price: Union[str, int, None] = None

    max_fee_per_gas: Union[str, int, None] = None

    max_priority_fee_per_gas: Union[str, int, None] = None

    nonce: Union[str, int, None] = None

    to: Optional[str] = None

    type: Optional[Literal[0, 1, 2]] = None

    value: Union[str, int, None] = None


class EthSendTransactionData(BaseModel):
    caip2: str

    hash: str

    transaction_id: Optional[str] = None

    transaction_request: Optional[EthSendTransactionDataTransactionRequest] = None


class EthSendTransactionError(BaseModel):
    code: str

    message: str


class EthSendTransaction(BaseModel):
    method: Literal["eth_sendTransaction"]

    data: Optional[EthSendTransactionData] = None

    error: Optional[EthSendTransactionError] = None


class PersonalSignData(BaseModel):
    encoding: Literal["hex"]

    signature: str


class PersonalSign(BaseModel):
    data: PersonalSignData

    method: Literal["personal_sign"]


class EthSignTypedDataV4Data(BaseModel):
    encoding: Literal["hex"]

    signature: str


class EthSignTypedDataV4(BaseModel):
    data: EthSignTypedDataV4Data

    method: Literal["eth_signTypedData_v4"]


class EthSign7702AuthorizationDataAuthorization(BaseModel):
    chain_id: Union[str, int]

    contract: str

    nonce: Union[str, int]

    r: str

    s: str

    y_parity: float


class EthSign7702AuthorizationData(BaseModel):
    authorization: EthSign7702AuthorizationDataAuthorization


class EthSign7702AuthorizationError(BaseModel):
    code: str

    message: str


class EthSign7702Authorization(BaseModel):
    method: Literal["eth_sign7702Authorization"]

    data: Optional[EthSign7702AuthorizationData] = None

    error: Optional[EthSign7702AuthorizationError] = None


class Secp256k1SignData(BaseModel):
    encoding: Literal["hex"]

    signature: str


class Secp256k1Sign(BaseModel):
    data: Secp256k1SignData

    method: Literal["secp256k1_sign"]


WalletRpcResponse: TypeAlias = Union[
    SignTransaction,
    SignAndSendTransaction,
    SignMessage,
    EthSignTransaction,
    EthSendTransaction,
    PersonalSign,
    EthSignTypedDataV4,
    EthSign7702Authorization,
    Secp256k1Sign,
]
