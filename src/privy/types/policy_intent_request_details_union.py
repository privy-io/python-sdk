# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .policy_intent_request_details import PolicyIntentRequestDetails
from .policy_intent_delete_request_details import PolicyIntentDeleteRequestDetails

__all__ = ["PolicyIntentRequestDetailsUnion"]

PolicyIntentRequestDetailsUnion: TypeAlias = Annotated[
    Union[PolicyIntentRequestDetails, PolicyIntentDeleteRequestDetails], PropertyInfo(discriminator="method")
]
