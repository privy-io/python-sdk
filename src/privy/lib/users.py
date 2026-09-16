"""Public user operations."""

from __future__ import annotations

from .auth import PrivyAuthService
from .._client import PrivyAPI
from ..types.user import User
from ..resources.users.users import UsersResource

__all__ = ["PrivyUsersService"]


class PrivyUsersService(UsersResource):
    def __init__(self, client: PrivyAPI, auth: PrivyAuthService) -> None:
        super().__init__(client)
        self._auth = auth

    def get_by_identity_token(self, identity_token: str) -> User:
        """Verify an identity token and return the user encoded in its claims."""

        return self._auth.verify_identity_token(identity_token)
