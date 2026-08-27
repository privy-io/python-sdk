"""Ethereum wallet operations."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .wallets import WalletsService

__all__ = ["EthereumWalletService"]


class EthereumWalletService:
    """Convenience methods for Ethereum wallet operations."""

    def __init__(self, wallets: WalletsService) -> None:
        self._wallets = wallets
