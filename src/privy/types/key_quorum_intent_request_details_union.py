# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .key_quorum_intent_request_details import KeyQuorumIntentRequestDetails
from .key_quorum_intent_delete_request_details import KeyQuorumIntentDeleteRequestDetails

__all__ = ["KeyQuorumIntentRequestDetailsUnion"]

KeyQuorumIntentRequestDetailsUnion: TypeAlias = Annotated[
    Union[KeyQuorumIntentRequestDetails, KeyQuorumIntentDeleteRequestDetails], PropertyInfo(discriminator="method")
]
