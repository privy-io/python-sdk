# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .tmmf_provider import TmmfProvider
from .tmmf_registration_status import TmmfRegistrationStatus

__all__ = ["TmmfUserRegistration"]


class TmmfUserRegistration(BaseModel):
    """A user's registration with one tMMF provider."""

    provider: TmmfProvider
    """The fund provider."""

    status: TmmfRegistrationStatus
    """A user's registration status with a tMMF provider, read live from the provider."""
