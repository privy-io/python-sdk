# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TypedDataTypeFieldInputParam"]


class TypedDataTypeFieldInputParam(TypedDict, total=False):
    """A single field definition in an EIP-712 typed data type."""

    name: Required[str]

    type: Required[str]
