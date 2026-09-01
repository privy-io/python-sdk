# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .spark_transfer_rpc_input import SparkTransferRpcInput
from .spark_withdraw_rpc_input import SparkWithdrawRpcInput
from .spark_get_balance_rpc_input import SparkGetBalanceRpcInput
from .export_private_key_rpc_input import ExportPrivateKeyRpcInput
from .export_seed_phrase_rpc_input import ExportSeedPhraseRpcInput
from .ethereum_send_calls_rpc_input import EthereumSendCallsRpcInput
from .solana_sign_message_rpc_input import SolanaSignMessageRpcInput
from .spark_transfer_tokens_rpc_input import SparkTransferTokensRpcInput
from .tron_send_transaction_rpc_input import TronSendTransactionRpcInput
from .tron_sign_transaction_rpc_input import TronSignTransactionRpcInput
from .xrpl_sign_transaction_rpc_input import XrplSignTransactionRpcInput
from .aptos_sign_transaction_rpc_input import AptosSignTransactionRpcInput
from .ethereum_personal_sign_rpc_input import EthereumPersonalSignRpcInput
from .solana_sign_transaction_rpc_input import SolanaSignTransactionRpcInput
from .ethereum_sign_typed_data_rpc_input import EthereumSignTypedDataRpcInput
from .ethereum_secp_256k_1_sign_rpc_input import EthereumSecp256k1SignRpcInput
from .ethereum_send_transaction_rpc_input import EthereumSendTransactionRpcInput
from .ethereum_sign_transaction_rpc_input import EthereumSignTransactionRpcInput
from .spark_claim_static_deposit_rpc_input import SparkClaimStaticDepositRpcInput
from .spark_pay_lightning_invoice_rpc_input import SparkPayLightningInvoiceRpcInput
from .ethereum_sign_user_operation_rpc_input import EthereumSignUserOperationRpcInput
from .near_sign_transaction_rpc_request_body import NearSignTransactionRpcRequestBody
from .spark_create_lightning_invoice_rpc_input import SparkCreateLightningInvoiceRpcInput
from .spark_get_withdrawal_fee_quote_rpc_input import SparkGetWithdrawalFeeQuoteRpcInput
from .ethereum_sign_7702_authorization_rpc_input import EthereumSign7702AuthorizationRpcInput
from .solana_sign_and_send_transaction_rpc_input import SolanaSignAndSendTransactionRpcInput
from .spark_get_static_deposit_address_rpc_input import SparkGetStaticDepositAddressRpcInput
from .spark_get_claim_static_deposit_quote_rpc_input import SparkGetClaimStaticDepositQuoteRpcInput
from .spark_sign_message_with_identity_key_rpc_input import SparkSignMessageWithIdentityKeyRpcInput

__all__ = ["WalletRpcRequestBody"]

WalletRpcRequestBody: TypeAlias = Annotated[
    Union[
        EthereumSignTransactionRpcInput,
        EthereumSendTransactionRpcInput,
        EthereumPersonalSignRpcInput,
        EthereumSignTypedDataRpcInput,
        EthereumSecp256k1SignRpcInput,
        EthereumSign7702AuthorizationRpcInput,
        EthereumSignUserOperationRpcInput,
        EthereumSendCallsRpcInput,
        AptosSignTransactionRpcInput,
        SolanaSignTransactionRpcInput,
        SolanaSignAndSendTransactionRpcInput,
        SolanaSignMessageRpcInput,
        SparkTransferRpcInput,
        SparkGetBalanceRpcInput,
        SparkTransferTokensRpcInput,
        SparkGetStaticDepositAddressRpcInput,
        SparkGetClaimStaticDepositQuoteRpcInput,
        SparkClaimStaticDepositRpcInput,
        SparkCreateLightningInvoiceRpcInput,
        SparkPayLightningInvoiceRpcInput,
        SparkSignMessageWithIdentityKeyRpcInput,
        SparkWithdrawRpcInput,
        SparkGetWithdrawalFeeQuoteRpcInput,
        TronSignTransactionRpcInput,
        TronSendTransactionRpcInput,
        XrplSignTransactionRpcInput,
        NearSignTransactionRpcRequestBody,
        ExportPrivateKeyRpcInput,
        ExportSeedPhraseRpcInput,
    ],
    PropertyInfo(discriminator="method"),
]
