# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .abi_schema import AbiSchema
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator

__all__ = ["TronCalldataCondition"]


class TronCalldataCondition(BaseModel):
    """Decoded calldata from a TRON TriggerSmartContract interaction."""

    abi: AbiSchema
    """A Solidity ABI definition for decoding smart contract calldata."""

    field: str

    field_source: Literal["tron_trigger_smart_contract_data"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
