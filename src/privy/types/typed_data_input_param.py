# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .typed_data_types_input_params_param import TypedDataTypesInputParamsParam

__all__ = ["TypedDataInputParam"]


class TypedDataInputParam(TypedDict, total=False):
    """
    The typed data structure containing EIP-712 types and the primary type for typed data message policy conditions.
    """

    primary_type: Required[str]

    types: Required[TypedDataTypesInputParamsParam]
    """The type definitions for EIP-712 typed data signing."""
