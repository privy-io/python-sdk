# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .intent_authorization_key_member import IntentAuthorizationKeyMember
from .intent_authorization_user_member import IntentAuthorizationUserMember

__all__ = ["IntentAuthorizationKeyQuorumMember"]

IntentAuthorizationKeyQuorumMember: TypeAlias = Annotated[
    Union[IntentAuthorizationUserMember, IntentAuthorizationKeyMember], PropertyInfo(discriminator="type")
]
