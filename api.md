# Wallets

Types:

```python
from privy.types import (
    Wallet,
    WalletAuthenticateWithJwtResponse,
    WalletCreateWalletsWithRecoveryResponse,
    WalletRpcResponse,
)
```

Methods:

- <code title="post /v1/wallets">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">create</a>(\*\*<a href="src/privy/types/wallet_create_params.py">params</a>) -> <a href="./src/privy/types/wallet.py">Wallet</a></code>
- <code title="patch /v1/wallets/{wallet_id}">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">update</a>(wallet_id, \*\*<a href="src/privy/types/wallet_update_params.py">params</a>) -> <a href="./src/privy/types/wallet.py">Wallet</a></code>
- <code title="get /v1/wallets">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">list</a>(\*\*<a href="src/privy/types/wallet_list_params.py">params</a>) -> <a href="./src/privy/types/wallet.py">SyncCursor[Wallet]</a></code>
- <code title="post /v1/user_signers/authenticate">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">authenticate_with_jwt</a>(\*\*<a href="src/privy/types/wallet_authenticate_with_jwt_params.py">params</a>) -> <a href="./src/privy/types/wallet_authenticate_with_jwt_response.py">WalletAuthenticateWithJwtResponse</a></code>
- <code title="post /v1/wallets_with_recovery">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">create_wallets_with_recovery</a>(\*\*<a href="src/privy/types/wallet_create_wallets_with_recovery_params.py">params</a>) -> <a href="./src/privy/types/wallet_create_wallets_with_recovery_response.py">WalletCreateWalletsWithRecoveryResponse</a></code>
- <code title="get /v1/wallets/{wallet_id}">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">get</a>(wallet_id) -> <a href="./src/privy/types/wallet.py">Wallet</a></code>
- <code title="post /v1/wallets/{wallet_id}/rpc">client.wallets.<a href="./src/privy/resources/wallets/wallets.py">rpc</a>(wallet_id, \*\*<a href="src/privy/types/wallet_rpc_params.py">params</a>) -> <a href="./src/privy/types/wallet_rpc_response.py">WalletRpcResponse</a></code>

## Transactions

Types:

```python
from privy.types.wallets import TransactionGetResponse
```

Methods:

- <code title="get /v1/wallets/{wallet_id}/transactions">client.wallets.transactions.<a href="./src/privy/resources/wallets/transactions.py">get</a>(wallet_id, \*\*<a href="src/privy/types/wallets/transaction_get_params.py">params</a>) -> <a href="./src/privy/types/wallets/transaction_get_response.py">TransactionGetResponse</a></code>

## Balance

Types:

```python
from privy.types.wallets import BalanceGetResponse
```

Methods:

- <code title="get /v1/wallets/{wallet_id}/balance">client.wallets.balance.<a href="./src/privy/resources/wallets/balance.py">get</a>(wallet_id, \*\*<a href="src/privy/types/wallets/balance_get_params.py">params</a>) -> <a href="./src/privy/types/wallets/balance_get_response.py">BalanceGetResponse</a></code>

# Users

Types:

```python
from privy.types import User, UserCreateCustomMetadataResponse
```

Methods:

- <code title="post /v1/users">client.users.<a href="./src/privy/resources/users.py">create</a>(\*\*<a href="src/privy/types/user_create_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="get /v1/users">client.users.<a href="./src/privy/resources/users.py">list</a>(\*\*<a href="src/privy/types/user_list_params.py">params</a>) -> <a href="./src/privy/types/user.py">SyncCursor[User]</a></code>
- <code title="delete /v1/users/{user_id}">client.users.<a href="./src/privy/resources/users.py">delete</a>(user_id) -> None</code>
- <code title="post /v1/users/{user_id}/custom_metadata">client.users.<a href="./src/privy/resources/users.py">create_custom_metadata</a>(user_id) -> <a href="./src/privy/types/user_create_custom_metadata_response.py">UserCreateCustomMetadataResponse</a></code>
- <code title="get /v1/users/{user_id}">client.users.<a href="./src/privy/resources/users.py">get</a>(user_id) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/email/address">client.users.<a href="./src/privy/resources/users.py">get_by_email_address</a>(\*\*<a href="src/privy/types/user_get_by_email_address_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/custom_auth/id">client.users.<a href="./src/privy/resources/users.py">get_by_jwt_subject_id</a>(\*\*<a href="src/privy/types/user_get_by_jwt_subject_id_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>
- <code title="post /v1/users/wallet/address">client.users.<a href="./src/privy/resources/users.py">get_by_wallet_address</a>(\*\*<a href="src/privy/types/user_get_by_wallet_address_params.py">params</a>) -> <a href="./src/privy/types/user.py">User</a></code>

# Policies

Types:

```python
from privy.types import Policy, PolicyDeleteResponse
```

Methods:

- <code title="post /v1/policies">client.policies.<a href="./src/privy/resources/policies.py">create</a>(\*\*<a href="src/privy/types/policy_create_params.py">params</a>) -> <a href="./src/privy/types/policy.py">Policy</a></code>
- <code title="patch /v1/policies/{policy_id}">client.policies.<a href="./src/privy/resources/policies.py">update</a>(policy_id, \*\*<a href="src/privy/types/policy_update_params.py">params</a>) -> <a href="./src/privy/types/policy.py">Policy</a></code>
- <code title="delete /v1/policies/{policy_id}">client.policies.<a href="./src/privy/resources/policies.py">delete</a>(policy_id) -> <a href="./src/privy/types/policy_delete_response.py">PolicyDeleteResponse</a></code>
- <code title="get /v1/policies/{policy_id}">client.policies.<a href="./src/privy/resources/policies.py">get</a>(policy_id) -> <a href="./src/privy/types/policy.py">Policy</a></code>

# Transactions

Types:

```python
from privy.types import TransactionGetResponse
```

Methods:

- <code title="get /v1/transactions/{transaction_id}">client.transactions.<a href="./src/privy/resources/transactions.py">get</a>(transaction_id) -> <a href="./src/privy/types/transaction_get_response.py">TransactionGetResponse</a></code>

# KeyQuorums

Types:

```python
from privy.types import KeyQuorum
```

Methods:

- <code title="post /v1/key_quorums">client.key_quorums.<a href="./src/privy/resources/key_quorums.py">create</a>(\*\*<a href="src/privy/types/key_quorum_create_params.py">params</a>) -> <a href="./src/privy/types/key_quorum.py">KeyQuorum</a></code>
- <code title="patch /v1/key_quorums/{key_quorum_id}">client.key_quorums.<a href="./src/privy/resources/key_quorums.py">update</a>(key_quorum_id, \*\*<a href="src/privy/types/key_quorum_update_params.py">params</a>) -> <a href="./src/privy/types/key_quorum.py">KeyQuorum</a></code>
- <code title="delete /v1/key_quorums/{key_quorum_id}">client.key_quorums.<a href="./src/privy/resources/key_quorums.py">delete</a>(key_quorum_id) -> <a href="./src/privy/types/key_quorum.py">KeyQuorum</a></code>
- <code title="get /v1/key_quorums/{key_quorum_id}">client.key_quorums.<a href="./src/privy/resources/key_quorums.py">get</a>(key_quorum_id) -> <a href="./src/privy/types/key_quorum.py">KeyQuorum</a></code>

# Fiat

Types:

```python
from privy.types import FiatConfigureAppResponse, FiatGetKYCLinkResponse, FiatGetStatusResponse
```

Methods:

- <code title="post /v1/apps/{app_id}/fiat">client.fiat.<a href="./src/privy/resources/fiat/fiat.py">configure_app</a>(app_id, \*\*<a href="src/privy/types/fiat_configure_app_params.py">params</a>) -> <a href="./src/privy/types/fiat_configure_app_response.py">FiatConfigureAppResponse</a></code>
- <code title="post /v1/users/{user_id}/fiat/kyc_link">client.fiat.<a href="./src/privy/resources/fiat/fiat.py">get_kyc_link</a>(user_id, \*\*<a href="src/privy/types/fiat_get_kyc_link_params.py">params</a>) -> <a href="./src/privy/types/fiat_get_kyc_link_response.py">FiatGetKYCLinkResponse</a></code>
- <code title="post /v1/users/{user_id}/fiat/status">client.fiat.<a href="./src/privy/resources/fiat/fiat.py">get_status</a>(user_id, \*\*<a href="src/privy/types/fiat_get_status_params.py">params</a>) -> <a href="./src/privy/types/fiat_get_status_response.py">FiatGetStatusResponse</a></code>

## Accounts

Types:

```python
from privy.types.fiat import AccountCreateResponse, AccountGetResponse
```

Methods:

- <code title="post /v1/users/{user_id}/fiat/accounts">client.fiat.accounts.<a href="./src/privy/resources/fiat/accounts.py">create</a>(user_id, \*\*<a href="src/privy/types/fiat/account_create_params.py">params</a>) -> <a href="./src/privy/types/fiat/account_create_response.py">AccountCreateResponse</a></code>
- <code title="get /v1/users/{user_id}/fiat/accounts">client.fiat.accounts.<a href="./src/privy/resources/fiat/accounts.py">get</a>(user_id, \*\*<a href="src/privy/types/fiat/account_get_params.py">params</a>) -> <a href="./src/privy/types/fiat/account_get_response.py">AccountGetResponse</a></code>

## KYC

Types:

```python
from privy.types.fiat import KYCCreateResponse, KYCUpdateResponse, KYCGetResponse
```

Methods:

- <code title="post /v1/users/{user_id}/fiat/kyc">client.fiat.kyc.<a href="./src/privy/resources/fiat/kyc.py">create</a>(user_id, \*\*<a href="src/privy/types/fiat/kyc_create_params.py">params</a>) -> <a href="./src/privy/types/fiat/kyc_create_response.py">KYCCreateResponse</a></code>
- <code title="patch /v1/users/{user_id}/fiat/kyc">client.fiat.kyc.<a href="./src/privy/resources/fiat/kyc.py">update</a>(user_id, \*\*<a href="src/privy/types/fiat/kyc_update_params.py">params</a>) -> <a href="./src/privy/types/fiat/kyc_update_response.py">KYCUpdateResponse</a></code>
- <code title="get /v1/users/{user_id}/fiat/kyc">client.fiat.kyc.<a href="./src/privy/resources/fiat/kyc.py">get</a>(user_id, \*\*<a href="src/privy/types/fiat/kyc_get_params.py">params</a>) -> <a href="./src/privy/types/fiat/kyc_get_response.py">KYCGetResponse</a></code>

## Onramp

Types:

```python
from privy.types.fiat import OnrampCreateResponse
```

Methods:

- <code title="post /v1/users/{user_id}/fiat/onramp">client.fiat.onramp.<a href="./src/privy/resources/fiat/onramp.py">create</a>(user_id, \*\*<a href="src/privy/types/fiat/onramp_create_params.py">params</a>) -> <a href="./src/privy/types/fiat/onramp_create_response.py">OnrampCreateResponse</a></code>

## Offramp

Types:

```python
from privy.types.fiat import OfframpCreateResponse
```

Methods:

- <code title="post /v1/users/{user_id}/fiat/offramp">client.fiat.offramp.<a href="./src/privy/resources/fiat/offramp.py">create</a>(user_id, \*\*<a href="src/privy/types/fiat/offramp_create_params.py">params</a>) -> <a href="./src/privy/types/fiat/offramp_create_response.py">OfframpCreateResponse</a></code>
