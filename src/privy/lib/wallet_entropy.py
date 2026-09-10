"""Chain-specific wallet entropy decoding for secure wallet imports."""

from __future__ import annotations

import base64
import binascii

from .._exceptions import PrivyAPIError
from ..types.wallet_import_supported_chains import WalletImportSupportedChains

_BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
_BASE58_VALUES = {character: index for index, character in enumerate(_BASE58_ALPHABET)}
_HEX_CHAINS = {"ethereum", "tron", "sui", "aptos", "xrpl"}


def _decode_base58(value: str) -> bytes:
    number = 0
    try:
        for character in value:
            number = number * 58 + _BASE58_VALUES[character]
    except KeyError as exc:
        raise ValueError("invalid base58 character") from exc

    decoded = number.to_bytes((number.bit_length() + 7) // 8, "big") if number else b""
    return b"\0" * (len(value) - len(value.lstrip("1"))) + decoded


def _decode_stellar_strkey(value: str) -> bytes:
    normalized = value.upper()
    normalized += "=" * (-len(normalized) % 8)
    decoded = base64.b32decode(normalized, casefold=True)
    if len(decoded) < 33:
        raise ValueError("invalid StrKey length")
    return decoded[1:33]


def entropy_to_bytes(
    entropy: str | bytes | bytearray,
    *,
    entropy_type: str,
    chain_type: WalletImportSupportedChains,
) -> bytes:
    """Encode a seed phrase or decode a chain-specific private key."""

    if isinstance(entropy, (bytes, bytearray)):
        return bytes(entropy)
    if entropy_type == "hd":
        return entropy.encode("utf-8")
    if entropy_type != "private-key":
        raise PrivyAPIError(f"Invalid entropy type: {entropy_type}")

    if chain_type in _HEX_CHAINS:
        value = entropy[2:] if entropy.startswith("0x") else entropy
        try:
            return binascii.unhexlify(value)
        except (ValueError, binascii.Error) as exc:
            raise PrivyAPIError(f"Invalid private key: {chain_type} entropy must be hex encoded") from exc

    if chain_type == "solana":
        try:
            return _decode_base58(entropy)
        except ValueError as exc:
            raise PrivyAPIError("Invalid private key: Solana entropy must be base58 encoded") from exc

    if chain_type == "stellar":
        try:
            return _decode_stellar_strkey(entropy)
        except (ValueError, binascii.Error) as exc:
            raise PrivyAPIError("Invalid private key: Stellar entropy must be StrKey encoded") from exc

    raise PrivyAPIError(f"Invalid chain type for imports: {chain_type}")
