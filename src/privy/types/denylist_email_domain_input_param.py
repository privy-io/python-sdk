# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .email_domain import EmailDomain

__all__ = ["DenylistEmailDomainInputParam"]


class DenylistEmailDomainInputParam(TypedDict, total=False):
    """
    Denylist input for an email domain, which blocks every email address on the domain.
    """

    type: Required[Literal["emailDomain"]]

    value: Required[EmailDomain]
    """An email domain."""
