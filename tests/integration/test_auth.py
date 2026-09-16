from __future__ import annotations

import time
from typing import Any, cast
from collections.abc import Mapping

import httpx
import pytest

from privy import PrivyClient, VerifyAccessTokenResponse, verify_access_token, create_privy_app_jwks
from privy.types.user import User

pytestmark = pytest.mark.integration


@pytest.fixture(scope="module")
def authenticated_test_account(privy_client: PrivyClient) -> Mapping[str, Any]:
    credentials = privy_client.apps.get_test_credentials(privy_client._client.app_id)
    assert credentials.data, "the staging app must have at least one configured test account"
    account = credentials.data[0]
    api_url = str(privy_client._client.base_url).rstrip("/")
    auth_url = api_url.replace("://api.", "://auth.")

    response: httpx.Response | None = None
    for attempt in range(4):
        response = httpx.post(
            f"{auth_url}/api/v1/passwordless/authenticate",
            json={"email": account.email, "code": account.otp_code},
            headers={
                "privy-app-id": privy_client._client.app_id,
                "Origin": "http://localhost:3000",
            },
        )
        if response.status_code != 429:
            break
        if attempt < 3:
            time.sleep(min(2**attempt, 15))

    assert response is not None
    response.raise_for_status()
    body = response.json()
    assert isinstance(body, dict)
    return cast("Mapping[str, Any]", body)


def test_verify_access_token_with_discovered_and_cached_jwks(
    privy_client: PrivyClient, authenticated_test_account: Mapping[str, Any]
) -> None:
    access_token = authenticated_test_account["token"]
    assert isinstance(access_token, str)

    first = privy_client.auth.verify_access_token(access_token)
    second = privy_client.auth.verify_access_token(access_token)

    assert isinstance(first, VerifyAccessTokenResponse)
    assert second == first
    assert first.app_id == privy_client._client.app_id
    assert first.issuer == "privy.io"
    assert first.session_id
    assert first.user_id


def test_verify_access_token_with_client_verification_key_override(
    privy_client: PrivyClient, authenticated_test_account: Mapping[str, Any]
) -> None:
    access_token = authenticated_test_account["token"]
    assert isinstance(access_token, str)
    settings = privy_client.apps.get_settings()

    with PrivyClient(
        app_id=privy_client._client.app_id,
        app_secret=privy_client._client.app_secret,
        base_url=str(privy_client._client.base_url),
        jwt_verification_key=settings.verification_key,
    ) as override_client:
        verified = override_client.auth.verify_access_token(access_token)

    assert verified.app_id == privy_client._client.app_id
    assert verified.user_id


def test_verify_access_token_with_public_helpers(
    privy_client: PrivyClient, authenticated_test_account: Mapping[str, Any]
) -> None:
    access_token = authenticated_test_account["token"]
    assert isinstance(access_token, str)
    app_id = privy_client._client.app_id
    jwks = create_privy_app_jwks(
        app_id=app_id,
        api_url=str(privy_client._client.base_url),
        headers={"privy-client": "python:integration-test"},
    )

    verified = verify_access_token(access_token=access_token, app_id=app_id, verification_key=jwks)

    assert verified.app_id == app_id
    assert verified.user_id


def test_verify_identity_token_and_extract_user(
    privy_client: PrivyClient, authenticated_test_account: Mapping[str, Any]
) -> None:
    identity_token = authenticated_test_account["identity_token"]
    assert isinstance(identity_token, str)

    verified_user = privy_client.auth.verify_identity_token(identity_token)
    extracted_user = privy_client.users.get_by_identity_token(identity_token)

    assert isinstance(verified_user, User)
    assert extracted_user == verified_user
    assert verified_user.id
    assert isinstance(verified_user.linked_accounts, list)
