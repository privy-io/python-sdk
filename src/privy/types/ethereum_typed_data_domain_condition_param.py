# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .ethereum_typed_data_domain_condition_field import EthereumTypedDataDomainConditionField

__all__ = ["EthereumTypedDataDomainConditionParam"]


class EthereumTypedDataDomainConditionParam(TypedDict, total=False):
    """Attributes from the signing domain that will verify the signature."""

    field: Required[EthereumTypedDataDomainConditionField]
    """Supported fields for Ethereum typed data domain conditions."""

    field_source: Required[Literal["ethereum_typed_data_domain"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
