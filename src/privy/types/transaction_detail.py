# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .transfer_sent_transaction_detail import TransferSentTransactionDetail
from .transfer_received_transaction_detail import TransferReceivedTransactionDetail

__all__ = ["TransactionDetail"]

TransactionDetail: TypeAlias = Annotated[
    Union[TransferSentTransactionDetail, TransferReceivedTransactionDetail], PropertyInfo(discriminator="type")
]
