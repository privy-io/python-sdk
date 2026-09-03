# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union

from .._models import BaseModel

__all__ = ["UserCreateCustomMetadataResponse"]


class UserCreateCustomMetadataResponse(BaseModel):
    custom_metadata: Dict[str, Union[str, float, bool]]
