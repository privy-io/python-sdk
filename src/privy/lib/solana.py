"""Solana wallet operations."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .wallets import WalletsService

__all__ = ["SolanaWalletService"]


class SolanaWalletService:
    """Convenience methods for Solana wallet operations."""

    def __init__(self, wallets: WalletsService) -> None:
        self._wallets = wallets
