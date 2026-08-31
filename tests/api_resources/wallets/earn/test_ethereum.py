# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from tests.utils import assert_matches_type
from privy.types.wallets import (
    EarnDepositActionResponse,
    EarnWithdrawActionResponse,
    EthereumEarnPositionResponse,
    EthereumEarnVaultDetailsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEthereum:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deposit(self, client: PrivyAPI) -> None:
        ethereum = client.wallets.earn.ethereum._deposit(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        )
        assert_matches_type(EarnDepositActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deposit_with_all_params(self, client: PrivyAPI) -> None:
        ethereum = client.wallets.earn.ethereum._deposit(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
            amount="1.5",
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            raw_amount="321669910225",
            reference_id="x",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(EarnDepositActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deposit(self, client: PrivyAPI) -> None:
        response = client.wallets.earn.ethereum.with_raw_response._deposit(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ethereum = response.parse()
        assert_matches_type(EarnDepositActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deposit(self, client: PrivyAPI) -> None:
        with client.wallets.earn.ethereum.with_streaming_response._deposit(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ethereum = response.parse()
            assert_matches_type(EarnDepositActionResponse, ethereum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deposit(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.earn.ethereum.with_raw_response._deposit(
                wallet_id="",
                vault_id="cm7oxq1el000e11o8iwp7d0d0",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_withdraw(self, client: PrivyAPI) -> None:
        ethereum = client.wallets.earn.ethereum._withdraw(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        )
        assert_matches_type(EarnWithdrawActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_withdraw_with_all_params(self, client: PrivyAPI) -> None:
        ethereum = client.wallets.earn.ethereum._withdraw(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
            amount="1.5",
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            raw_amount="321669910225",
            reference_id="x",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(EarnWithdrawActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_withdraw(self, client: PrivyAPI) -> None:
        response = client.wallets.earn.ethereum.with_raw_response._withdraw(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ethereum = response.parse()
        assert_matches_type(EarnWithdrawActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_withdraw(self, client: PrivyAPI) -> None:
        with client.wallets.earn.ethereum.with_streaming_response._withdraw(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ethereum = response.parse()
            assert_matches_type(EarnWithdrawActionResponse, ethereum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_withdraw(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.earn.ethereum.with_raw_response._withdraw(
                wallet_id="",
                vault_id="cm7oxq1el000e11o8iwp7d0d0",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_vault_details(self, client: PrivyAPI) -> None:
        ethereum = client.wallets.earn.ethereum.vault_details(
            "vault_id",
        )
        assert_matches_type(EthereumEarnVaultDetailsResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_vault_details(self, client: PrivyAPI) -> None:
        response = client.wallets.earn.ethereum.with_raw_response.vault_details(
            "vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ethereum = response.parse()
        assert_matches_type(EthereumEarnVaultDetailsResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_vault_details(self, client: PrivyAPI) -> None:
        with client.wallets.earn.ethereum.with_streaming_response.vault_details(
            "vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ethereum = response.parse()
            assert_matches_type(EthereumEarnVaultDetailsResponse, ethereum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_vault_details(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vault_id` but received ''"):
            client.wallets.earn.ethereum.with_raw_response.vault_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_vault_position(self, client: PrivyAPI) -> None:
        ethereum = client.wallets.earn.ethereum.vault_position(
            wallet_id="wallet_id",
            vault_id="vault_id",
        )
        assert_matches_type(EthereumEarnPositionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_vault_position_with_all_params(self, client: PrivyAPI) -> None:
        ethereum = client.wallets.earn.ethereum.vault_position(
            wallet_id="wallet_id",
            vault_id="vault_id",
            include_archived=True,
        )
        assert_matches_type(EthereumEarnPositionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_vault_position(self, client: PrivyAPI) -> None:
        response = client.wallets.earn.ethereum.with_raw_response.vault_position(
            wallet_id="wallet_id",
            vault_id="vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ethereum = response.parse()
        assert_matches_type(EthereumEarnPositionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_vault_position(self, client: PrivyAPI) -> None:
        with client.wallets.earn.ethereum.with_streaming_response.vault_position(
            wallet_id="wallet_id",
            vault_id="vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ethereum = response.parse()
            assert_matches_type(EthereumEarnPositionResponse, ethereum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_vault_position(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.earn.ethereum.with_raw_response.vault_position(
                wallet_id="",
                vault_id="vault_id",
            )


class TestAsyncEthereum:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deposit(self, async_client: AsyncPrivyAPI) -> None:
        ethereum = await async_client.wallets.earn.ethereum._deposit(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        )
        assert_matches_type(EarnDepositActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deposit_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        ethereum = await async_client.wallets.earn.ethereum._deposit(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
            amount="1.5",
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            raw_amount="321669910225",
            reference_id="x",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(EarnDepositActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deposit(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.earn.ethereum.with_raw_response._deposit(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ethereum = await response.parse()
        assert_matches_type(EarnDepositActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deposit(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.earn.ethereum.with_streaming_response._deposit(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ethereum = await response.parse()
            assert_matches_type(EarnDepositActionResponse, ethereum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deposit(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.earn.ethereum.with_raw_response._deposit(
                wallet_id="",
                vault_id="cm7oxq1el000e11o8iwp7d0d0",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_withdraw(self, async_client: AsyncPrivyAPI) -> None:
        ethereum = await async_client.wallets.earn.ethereum._withdraw(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        )
        assert_matches_type(EarnWithdrawActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_withdraw_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        ethereum = await async_client.wallets.earn.ethereum._withdraw(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
            amount="1.5",
            nonce="xxxxxxxxxxxxxxxxxxxxxxxx",
            raw_amount="321669910225",
            reference_id="x",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
            privy_request_expiry="privy-request-expiry",
        )
        assert_matches_type(EarnWithdrawActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_withdraw(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.earn.ethereum.with_raw_response._withdraw(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ethereum = await response.parse()
        assert_matches_type(EarnWithdrawActionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_withdraw(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.earn.ethereum.with_streaming_response._withdraw(
            wallet_id="wallet_id",
            vault_id="cm7oxq1el000e11o8iwp7d0d0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ethereum = await response.parse()
            assert_matches_type(EarnWithdrawActionResponse, ethereum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_withdraw(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.earn.ethereum.with_raw_response._withdraw(
                wallet_id="",
                vault_id="cm7oxq1el000e11o8iwp7d0d0",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_vault_details(self, async_client: AsyncPrivyAPI) -> None:
        ethereum = await async_client.wallets.earn.ethereum.vault_details(
            "vault_id",
        )
        assert_matches_type(EthereumEarnVaultDetailsResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_vault_details(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.earn.ethereum.with_raw_response.vault_details(
            "vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ethereum = await response.parse()
        assert_matches_type(EthereumEarnVaultDetailsResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_vault_details(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.earn.ethereum.with_streaming_response.vault_details(
            "vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ethereum = await response.parse()
            assert_matches_type(EthereumEarnVaultDetailsResponse, ethereum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_vault_details(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vault_id` but received ''"):
            await async_client.wallets.earn.ethereum.with_raw_response.vault_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_vault_position(self, async_client: AsyncPrivyAPI) -> None:
        ethereum = await async_client.wallets.earn.ethereum.vault_position(
            wallet_id="wallet_id",
            vault_id="vault_id",
        )
        assert_matches_type(EthereumEarnPositionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_vault_position_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        ethereum = await async_client.wallets.earn.ethereum.vault_position(
            wallet_id="wallet_id",
            vault_id="vault_id",
            include_archived=True,
        )
        assert_matches_type(EthereumEarnPositionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_vault_position(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.earn.ethereum.with_raw_response.vault_position(
            wallet_id="wallet_id",
            vault_id="vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ethereum = await response.parse()
        assert_matches_type(EthereumEarnPositionResponse, ethereum, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_vault_position(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.earn.ethereum.with_streaming_response.vault_position(
            wallet_id="wallet_id",
            vault_id="vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ethereum = await response.parse()
            assert_matches_type(EthereumEarnPositionResponse, ethereum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_vault_position(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.earn.ethereum.with_raw_response.vault_position(
                wallet_id="",
                vault_id="vault_id",
            )
