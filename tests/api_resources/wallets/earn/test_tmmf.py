# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from tests.utils import assert_matches_type
from privy.types.wallets import (
    TmmfWalletResponse,
    TmmfPositionResponse,
    TmmfDepositActionResponse,
    TmmfWithdrawActionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTmmf:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deposit(self, client: PrivyAPI) -> None:
        tmmf = client.wallets.earn.tmmf._deposit(
            wallet_id="wallet_id",
            amount="1000.00",
            chain="ethereum_sepolia",
            deposit_asset="USDC",
            fund="WTGXX",
            order_type="secondary",
        )
        assert_matches_type(TmmfDepositActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deposit_with_all_params(self, client: PrivyAPI) -> None:
        tmmf = client.wallets.earn.tmmf._deposit(
            wallet_id="wallet_id",
            amount="1000.00",
            chain="ethereum_sepolia",
            deposit_asset="USDC",
            fund="WTGXX",
            order_type="secondary",
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            reference_id="x",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(TmmfDepositActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deposit(self, client: PrivyAPI) -> None:
        response = client.wallets.earn.tmmf.with_raw_response._deposit(
            wallet_id="wallet_id",
            amount="1000.00",
            chain="ethereum_sepolia",
            deposit_asset="USDC",
            fund="WTGXX",
            order_type="secondary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = response.parse()
        assert_matches_type(TmmfDepositActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deposit(self, client: PrivyAPI) -> None:
        with client.wallets.earn.tmmf.with_streaming_response._deposit(
            wallet_id="wallet_id",
            amount="1000.00",
            chain="ethereum_sepolia",
            deposit_asset="USDC",
            fund="WTGXX",
            order_type="secondary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = response.parse()
            assert_matches_type(TmmfDepositActionResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deposit(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.earn.tmmf.with_raw_response._deposit(
                wallet_id="",
                amount="1000.00",
                chain="ethereum_sepolia",
                deposit_asset="USDC",
                fund="WTGXX",
                order_type="secondary",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_withdraw(self, client: PrivyAPI) -> None:
        tmmf = client.wallets.earn.tmmf._withdraw(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            fund="WTGXX",
            order_type="primary",
            shares="1000.000000",
            withdraw_asset="USDC",
        )
        assert_matches_type(TmmfWithdrawActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_withdraw_with_all_params(self, client: PrivyAPI) -> None:
        tmmf = client.wallets.earn.tmmf._withdraw(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            fund="WTGXX",
            order_type="primary",
            shares="1000.000000",
            withdraw_asset="USDC",
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            reference_id="x",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(TmmfWithdrawActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_withdraw(self, client: PrivyAPI) -> None:
        response = client.wallets.earn.tmmf.with_raw_response._withdraw(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            fund="WTGXX",
            order_type="primary",
            shares="1000.000000",
            withdraw_asset="USDC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = response.parse()
        assert_matches_type(TmmfWithdrawActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_withdraw(self, client: PrivyAPI) -> None:
        with client.wallets.earn.tmmf.with_streaming_response._withdraw(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            fund="WTGXX",
            order_type="primary",
            shares="1000.000000",
            withdraw_asset="USDC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = response.parse()
            assert_matches_type(TmmfWithdrawActionResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_withdraw(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.earn.tmmf.with_raw_response._withdraw(
                wallet_id="",
                chain="ethereum_sepolia",
                fund="WTGXX",
                order_type="primary",
                shares="1000.000000",
                withdraw_asset="USDC",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_positions(self, client: PrivyAPI) -> None:
        tmmf = client.wallets.earn.tmmf.list_positions(
            wallet_id="wallet_id",
        )
        assert_matches_type(TmmfPositionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_positions_with_all_params(self, client: PrivyAPI) -> None:
        tmmf = client.wallets.earn.tmmf.list_positions(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            cursor="x",
            fund="WTGXX",
            limit=1,
            provider="wisdomtree",
        )
        assert_matches_type(TmmfPositionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_positions(self, client: PrivyAPI) -> None:
        response = client.wallets.earn.tmmf.with_raw_response.list_positions(
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = response.parse()
        assert_matches_type(TmmfPositionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_positions(self, client: PrivyAPI) -> None:
        with client.wallets.earn.tmmf.with_streaming_response.list_positions(
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = response.parse()
            assert_matches_type(TmmfPositionResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_positions(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.earn.tmmf.with_raw_response.list_positions(
                wallet_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_register(self, client: PrivyAPI) -> None:
        tmmf = client.wallets.earn.tmmf.register(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            provider="wisdomtree",
        )
        assert_matches_type(TmmfWalletResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_register(self, client: PrivyAPI) -> None:
        response = client.wallets.earn.tmmf.with_raw_response.register(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            provider="wisdomtree",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = response.parse()
        assert_matches_type(TmmfWalletResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_register(self, client: PrivyAPI) -> None:
        with client.wallets.earn.tmmf.with_streaming_response.register(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            provider="wisdomtree",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = response.parse()
            assert_matches_type(TmmfWalletResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_register(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.earn.tmmf.with_raw_response.register(
                wallet_id="",
                chain="ethereum_sepolia",
                provider="wisdomtree",
            )


class TestAsyncTmmf:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deposit(self, async_client: AsyncPrivyAPI) -> None:
        tmmf = await async_client.wallets.earn.tmmf._deposit(
            wallet_id="wallet_id",
            amount="1000.00",
            chain="ethereum_sepolia",
            deposit_asset="USDC",
            fund="WTGXX",
            order_type="secondary",
        )
        assert_matches_type(TmmfDepositActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deposit_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        tmmf = await async_client.wallets.earn.tmmf._deposit(
            wallet_id="wallet_id",
            amount="1000.00",
            chain="ethereum_sepolia",
            deposit_asset="USDC",
            fund="WTGXX",
            order_type="secondary",
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            reference_id="x",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(TmmfDepositActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deposit(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.earn.tmmf.with_raw_response._deposit(
            wallet_id="wallet_id",
            amount="1000.00",
            chain="ethereum_sepolia",
            deposit_asset="USDC",
            fund="WTGXX",
            order_type="secondary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = await response.parse()
        assert_matches_type(TmmfDepositActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deposit(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.earn.tmmf.with_streaming_response._deposit(
            wallet_id="wallet_id",
            amount="1000.00",
            chain="ethereum_sepolia",
            deposit_asset="USDC",
            fund="WTGXX",
            order_type="secondary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = await response.parse()
            assert_matches_type(TmmfDepositActionResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deposit(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.earn.tmmf.with_raw_response._deposit(
                wallet_id="",
                amount="1000.00",
                chain="ethereum_sepolia",
                deposit_asset="USDC",
                fund="WTGXX",
                order_type="secondary",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_withdraw(self, async_client: AsyncPrivyAPI) -> None:
        tmmf = await async_client.wallets.earn.tmmf._withdraw(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            fund="WTGXX",
            order_type="primary",
            shares="1000.000000",
            withdraw_asset="USDC",
        )
        assert_matches_type(TmmfWithdrawActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_withdraw_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        tmmf = await async_client.wallets.earn.tmmf._withdraw(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            fund="WTGXX",
            order_type="primary",
            shares="1000.000000",
            withdraw_asset="USDC",
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            reference_id="x",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(TmmfWithdrawActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_withdraw(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.earn.tmmf.with_raw_response._withdraw(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            fund="WTGXX",
            order_type="primary",
            shares="1000.000000",
            withdraw_asset="USDC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = await response.parse()
        assert_matches_type(TmmfWithdrawActionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_withdraw(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.earn.tmmf.with_streaming_response._withdraw(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            fund="WTGXX",
            order_type="primary",
            shares="1000.000000",
            withdraw_asset="USDC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = await response.parse()
            assert_matches_type(TmmfWithdrawActionResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_withdraw(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.earn.tmmf.with_raw_response._withdraw(
                wallet_id="",
                chain="ethereum_sepolia",
                fund="WTGXX",
                order_type="primary",
                shares="1000.000000",
                withdraw_asset="USDC",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_positions(self, async_client: AsyncPrivyAPI) -> None:
        tmmf = await async_client.wallets.earn.tmmf.list_positions(
            wallet_id="wallet_id",
        )
        assert_matches_type(TmmfPositionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_positions_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        tmmf = await async_client.wallets.earn.tmmf.list_positions(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            cursor="x",
            fund="WTGXX",
            limit=1,
            provider="wisdomtree",
        )
        assert_matches_type(TmmfPositionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_positions(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.earn.tmmf.with_raw_response.list_positions(
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = await response.parse()
        assert_matches_type(TmmfPositionResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_positions(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.earn.tmmf.with_streaming_response.list_positions(
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = await response.parse()
            assert_matches_type(TmmfPositionResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_positions(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.earn.tmmf.with_raw_response.list_positions(
                wallet_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_register(self, async_client: AsyncPrivyAPI) -> None:
        tmmf = await async_client.wallets.earn.tmmf.register(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            provider="wisdomtree",
        )
        assert_matches_type(TmmfWalletResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.earn.tmmf.with_raw_response.register(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            provider="wisdomtree",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tmmf = await response.parse()
        assert_matches_type(TmmfWalletResponse, tmmf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.earn.tmmf.with_streaming_response.register(
            wallet_id="wallet_id",
            chain="ethereum_sepolia",
            provider="wisdomtree",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tmmf = await response.parse()
            assert_matches_type(TmmfWalletResponse, tmmf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_register(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.earn.tmmf.with_raw_response.register(
                wallet_id="",
                chain="ethereum_sepolia",
                provider="wisdomtree",
            )
