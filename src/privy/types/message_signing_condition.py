# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator
from .message_signing_field import MessageSigningField

__all__ = ["MessageSigningCondition"]


class MessageSigningCondition(BaseModel):
    """Condition on the message being signed (e.g. in personal_sign)."""

    field: MessageSigningField
    """Supported fields for message signing conditions."""

    field_source: Literal["message"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
