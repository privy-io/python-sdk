# The public client is introduced in a follow-up. Remove these suppressions once
# PrivyClient is available for Pyright to inspect.
# pyright: reportUnknownVariableType=false, reportUnknownParameterType=false

from __future__ import annotations

import os
from collections.abc import Iterator

import pytest

from privy import PrivyClient  # pyright: ignore[reportAttributeAccessIssue]

STAGING_API_URL = "https://api.staging.privy.io"


def required_environment(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        pytest.fail(f"{name} is required for live integration tests")
    return value


@pytest.fixture(scope="session")
def privy_client() -> Iterator[PrivyClient]:
    api_url = (os.environ.get("TEST_API_URL") or STAGING_API_URL).rstrip("/")
    if api_url == "https://api.privy.io":
        pytest.fail("Live integration tests must not target the production API")

    with PrivyClient(
        app_id=required_environment("TEST_APP_ID"),
        app_secret=required_environment("TEST_APP_SECRET"),
        base_url=api_url,
    ) as client:
        yield client
