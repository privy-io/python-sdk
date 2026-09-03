import json
from typing import Any, Dict, List, Union, Optional, TypedDict

import jwt
import httpx
from jwt import PyJWK

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from ..types.user import User
from .._base_client import make_request_options
from ..resources.users import (
    UsersResource as BaseUsersResource,
    AsyncUsersResource as BaseAsyncUsersResource,
)
from .._utils._user_utils import convert_to_linked_accounts
from ..types.wallet_create_wallets_with_recovery_params import (
    Wallet,
    RecoveryUserLinkedAccount,
)
from ..types.wallet_create_wallets_with_recovery_response import (
    WalletCreateWalletsWithRecoveryResponse,
)


class AccessTokenClaims(TypedDict):
    app_id: str
    user_id: str
    issuer: str
    issued_at: str
    expiration: str
    session_id: str


class UsersResource(BaseUsersResource):
    _verification_key: Optional[PyJWK] = None

    def create_with_jwt_auth(
        self,
        *,
        jwt_subject_id: str,
        wallets: List[Wallet],
        additional_linked_accounts: Optional[List[RecoveryUserLinkedAccount]] = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> WalletCreateWalletsWithRecoveryResponse:
        """Create a wallet with a simplified interface.

        This method provides a simplified interface for creating wallets that:
        1. Sets up a primary signer with the provided jwt_subject_id
        2. Creates a recovery user with the custom JWT account and any additional linked accounts
        3. Creates the specified wallet(s)

        Args:
            jwt_subject_id: The JWT subject ID of the user
            wallets: List of wallet configurations (e.g. [{"chain_type": "ethereum"}])
            additional_linked_accounts: Optional list of additional linked accounts to add to the recovery user
            extra_headers: Optional additional headers for the request
            extra_query: Optional additional query parameters
            extra_body: Optional additional body parameters
            timeout: Optional timeout for the request

        Returns:
            WalletCreateWalletsWithRecoveryResponse containing the created wallets and recovery user ID
        """
        # Prepare linked accounts, ensuring custom JWT account is included
        linked_accounts: List[RecoveryUserLinkedAccount] = [
            {"custom_user_id": jwt_subject_id, "type": "custom_auth"}
        ]

        # Add any additional linked accounts if provided
        if additional_linked_accounts:
            # Check if any additional account conflicts with the custom JWT account
            for account in additional_linked_accounts:
                if account.get("type") == "custom_auth":
                    raise ValueError(
                        "Custom JWT account should only be specified in jwt_subject_id"
                    )
            linked_accounts.extend(additional_linked_accounts)

        # TODO: figure out if we can use the underlying method instead (client.wallets.create_wallets_with_recovery)
        return self._post(
            "/v1/wallets_with_recovery",
            body=maybe_transform(
                {
                    "primary_signer": {"subject_id": jwt_subject_id},
                    "recovery_user": {"linked_accounts": linked_accounts},
                    "wallets": wallets,
                },
                "wallet_create_wallets_with_recovery_params",
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=WalletCreateWalletsWithRecoveryResponse,
        )

    def _get_verification_key(
        self,
    ) -> PyJWK:
        if self._verification_key is not None:
            return self._verification_key

        response = self._get(
            (
                f"/api/v1/apps/{self._client.app_id}/jwks.json"
                if self._client._base_url_overridden
                else f"https://auth.privy.io/api/v1/apps/{self._client.app_id}/jwks.json"
            ),
            cast_to=Dict[str, Any],
        )
        self._verification_key = jwt.PyJWK.from_json(json.dumps(response["keys"][0]))
        return self._verification_key

    def verify_access_token(
        self, *, auth_token: str, verification_key: Optional[Union[str, PyJWK]] = None
    ) -> AccessTokenClaims:
        """Verify the user access token. The access token is a standard ES256 JWT.

        Args:
            auth_token: The access token to verify
            verification_key: The Ed25519 public key from the Privy dashboard. Set this to avoid an API call to Privy. If not provided, the verification key will be fetched from the Privy API.

        Returns:
            The decoded access token claims. If the token is invalid, an exception will be raised.
        """
        if not verification_key:
            verification_key = self._get_verification_key()

        decoded = jwt.decode(
            auth_token,
            verification_key,
            issuer="privy.io",
            audience=self._client.app_id,
            algorithms=["ES256"],
        )
        result = AccessTokenClaims(
            app_id=decoded["aud"],
            user_id=decoded["sub"],
            session_id=decoded["sid"],
            issuer=decoded["iss"],
            issued_at=str(decoded["iat"]),
            expiration=str(decoded["exp"]),
        )
        return result

    def get_by_id_token(self, *, id_token: str) -> User:
        """
        Get a user by their ID token.

        Args:
            id_token: The identity token which contains the users information

        Returns:
            GetUserByIdTokenResponse containing the id, custom metadata, linked accounts, whether they are a guest, and timestamp of when they were created
        """
        verification_key = self._get_verification_key()
        decoded = jwt.decode(
            id_token,
            verification_key,
            issuer="privy.io",
            audience=self._client.app_id,
            algorithms=["ES256"],
        )
        linked_accounts = convert_to_linked_accounts(
            json.loads(decoded.get("linked_accounts"))
        )

        return User(
            id=decoded.get("sub"),
            linked_accounts=linked_accounts,
            is_guest=decoded.get("guest") == "t",
            custom_metadata=decoded.get("custom_metadata"),
            created_at=decoded.get("cr"),
        )


class AsyncUsersResource(BaseAsyncUsersResource):
    _verification_key: Optional[PyJWK] = None

    async def create_with_jwt_auth(
        self,
        *,
        jwt_subject_id: str,
        wallets: List[Wallet],
        additional_linked_accounts: Optional[List[RecoveryUserLinkedAccount]] = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> WalletCreateWalletsWithRecoveryResponse:
        """Create a wallet with a simplified interface.

        This method provides a simplified interface for creating wallets that:
        1. Sets up a primary signer with the provided jwt_subject_id
        2. Creates a recovery user with the custom JWT account and any additional linked accounts
        3. Creates the specified wallet(s)

        Args:
            jwt_subject_id: The JWT subject ID of the user
            wallets: List of wallet configurations (e.g. [{"chain_type": "ethereum"}])
            additional_linked_accounts: Optional list of additional linked accounts to add to the recovery user
            extra_headers: Optional additional headers for the request
            extra_query: Optional additional query parameters
            extra_body: Optional additional body parameters
            timeout: Optional timeout for the request

        Returns:
            WalletCreateWalletsWithRecoveryResponse containing the created wallets and recovery user ID
        """
        # Prepare linked accounts, ensuring custom JWT account is included
        linked_accounts: List[RecoveryUserLinkedAccount] = [
            {"custom_user_id": jwt_subject_id, "type": "custom_auth"}
        ]

        # Add any additional linked accounts if provided
        if additional_linked_accounts:
            # Check if any additional account conflicts with the custom JWT account
            for account in additional_linked_accounts:
                if account.get("type") == "custom_auth":
                    raise ValueError(
                        "Custom JWT account should only be specified in jwt_subject_id"
                    )
            linked_accounts.extend(additional_linked_accounts)

        # TODO: figure out if we can use the underlying method instead (client.wallets.create_wallets_with_recovery)
        return await self._post(
            "/v1/wallets_with_recovery",
            body=await async_maybe_transform(
                {
                    "primary_signer": {"subject_id": jwt_subject_id},
                    "recovery_user": {"linked_accounts": linked_accounts},
                    "wallets": wallets,
                },
                "wallet_create_wallets_with_recovery_params",
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=WalletCreateWalletsWithRecoveryResponse,
        )

    async def _get_verification_key(
        self,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> PyJWK:
        if self._verification_key is not None:
            return self._verification_key

        response = await self._get(
            (
                f"/api/v1/apps/{self._client.app_id}/jwks.json"
                if self._client._base_url_overridden
                else f"https://auth.privy.io/api/v1/apps/{self._client.app_id}/jwks.json"
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Dict[str, Any],
        )
        self._verification_key = jwt.PyJWK.from_json(json.dumps(response["keys"][0]))
        return self._verification_key

    async def verify_access_token(
        self,
        *,
        auth_token: str,
        verification_key: Optional[Union[str, PyJWK]] = None,
    ) -> AccessTokenClaims:
        """Verify the user access token. The access token is a standard ES256 JWT.

        Args:
            auth_token: The access token to verify
            verification_key: The Ed25519 public key from the Privy dashboard. Set this to avoid an API call to Privy. If not provided, the verification key will be fetched from the Privy API.

        Returns:
            The decoded access token claims. If the token is invalid, an exception will be raised.
        """
        if not verification_key:
            verification_key = await self._get_verification_key()

        decoded = jwt.decode(
            auth_token,
            verification_key,
            issuer="privy.io",
            audience=self._client.app_id,
            algorithms=["ES256"],
        )
        result = AccessTokenClaims(
            app_id=decoded["aud"],
            user_id=decoded["sub"],
            session_id=decoded["sid"],
            issuer=decoded["iss"],
            issued_at=str(decoded["iat"]),
            expiration=str(decoded["exp"]),
        )
        return result

    async def get_by_id_token(self, *, id_token: str) -> User:
        """
        Get a user by their ID token.

        Args:
            id_token: The identity token which contains the users information

        Returns:
            GetUserByIdTokenResponse containing the id, custom metadata, linked accounts, whether they are a guest, and timestamp of when they were created
        """
        verification_key = await self._get_verification_key()
        decoded = jwt.decode(
            id_token,
            verification_key,
            issuer="privy.io",
            audience=self._client.app_id,
            algorithms=["ES256"],
        )
        linked_accounts = convert_to_linked_accounts(
            json.loads(decoded.get("linked_accounts"))
        )

        return User(
            id=decoded.get("sub"),
            linked_accounts=linked_accounts,
            is_guest=decoded.get("guest") == "t",
            custom_metadata=decoded.get("custom_metadata"),
            created_at=decoded.get("cr"),
        )
