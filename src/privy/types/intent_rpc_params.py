# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .hex import Hex
from .caip_2 import Caip2
from .._utils import PropertyInfo
from .spark_network import SparkNetwork
from .signature_options_param import SignatureOptionsParam
from .rpc_sponsor_options_param import RpcSponsorOptionsParam
from .private_key_export_input_param import PrivateKeyExportInputParam
from .seed_phrase_export_input_param import SeedPhraseExportInputParam
from .spark_transfer_rpc_input_params_param import SparkTransferRpcInputParamsParam
from .spark_withdraw_rpc_input_params_param import SparkWithdrawRpcInputParamsParam
from .ethereum_send_calls_rpc_input_params_param import EthereumSendCallsRpcInputParamsParam
from .solana_sign_message_rpc_input_params_param import SolanaSignMessageRpcInputParamsParam
from .spark_transfer_tokens_rpc_input_params_param import SparkTransferTokensRpcInputParamsParam
from .tron_send_transaction_rpc_input_params_param import TronSendTransactionRpcInputParamsParam
from .tron_sign_transaction_rpc_input_params_param import TronSignTransactionRpcInputParamsParam
from .ethereum_personal_sign_rpc_input_params_param import EthereumPersonalSignRpcInputParamsParam
from .solana_sign_transaction_rpc_input_params_param import SolanaSignTransactionRpcInputParamsParam
from .ethereum_sign_typed_data_rpc_input_params_param import EthereumSignTypedDataRpcInputParamsParam
from .ethereum_secp_256k_1_sign_rpc_input_params_param import EthereumSecp256k1SignRpcInputParamsParam
from .ethereum_send_transaction_rpc_input_params_param import EthereumSendTransactionRpcInputParamsParam
from .ethereum_sign_transaction_rpc_input_params_param import EthereumSignTransactionRpcInputParamsParam
from .spark_claim_static_deposit_rpc_input_params_param import SparkClaimStaticDepositRpcInputParamsParam
from .spark_pay_lightning_invoice_rpc_input_params_param import SparkPayLightningInvoiceRpcInputParamsParam
from .ethereum_sign_user_operation_rpc_input_params_param import EthereumSignUserOperationRpcInputParamsParam
from .spark_create_lightning_invoice_rpc_input_params_param import SparkCreateLightningInvoiceRpcInputParamsParam
from .spark_get_withdrawal_fee_quote_rpc_input_params_param import SparkGetWithdrawalFeeQuoteRpcInputParamsParam
from .ethereum_sign_7702_authorization_rpc_input_params_param import EthereumSign7702AuthorizationRpcInputParamsParam
from .solana_sign_and_send_transaction_rpc_input_params_param import SolanaSignAndSendTransactionRpcInputParamsParam
from .spark_get_claim_static_deposit_quote_rpc_input_params_param import (
    SparkGetClaimStaticDepositQuoteRpcInputParamsParam,
)
from .spark_sign_message_with_identity_key_rpc_input_params_param import (
    SparkSignMessageWithIdentityKeyRpcInputParamsParam,
)

__all__ = [
    "IntentRpcParams",
    "EthereumSignTransactionRpcInput",
    "EthereumSendTransactionRpcInput",
    "EthereumPersonalSignRpcInput",
    "EthereumSignTypedDataRpcInput",
    "EthereumSecp256k1SignRpcInput",
    "EthereumSign7702AuthorizationRpcInput",
    "EthereumSignUserOperationRpcInput",
    "EthereumSendCallsRpcInput",
    "SolanaSignTransactionRpcInput",
    "SolanaSignAndSendTransactionRpcInput",
    "SolanaSignMessageRpcInput",
    "SparkTransferRpcInput",
    "SparkGetBalanceRpcInput",
    "SparkTransferTokensRpcInput",
    "SparkGetStaticDepositAddressRpcInput",
    "SparkGetClaimStaticDepositQuoteRpcInput",
    "SparkClaimStaticDepositRpcInput",
    "SparkCreateLightningInvoiceRpcInput",
    "SparkPayLightningInvoiceRpcInput",
    "SparkSignMessageWithIdentityKeyRpcInput",
    "SparkWithdrawRpcInput",
    "SparkGetWithdrawalFeeQuoteRpcInput",
    "TronSignTransactionRpcInput",
    "TronSendTransactionRpcInput",
    "ExportPrivateKeyRpcInput",
    "ExportSeedPhraseRpcInput",
]


class EthereumSignTransactionRpcInput(TypedDict, total=False):
    method: Required[Literal["eth_signTransaction"]]

    params: Required[EthereumSignTransactionRpcInputParamsParam]
    """Parameters for the EVM `eth_signTransaction` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class EthereumSendTransactionRpcInput(TypedDict, total=False):
    caip2: Required[Caip2]
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    method: Required[Literal["eth_sendTransaction"]]

    params: Required[EthereumSendTransactionRpcInputParamsParam]
    """Parameters for the EVM `eth_sendTransaction` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    experimental_data_suffix: Hex
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    reference_id: str

    sponsor: bool

    sponsor_options: RpcSponsorOptionsParam
    """Options for user-pays gas sponsorship on the RPC endpoint.

    When provided alongside `sponsor: true`, controls which token asset the user
    pays gas with.
    """

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class EthereumPersonalSignRpcInput(TypedDict, total=False):
    method: Required[Literal["personal_sign"]]

    params: Required[EthereumPersonalSignRpcInputParamsParam]
    """Parameters for the EVM `personal_sign` RPC."""

    address: str

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    chain_type: Literal["ethereum"]

    signature_options: SignatureOptionsParam
    """
    Options controlling signature production for personal_sign and
    eth_signTypedData_v4.
    """

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class EthereumSignTypedDataRpcInput(TypedDict, total=False):
    method: Required[Literal["eth_signTypedData_v4"]]

    params: Required[EthereumSignTypedDataRpcInputParamsParam]
    """Parameters for the EVM `eth_signTypedData_v4` RPC."""

    address: str

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    chain_type: Literal["ethereum"]

    signature_options: SignatureOptionsParam
    """
    Options controlling signature production for personal_sign and
    eth_signTypedData_v4.
    """

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class EthereumSecp256k1SignRpcInput(TypedDict, total=False):
    method: Required[Literal["secp256k1_sign"]]

    params: Required[EthereumSecp256k1SignRpcInputParamsParam]
    """Parameters for the EVM `secp256k1_sign` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class EthereumSign7702AuthorizationRpcInput(TypedDict, total=False):
    method: Required[Literal["eth_sign7702Authorization"]]

    params: Required[EthereumSign7702AuthorizationRpcInputParamsParam]
    """Parameters for the EVM `eth_sign7702Authorization` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class EthereumSignUserOperationRpcInput(TypedDict, total=False):
    method: Required[Literal["eth_signUserOperation"]]

    params: Required[EthereumSignUserOperationRpcInputParamsParam]
    """Parameters for the EVM `eth_signUserOperation` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class EthereumSendCallsRpcInput(TypedDict, total=False):
    caip2: Required[Caip2]
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    method: Required[Literal["wallet_sendCalls"]]

    params: Required[EthereumSendCallsRpcInputParamsParam]
    """Parameters for the `wallet_sendCalls` RPC."""

    address: str

    chain_type: Literal["ethereum"]

    experimental_data_suffix: Hex
    """
    A hex-encoded string prefixed with '0x', capped at 300002 characters (150,000
    bytes).
    """

    sponsor: bool

    sponsor_options: RpcSponsorOptionsParam
    """Options for user-pays gas sponsorship on the RPC endpoint.

    When provided alongside `sponsor: true`, controls which token asset the user
    pays gas with.
    """

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SolanaSignTransactionRpcInput(TypedDict, total=False):
    method: Required[Literal["signTransaction"]]

    params: Required[SolanaSignTransactionRpcInputParamsParam]
    """Parameters for the SVM `signTransaction` RPC."""

    address: str

    chain_type: Literal["solana"]

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SolanaSignAndSendTransactionRpcInput(TypedDict, total=False):
    caip2: Required[Caip2]
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    method: Required[Literal["signAndSendTransaction"]]

    params: Required[SolanaSignAndSendTransactionRpcInputParamsParam]
    """Parameters for the SVM `signAndSendTransaction` RPC."""

    address: str

    chain_type: Literal["solana"]

    optimistic_broadcast: bool

    reference_id: str

    sponsor: bool

    sponsor_options: RpcSponsorOptionsParam
    """Options for user-pays gas sponsorship on the RPC endpoint.

    When provided alongside `sponsor: true`, controls which token asset the user
    pays gas with.
    """

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SolanaSignMessageRpcInput(TypedDict, total=False):
    method: Required[Literal["signMessage"]]

    params: Required[SolanaSignMessageRpcInputParamsParam]
    """Parameters for the SVM `signMessage` RPC."""

    address: str

    chain_type: Literal["solana"]

    body_wallet_id: Annotated[str, PropertyInfo(alias="wallet_id")]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkTransferRpcInput(TypedDict, total=False):
    method: Required[Literal["transfer"]]

    params: Required[SparkTransferRpcInputParamsParam]
    """Parameters for the Spark `transfer` RPC."""

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkGetBalanceRpcInput(TypedDict, total=False):
    method: Required[Literal["getBalance"]]

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkTransferTokensRpcInput(TypedDict, total=False):
    method: Required[Literal["transferTokens"]]

    params: Required[SparkTransferTokensRpcInputParamsParam]
    """Parameters for the Spark `transferTokens` RPC."""

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkGetStaticDepositAddressRpcInput(TypedDict, total=False):
    method: Required[Literal["getStaticDepositAddress"]]

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkGetClaimStaticDepositQuoteRpcInput(TypedDict, total=False):
    method: Required[Literal["getClaimStaticDepositQuote"]]

    params: Required[SparkGetClaimStaticDepositQuoteRpcInputParamsParam]
    """Parameters for the Spark `getClaimStaticDepositQuote` RPC."""

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkClaimStaticDepositRpcInput(TypedDict, total=False):
    method: Required[Literal["claimStaticDeposit"]]

    params: Required[SparkClaimStaticDepositRpcInputParamsParam]
    """Parameters for the Spark `claimStaticDeposit` RPC."""

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkCreateLightningInvoiceRpcInput(TypedDict, total=False):
    method: Required[Literal["createLightningInvoice"]]

    params: Required[SparkCreateLightningInvoiceRpcInputParamsParam]
    """Parameters for the Spark `createLightningInvoice` RPC."""

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkPayLightningInvoiceRpcInput(TypedDict, total=False):
    method: Required[Literal["payLightningInvoice"]]

    params: Required[SparkPayLightningInvoiceRpcInputParamsParam]
    """Parameters for the Spark `payLightningInvoice` RPC."""

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkSignMessageWithIdentityKeyRpcInput(TypedDict, total=False):
    method: Required[Literal["signMessageWithIdentityKey"]]

    params: Required[SparkSignMessageWithIdentityKeyRpcInputParamsParam]
    """Parameters for the Spark `signMessageWithIdentityKey` RPC."""

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkWithdrawRpcInput(TypedDict, total=False):
    method: Required[Literal["withdraw"]]

    params: Required[SparkWithdrawRpcInputParamsParam]
    """Parameters for the Spark `withdraw` RPC."""

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class SparkGetWithdrawalFeeQuoteRpcInput(TypedDict, total=False):
    method: Required[Literal["getWithdrawalFeeQuote"]]

    params: Required[SparkGetWithdrawalFeeQuoteRpcInputParamsParam]
    """Parameters for the Spark `getWithdrawalFeeQuote` RPC."""

    network: SparkNetwork
    """The Spark network."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class TronSignTransactionRpcInput(TypedDict, total=False):
    method: Required[Literal["tron_signTransaction"]]

    params: Required[TronSignTransactionRpcInputParamsParam]
    """Parameters for the Tron `tron_signTransaction` RPC."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class TronSendTransactionRpcInput(TypedDict, total=False):
    method: Required[Literal["tron_sendTransaction"]]

    params: Required[TronSendTransactionRpcInputParamsParam]
    """Parameters for the Tron `tron_sendTransaction` RPC."""

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class ExportPrivateKeyRpcInput(TypedDict, total=False):
    address: Required[str]

    method: Required[Literal["exportPrivateKey"]]

    params: Required[PrivateKeyExportInputParam]
    """Input for exporting a wallet (private key or seed phrase) with HPKE encryption."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


class ExportSeedPhraseRpcInput(TypedDict, total=False):
    address: Required[str]

    method: Required[Literal["exportSeedPhrase"]]

    params: Required[SeedPhraseExportInputParam]
    """Input for exporting a wallet (private key or seed phrase) with HPKE encryption."""

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """


IntentRpcParams: TypeAlias = Union[
    EthereumSignTransactionRpcInput,
    EthereumSendTransactionRpcInput,
    EthereumPersonalSignRpcInput,
    EthereumSignTypedDataRpcInput,
    EthereumSecp256k1SignRpcInput,
    EthereumSign7702AuthorizationRpcInput,
    EthereumSignUserOperationRpcInput,
    EthereumSendCallsRpcInput,
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
    ExportPrivateKeyRpcInput,
    ExportSeedPhraseRpcInput,
]
