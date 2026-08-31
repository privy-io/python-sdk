# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .spark_transfer_rpc_response import SparkTransferRpcResponse
from .spark_withdraw_rpc_response import SparkWithdrawRpcResponse
from .spark_get_balance_rpc_response import SparkGetBalanceRpcResponse
from .export_private_key_rpc_response import ExportPrivateKeyRpcResponse
from .export_seed_phrase_rpc_response import ExportSeedPhraseRpcResponse
from .ethereum_send_calls_rpc_response import EthereumSendCallsRpcResponse
from .solana_sign_message_rpc_response import SolanaSignMessageRpcResponse
from .spark_transfer_tokens_rpc_response import SparkTransferTokensRpcResponse
from .tron_send_transaction_rpc_response import TronSendTransactionRpcResponse
from .tron_sign_transaction_rpc_response import TronSignTransactionRpcResponse
from .xrpl_sign_transaction_rpc_response import XrplSignTransactionRpcResponse
from .aptos_sign_transaction_rpc_response import AptosSignTransactionRpcResponse
from .ethereum_personal_sign_rpc_response import EthereumPersonalSignRpcResponse
from .solana_sign_transaction_rpc_response import SolanaSignTransactionRpcResponse
from .ethereum_sign_typed_data_rpc_response import EthereumSignTypedDataRpcResponse
from .ethereum_secp_256k_1_sign_rpc_response import EthereumSecp256k1SignRpcResponse
from .ethereum_send_transaction_rpc_response import EthereumSendTransactionRpcResponse
from .ethereum_sign_transaction_rpc_response import EthereumSignTransactionRpcResponse
from .spark_claim_static_deposit_rpc_response import SparkClaimStaticDepositRpcResponse
from .spark_pay_lightning_invoice_rpc_response import SparkPayLightningInvoiceRpcResponse
from .ethereum_sign_user_operation_rpc_response import EthereumSignUserOperationRpcResponse
from .spark_create_lightning_invoice_rpc_response import SparkCreateLightningInvoiceRpcResponse
from .spark_get_withdrawal_fee_quote_rpc_response import SparkGetWithdrawalFeeQuoteRpcResponse
from .ethereum_sign_7702_authorization_rpc_response import EthereumSign7702AuthorizationRpcResponse
from .solana_sign_and_send_transaction_rpc_response import SolanaSignAndSendTransactionRpcResponse
from .spark_get_static_deposit_address_rpc_response import SparkGetStaticDepositAddressRpcResponse
from .spark_get_claim_static_deposit_quote_rpc_response import SparkGetClaimStaticDepositQuoteRpcResponse
from .spark_sign_message_with_identity_key_rpc_response import SparkSignMessageWithIdentityKeyRpcResponse

__all__ = ["WalletRpcResponse"]

WalletRpcResponse: TypeAlias = Annotated[
    Union[
        EthereumPersonalSignRpcResponse,
        EthereumSignTypedDataRpcResponse,
        EthereumSignTransactionRpcResponse,
        EthereumSendTransactionRpcResponse,
        EthereumSignUserOperationRpcResponse,
        EthereumSign7702AuthorizationRpcResponse,
        EthereumSecp256k1SignRpcResponse,
        EthereumSendCallsRpcResponse,
        AptosSignTransactionRpcResponse,
        SolanaSignMessageRpcResponse,
        SolanaSignTransactionRpcResponse,
        SolanaSignAndSendTransactionRpcResponse,
        SparkTransferRpcResponse,
        SparkGetBalanceRpcResponse,
        SparkTransferTokensRpcResponse,
        SparkGetStaticDepositAddressRpcResponse,
        SparkGetClaimStaticDepositQuoteRpcResponse,
        SparkClaimStaticDepositRpcResponse,
        SparkCreateLightningInvoiceRpcResponse,
        SparkPayLightningInvoiceRpcResponse,
        SparkSignMessageWithIdentityKeyRpcResponse,
        SparkWithdrawRpcResponse,
        SparkGetWithdrawalFeeQuoteRpcResponse,
        TronSignTransactionRpcResponse,
        TronSendTransactionRpcResponse,
        XrplSignTransactionRpcResponse,
        ExportPrivateKeyRpcResponse,
        ExportSeedPhraseRpcResponse,
    ],
    PropertyInfo(discriminator="method"),
]
