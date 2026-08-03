# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WalletRecoverySetupMethod"]

WalletRecoverySetupMethod: TypeAlias = Literal[
    "user_passcode_derived_recovery_key",
    "privy_passcode_derived_recovery_key",
    "privy_generated_recovery_key",
    "google_drive_recovery_secret",
    "icloud_recovery_secret",
    "recovery_encryption_key",
]
