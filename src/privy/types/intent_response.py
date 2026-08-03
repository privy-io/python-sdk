# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .rpc_intent_response import RpcIntentResponse
from .rule_intent_response import RuleIntentResponse
from .policy_intent_response import PolicyIntentResponse
from .wallet_intent_response import WalletIntentResponse
from .transfer_intent_response import TransferIntentResponse
from .key_quorum_intent_response import KeyQuorumIntentResponse

__all__ = ["IntentResponse"]

IntentResponse: TypeAlias = Annotated[
    Union[
        RpcIntentResponse,
        TransferIntentResponse,
        WalletIntentResponse,
        PolicyIntentResponse,
        RuleIntentResponse,
        KeyQuorumIntentResponse,
    ],
    PropertyInfo(discriminator="intent_type"),
]
