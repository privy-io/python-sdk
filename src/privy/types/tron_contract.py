# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .tron_transfer_contract import TronTransferContract
from .tron_trigger_smart_contract import TronTriggerSmartContract

__all__ = ["TronContract"]

TronContract: TypeAlias = Annotated[
    Union[TronTransferContract, TronTriggerSmartContract], PropertyInfo(discriminator="type")
]
