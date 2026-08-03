# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel
from .typed_data_types_input_params import TypedDataTypesInputParams
from .typed_data_domain_input_params import TypedDataDomainInputParams

__all__ = ["EthereumTypedDataInput"]


class EthereumTypedDataInput(BaseModel):
    """EIP-712 typed data object."""

    domain: TypedDataDomainInputParams
    """The domain parameters for EIP-712 typed data signing."""

    message: Dict[str, object]

    primary_type: str

    types: TypedDataTypesInputParams
    """The type definitions for EIP-712 typed data signing."""
