# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .abi_schema_param import AbiSchemaParam
from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam

__all__ = ["TronCalldataConditionParam"]


class TronCalldataConditionParam(TypedDict, total=False):
    """Decoded calldata from a TRON TriggerSmartContract interaction."""

    abi: Required[AbiSchemaParam]
    """A Solidity ABI definition for decoding smart contract calldata."""

    field: Required[str]

    field_source: Required[Literal["tron_trigger_smart_contract_data"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
