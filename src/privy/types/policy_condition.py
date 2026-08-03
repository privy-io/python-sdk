# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .system_condition import SystemCondition
from .aggregation_condition import AggregationCondition
from .tron_calldata_condition import TronCalldataCondition
from .message_signing_condition import MessageSigningCondition
from .tron_transaction_condition import TronTransactionCondition
from .ethereum_calldata_condition import EthereumCalldataCondition
from .tempo_transaction_condition import TempoTransactionCondition
from .action_request_body_condition import ActionRequestBodyCondition
from .ethereum_transaction_condition import EthereumTransactionCondition
from .sui_transaction_command_condition import SuiTransactionCommandCondition
from .ethereum_typed_data_domain_condition import EthereumTypedDataDomainCondition
from .solana_program_instruction_condition import SolanaProgramInstructionCondition
from .ethereum_7702_authorization_condition import Ethereum7702AuthorizationCondition
from .ethereum_typed_data_message_condition import EthereumTypedDataMessageCondition
from .sui_transfer_objects_command_condition import SuiTransferObjectsCommandCondition
from .solana_token_program_instruction_condition import SolanaTokenProgramInstructionCondition
from .solana_system_program_instruction_condition import SolanaSystemProgramInstructionCondition

__all__ = ["PolicyCondition"]

PolicyCondition: TypeAlias = Annotated[
    Union[
        EthereumTransactionCondition,
        EthereumCalldataCondition,
        EthereumTypedDataDomainCondition,
        EthereumTypedDataMessageCondition,
        Ethereum7702AuthorizationCondition,
        TempoTransactionCondition,
        SolanaProgramInstructionCondition,
        SolanaSystemProgramInstructionCondition,
        SolanaTokenProgramInstructionCondition,
        SystemCondition,
        TronTransactionCondition,
        TronCalldataCondition,
        SuiTransactionCommandCondition,
        SuiTransferObjectsCommandCondition,
        ActionRequestBodyCondition,
        AggregationCondition,
        MessageSigningCondition,
    ],
    PropertyInfo(discriminator="field_source"),
]
