# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    CryptoDepositAddressRoute,
    CreateCryptoDepositAccountResponse,
    CryptoDepositAccountConfigResponse,
)
from tests.utils import assert_matches_type
from privy.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCrypto:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        crypto = client.wallets.deposit_accounts.crypto.list(
            wallet_id="wallet_id",
        )
        assert_matches_type(SyncCursor[CryptoDepositAddressRoute], crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PrivyAPI) -> None:
        crypto = client.wallets.deposit_accounts.crypto.list(
            wallet_id="wallet_id",
            cursor="x",
            limit=1,
        )
        assert_matches_type(SyncCursor[CryptoDepositAddressRoute], crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.wallets.deposit_accounts.crypto.with_raw_response.list(
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = response.parse()
        assert_matches_type(SyncCursor[CryptoDepositAddressRoute], crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.wallets.deposit_accounts.crypto.with_streaming_response.list(
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = response.parse()
            assert_matches_type(SyncCursor[CryptoDepositAddressRoute], crypto, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.deposit_accounts.crypto.with_raw_response.list(
                wallet_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: PrivyAPI) -> None:
        crypto = client.wallets.deposit_accounts.crypto._create(
            wallet_id="wallet_id",
            deposit_config_id="x",
            type="deposit_config",
        )
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: PrivyAPI) -> None:
        crypto = client.wallets.deposit_accounts.crypto._create(
            wallet_id="wallet_id",
            deposit_config_id="x",
            type="deposit_config",
            deposit_address_strategy="dedicated",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: PrivyAPI) -> None:
        response = client.wallets.deposit_accounts.crypto.with_raw_response._create(
            wallet_id="wallet_id",
            deposit_config_id="x",
            type="deposit_config",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = response.parse()
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: PrivyAPI) -> None:
        with client.wallets.deposit_accounts.crypto.with_streaming_response._create(
            wallet_id="wallet_id",
            deposit_config_id="x",
            type="deposit_config",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = response.parse()
            assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.deposit_accounts.crypto.with_raw_response._create(
                wallet_id="",
                deposit_config_id="x",
                type="deposit_config",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: PrivyAPI) -> None:
        crypto = client.wallets.deposit_accounts.crypto._create(
            wallet_id="wallet_id",
            destination={"asset": "usdc"},
            source={"mode": "all"},
            type="inline_route",
        )
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: PrivyAPI) -> None:
        crypto = client.wallets.deposit_accounts.crypto._create(
            wallet_id="wallet_id",
            destination={
                "asset": "usdc",
                "chain": "tempo",
            },
            source={"mode": "all"},
            type="inline_route",
            deposit_address_strategy="dedicated",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: PrivyAPI) -> None:
        response = client.wallets.deposit_accounts.crypto.with_raw_response._create(
            wallet_id="wallet_id",
            destination={"asset": "usdc"},
            source={"mode": "all"},
            type="inline_route",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = response.parse()
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: PrivyAPI) -> None:
        with client.wallets.deposit_accounts.crypto.with_streaming_response._create(
            wallet_id="wallet_id",
            destination={"asset": "usdc"},
            source={"mode": "all"},
            type="inline_route",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = response.parse()
            assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.deposit_accounts.crypto.with_raw_response._create(
                wallet_id="",
                destination={"asset": "usdc"},
                source={"mode": "all"},
                type="inline_route",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_config(self, client: PrivyAPI) -> None:
        crypto = client.wallets.deposit_accounts.crypto.get_config()
        assert_matches_type(CryptoDepositAccountConfigResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_config(self, client: PrivyAPI) -> None:
        response = client.wallets.deposit_accounts.crypto.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = response.parse()
        assert_matches_type(CryptoDepositAccountConfigResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_config(self, client: PrivyAPI) -> None:
        with client.wallets.deposit_accounts.crypto.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = response.parse()
            assert_matches_type(CryptoDepositAccountConfigResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCrypto:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        crypto = await async_client.wallets.deposit_accounts.crypto.list(
            wallet_id="wallet_id",
        )
        assert_matches_type(AsyncCursor[CryptoDepositAddressRoute], crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        crypto = await async_client.wallets.deposit_accounts.crypto.list(
            wallet_id="wallet_id",
            cursor="x",
            limit=1,
        )
        assert_matches_type(AsyncCursor[CryptoDepositAddressRoute], crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.deposit_accounts.crypto.with_raw_response.list(
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = await response.parse()
        assert_matches_type(AsyncCursor[CryptoDepositAddressRoute], crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.deposit_accounts.crypto.with_streaming_response.list(
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = await response.parse()
            assert_matches_type(AsyncCursor[CryptoDepositAddressRoute], crypto, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.deposit_accounts.crypto.with_raw_response.list(
                wallet_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        crypto = await async_client.wallets.deposit_accounts.crypto._create(
            wallet_id="wallet_id",
            deposit_config_id="x",
            type="deposit_config",
        )
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        crypto = await async_client.wallets.deposit_accounts.crypto._create(
            wallet_id="wallet_id",
            deposit_config_id="x",
            type="deposit_config",
            deposit_address_strategy="dedicated",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.deposit_accounts.crypto.with_raw_response._create(
            wallet_id="wallet_id",
            deposit_config_id="x",
            type="deposit_config",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = await response.parse()
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.deposit_accounts.crypto.with_streaming_response._create(
            wallet_id="wallet_id",
            deposit_config_id="x",
            type="deposit_config",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = await response.parse()
            assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.deposit_accounts.crypto.with_raw_response._create(
                wallet_id="",
                deposit_config_id="x",
                type="deposit_config",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        crypto = await async_client.wallets.deposit_accounts.crypto._create(
            wallet_id="wallet_id",
            destination={"asset": "usdc"},
            source={"mode": "all"},
            type="inline_route",
        )
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        crypto = await async_client.wallets.deposit_accounts.crypto._create(
            wallet_id="wallet_id",
            destination={
                "asset": "usdc",
                "chain": "tempo",
            },
            source={"mode": "all"},
            type="inline_route",
            deposit_address_strategy="dedicated",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.deposit_accounts.crypto.with_raw_response._create(
            wallet_id="wallet_id",
            destination={"asset": "usdc"},
            source={"mode": "all"},
            type="inline_route",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = await response.parse()
        assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.deposit_accounts.crypto.with_streaming_response._create(
            wallet_id="wallet_id",
            destination={"asset": "usdc"},
            source={"mode": "all"},
            type="inline_route",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = await response.parse()
            assert_matches_type(CreateCryptoDepositAccountResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.deposit_accounts.crypto.with_raw_response._create(
                wallet_id="",
                destination={"asset": "usdc"},
                source={"mode": "all"},
                type="inline_route",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_config(self, async_client: AsyncPrivyAPI) -> None:
        crypto = await async_client.wallets.deposit_accounts.crypto.get_config()
        assert_matches_type(CryptoDepositAccountConfigResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_config(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.deposit_accounts.crypto.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = await response.parse()
        assert_matches_type(CryptoDepositAccountConfigResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_config(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.deposit_accounts.crypto.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = await response.parse()
            assert_matches_type(CryptoDepositAccountConfigResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True
