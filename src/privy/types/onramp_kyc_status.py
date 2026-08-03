# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["OnrampKYCStatus"]

OnrampKYCStatus: TypeAlias = Literal[
    "not_found",
    "active",
    "awaiting_questionnaire",
    "awaiting_ubo",
    "incomplete",
    "not_started",
    "offboarded",
    "paused",
    "rejected",
    "under_review",
]
