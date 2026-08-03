# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AbiParameter"]


class AbiParameter(BaseModel):
    """A parameter in a Solidity ABI function or event definition."""

    type: str

    components: Optional[List[Dict[str, object]]] = None

    indexed: Optional[bool] = None

    internal_type: Optional[str] = FieldInfo(alias="internalType", default=None)

    name: Optional[str] = None
