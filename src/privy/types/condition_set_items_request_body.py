# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .condition_set_item_value_input import ConditionSetItemValueInput

__all__ = ["ConditionSetItemsRequestBody"]

ConditionSetItemsRequestBody: TypeAlias = List[ConditionSetItemValueInput]
