# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .tron_transfer_contract_param import TronTransferContractParam
from .tron_trigger_smart_contract_param import TronTriggerSmartContractParam

__all__ = ["TronContractParam"]

TronContractParam: TypeAlias = Union[TronTransferContractParam, TronTriggerSmartContractParam]
