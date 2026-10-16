# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .condition_set_item_intent_create_request_details import ConditionSetItemIntentCreateRequestDetails
from .condition_set_item_intent_delete_request_details import ConditionSetItemIntentDeleteRequestDetails
from .condition_set_item_intent_update_request_details import ConditionSetItemIntentUpdateRequestDetails

__all__ = ["ConditionSetItemIntentRequestDetails"]

ConditionSetItemIntentRequestDetails: TypeAlias = Annotated[
    Union[
        ConditionSetItemIntentCreateRequestDetails,
        ConditionSetItemIntentUpdateRequestDetails,
        ConditionSetItemIntentDeleteRequestDetails,
    ],
    PropertyInfo(discriminator="method"),
]
