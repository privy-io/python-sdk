from __future__ import annotations

import os
from collections.abc import Iterator

import pytest

from privy import PrivyClient, PrivyRequestExpiryOptions

STAGING_API_URL = "https://api.staging.privy.io"


def required_environment(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        pytest.fail(f"{name} is required for live integration tests")
    return value


def staging_client(request_expiry: PrivyRequestExpiryOptions | None = None) -> PrivyClient:
    api_url = (os.environ.get("TEST_API_URL") or STAGING_API_URL).rstrip("/")
    if api_url == "https://api.privy.io":
        pytest.fail("Live integration tests must not target the production API")

    return PrivyClient(
        app_id=required_environment("TEST_APP_ID"),
        app_secret=required_environment("TEST_APP_SECRET"),
        base_url=api_url,
        request_expiry=request_expiry,
    )


@pytest.fixture(scope="session")
def jwt_auth_private_key() -> str:
    return required_environment("JWT_AUTH_SK").replace("\\n", "\n").strip()


@pytest.fixture(scope="session")
def privy_client() -> Iterator[PrivyClient]:
    with staging_client() as client:
        yield client


@pytest.fixture(scope="session")
def privy_client_without_request_expiry() -> Iterator[PrivyClient]:
    with staging_client(request_expiry=PrivyRequestExpiryOptions(disabled=True)) as client:
        yield client
