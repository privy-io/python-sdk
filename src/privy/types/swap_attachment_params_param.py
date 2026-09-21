# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SwapAttachmentParamsParam"]


class SwapAttachmentParamsParam(TypedDict, total=False):
    """Per-attachment parameters for swap automations."""

    destination_address: Required[str]
