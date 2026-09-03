from typing import Any, List, Union, Optional

import httpx

from .hpke import open, generate_keypair
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..resources.wallets import (
    WalletsResource as BaseWalletsResource,
    AsyncWalletsResource as BaseAsyncWalletsResource,
)
from ..types.wallet_authenticate_with_jwt_response import WithEncryption


class DecryptedWalletAuthenticateWithJwtResponse:
    """Response containing the decrypted authorization key and associated wallet information.

    This response contains the decrypted authorization key that can be used directly
    for wallet operations, along with the expiration time and wallet information.
    """

    def __init__(
        self,
        *,
        decrypted_authorization_key: str,
        expires_at: float,
        wallets: List[Any],
    ):
        self.decrypted_authorization_key = decrypted_authorization_key
        self.expires_at = expires_at
        self.wallets = wallets


class WalletsResource(BaseWalletsResource):
    def generate_user_signer(
        self,
        *,
        user_jwt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> DecryptedWalletAuthenticateWithJwtResponse:
        """Authenticate with a JWT and automatically handle keypair generation and decryption.

        This method performs a complete authentication flow that:
        1. Generates an ephemeral keypair for secure key exchange
        2. Authenticates with the provided JWT
        3. Decrypts the authorization key using the generated keypair

        Args:
            user_jwt: The JWT token for authentication
            extra_headers: Optional additional headers for the request
            extra_query: Optional additional query parameters
            extra_body: Optional additional body parameters
            timeout: Optional timeout for the request

        Returns:
            DecryptedWalletAuthenticateWithJwtResponse containing the decrypted authorization key
        """
        # Generate an ephemeral keypair for the exchange
        ephemeral_keypair = generate_keypair()
        encrypted_payload = super().authenticate_with_jwt(  # pyright: ignore[reportDeprecated]
            encryption_type="HPKE",
            recipient_public_key=ephemeral_keypair["public_key"],
            user_jwt=user_jwt,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not isinstance(encrypted_payload, WithEncryption):
            raise TypeError("Expected encrypted response when encryption_type is HPKE")
        decrypted_authorization_key = open(
            private_key=ephemeral_keypair["private_key"],
            encapsulated_key=encrypted_payload.encrypted_authorization_key.encapsulated_key,
            ciphertext=encrypted_payload.encrypted_authorization_key.ciphertext,
        )
        return DecryptedWalletAuthenticateWithJwtResponse(
            decrypted_authorization_key=decrypted_authorization_key["message"],
            expires_at=encrypted_payload.expires_at,
            wallets=encrypted_payload.wallets,
        )


class AsyncWalletsResource(BaseAsyncWalletsResource):
    async def generate_user_signer(
        self,
        *,
        user_jwt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> DecryptedWalletAuthenticateWithJwtResponse:
        """Asynchronously authenticate with a JWT and automatically handle keypair generation and decryption.

        This method provides a safe, all-in-one authentication flow that:
        1. Automatically generates a secure ephemeral keypair for the exchange
        2. Handles the authentication with the provided JWT
        3. Securely decrypts the authorization key using the generated keypair
        4. Returns the decrypted authorization key along with wallet information

        This is the recommended method for authentication as it handles all security-critical
        operations in a single call while maintaining proper key management.

        Args:
            user_jwt: The JWT token for authentication
            extra_headers: Optional additional headers for the request
            extra_query: Optional additional query parameters
            extra_body: Optional additional body parameters
            timeout: Optional timeout for the request

        Returns:
            DecryptedWalletAuthenticateWithJwtResponse containing the decrypted authorization key
        """
        # Generate an ephemeral keypair for the exchange
        ephemeral_keypair = generate_keypair()
        encrypted_payload = await super().authenticate_with_jwt(  # pyright: ignore[reportDeprecated]
            encryption_type="HPKE",
            recipient_public_key=ephemeral_keypair["public_key"],
            user_jwt=user_jwt,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not isinstance(encrypted_payload, WithEncryption):
            raise TypeError("Expected encrypted response when encryption_type is HPKE")
        decrypted_authorization_key = open(
            private_key=ephemeral_keypair["private_key"],
            encapsulated_key=encrypted_payload.encrypted_authorization_key.encapsulated_key,
            ciphertext=encrypted_payload.encrypted_authorization_key.ciphertext,
        )
        return DecryptedWalletAuthenticateWithJwtResponse(
            decrypted_authorization_key=decrypted_authorization_key["message"],
            expires_at=encrypted_payload.expires_at,
            wallets=encrypted_payload.wallets,
        )
