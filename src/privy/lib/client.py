"""Public Privy client."""

from __future__ import annotations

from types import TracebackType

from .users import UsersService
from .wallets import WalletsService
from .._client import PrivyAPI
from .._version import __version__
from .key_quorums import KeyQuorumsService
from .transactions import TransactionsService

__all__ = ["PrivyClient"]


class PrivyClient:
    """Synchronous entrypoint for the Privy API."""

    def __init__(self, *, app_id: str, app_secret: str, base_url: str) -> None:
        self._client = PrivyAPI(
            app_id=app_id,
            app_secret=app_secret,
            base_url=base_url,
            default_headers={"privy-client": f"python:{__version__}"},
        )
        self.wallets = WalletsService(self._client)
        self.key_quorums = KeyQuorumsService(self._client)
        self.users = UsersService(self._client)
        self.transactions = TransactionsService(self._client)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> PrivyClient:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()
