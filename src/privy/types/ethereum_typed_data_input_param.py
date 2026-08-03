# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .typed_data_types_input_params_param import TypedDataTypesInputParamsParam
from .typed_data_domain_input_params_param import TypedDataDomainInputParamsParam

__all__ = ["EthereumTypedDataInputParam"]


class EthereumTypedDataInputParam(TypedDict, total=False):
    """EIP-712 typed data object."""

    domain: Required[TypedDataDomainInputParamsParam]
    """The domain parameters for EIP-712 typed data signing."""

    message: Required[Dict[str, object]]

    primary_type: Required[str]

    types: Required[TypedDataTypesInputParamsParam]
    """The type definitions for EIP-712 typed data signing."""
