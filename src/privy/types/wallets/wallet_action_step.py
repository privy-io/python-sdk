# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .evm_transaction_wallet_action_step import EvmTransactionWalletActionStep
from .svm_transaction_wallet_action_step import SvmTransactionWalletActionStep
from .tvm_transaction_wallet_action_step import TvmTransactionWalletActionStep
from .evm_user_operation_wallet_action_step import EvmUserOperationWalletActionStep
from .external_transaction_wallet_action_step import ExternalTransactionWalletActionStep
from .custodian_transaction_wallet_action_step import CustodianTransactionWalletActionStep

__all__ = ["WalletActionStep"]

WalletActionStep: TypeAlias = Annotated[
    Union[
        EvmTransactionWalletActionStep,
        EvmUserOperationWalletActionStep,
        SvmTransactionWalletActionStep,
        TvmTransactionWalletActionStep,
        ExternalTransactionWalletActionStep,
        CustodianTransactionWalletActionStep,
    ],
    PropertyInfo(discriminator="type"),
]
