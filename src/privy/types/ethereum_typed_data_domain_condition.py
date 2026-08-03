# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator
from .ethereum_typed_data_domain_condition_field import EthereumTypedDataDomainConditionField

__all__ = ["EthereumTypedDataDomainCondition"]


class EthereumTypedDataDomainCondition(BaseModel):
    """Attributes from the signing domain that will verify the signature."""

    field: EthereumTypedDataDomainConditionField
    """Supported fields for Ethereum typed data domain conditions."""

    field_source: Literal["ethereum_typed_data_domain"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
