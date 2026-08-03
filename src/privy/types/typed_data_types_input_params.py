# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import TypeAlias

from .typed_data_type_field_input import TypedDataTypeFieldInput

__all__ = ["TypedDataTypesInputParams"]

TypedDataTypesInputParams: TypeAlias = Dict[str, List[TypedDataTypeFieldInput]]
