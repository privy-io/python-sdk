# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .rule_intent_create_request_details import RuleIntentCreateRequestDetails
from .rule_intent_delete_request_details import RuleIntentDeleteRequestDetails
from .rule_intent_update_request_details import RuleIntentUpdateRequestDetails

__all__ = ["RuleIntentRequestDetails"]

RuleIntentRequestDetails: TypeAlias = Annotated[
    Union[RuleIntentCreateRequestDetails, RuleIntentUpdateRequestDetails, RuleIntentDeleteRequestDetails],
    PropertyInfo(discriminator="method"),
]
