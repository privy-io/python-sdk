# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .custom_metadata_param import CustomMetadataParam

__all__ = ["UserSetCustomMetadataParams"]


class UserSetCustomMetadataParams(TypedDict, total=False):
    custom_metadata: Required[CustomMetadataParam]
    """Custom metadata associated with the user."""
