# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .hpke_encryption import HpkeEncryption
from .hpke_import_config_param import HpkeImportConfigParam
from .wallet_import_supported_chains import WalletImportSupportedChains

__all__ = ["HDSubmitInputParam"]


class HDSubmitInputParam(TypedDict, total=False):
    """The submission input for importing an HD wallet."""

    address: Required[str]
    """The address of the wallet to import."""

    chain_type: Required[WalletImportSupportedChains]
    """The chain type of the wallet to import.

    Supports `ethereum`, `solana`, `stellar`, `tron`, `sui`, and `aptos`.
    """

    ciphertext: Required[str]
    """The encrypted entropy of the wallet to import."""

    encapsulated_key: Required[str]
    """
    The base64-encoded encapsulated key that was generated during encryption, for
    use during decryption inside the TEE.
    """

    encryption_type: Required[HpkeEncryption]
    """The encryption type of the wallet to import. Currently only supports `HPKE`."""

    entropy_type: Required[Literal["hd"]]
    """The entropy type of the wallet to import."""

    index: Required[int]
    """The index of the wallet to import."""

    hpke_config: HpkeImportConfigParam
    """Optional HPKE configuration for wallet import decryption.

    These parameters allow importing wallets encrypted by external providers that
    use different HPKE configurations.
    """
