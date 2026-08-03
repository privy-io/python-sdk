# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .typed_data_types_input_params import TypedDataTypesInputParams

__all__ = ["TypedDataInput"]


class TypedDataInput(BaseModel):
    """
    The typed data structure containing EIP-712 types and the primary type for typed data message policy conditions.
    """

    primary_type: str

    types: TypedDataTypesInputParams
    """The type definitions for EIP-712 typed data signing."""
