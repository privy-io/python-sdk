# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .raw_wallet_authenticate_response import RawWalletAuthenticateResponse
from .encrypted_wallet_authenticate_response import EncryptedWalletAuthenticateResponse

__all__ = ["WalletAuthenticateWithJwtResponse"]

WalletAuthenticateWithJwtResponse: TypeAlias = Union[EncryptedWalletAuthenticateResponse, RawWalletAuthenticateResponse]
