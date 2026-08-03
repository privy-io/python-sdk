# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TypedDataTypeFieldInput"]


class TypedDataTypeFieldInput(BaseModel):
    """A single field definition in an EIP-712 typed data type."""

    name: str

    type: str
