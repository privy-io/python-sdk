"""Hand-written public API layered on top of the generated client."""

from .client import PrivyClient
from .wallets import WalletsService

__all__ = ["PrivyClient", "WalletsService"]
