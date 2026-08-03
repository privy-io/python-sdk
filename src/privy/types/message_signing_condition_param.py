# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .message_signing_field import MessageSigningField

__all__ = ["MessageSigningConditionParam"]


class MessageSigningConditionParam(TypedDict, total=False):
    """Condition on the message being signed (e.g. in personal_sign)."""

    field: Required[MessageSigningField]
    """Supported fields for message signing conditions."""

    field_source: Required[Literal["message"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
