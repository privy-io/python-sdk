# Apps

Types:

```python
from privy.types import (
    AllowlistDeletionResponse,
    AllowlistEntry,
    AppAllowlistConfig,
    AppCustomOAuthProvider,
    AppResponse,
    Caip2,
    CaptchaProvider,
    Currency,
    CurrencyAsset,
    EmailDomain,
    EmailDomainInviteInput,
    EmailInviteInput,
    EmbeddedWalletChainConfig,
    EmbeddedWalletConfigSchema,
    EmbeddedWalletCreateOnLogin,
    EmbeddedWalletInputSchema,
    EmbeddedWalletMode,
    FundingConfigResponseSchema,
    FundingMethodEnum,
    FundingOption,
    GasSpendCurrency,
    GasSpendRequestBody,
    GasSpendResponseBody,
    MfaMethod,
    PhoneInviteInput,
    TelegramAuthConfigSchema,
    TestAccount,
    TestAccountsResponse,
    UserInviteInput,
    UserOwnedRecoveryOption,
    WalletInviteInput,
)
```

Methods:

- <code title="get /v1/apps/{app_id}">client.apps.<a href="./src/privy/resources/apps/apps.py">get</a>(app_id) -> <a href="./src/privy/types/app_response.py">AppResponse</a></code>
- <code title="get /v1/apps/gas_spend">client.apps.<a href="./src/privy/resources/apps/apps.py">get_gas_spend</a>(\*\*<a href="src/privy/types/app_get_gas_spend_params.py">params</a>) -> <a href="./src/privy/types/gas_spend_response_body.py">GasSpendResponseBody</a></code>
- <code title="get /v1/apps/{app_id}/test_credentials">client.apps.<a href="./src/privy/resources/apps/apps.py">get_test_credentials</a>(app_id) -> <a href="./src/privy/types/test_accounts_response.py">TestAccountsResponse</a></code>

## Allowlist

Types:

```python
from privy.types.apps import AllowlistListResponse
```

Methods:

- <code title="post /v1/apps/{app_id}/allowlist">client.apps.allowlist.<a href="./src/privy/resources/apps/allowlist.py">create</a>(app_id, \*\*<a href="src/privy/types/apps/allowlist_create_params.py">params</a>) -> <a href="./src/privy/types/allowlist_entry.py">AllowlistEntry</a></code>
- <code title="get /v1/apps/{app_id}/allowlist">client.apps.allowlist.<a href="./src/privy/resources/apps/allowlist.py">list</a>(app_id) -> <a href="./src/privy/types/apps/allowlist_list_response.py">AllowlistListResponse</a></code>
- <code title="delete /v1/apps/{app_id}/allowlist">client.apps.allowlist.<a href="./src/privy/resources/apps/allowlist.py">delete</a>(app_id, \*\*<a href="src/privy/types/apps/allowlist_delete_params.py">params</a>) -> <a href="./src/privy/types/allowlist_deletion_response.py">AllowlistDeletionResponse</a></code>

# Cards

Types:

```python
from privy.types import (
    CardIssuingBankAgreement,
    CardIssuingBankInfo,
    CardIssuingCancellationReason,
    CardIssuingCardResponse,
    CardIssuingCardStatus,
    CardIssuingCardholder,
    CardIssuingCardsResponse,
    CardIssuingConfig,
    CardIssuingConfigQueryParams,
    CardIssuingConfigResponse,
    CardIssuingCreateCardInput,
    CardIssuingCustomerBankTermsRequiredResponse,
    CardIssuingCustomerConsentsRequestBody,
    CardIssuingCustomerElectronicDisclosureRequiredResponse,
    CardIssuingCustomerErrorResponse,
    CardIssuingCustomerInput,
    CardIssuingCustomerKYCRequiredResponse,
    CardIssuingCustomerNotCreatedResponse,
    CardIssuingCustomerPendingResponse,
    CardIssuingCustomerProviderTermsRequiredResponse,
    CardIssuingCustomerReadyResponse,
    CardIssuingCustomerRejectedResponse,
    CardIssuingCustomerRejectionReason,
    CardIssuingCustomerResponse,
    CardIssuingCustomerUnderReviewResponse,
    CardIssuingDispute,
    CardIssuingDisputeStatus,
    CardIssuingEphemeralKey,
    CardIssuingEphemeralKeyRequestBody,
    CardIssuingEphemeralKeyResponse,
    CardIssuingListCardsInput,
    CardIssuingListTransactionsInput,
    CardIssuingMerchant,
    CardIssuingReplaceCardRequestBody,
    CardIssuingReplacementReason,
    CardIssuingStatementQueryParams,
    CardIssuingTransactionResponse,
    CardIssuingTransactionStatus,
    CardIssuingTransactionsResponse,
    CardIssuingUpdateCardInput,
)
```

# Intents

Types:

```python
from privy.types import (
    BaseActionResult,
    BaseIntentResponse,
    IntentAuthorization,
    IntentAuthorizationKeyMember,
    IntentAuthorizationKeyQuorum,
    IntentAuthorizationKeyQuorumMember,
    IntentAuthorizationMember,
    IntentAuthorizationUserMember,
    IntentAuthorizeInput,
    IntentCreationHeaders,
    IntentResponse,
    IntentStatus,
    IntentType,
    KeyQuorumIntentResponse,
    PolicyIntentRequestDetails,
    PolicyIntentResponse,
    RpcIntentRequestDetails,
    RpcIntentResponse,
    RuleDeleteIntentResponse,
    RuleIntentCreateRequestDetails,
    RuleIntentDeleteRequestBody,
    RuleIntentDeleteRequestDetails,
    RuleIntentRequestDetails,
    RuleIntentResponse,
    RuleIntentUpdateRequestDetails,
    RuleMutateIntentResponse,
    TransferIntentRequestDetails,
    TransferIntentResponse,
    WalletIntentResponse,
)
```

Methods:

- <code title="get /v1/intents">client.intents.<a href="./src/privy/resources/intents.py">list</a>(\*\*<a href="src/privy/types/intent_list_params.py">params</a>) -> <a href="./src/privy/types/intent_response.py">SyncCursor[IntentResponse]</a></code>
- <code title="post /v1/intents/policies/{policy_id}/rules">client.intents.<a href="./src/privy/resources/intents.py">create_policy_rule</a>(policy_id, \*\*<a href="src/privy/types/intent_create_policy_rule_params.py">params</a>) -> <a href="./src/privy/types/rule_mutate_intent_response.py">RuleMutateIntentResponse</a></code>
- <code title="delete /v1/intents/policies/{policy_id}/rules/{rule_id}">client.intents.<a href="./src/privy/resources/intents.py">delete_policy_rule</a>(rule_id, \*, policy_id) -> <a href="./src/privy/types/rule_delete_intent_response.py">RuleDeleteIntentResponse</a></code>
- <code title="get /v1/intents/{intent_id}">client.intents.<a href="./src/privy/resources/intents.py">get</a>(intent_id) -> <a href="./src/privy/types/intent_response.py">IntentResponse</a></code>
- <code title="post /v1/intents/{intent_id}/reject">client.intents.<a href="./src/privy/resources/intents.py">reject</a>(intent_id) -> <a href="./src/privy/types/intent_response.py">IntentResponse</a></code>
- <code title="post /v1/intents/wallets/{wallet_id}/rpc">client.intents.<a href="./src/privy/resources/intents.py">rpc</a>(path_wallet_id, \*\*<a href="src/privy/types/intent_rpc_params.py">params</a>) -> <a href="./src/privy/types/rpc_intent_response.py">RpcIntentResponse</a></code>
- <code title="post /v1/intents/wallets/{wallet_id}/transfer">client.intents.<a href="./src/privy/resources/intents.py">transfer</a>(wallet_id, \*\*<a href="src/privy/types/intent_transfer_params.py">params</a>) -> <a href="./src/privy/types/transfer_intent_response.py">TransferIntentResponse</a></code>
- <code title="patch /v1/intents/key_quorums/{key_quorum_id}">client.intents.<a href="./src/privy/resources/intents.py">update_key_quorum</a>(key_quorum_id, \*\*<a href="src/privy/types/intent_update_key_quorum_params.py">params</a>) -> <a href="./src/privy/types/key_quorum_intent_response.py">KeyQuorumIntentResponse</a></code>
- <code title="patch /v1/intents/policies/{policy_id}">client.intents.<a href="./src/privy/resources/intents.py">update_policy</a>(policy_id, \*\*<a href="src/privy/types/intent_update_policy_params.py">params</a>) -> <a href="./src/privy/types/policy_intent_response.py">PolicyIntentResponse</a></code>
- <code title="patch /v1/intents/policies/{policy_id}/rules/{rule_id}">client.intents.<a href="./src/privy/resources/intents.py">update_policy_rule</a>(rule_id, \*, policy_id, \*\*<a href="src/privy/types/intent_update_policy_rule_params.py">params</a>) -> <a href="./src/privy/types/rule_mutate_intent_response.py">RuleMutateIntentResponse</a></code>
- <code title="patch /v1/intents/wallets/{wallet_id}">client.intents.<a href="./src/privy/resources/intents.py">update_wallet</a>(wallet_id, \*\*<a href="src/privy/types/intent_update_wallet_params.py">params</a>) -> <a href="./src/privy/types/wallet_intent_response.py">WalletIntentResponse</a></code>

# KeyQuorums

Types:

```python
from privy.types import (
    AuthorizationKey,
    KeyQuorum,
    KeyQuorumAuthorizationHeaders,
    KeyQuorumCreateRequestBody,
    KeyQuorumUpdateRequestBody,
)
```

Methods:

- <code title="post /v1/key_quorums">client.key_quorums.<a href="./src/privy/resources/key_quorums.py">create</a>(\*\*<a href="src/privy/types/key_quorum_create_params.py">params</a>) -> <a href="./src/privy/types/key_quorum.py">KeyQuorum</a></code>
- <code title="delete /v1/key_quorums/{key_quorum_id}">client.key_quorums.<a href="./src/privy/resources/key_quorums.py">\_delete_key_quorum</a>(key_quorum_id) -> <a href="./src/privy/types/success_response.py">SuccessResponse</a></code>
- <code title="patch /v1/key_quorums/{key_quorum_id}">client.key_quorums.<a href="./src/privy/resources/key_quorums.py">\_update</a>(key_quorum_id, \*\*<a href="src/privy/types/key_quorum_update_params.py">params</a>) -> <a href="./src/privy/types/key_quorum.py">KeyQuorum</a></code>
- <code title="get /v1/key_quorums/{key_quorum_id}">client.key_quorums.<a href="./src/privy/resources/key_quorums.py">get</a>(key_quorum_id) -> <a href="./src/privy/types/key_quorum.py">KeyQuorum</a></code>

# Organizations

Types:

```python
from privy.types import (
    CreateOrganizationSecretResponse,
    Organization,
    OrganizationCreateRequestBody,
    OrganizationSecretIDInput,
    OrganizationSecretView,
    OrganizationSecretsListResponse,
    OrganizationUpdateRequestBody,
    OrganizationsListResponse,
    UpdateOrganizationSecretSigningKeyInput,
)
```

Methods:

- <code title="post /v1/organizations">client.organizations.<a href="./src/privy/resources/organizations/organizations.py">create</a>(\*\*<a href="src/privy/types/organization_create_params.py">params</a>) -> <a href="./src/privy/types/organization.py">Organization</a></code>
- <code title="patch /v1/organizations/{organization_id}">client.organizations.<a href="./src/privy/resources/organizations/organizations.py">update</a>(organization_id, \*\*<a href="src/privy/types/organization_update_params.py">params</a>) -> <a href="./src/privy/types/organization.py">Organization</a></code>
- <code title="get /v1/organizations">client.organizations.<a href="./src/privy/resources/organizations/organizations.py">list</a>(\*\*<a href="src/privy/types/organization_list_params.py">params</a>) -> <a href="./src/privy/types/organization.py">SyncCursor[Organization]</a></code>
- <code title="delete /v1/organizations/{organization_id}">client.organizations.<a href="./src/privy/resources/organizations/organizations.py">delete</a>(organization_id) -> None</code>
- <code title="get /v1/organizations/{organization_id}">client.organizations.<a href="./src/privy/resources/organizations/organizations.py">get</a>(organization_id) -> <a href="./src/privy/types/organization.py">Organization</a></code>

## ExternalFiatAccounts

Methods:

- <code title="post /v1/organizations/{organization_id}/external_fiat_accounts">client.organizations.external_fiat_accounts.<a href="./src/privy/resources/organizations/external_fiat_accounts.py">create</a>(organization_id, \*\*<a href="src/privy/types/organizations/external_fiat_account_create_params.py">params</a>) -> <a href="./src/privy/types/organization_external_fiat_account_response.py">OrganizationExternalFiatAccountResponse</a></code>
- <code title="get /v1/organizations/{organization_id}/external_fiat_accounts">client.organizations.external_fiat_accounts.<a href="./src/privy/resources/organizations/external_fiat_accounts.py">list</a>(organization_id, \*\*<a href="src/privy/types/organizations/external_fiat_account_list_params.py">params</a>) -> <a href="./src/privy/types/list_organization_external_fiat_accounts_response.py">ListOrganizationExternalFiatAccountsResponse</a></code>
- <code title="delete /v1/organizations/{organization_id}/external_fiat_accounts/{account_id}">client.organizations.external_fiat_accounts.<a href="./src/privy/resources/organizations/external_fiat_accounts.py">delete</a>(account_id, \*, organization_id) -> <a href="./src/privy/types/success_response.py">SuccessResponse</a></code>
- <code title="get /v1/organizations/{organization_id}/external_fiat_accounts/{account_id}">client.organizations.external_fiat_accounts.<a href="./src/privy/resources/organizations/external_fiat_accounts.py">get</a>(account_id, \*, organization_id) -> <a href="./src/privy/types/organization_external_fiat_account_response.py">OrganizationExternalFiatAccountResponse</a></code>

## KYB

Methods:

- <code title="get /v1/organizations/{organization_id}/kyb">client.organizations.kyb.<a href="./src/privy/resources/organizations/kyb.py">list</a>(organization_id) -> <a href="./src/privy/types/kyb_status_list_response.py">KYBStatusListResponse</a></code>
- <code title="post /v1/organizations/{organization_id}/kyb/links">client.organizations.kyb.<a href="./src/privy/resources/organizations/kyb.py">initiate_links</a>(organization_id, \*\*<a href="src/privy/types/organizations/kyb_initiate_links_params.py">params</a>) -> <a href="./src/privy/types/kyb_status_response.py">KYBStatusResponse</a></code>
- <code title="post /v1/organizations/{organization_id}/kyb/tos">client.organizations.kyb.<a href="./src/privy/resources/organizations/kyb.py">initiate_tos</a>(organization_id, \*\*<a href="src/privy/types/organizations/kyb_initiate_tos_params.py">params</a>) -> <a href="./src/privy/types/kyx_tos_response.py">KyxTosResponse</a></code>

# Policies

Types:

```python
from privy.types import (
    AbiParameter,
    AbiSchema,
    ActionRequestBodyCondition,
    AggregationCondition,
    ConditionOperator,
    ConditionSet,
    ConditionSetAuthorizationHeaders,
    ConditionSetItem,
    ConditionSetItemRequestParams,
    ConditionSetItemValueInput,
    ConditionSetItems,
    ConditionSetItemsRequestBody,
    ConditionSetItemsResponse,
    ConditionSetRequestBody,
    ConditionSetRequestParams,
    ConditionValue,
    Ethereum7702AuthorizationCondition,
    EthereumCalldataCondition,
    EthereumTransactionCondition,
    EthereumTransactionConditionField,
    EthereumTypedDataDomainCondition,
    EthereumTypedDataDomainConditionField,
    EthereumTypedDataMessageCondition,
    MessageSigningCondition,
    MessageSigningField,
    Policy,
    PolicyAction,
    PolicyAuthorizationHeaders,
    PolicyCondition,
    PolicyMethod,
    PolicyRequestBody,
    PolicyRuleRequestBody,
    PolicyRuleRequestParams,
    PolicyRuleResponse,
    SolanaProgramInstructionCondition,
    SolanaSystemProgramInstructionCondition,
    SolanaSystemProgramInstructionConditionField,
    SolanaTokenProgramInstructionCondition,
    SolanaTokenProgramInstructionConditionField,
    SuiTransactionCommandCondition,
    SuiTransactionCommandOperator,
    SuiTransferObjectsCommandCondition,
    SuiTransferObjectsCommandField,
    SystemCondition,
    TempoTransactionCondition,
    TempoTransactionConditionField,
    TronCalldataCondition,
    TronTransactionCondition,
    TronTransactionConditionField,
    TypedDataInput,
    UpdateConditionSetRequestBody,
    XrplTransactionCondition,
    XrplTransactionConditionField,
)
```

Methods:

- <code title="post /v1/policies">client.policies.<a href="./src/privy/resources/policies.py">create</a>(\*\*<a href="src/privy/types/policy_create_params.py">params</a>) -> <a href="./src/privy/types/policy.py">Policy</a></code>
- <code title="post /v1/policies/{policy_id}/rules">client.policies.<a href="./src/privy/resources/policies.py">\_create_rule</a>(policy_id, \*\*<a href="src/privy/types/policy_create_rule_params.py">params</a>) -> <a href="./src/privy/types/policy_rule_response.py">PolicyRuleResponse</a></code>
- <code title="delete /v1/policies/{policy_id}">client.policies.<a href="./src/privy/resources/policies.py">\_delete_policy</a>(policy_id) -> <a href="./src/privy/types/success_response.py">SuccessResponse</a></code>
- <code title="delete /v1/policies/{policy_id}/rules/{rule_id}">client.policies.<a href="./src/privy/resources/policies.py">\_delete_rule</a>(rule_id, \*, policy_id) -> <a href="./src/privy/types/success_response.py">SuccessResponse</a></code>
- <code title="patch /v1/policies/{policy_id}">client.policies.<a href="./src/privy/resources/policies.py">\_update</a>(policy_id, \*\*<a href="src/privy/types/policy_update_params.py">params</a>) -> <a href="./src/privy/types/policy.py">Policy</a></code>
- <code title="patch /v1/policies/{policy_id}/rules/{rule_id}">client.policies.<a href="./src/privy/resources/policies.py">\_update_rule</a>(rule_id, \*, policy_id, \*\*<a href="src/privy/types/policy_update_rule_params.py">params</a>) -> <a href="./src/privy/types/policy_rule_response.py">PolicyRuleResponse</a></code>
- <code title="get /v1/policies/{policy_id}">client.policies.<a href="./src/privy/resources/policies.py">get</a>(policy_id) -> <a href="./src/privy/types/policy.py">Policy</a></code>
- <code title="get /v1/policies/{policy_id}/rules/{rule_id}">client.policies.<a href="./src/privy/resources/policies.py">get_rule</a>(rule_id, \*, policy_id) -> <a href="./src/privy/types/policy_rule_response.py">PolicyRuleResponse</a></code>

# Transactions

Types:

```python
from privy.types import (
    BlockchainTransactionStatus,
    Transaction,
    TransactionList,
    TransactionScanningAssetDiff,
    TransactionScanningAssetInfo,
    TransactionScanningAssetValue,
    TransactionScanningCalldata,
    TransactionScanningExposure,
    TransactionScanningMetadata,
    TransactionScanningParams,
    TransactionScanningRequestBody,
    TransactionScanningResponseBody,
    TransactionScanningRpcRequest,
    TransactionScanningSimulationErrorResult,
    TransactionScanningSimulationResult,
    TransactionScanningSimulationSuccessResult,
    TransactionScanningValidationErrorResult,
    TransactionScanningValidationResult,
    TransactionScanningValidationSuccessResult,
)
```

Methods:

- <code title="get /v1/transactions/{transaction_id}">client.transactions.<a href="./src/privy/resources/transactions.py">get</a>(transaction_id) -> <a href="./src/privy/types/transaction.py">Transaction</a></code>

# Users

Types:

```python
from privy.types import (
    AuthenticatedUser,
    ClientSessionUpdateAction,
    CrossAppEmbeddedWallet,
    CrossAppSmartWallet,
    CustomMetadata,
    EmailMfaMethod,
    EmbeddedWalletRecoveryMethod,
    LinkedAccount,
    LinkedAccountAppleInput,
    LinkedAccountAppleOAuth,
    LinkedAccountAuthorizationKey,
    LinkedAccountBaseWallet,
    LinkedAccountBaseWalletType,
    LinkedAccountBitcoinSegwitEmbeddedWallet,
    LinkedAccountBitcoinTaprootEmbeddedWallet,
    LinkedAccountCrossApp,
    LinkedAccountCurveSigningEmbeddedWallet,
    LinkedAccountCustomJwtInput,
    LinkedAccountCustomJwt,
    LinkedAccountCustomOAuth,
    LinkedAccountDiscordInput,
    LinkedAccountDiscordOAuth,
    LinkedAccountEmail,
    LinkedAccountEmailInput,
    LinkedAccountEmbeddedWallet,
    LinkedAccountEmbeddedWalletWithID,
    LinkedAccountEthereum,
    LinkedAccountEthereumEmbeddedWallet,
    LinkedAccountFarcaster,
    LinkedAccountFarcasterInput,
    LinkedAccountGitHubInput,
    LinkedAccountGitHubOAuth,
    LinkedAccountGoogleInput,
    LinkedAccountGoogleOAuth,
    LinkedAccountInput,
    LinkedAccountInstagramInput,
    LinkedAccountInstagramOAuth,
    LinkedAccountLineInput,
    LinkedAccountLineOAuth,
    LinkedAccountLinkedInInput,
    LinkedAccountLinkedInOAuth,
    LinkedAccountPasskey,
    LinkedAccountPasskeyCredentialDeviceType,
    LinkedAccountPasskeyInput,
    LinkedAccountPhone,
    LinkedAccountPhoneInput,
    LinkedAccountSmartWallet,
    LinkedAccountSolana,
    LinkedAccountSolanaEmbeddedWallet,
    LinkedAccountSpotifyInput,
    LinkedAccountSpotifyOAuth,
    LinkedAccountTelegram,
    LinkedAccountTelegramInput,
    LinkedAccountTiktokInput,
    LinkedAccountTiktokOAuth,
    LinkedAccountTwitchInput,
    LinkedAccountTwitchOAuth,
    LinkedAccountTwitterInput,
    LinkedAccountTwitterOAuth,
    LinkedAccountType,
    LinkedAccountWalletInput,
    LinkedMfaMethod,
    OAuthTokens,
    PasskeyMfaMethod,
    PatchUsersCustomMetadata,
    SMSMfaMethod,
    TotpMfaMethod,
    User,
    UserBatchCreateInput,
    UserWithIdentityToken,
)
```

Methods:

- <code title="post /v1/users">client.users.<a href="./src/privy/resources/users/users.py">create</a>(\*\*<a href="src/privy/types/user_create_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="get /v1/users">client.users.<a href="./src/privy/resources/users/users.py">list</a>(\*\*<a href="src/privy/types/user_list_params.py">params</a>) -> <a href="./src/privy/types/user.py">SyncCursor[User]</a></code>
- <code title="delete /v1/users/{user_id}">client.users.<a href="./src/privy/resources/users/users.py">delete</a>(user_id) -> None</code>
- <code title="get /v1/users/{user_id}">client.users.<a href="./src/privy/resources/users/users.py">get</a>(user_id) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/custom_auth/id">client.users.<a href="./src/privy/resources/users/users.py">get_by_custom_auth_id</a>(\*\*<a href="src/privy/types/user_get_by_custom_auth_id_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/discord/username">client.users.<a href="./src/privy/resources/users/users.py">get_by_discord_username</a>(\*\*<a href="src/privy/types/user_get_by_discord_username_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/email/address">client.users.<a href="./src/privy/resources/users/users.py">get_by_email_address</a>(\*\*<a href="src/privy/types/user_get_by_email_address_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/farcaster/fid">client.users.<a href="./src/privy/resources/users/users.py">get_by_farcaster_id</a>(\*\*<a href="src/privy/types/user_get_by_farcaster_id_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/github/username">client.users.<a href="./src/privy/resources/users/users.py">get_by_github_username</a>(\*\*<a href="src/privy/types/user_get_by_github_username_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/phone/number">client.users.<a href="./src/privy/resources/users/users.py">get_by_phone_number</a>(\*\*<a href="src/privy/types/user_get_by_phone_number_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/smart_wallet/address">client.users.<a href="./src/privy/resources/users/users.py">get_by_smart_wallet_address</a>(\*\*<a href="src/privy/types/user_get_by_smart_wallet_address_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/telegram/telegram_user_id">client.users.<a href="./src/privy/resources/users/users.py">get_by_telegram_user_id</a>(\*\*<a href="src/privy/types/user_get_by_telegram_user_id_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/telegram/username">client.users.<a href="./src/privy/resources/users/users.py">get_by_telegram_username</a>(\*\*<a href="src/privy/types/user_get_by_telegram_username_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/twitter/subject">client.users.<a href="./src/privy/resources/users/users.py">get_by_twitter_subject</a>(\*\*<a href="src/privy/types/user_get_by_twitter_subject_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/twitter/username">client.users.<a href="./src/privy/resources/users/users.py">get_by_twitter_username</a>(\*\*<a href="src/privy/types/user_get_by_twitter_username_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/wallet/address">client.users.<a href="./src/privy/resources/users/users.py">get_by_wallet_address</a>(\*\*<a href="src/privy/types/user_get_by_wallet_address_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/{user_id}/wallets">client.users.<a href="./src/privy/resources/users/users.py">pregenerate_wallets</a>(user_id, \*\*<a href="src/privy/types/user_pregenerate_wallets_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/search">client.users.<a href="./src/privy/resources/users/users.py">search</a>(\*\*<a href="src/privy/types/user_search_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/{user_id}/custom_metadata">client.users.<a href="./src/privy/resources/users/users.py">set_custom_metadata</a>(user_id, \*\*<a href="src/privy/types/user_set_custom_metadata_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/{user_id}/accounts/unlink">client.users.<a href="./src/privy/resources/users/users.py">unlink_linked_account</a>(user_id, \*\*<a href="src/privy/types/user_unlink_linked_account_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>

## ExternalFiatAccounts

Methods:

- <code title="post /v1/users/{user_id}/external_fiat_accounts">client.users.external_fiat_accounts.<a href="./src/privy/resources/users/external_fiat_accounts.py">create</a>(user_id, \*\*<a href="src/privy/types/users/external_fiat_account_create_params.py">params</a>) -> <a href="./src/privy/types/external_fiat_account_response.py">ExternalFiatAccountResponse</a></code>
- <code title="get /v1/users/{user_id}/external_fiat_accounts">client.users.external_fiat_accounts.<a href="./src/privy/resources/users/external_fiat_accounts.py">list</a>(user_id, \*\*<a href="src/privy/types/users/external_fiat_account_list_params.py">params</a>) -> <a href="./src/privy/types/list_external_fiat_accounts_response.py">ListExternalFiatAccountsResponse</a></code>
- <code title="delete /v1/users/{user_id}/external_fiat_accounts/{account_id}">client.users.external_fiat_accounts.<a href="./src/privy/resources/users/external_fiat_accounts.py">delete</a>(account_id, \*, user_id) -> <a href="./src/privy/types/success_response.py">SuccessResponse</a></code>
- <code title="get /v1/users/{user_id}/external_fiat_accounts/{account_id}">client.users.external_fiat_accounts.<a href="./src/privy/resources/users/external_fiat_accounts.py">get</a>(account_id, \*, user_id) -> <a href="./src/privy/types/external_fiat_account_response.py">ExternalFiatAccountResponse</a></code>

## KYC

Methods:

- <code title="get /v1/users/{user_id}/kyc">client.users.kyc.<a href="./src/privy/resources/users/kyc.py">list</a>(user_id) -> <a href="./src/privy/types/kyc_status_list_response.py">KYCStatusListResponse</a></code>
- <code title="post /v1/users/{user_id}/kyc/links">client.users.kyc.<a href="./src/privy/resources/users/kyc.py">initiate_links</a>(user_id, \*\*<a href="src/privy/types/users/kyc_initiate_links_params.py">params</a>) -> <a href="./src/privy/types/kyc_status_response.py">KYCStatusResponse</a></code>
- <code title="post /v1/users/{user_id}/kyc/tos">client.users.kyc.<a href="./src/privy/resources/users/kyc.py">initiate_tos</a>(user_id, \*\*<a href="src/privy/types/users/kyc_initiate_tos_params.py">params</a>) -> <a href="./src/privy/types/kyx_tos_response.py">KyxTosResponse</a></code>

# Wallets

Types:

```python
from privy.types import (
    AccessListEntry,
    AdditionalSignerInput,
    AdditionalSignerItemInput,
    Address,
    AdvancedSwapPlatformFee,
    AdvancedSwapRequestBody,
    AdvancedSwapResponse,
    AmountType,
    AptosBcsHex,
    AptosRpcInput,
    AptosRpcResponse,
    AptosSignTransactionRpcInput,
    AptosSignTransactionRpcInputParams,
    AptosSignTransactionRpcResponse,
    AptosSignTransactionRpcResponseData,
    AptosSignedTransactionBcsHex,
    AttachWalletAutomationRequestBody,
    AuthorizationKeyDashboardResponse,
    AuthorizationKeyResponse,
    AuthorizationKeyRole,
    CreateCryptoDepositAccountRequestBody,
    CreateCryptoDepositAccountResponse,
    CreateCryptoDepositAccountWithConfigRequestBody,
    CreateCryptoDepositAccountWithRouteRequestBody,
    CryptoDepositAddressRoute,
    CryptoDepositAsset,
    CryptoDepositAssetFilter,
    CryptoDepositAssetFilterAll,
    CryptoDepositAssetFilterExclude,
    CryptoDepositAssetFilterInclude,
    CurveSigningChainType,
    CurveType,
    CustodialWallet,
    CustodialWalletChainType,
    CustodialWalletCreateInput,
    CustodialWalletProvider,
    CustomTokenTransferSource,
    DetachWalletAutomationRequestBody,
    DeveloperFee,
    EncryptedAuthorizationKey,
    EncryptedBoundAuthenticateResponse,
    EncryptedWalletAuthenticateResponse,
    EntityID,
    EthereumPersonalSignRpcInput,
    EthereumPersonalSignRpcInputParams,
    EthereumPersonalSignRpcResponse,
    EthereumPersonalSignRpcResponseData,
    EthereumRpcInput,
    EthereumRpcResponse,
    EthereumSecp256k1SignRpcInput,
    EthereumSecp256k1SignRpcInputParams,
    EthereumSecp256k1SignRpcResponse,
    EthereumSecp256k1SignRpcResponseData,
    EthereumSendCallsCall,
    EthereumSendCallsRpcInput,
    EthereumSendCallsRpcInputParams,
    EthereumSendCallsRpcResponse,
    EthereumSendCallsRpcResponseData,
    EthereumSendTransactionRpcInput,
    EthereumSendTransactionRpcInputParams,
    EthereumSendTransactionRpcResponse,
    EthereumSendTransactionRpcResponseData,
    EthereumSign7702Authorization,
    EthereumSign7702AuthorizationRpcInput,
    EthereumSign7702AuthorizationRpcInputParams,
    EthereumSign7702AuthorizationRpcResponse,
    EthereumSign7702AuthorizationRpcResponseData,
    EthereumSignTransactionRpcInput,
    EthereumSignTransactionRpcInputParams,
    EthereumSignTransactionRpcResponse,
    EthereumSignTransactionRpcResponseData,
    EthereumSignTypedDataRpcInput,
    EthereumSignTypedDataRpcInputParams,
    EthereumSignTypedDataRpcResponse,
    EthereumSignTypedDataRpcResponseData,
    EthereumSignUserOperationRpcInput,
    EthereumSignUserOperationRpcInputParams,
    EthereumSignUserOperationRpcResponse,
    EthereumSignUserOperationRpcResponseData,
    EthereumTypedDataInput,
    ExportPrivateKeyRpcInput,
    ExportPrivateKeyRpcResponse,
    ExportSeedPhraseRpcInput,
    ExportSeedPhraseRpcResponse,
    ExportType,
    ExtendedChainType,
    FeeConfiguration,
    FeeLineItem,
    FirstClassChainType,
    Gas,
    GetByWalletAddressRequestBody,
    HDInitInput,
    HDPath,
    HDSubmitInput,
    HpkeAeadAlgorithm,
    HpkeEncryption,
    HpkeImportConfig,
    Hex,
    IntentBinding,
    NamedTokenTransferSource,
    NearRpcRequestBody,
    NearRpcResponse,
    NearSignTransactionRpcRequestBody,
    NearSignTransactionRpcRequestBodyParams,
    NearSignTransactionRpcResponse,
    NearSignTransactionRpcResponseData,
    NearSignedTransactionBorshBase64,
    NearUnsignedTransactionBorshBase64,
    OutputWithPreviousTransactionData,
    PolicyInput,
    PrivateKeyExportInput,
    PrivateKeyExportResponse,
    PrivateKeyInitInput,
    PrivateKeySubmitInput,
    PrivyFee,
    Quantity,
    RawBoundAuthenticateResponse,
    RawSignBytesEncoding,
    RawSignBytesHashFunction,
    RawSignBytesParams,
    RawSignHashParams,
    RawSignInput,
    RawSignInputParams,
    RawSignResponse,
    RawSignResponseData,
    RawWalletAuthenticateResponse,
    RecipientPublicKey,
    RelayerFee,
    RpcSponsorAsset,
    RpcSponsorOptions,
    SeedPhraseExportInput,
    SeedPhraseExportResponse,
    SignatureOptions,
    SignatureType,
    SigningAlgorithm,
    SolanaRpcInput,
    SolanaRpcResponse,
    SolanaSignAndSendTransactionRpcInput,
    SolanaSignAndSendTransactionRpcInputParams,
    SolanaSignAndSendTransactionRpcResponse,
    SolanaSignAndSendTransactionRpcResponseData,
    SolanaSignMessageRpcInput,
    SolanaSignMessageRpcInputParams,
    SolanaSignMessageRpcResponse,
    SolanaSignMessageRpcResponseData,
    SolanaSignTransactionRpcInput,
    SolanaSignTransactionRpcInputParams,
    SolanaSignTransactionRpcResponse,
    SolanaSignTransactionRpcResponseData,
    SolanaWalletDerivationStrategy,
    SparkBalance,
    SparkClaimStaticDepositRpcInput,
    SparkClaimStaticDepositRpcInputParams,
    SparkClaimStaticDepositRpcResponse,
    SparkClaimStaticDepositRpcResponseData,
    SparkCoopExitFeeQuote,
    SparkCoopExitRequest,
    SparkCreateLightningInvoiceRpcInput,
    SparkCreateLightningInvoiceRpcInputParams,
    SparkCreateLightningInvoiceRpcResponse,
    SparkCurrencyAmount,
    SparkExitSpeed,
    SparkGetBalanceRpcInput,
    SparkGetBalanceRpcResponse,
    SparkGetClaimStaticDepositQuoteRpcInput,
    SparkGetClaimStaticDepositQuoteRpcInputParams,
    SparkGetClaimStaticDepositQuoteRpcResponse,
    SparkGetClaimStaticDepositQuoteRpcResponseData,
    SparkGetStaticDepositAddressRpcInput,
    SparkGetStaticDepositAddressRpcResponse,
    SparkGetStaticDepositAddressRpcResponseData,
    SparkGetWithdrawalFeeQuoteRpcInput,
    SparkGetWithdrawalFeeQuoteRpcInputParams,
    SparkGetWithdrawalFeeQuoteRpcResponse,
    SparkLightningFee,
    SparkLightningReceiveRequest,
    SparkLightningSendRequest,
    SparkNetwork,
    SparkOutputSelectionStrategy,
    SparkPayLightningInvoiceRpcInput,
    SparkPayLightningInvoiceRpcInputParams,
    SparkPayLightningInvoiceRpcResponse,
    SparkRpcInput,
    SparkRpcResponse,
    SparkSignMessageWithIdentityKeyRpcInput,
    SparkSignMessageWithIdentityKeyRpcInputParams,
    SparkSignMessageWithIdentityKeyRpcResponse,
    SparkSignMessageWithIdentityKeyRpcResponseData,
    SparkSigningKeyshare,
    SparkTokenBalance,
    SparkTransfer,
    SparkTransferLeaf,
    SparkTransferRpcInput,
    SparkTransferRpcInputParams,
    SparkTransferRpcResponse,
    SparkTransferTokensRpcInput,
    SparkTransferTokensRpcInputParams,
    SparkTransferTokensRpcResponse,
    SparkTransferTokensRpcResponseData,
    SparkUserTokenMetadata,
    SparkWalletLeaf,
    SparkWithdrawRpcInput,
    SparkWithdrawRpcInputParams,
    SparkWithdrawRpcResponse,
    SuiCommandName,
    SwapSubmissionStatus,
    TempoAaAuthorization,
    TempoCall,
    TempoFeePayerSignature,
    TokenOutput,
    TokenTransferDestination,
    TokenTransferSource,
    TotalFeeConfigurationBps,
    TransactionChainNameInput,
    TransactionDetail,
    TransactionTokenAddressInput,
    TransferQuoteRequestBody,
    TransferQuoteResponse,
    TransferReceivedTransactionDetail,
    TransferRequestBody,
    TransferSentTransactionDetail,
    TronContract,
    TronRawDataForSend,
    TronRawDataForSign,
    TronRpcInput,
    TronRpcResponse,
    TronSendTransactionRpcInput,
    TronSendTransactionRpcInputParams,
    TronSendTransactionRpcResponse,
    TronSendTransactionRpcResponseData,
    TronSignTransactionRpcInput,
    TronSignTransactionRpcInputParams,
    TronSignTransactionRpcResponse,
    TronSignTransactionRpcResponseData,
    TronTransferContract,
    TronTriggerSmartContract,
    TypedDataDomainInputParams,
    TypedDataTypeFieldInput,
    TypedDataTypesInputParams,
    UnsignedEthereumTransaction,
    UnsignedStandardEthereumTransaction,
    UnsignedTempoTransaction,
    UserOperationInput,
    UserSigningKeyBinding,
    Wallet,
    WalletActionNonce,
    WalletAdditionalSigner,
    WalletAdditionalSignerItem,
    WalletAPIRegisterAuthorizationKeyInput,
    WalletAPIRevokeAuthorizationKeyInput,
    WalletAsset,
    WalletAssetChainNameInput,
    WalletAuthenticateBoundEncryptedRequestBody,
    WalletAuthenticateBoundRequestBody,
    WalletAuthenticateBoundUnencryptedRequestBody,
    WalletAuthenticateIntentsResponse,
    WalletAuthenticateRequestBody,
    WalletAuthenticateWithJwtResponse,
    WalletAuthorizationHeaders,
    WalletAutomationAttachmentListResponse,
    WalletAutomationAttachmentResponse,
    WalletBatchCreateInput,
    WalletBatchCreateResponse,
    WalletBatchCreateResult,
    WalletBatchItemInput,
    WalletChainType,
    WalletCreateWalletsWithRecoveryResponse,
    WalletCustodian,
    WalletEntity,
    WalletEntityAssignmentRequestBody,
    WalletEntityAssignmentResponse,
    WalletEntityType,
    WalletEntropyType,
    WalletEthereumAsset,
    WalletExportRequestBody,
    WalletExportResponseBody,
    WalletImportInitResponse,
    WalletImportSupportedChains,
    WalletImportSupportedEntropyTypes,
    WalletRevokeResponse,
    WalletRpcRequestBody,
    WalletRpcResponse,
    WalletSolanaAsset,
    WalletTronAsset,
    WalletUpdateRequestBody,
    XrplRpcInput,
    XrplRpcResponse,
    XrplSignTransactionRpcInput,
    XrplSignTransactionRpcInputParams,
    XrplSignTransactionRpcResponse,
    XrplSignTransactionRpcResponseData,
    WalletInitImportResponse,
)
```

Methods:

- <code title="post /v1/wallets">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">create</a>(\*\*<a href="src/privy/types/wallet_create_params.py">params</a>) -> <a href="./src/privy/types/wallet.py">Wallet</a></code>
- <code title="get /v1/wallets">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">list</a>(\*\*<a href="src/privy/types/wallet_list_params.py">params</a>) -> <a href="./src/privy/types/wallet.py">SyncCursor[Wallet]</a></code>
- <code title="post /v1/wallets/{wallet_id}/export">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">\_export</a>(wallet_id, \*\*<a href="src/privy/types/wallet_export_params.py">params</a>) -> <a href="./src/privy/types/wallet_export_response_body.py">WalletExportResponseBody</a></code>
- <code title="post /v1/wallets/import/init">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">\_init_import</a>(\*\*<a href="src/privy/types/wallet_init_import_params.py">params</a>) -> <a href="./src/privy/types/wallet_init_import_response.py">WalletInitImportResponse</a></code>
- <code title="post /v1/wallets/{wallet_id}/raw_sign">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">\_raw_sign</a>(wallet_id, \*\*<a href="src/privy/types/wallet_raw_sign_params.py">params</a>) -> <a href="./src/privy/types/raw_sign_response.py">RawSignResponse</a></code>
- <code title="post /v1/wallets/{wallet_id}/rpc">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">\_rpc</a>(path_wallet_id, \*\*<a href="src/privy/types/wallet_rpc_params.py">params</a>) -> <a href="./src/privy/types/wallet_rpc_response.py">WalletRpcResponse</a></code>
- <code title="post /v1/wallets/import/submit">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">\_submit_import</a>(\*\*<a href="src/privy/types/wallet_submit_import_params.py">params</a>) -> <a href="./src/privy/types/wallet.py">Wallet</a></code>
- <code title="post /v1/wallets/{wallet_id}/transfer">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">\_transfer</a>(wallet_id, \*\*<a href="src/privy/types/wallet_transfer_params.py">params</a>) -> <a href="./src/privy/types/wallets/transfer_action_response.py">TransferActionResponse</a></code>
- <code title="patch /v1/wallets/{wallet_id}">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">\_update</a>(wallet_id, \*\*<a href="src/privy/types/wallet_update_params.py">params</a>) -> <a href="./src/privy/types/wallet.py">Wallet</a></code>
- <code title="post /v1/wallets/{wallet_id}/archive">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">archive</a>(wallet_id) -> <a href="./src/privy/types/wallet.py">Wallet</a></code>
- <code title="post /v1/wallets/{wallet_id}/entity">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">assign_entity</a>(wallet_id, \*\*<a href="src/privy/types/wallet_assign_entity_params.py">params</a>) -> <a href="./src/privy/types/wallet_entity_assignment_response.py">WalletEntityAssignmentResponse</a></code>
- <code title="post /v1/wallets/authenticate">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">authenticate_with_jwt</a>(\*\*<a href="src/privy/types/wallet_authenticate_with_jwt_params.py">params</a>) -> <a href="./src/privy/types/wallet_authenticate_with_jwt_response.py">WalletAuthenticateWithJwtResponse</a></code>
- <code title="post /v1/wallets/batch">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">create_batch</a>(\*\*<a href="src/privy/types/wallet_create_batch_params.py">params</a>) -> <a href="./src/privy/types/wallet_batch_create_response.py">WalletBatchCreateResponse</a></code>
- <code title="post /v1/wallets_with_recovery">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">create_wallets_with_recovery</a>(\*\*<a href="src/privy/types/wallet_create_wallets_with_recovery_params.py">params</a>) -> <a href="./src/privy/types/wallet_create_wallets_with_recovery_response.py">WalletCreateWalletsWithRecoveryResponse</a></code>
- <code title="get /v1/wallets/{wallet_id}">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">get</a>(wallet_id, \*\*<a href="src/privy/types/wallet_get_params.py">params</a>) -> <a href="./src/privy/types/wallet.py">Wallet</a></code>
- <code title="post /v1/wallets/address">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">get_wallet_by_address</a>(\*\*<a href="src/privy/types/wallet_get_wallet_by_address_params.py">params</a>) -> <a href="./src/privy/types/wallet.py">Wallet</a></code>

## Actions

Types:

```python
from privy.types.wallets import (
    AaveVaultDetails,
    CustodianTransactionWalletActionStep,
    CustodianTransactionWalletActionStepStatus,
    EvmTransactionWalletActionStep,
    EvmUserOperationEntrypointVersion,
    EvmUserOperationWalletActionStep,
    EvmWalletActionStepStatus,
    EarnAsset,
    EarnDepositActionResponse,
    EarnDepositRequestBody,
    EarnFeeCollectActionResponse,
    EarnFeeCollectRequestBody,
    EarnIncentiveClaimActionResponse,
    EarnIncentiveClaimRequestBody,
    EarnIncentiveRewardEntry,
    EarnIncentiveRewardsQuery,
    EarnIncentiveRewardsResponse,
    EarnIncetiveClaimRewardEntry,
    EarnWithdrawActionResponse,
    EarnWithdrawRequestBody,
    EthereumEarnPositionQuery,
    EthereumEarnPositionResponse,
    EthereumEarnProvider,
    EthereumEarnVaultDetailsResponse,
    ExternalTransactionWalletActionStep,
    ExternalTransactionWalletActionStepStatus,
    FailureReason,
    ListWalletActionsQuery,
    ListWalletActionsResponse,
    MorphoVaultDetails,
    PayoutResponse,
    SvmTransactionWalletActionStep,
    SvmWalletActionStepStatus,
    SwapActionResponse,
    TvmTransactionWalletActionStep,
    TvmWalletActionStepStatus,
    TempoVaultDetails,
    TransferActionResponse,
    VedaVaultDetails,
    WalletActionInclude,
    WalletActionResponse,
    WalletActionStatus,
    WalletActionStep,
    WalletActionStepType,
    WalletActionType,
)
```

Methods:

- <code title="get /v1/wallets/{wallet_id}/actions/{action_id}">client.wallets.actions.<a href="./src/privy/resources/wallets/actions.py">get</a>(action_id, \*, wallet_id, \*\*<a href="src/privy/types/wallets/action_get_params.py">params</a>) -> <a href="./src/privy/types/wallets/wallet_action_response.py">WalletActionResponse</a></code>

## Balance

Types:

```python
from privy.types.wallets import BalanceGetResponse
```

Methods:

- <code title="get /v1/wallets/{wallet_id}/balance">client.wallets.balance.<a href="./src/privy/resources/wallets/balance.py">get</a>(wallet_id, \*\*<a href="src/privy/types/wallets/balance_get_params.py">params</a>) -> <a href="./src/privy/types/wallets/balance_get_response.py">BalanceGetResponse</a></code>

## DepositAccounts

### Crypto

Methods:

- <code title="post /v1/wallets/{wallet_id}/deposit_accounts/crypto">client.wallets.deposit_accounts.crypto.<a href="./src/privy/resources/wallets/deposit_accounts/crypto.py">\_create</a>(wallet_id, \*\*<a href="src/privy/types/wallets/deposit_accounts/crypto_create_params.py">params</a>) -> <a href="./src/privy/types/create_crypto_deposit_account_response.py">CreateCryptoDepositAccountResponse</a></code>

### Fiat

Methods:

- <code title="post /v1/wallets/{wallet_id}/deposit_accounts/fiat">client.wallets.deposit_accounts.fiat.<a href="./src/privy/resources/wallets/deposit_accounts/fiat.py">create</a>(wallet_id, \*\*<a href="src/privy/types/wallets/deposit_accounts/fiat_create_params.py">params</a>) -> <a href="./src/privy/types/fiat_deposit_account_response.py">FiatDepositAccountResponse</a></code>
- <code title="get /v1/wallets/{wallet_id}/deposit_accounts/fiat">client.wallets.deposit_accounts.fiat.<a href="./src/privy/resources/wallets/deposit_accounts/fiat.py">list</a>(wallet_id, \*\*<a href="src/privy/types/wallets/deposit_accounts/fiat_list_params.py">params</a>) -> <a href="./src/privy/types/list_fiat_deposit_accounts_response.py">ListFiatDepositAccountsResponse</a></code>
- <code title="get /v1/wallets/{wallet_id}/deposit_accounts/fiat/{deposit_account_id}">client.wallets.deposit_accounts.fiat.<a href="./src/privy/resources/wallets/deposit_accounts/fiat.py">get</a>(deposit_account_id, \*, wallet_id) -> <a href="./src/privy/types/fiat_deposit_account_response.py">FiatDepositAccountResponse</a></code>

## Earn

### Ethereum

Methods:

- <code title="post /v1/wallets/{wallet_id}/earn/ethereum/deposit">client.wallets.earn.ethereum.<a href="./src/privy/resources/wallets/earn/ethereum/ethereum.py">\_deposit</a>(wallet_id, \*\*<a href="src/privy/types/wallets/earn/ethereum_deposit_params.py">params</a>) -> <a href="./src/privy/types/wallets/earn_deposit_action_response.py">EarnDepositActionResponse</a></code>
- <code title="post /v1/wallets/{wallet_id}/earn/ethereum/withdraw">client.wallets.earn.ethereum.<a href="./src/privy/resources/wallets/earn/ethereum/ethereum.py">\_withdraw</a>(wallet_id, \*\*<a href="src/privy/types/wallets/earn/ethereum_withdraw_params.py">params</a>) -> <a href="./src/privy/types/wallets/earn_withdraw_action_response.py">EarnWithdrawActionResponse</a></code>
- <code title="get /v1/earn/ethereum/vaults/{vault_id}">client.wallets.earn.ethereum.<a href="./src/privy/resources/wallets/earn/ethereum/ethereum.py">vault_details</a>(vault_id) -> <a href="./src/privy/types/wallets/ethereum_earn_vault_details_response.py">EthereumEarnVaultDetailsResponse</a></code>
- <code title="get /v1/wallets/{wallet_id}/earn/ethereum/vaults">client.wallets.earn.ethereum.<a href="./src/privy/resources/wallets/earn/ethereum/ethereum.py">vault_position</a>(wallet_id, \*\*<a href="src/privy/types/wallets/earn/ethereum_vault_position_params.py">params</a>) -> <a href="./src/privy/types/wallets/ethereum_earn_position_response.py">EthereumEarnPositionResponse</a></code>

#### Incentive

Methods:

- <code title="post /v1/wallets/{wallet_id}/earn/ethereum/incentive/claim">client.wallets.earn.ethereum.incentive.<a href="./src/privy/resources/wallets/earn/ethereum/incentive.py">\_claim</a>(wallet_id, \*\*<a href="src/privy/types/wallets/earn/ethereum/incentive_claim_params.py">params</a>) -> <a href="./src/privy/types/wallets/earn_incentive_claim_action_response.py">EarnIncentiveClaimActionResponse</a></code>

## Swap

Methods:

- <code title="post /v1/wallets/{wallet_id}/swap">client.wallets.swap.<a href="./src/privy/resources/wallets/swap.py">execute</a>(wallet_id, \*\*<a href="src/privy/types/wallets/swap_execute_params.py">params</a>) -> <a href="./src/privy/types/wallets/swap_action_response.py">SwapActionResponse</a></code>
- <code title="post /v1/wallets/{wallet_id}/swap/quote">client.wallets.swap.<a href="./src/privy/resources/wallets/swap.py">quote</a>(wallet_id, \*\*<a href="src/privy/types/wallets/swap_quote_params.py">params</a>) -> <a href="./src/privy/types/swap_quote_response.py">SwapQuoteResponse</a></code>

## Transactions

Types:

```python
from privy.types.wallets import TransactionGetResponse
```

Methods:

- <code title="get /v1/wallets/{wallet_id}/transactions">client.wallets.transactions.<a href="./src/privy/resources/wallets/transactions.py">get</a>(wallet_id, \*\*<a href="src/privy/types/wallets/transaction_get_params.py">params</a>) -> <a href="./src/privy/types/wallets/transaction_get_response.py">TransactionGetResponse</a></code>

# Webhooks

Types:

```python
from privy.types import (
    BlockInfo,
    BridgeCryptoDepositMetadata,
    BridgeCryptoTransferMetadata,
    BridgeFiatDepositMetadata,
    BridgeFiatTransferMetadata,
    BridgeMetadata,
    BridgeRefundMetadata,
    BridgeStaticMemoDepositMetadata,
    BridgeTransferRefundMetadata,
    DepositCompletedData,
    DepositCompletedDestination,
    DepositFailedData,
    DepositStartedData,
    DepositStartedDestination,
    DepositStartedSource,
    FiatDepositCurrency,
    FundsDepositedWebhookPayload,
    FundsWithdrawnWebhookPayload,
    IntentAuthorizedWebhookPayload,
    IntentCreatedWebhookPayload,
    IntentExecutedWebhookPayload,
    IntentFailedWebhookPayload,
    IntentRejectedWebhookPayload,
    KrakenEmbedCustomOrderCancelledWebhookPayload,
    KrakenEmbedCustomOrderExecutedWebhookPayload,
    KrakenEmbedCustomOrderExecutionFailedWebhookPayload,
    KrakenEmbedQuoteCancelledWebhookPayload,
    KrakenEmbedQuoteExecutedWebhookPayload,
    KrakenEmbedQuoteExecutionFailedWebhookPayload,
    KrakenEmbedUserClosedWebhookPayload,
    KrakenEmbedUserDisabledWebhookPayload,
    KrakenEmbedUserVerifiedWebhookPayload,
    MfaDisabledWebhookPayload,
    MfaEnabledWebhookPayload,
    OrganizationKYBUpdatedData,
    OrganizationKYBUpdatedKYBData,
    OrganizationKYBUpdatedTosData,
    PrivateKeyExportWebhookPayload,
    SeedPhraseExportWebhookPayload,
    TransactionBroadcastedWebhookPayload,
    TransactionConfirmedWebhookPayload,
    TransactionExecutionRevertedWebhookPayload,
    TransactionFailedWebhookPayload,
    TransactionProviderErrorWebhookPayload,
    TransactionReplacedWebhookPayload,
    TransactionStillPendingWebhookPayload,
    UsageCrossChainFeeRecordedWebhookPayload,
    UsageGasSponsorshipRecordedWebhookPayload,
    UsageSourceType,
    UserAuthenticatedWebhookPayload,
    UserCreatedWebhookPayload,
    UserDeletedWebhookPayload,
    UserKYCUpdatedData,
    UserKYCUpdatedKYCData,
    UserKYCUpdatedTosData,
    UserLinkedAccountWebhookPayload,
    UserOperationCompletedWebhookPayload,
    UserReference,
    UserTransferredAccountWebhookPayload,
    UserUnlinkedAccountWebhookPayload,
    UserUpdatedAccountWebhookPayload,
    UserWalletCreatedWebhookPayload,
    WalletActionEarnDepositCreatedWebhookPayload,
    WalletActionEarnDepositFailedWebhookPayload,
    WalletActionEarnDepositRejectedWebhookPayload,
    WalletActionEarnDepositSucceededWebhookPayload,
    WalletActionEarnFeeCollectCreatedWebhookPayload,
    WalletActionEarnFeeCollectFailedWebhookPayload,
    WalletActionEarnFeeCollectRejectedWebhookPayload,
    WalletActionEarnFeeCollectSucceededWebhookPayload,
    WalletActionEarnIncentiveClaimCreatedWebhookPayload,
    WalletActionEarnIncentiveClaimFailedWebhookPayload,
    WalletActionEarnIncentiveClaimRejectedWebhookPayload,
    WalletActionEarnIncentiveClaimSucceededWebhookPayload,
    WalletActionEarnWithdrawCreatedWebhookPayload,
    WalletActionEarnWithdrawFailedWebhookPayload,
    WalletActionEarnWithdrawRejectedWebhookPayload,
    WalletActionEarnWithdrawSucceededWebhookPayload,
    WalletActionPayoutCreatedWebhookPayload,
    WalletActionPayoutFailedWebhookPayload,
    WalletActionPayoutRejectedWebhookPayload,
    WalletActionPayoutSucceededWebhookPayload,
    WalletActionSwapCreatedWebhookPayload,
    WalletActionSwapFailedWebhookPayload,
    WalletActionSwapRejectedWebhookPayload,
    WalletActionSwapSucceededWebhookPayload,
    WalletActionTransferCreatedWebhookPayload,
    WalletActionTransferFailedWebhookPayload,
    WalletActionTransferRejectedWebhookPayload,
    WalletActionTransferSucceededWebhookPayload,
    WalletArchivedWebhookPayload,
    WalletAutomationSubmittedWebhookPayload,
    WalletFundsAsset,
    WalletFundsErc20Asset,
    WalletFundsNativeTokenAsset,
    WalletFundsSacAsset,
    WalletFundsSplAsset,
    WalletFundsTrc20Asset,
    WalletRecoveredWebhookPayload,
    WalletRecoverySetupMethod,
    WalletRecoverySetupWebhookPayload,
    WalletRestoredWebhookPayload,
    WebhookPayload,
    YieldClaimConfirmedWebhookPayload,
    YieldClaimReward,
    YieldDepositConfirmedWebhookPayload,
    YieldWithdrawConfirmedWebhookPayload,
    OrganizationKYBUpdatedWebhookEvent,
    UserKYCUpdatedWebhookEvent,
    WalletDepositAccountDepositCompletedWebhookEvent,
    WalletDepositAccountDepositFailedWebhookEvent,
    WalletDepositAccountDepositStartedWebhookEvent,
    UnsafeUnwrapWebhookEvent,
)
```

# Accounts

Types:

```python
from privy.types import (
    AccountBalanceParams,
    AccountBalanceResponse,
    AccountDisplayName,
    AccountResponse,
    AccountWallet,
    AccountWalletConfigurationItem,
    AccountWalletIDs,
    AccountWalletsConfiguration,
    AccountsDashboardListResponse,
    AccountsListResponse,
    AssetAccountWithBalance,
    BalanceAsset,
    BalanceAssetByChain,
    BalanceResponse,
    ChainTestnetMode,
    CreateAccountFromWalletIDsInput,
    CreateAccountFromWalletsConfigurationInput,
    CreateAccountInput,
    UpdateAccountFromWalletIDsInput,
    UpdateAccountFromWalletsConfigurationInput,
    UpdateAccountInput,
)
```

# Aggregations

Types:

```python
from privy.types import (
    Aggregation,
    AggregationGroupBy,
    AggregationInput,
    AggregationMethod,
    AggregationMetric,
    AggregationWindow,
    RollingAggregationWindow,
)
```

# EmbeddedWallets

Types:

```python
from privy.types import (
    AlchemyPaymasterContext,
    EmbeddedWalletCreationInput,
    ICloudClientType,
    OAuthAuthenticateRecoveryResponse,
    OAuthCallbackICloudExpoInput,
    OAuthInitICloudRecoveryInput,
    OAuthInitRecoveryInput,
    RecoveryConfigurationICloudInput,
    RecoveryConfigurationICloudResponse,
    RecoveryKeyMaterialInput,
    RecoveryKeyMaterialResponse,
    RecoveryType,
    SmartWalletConfiguration,
    SmartWalletConfigurationDisabled,
    SmartWalletConfigurationEnabled,
    SmartWalletConfigurationInput,
    SmartWalletConfigurationInputEnabled,
    SmartWalletNetworkConfiguration,
    SmartWalletNetworkConfigurationInput,
    SmartWalletType,
    WalletCreationAdditionalSignerItem,
    WalletCreationInput,
)
```

# Analytics

Types:

```python
from privy.types import AnalyticsEventInput
```

# ClientAuth

Types:

```python
from privy.types import (
    AuthenticateJwtInput,
    AuthenticateMode,
    AuthenticateModeOption,
    AuthenticateSiweInput,
    AuthenticateSiwsInput,
    BridgeBrlFiatVirtualAccountDepositInstructions,
    BridgeDestinationAsset,
    BridgeEurFiatVirtualAccountDepositInstructions,
    BridgeFiatVirtualAccountDepositInstructions,
    BridgeFiatVirtualAccountDestination,
    BridgeFiatVirtualAccountRequest,
    BridgeFiatVirtualAccountResponse,
    BridgeFiatVirtualAccountSource,
    BridgeGbpFiatVirtualAccountDepositInstructions,
    BridgeMxnFiatVirtualAccountDepositInstructions,
    BridgeOnrampProvider,
    BridgeSandboxFiatVirtualAccountRequest,
    BridgeSandboxFiatVirtualAccountResponse,
    BridgeSourceAsset,
    BridgeUsdFiatVirtualAccountDepositInstructions,
    BridgeUsdFiatVirtualAccountDepositPaymentRail,
    CustomJwtAuthenticateRequestBody,
    CustomJwtLinkRequestBody,
    CustomOAuthProviderID,
    DeviceVerifyAction,
    DeviceVerifyRequestBody,
    DeviceVerifyResponse,
    ExternalOAuthProviderID,
    FarcasterAuthenticateInput,
    FarcasterAuthenticateRequestBody,
    FarcasterConnectInitResponse,
    FarcasterConnectInitResponseBody,
    FarcasterConnectStatusCompletedResponse,
    FarcasterConnectStatusCompletedResponseBody,
    FarcasterConnectStatusPendingResponse,
    FarcasterConnectStatusPendingResponseBody,
    FarcasterInitInput,
    FarcasterInitRequestBody,
    FarcasterLinkInput,
    FarcasterLinkRequestBody,
    FarcasterSignerApproved,
    FarcasterSignerInitPendingApproval,
    FarcasterSignerInitRequestBody,
    FarcasterSignerInitResponseBody,
    FarcasterSignerRevoked,
    FarcasterSignerStatusPendingApproval,
    FarcasterSignerStatusResponseBody,
    FarcasterUnlinkInput,
    FarcasterUnlinkRequestBody,
    FarcasterV2AuthenticateInput,
    FarcasterV2AuthenticateRequestBody,
    FarcasterV2InitInput,
    FarcasterV2InitRequestBody,
    FarcasterV2InitResponse,
    FarcasterV2InitResponseBody,
    FiatVirtualAccountRequest,
    FiatVirtualAccountResponse,
    GuestAuthenticateRequestBody,
    LinkJwtInput,
    MfaEmailEnrollRequestBody,
    MfaEmailInitEnrollInput,
    MfaEmailInitRequestBody,
    MfaEmailInitVerifyInput,
    MfaEmailVerifyRequestBody,
    MfaPasskeyEnrollmentRequestBody,
    MfaPasskeyInitRequestBody,
    MfaPasskeyInitResponseBody,
    MfaPasskeyVerifyRequestBody,
    MfaSMSEnrollRequestBody,
    MfaSMSInitEnrollInput,
    MfaSMSInitRequestBody,
    MfaSMSInitVerifyInput,
    MfaSMSVerifyRequestBody,
    MfaTotpInitResponseBody,
    MfaTotpInput,
    MfaVerifyResponseBody,
    OAuthAuthenticateRequestBody,
    OAuthAuthorizationCodeRequestBody,
    OAuthCodeType,
    OAuthInitRequestBody,
    OAuthInitResponseBody,
    OAuthLinkRequestBody,
    OAuthLinkResponseBody,
    OAuthProviderID,
    OAuthTokenAuthorizationCodeRequestBody,
    OAuthTokenDeviceCodePendingError,
    OAuthTokenDeviceCodePendingErrorCode,
    OAuthTokenDeviceCodeRequestBody,
    OAuthTokenGrantType,
    OAuthTokenRefreshTokenRequestBody,
    OAuthTokenRequestBody,
    OAuthTokenSuccessResponse,
    OAuthTransferNativeSDKRequestBody,
    OAuthTransferRequestBody,
    OAuthTransferUserInfo,
    OAuthTransferUserInfoMeta,
    OAuthTransferWebSDKRequestBody,
    OAuthUnlinkRequestBody,
    OAuthVerifyRequestBody,
    OAuthVerifyResponseBody,
    OnrampProvider,
    OptionalRefreshTokenInput,
    PasskeyAssertionResponse,
    PasskeyAttestationResponse,
    PasskeyAuthenticateInput,
    PasskeyAuthenticatorEnrollmentOptions,
    PasskeyAuthenticatorEnrollmentResponse,
    PasskeyAuthenticatorSelection,
    PasskeyAuthenticatorVerifyOptions,
    PasskeyAuthenticatorVerifyResponse,
    PasskeyClientExtensionResults,
    PasskeyCredPropsResult,
    PasskeyCredentialDescriptor,
    PasskeyEnrollmentExtensions,
    PasskeyInitInput,
    PasskeyLinkInput,
    PasskeyPubKeyCredParam,
    PasskeyRegisterInput,
    PasskeyRelyingParty,
    PasskeyUser,
    PasskeyVerifyExtensions,
    PasswordlessAuthenticateRequestBody,
    PasswordlessInitRequestBody,
    PasswordlessLinkRequestBody,
    PasswordlessSMSAuthenticateRequestBody,
    PasswordlessSMSInitRequestBody,
    PasswordlessSMSLinkRequestBody,
    PasswordlessSMSTransferRequestBody,
    PasswordlessSMSUnlinkRequestBody,
    PasswordlessSMSUpdateRequestBody,
    PasswordlessTransferRequestBody,
    PasswordlessUnlinkRequestBody,
    PasswordlessUpdateRequestBody,
    PrivyOAuthProviderID,
    ResponsePasskeyInitAuthenticate,
    ResponsePasskeyInitLink,
    ResponsePasskeyInitRegister,
    SiweAddressInput,
    SiweAuthenticateRequestBody,
    SiweInitInput,
    SiweInitRequestBody,
    SiweInitResponseBody,
    SiweInput,
    SiweLinkRequestBody,
    SiweLinkSmartWalletRequestBody,
    SiweNonce,
    SiweUnlinkRequestBody,
    SiwsAddressInput,
    SiwsAuthenticateRequestBody,
    SiwsInitInput,
    SiwsInitRequestBody,
    SiwsInitResponseBody,
    SiwsInput,
    SiwsLinkRequestBody,
    SiwsMessageType,
    SiwsNonce,
    SiwsUnlinkRequestBody,
    SmartWalletSiweInput,
    TelegramAuthResult,
    TelegramAuthenticateInput,
    TelegramAuthenticateRequestBody,
    TelegramLinkRequestBody,
    TelegramUnlinkInput,
    TelegramUnlinkRequestBody,
    TelegramWebAppData,
    TransferFarcasterInput,
    TransferSiweInput,
    TransferSiwsInput,
    TransferTelegramInput,
    UnlinkPasskeyInput,
)
```

# WalletAutomations

Types:

```python
from privy.types import (
    AutomationActionConfig,
    AutomationActionConfigInput,
    AutomationAssetFilter,
    AutomationAssetFilterAll,
    AutomationAssetFilterExclude,
    AutomationAssetFilterInclude,
    AutomationAssetFilterInput,
    AutomationAssetFilterInputExclude,
    AutomationAssetFilterInputInclude,
    AutomationAssetSpec,
    AutomationAssetSpecInput,
    AutomationConfig,
    AutomationConfigInput,
    AutomationDepositTriggerConfig,
    AutomationDepositTriggerConfigInput,
    AutomationDestinationAsset,
    AutomationDestinationAssetInput,
    AutomationEarnDepositActionConfig,
    AutomationEarnDepositActionConfigInput,
    AutomationSwapActionConfig,
    AutomationSwapActionConfigInput,
    AutomationTriggerConfig,
    AutomationTriggerConfigInput,
    CreateAutomationRequestBody,
    SwapAttachmentParams,
    UpdateAutomationRequestBody,
    WalletAutomationExecutionListResponse,
    WalletAutomationExecutionResponse,
    WalletAutomationExecutionStatus,
    WalletAutomationListResponse,
    WalletAutomationResponse,
    WalletAutomationStatus,
    WalletAutomationSuccessResponse,
)
```

# Shared

Types:

```python
from privy.types import (
    BitcoinAddress,
    CurrencyAmount,
    Environment,
    EvmAddress,
    EvmChecksumAddress,
    HyperliquidTokenAddress,
    KeyQuorumID,
    OrchestrationProvider,
    OwnerIDInput,
    OwnerInput,
    OwnerInputPublicKey,
    OwnerInputUser,
    P256PublicKey,
    SolanaAddress,
    SuccessResponse,
    TokenIdentifier,
    TronAddress,
    TronHexAddress,
)
```

# Fiat

Types:

```python
from privy.types import (
    BridgeCreateExternalFiatAccountRequestBody,
    BridgeCreateFiatDepositAccountRequestBody,
    BridgeExternalFiatAccount,
    BridgeFiatDepositAccount,
    BridgeOrganizationExternalFiatAccount,
    CreateExternalFiatAccountRequestBody,
    CreateFiatDepositAccountRequestBody,
    CreateFiatDepositAccountSource,
    CreatePayoutRequestBody,
    ExternalFiatAccount,
    ExternalFiatAccountAddress,
    ExternalFiatAccountData,
    ExternalFiatAccountGBData,
    ExternalFiatAccountIbanData,
    ExternalFiatAccountPixData,
    ExternalFiatAccountResponse,
    ExternalFiatAccountSwiftCategory,
    ExternalFiatAccountSwiftData,
    ExternalFiatAccountSwiftPurposeOfFunds,
    ExternalFiatAccountUsData,
    FiatCurrency,
    FiatDepositAccount,
    FiatDepositAccountDestination,
    FiatDepositAccountResponse,
    FiatDepositAccountSource,
    FiatDepositAccountStatus,
    FiatDepositInstructions,
    FiatPaymentRail,
    KYBLinksRequestBody,
    KYBStatusListResponse,
    KYBStatusResponse,
    KYBTosRequestBody,
    KYCIdentifyingDocument,
    KYCLinksRequestBody,
    KYCResidentialAddress,
    KYCStatusListResponse,
    KYCStatusResponse,
    KYCSubmitData,
    KYCSubmitRequestBody,
    KyxCapabilities,
    KyxCapabilityStatus,
    KyxEndorsement,
    KyxEndorsementName,
    KyxEndorsementStatus,
    KyxEnvironment,
    KyxProvider,
    KyxProviderStatus,
    KyxTosRequestBody,
    KyxTosResponse,
    KyxTosStatus,
    KyxTosStatusDetail,
    KyxVerificationStatus,
    KyxVerificationStatusDetail,
    ListExternalFiatAccountsResponse,
    ListFiatDepositAccountsResponse,
    ListOrganizationExternalFiatAccountsResponse,
    OfframpDepositInstructions,
    OfframpResponse,
    OnrampAsset,
    OnrampChain,
    OnrampDepositInstructions,
    OnrampKYCResponse,
    OnrampKYCStatus,
    OnrampResponse,
    OnrampTransferStatus,
    OrganizationExternalFiatAccount,
    OrganizationExternalFiatAccountResponse,
    PayoutDestination,
    PayoutSource,
)
```

# Onramps

Types:

```python
from privy.types import (
    BridgeFiatCustomerResponse,
    BridgeFiatRejectionReason,
    BridgeSandboxFiatCustomerResponse,
    Caip2ChainID,
    CreateLinkAuthIntentInput,
    CreateLinkAuthIntentResponse,
    CreateOrUpdateFiatCustomerRequestInput,
    CreateStripeOnrampSessionInput,
    CreateStripeOnrampSessionResponse,
    ExchangeStripeTokensInput,
    ExchangeStripeTokensResponse,
    FiatAmount,
    FiatCurrencyCode,
    FiatCustomerResponse,
    FiatOnrampDestination,
    FiatOnrampEnvironment,
    FiatOnrampProvider,
    FiatOnrampProviderError,
    FiatOnrampQuote,
    FiatOnrampSource,
    FiatOnrampStripeSDKSessionResponse,
    FiatOnrampTransactionStatus,
    FiatOnrampURLSessionResponse,
    GetFiatCustomerRequestInput,
    GetFiatOnrampQuotesInput,
    GetFiatOnrampQuotesResponse,
    GetFiatOnrampTransactionStatusInput,
    GetFiatOnrampTransactionStatusResponse,
    GetFiatOnrampURLInput,
    GetFiatOnrampURLResponse,
    GetStripeCryptoCustomerResponse,
    GetStripeOnrampTransactionLimitsQueryParams,
    GetStripeOnrampTransactionLimitsResponse,
    LinkAuthIntentCreated,
    LinkAuthIntentNoAccount,
    ListStripeConsumerWalletsResponse,
    ListStripePaymentTokensResponse,
    OnrampSessionParams,
    OnrampSessionTransactionDetails,
    RefreshStripeQuoteResponse,
    StripeConsumerWallet,
    StripeCryptoCustomerActive,
    StripeCryptoCustomerExpired,
    StripeCryptoCustomerNone,
    StripeKYCRegion,
    StripeKYCTier,
    StripeOnrampCheckoutResponse,
    StripeOnrampSessionStatus,
    StripeOnrampTransactionLimit,
    StripePaymentToken,
    StripeTransactionDetails,
    StripeVerification,
)
```

# Funding

Types:

```python
from privy.types import (
    CoinbaseBlockchain,
    CoinbaseEthereumAsset,
    CoinbaseOnRampEthereumAddress,
    CoinbaseOnRampInitEthereumInput,
    CoinbaseOnRampInitInput,
    CoinbaseOnRampInitResponse,
    CoinbaseOnRampInitSolanaInput,
    CoinbaseOnRampSolanaAddress,
    CoinbaseOnRampStatus,
    CoinbaseOnRampStatusResponse,
    CoinbaseSolanaAsset,
    MoonpayCurrencyCode,
    MoonpayFiatOnRampEthereumConfig,
    MoonpayFiatOnRampEthereumInput,
    MoonpayFiatOnRampSolanaConfig,
    MoonpayFiatOnRampSolanaInput,
    MoonpayOnRampSandboxConfig,
    MoonpayOnRampSignInput,
    MoonpayOnRampSignResponse,
    MoonpayPaymentMethod,
    MoonpaySolanaCurrencyCode,
    MoonpayUiConfig,
    MoonpayUiTheme,
)
```

# CrossApp

Types:

```python
from privy.types import CrossAppConnection, CrossAppConnectionsResponse
```

# OAuth

Types:

```python
from privy.types import (
    DeviceAuthorizationResponse,
    OAuthGrant,
    OAuthGrantListResponse,
    OAuthGrantRevokeResponse,
)
```

# Yield

Types:

```python
from privy.types import (
    EthereumVaultDetailsInput,
    EthereumVaultDetailsResponse,
    EthereumVaultPosition,
    EthereumVaultResponse,
    EthereumYieldClaimIDInput,
    EthereumYieldClaimInput,
    EthereumYieldClaimResponse,
    EthereumYieldClaimReward,
    EthereumYieldDepositInput,
    EthereumYieldPositionResponse,
    EthereumYieldPositionsInput,
    EthereumYieldProvider,
    EthereumYieldSweepIDInput,
    EthereumYieldSweepResponse,
    EthereumYieldSweepStatus,
    EthereumYieldSweepType,
    EthereumYieldWithdrawInput,
    EvmCaip2ChainID,
    VaultAsset,
    YieldAuthorizationHeaders,
)
```

# KrakenEmbed

Types:

```python
from privy.types import (
    KrakenEmbedAssetSortOption,
    KrakenEmbedCancelCustomOrderInput,
    KrakenEmbedCancelCustomOrderPath,
    KrakenEmbedCancelCustomOrderResponse,
    KrakenEmbedCancelCustomOrderResult,
    KrakenEmbedCountryCode,
    KrakenEmbedCreateCustomOrderInput,
    KrakenEmbedCreateCustomOrderResponse,
    KrakenEmbedCreateCustomOrderResult,
    KrakenEmbedCurrentDayPnl,
    KrakenEmbedCustomOrder,
    KrakenEmbedCustomOrderAction,
    KrakenEmbedCustomOrderAmount,
    KrakenEmbedCustomOrderOccurrence,
    KrakenEmbedCustomOrderOccurrenceExecutedAction,
    KrakenEmbedCustomOrderOccurrenceStatus,
    KrakenEmbedCustomOrderOccurrenceTrigger,
    KrakenEmbedCustomOrderOccurrenceTriggerType,
    KrakenEmbedCustomOrderQuoteAsset,
    KrakenEmbedCustomOrderStatus,
    KrakenEmbedCustomOrderStatusValue,
    KrakenEmbedCustomOrderTrigger,
    KrakenEmbedCustomOrderTriggerCondition,
    KrakenEmbedEarnAmount,
    KrakenEmbedEarnAprEstimate,
    KrakenEmbedEarnAsset,
    KrakenEmbedEarnUserAllocation,
    KrakenEmbedFullName,
    KrakenEmbedGetAssetListQueryParamsSchema,
    KrakenEmbedGetCustomOrderHistoryQueryParams,
    KrakenEmbedGetCustomOrderHistoryResponse,
    KrakenEmbedGetCustomOrderHistoryResult,
    KrakenEmbedGetCustomOrderQueryParams,
    KrakenEmbedGetCustomOrderResponse,
    KrakenEmbedGetCustomOrderResult,
    KrakenEmbedGetEarnAssetsKrakenResponse,
    KrakenEmbedGetEarnAssetsQueryParams,
    KrakenEmbedGetEarnAssetsResponse,
    KrakenEmbedGetEarnAssetsResult,
    KrakenEmbedGetEarnSummaryKrakenResponse,
    KrakenEmbedGetEarnSummaryQueryParams,
    KrakenEmbedGetEarnSummaryResponse,
    KrakenEmbedGetEarnSummaryResult,
    KrakenEmbedGetPortfolioDetailsQueryParamsSchema,
    KrakenEmbedGetPortfolioSummaryQueryParams,
    KrakenEmbedGetPortfolioSummaryResponse,
    KrakenEmbedGetPortfolioSummaryResult,
    KrakenEmbedGetPortfolioTransactionsQueryParamsSchema,
    KrakenEmbedGetQuoteQueryParams,
    KrakenEmbedIdentityDocumentType,
    KrakenEmbedIncludeCurrentDayPnlQueryParam,
    KrakenEmbedListCustomOrdersQueryParams,
    KrakenEmbedListCustomOrdersResponse,
    KrakenEmbedListCustomOrdersResult,
    KrakenEmbedPortfolioSummaryPayload,
    KrakenEmbedPortfolioTransactionRefID,
    KrakenEmbedPortfolioTransactionRefIDType,
    KrakenEmbedQuoteType,
    KrakenEmbedResidence,
    KrakenEmbedResidenceDocumentType,
    KrakenEmbedSortingOrder,
    KrakenEmbedStartAddressMetadata,
    KrakenEmbedStartAddressVerificationURLInput,
    KrakenEmbedStartIdentityInfo,
    KrakenEmbedStartIdentityMetadata,
    KrakenEmbedStartIdentityVerificationURLInput,
    KrakenEmbedStartLivenessVerificationURLInput,
    KrakenEmbedStartVerificationDebug,
    KrakenEmbedStartVerificationURLInput,
    KrakenEmbedStartVerificationURLResponse,
    KrakenEmbedStartVerificationURLResult,
    KrakenEmbedToggleAutoEarnKrakenResponse,
    KrakenEmbedToggleAutoEarnQueryParams,
    KrakenEmbedToggleAutoEarnResponse,
    KrakenEmbedTransactionStatus,
    KrakenEmbedTransactionType,
    KrakenEmbedUpcomingReward,
)
```

# Actions

Types:

```python
from privy.types import ListActions
```

# Swaps

Types:

```python
from privy.types import (
    SwapDestination,
    SwapQuoteDestination,
    SwapQuoteRequestBody,
    SwapQuoteResponse,
    SwapRequestBody,
    SwapSource,
)
```
