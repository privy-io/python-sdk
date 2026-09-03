# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from privy import PrivyAPI, AsyncPrivyAPI
from privy.types import (
    Wallet,
    WalletRpcResponse,
    WalletAuthenticateWithJwtResponse,
    WalletCreateWalletsWithRecoveryResponse,
)
from tests.utils import assert_matches_type
from privy.pagination import SyncCursor, AsyncCursor

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWallets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: PrivyAPI) -> None:
        wallet = client.wallets.create(
            chain_type="ethereum",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: PrivyAPI) -> None:
        wallet = client.wallets.create(
            chain_type="ethereum",
            additional_signers=[
                {
                    "override_policy_ids": ["string"],
                    "signer_id": "signer_id",
                }
            ],
            owner={"public_key": "public_key"},
            owner_id="owner_id",
            policy_ids=["xxxxxxxxxxxxxxxxxxxxxxxx"],
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.create(
            chain_type="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.create(
            chain_type="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(Wallet, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: PrivyAPI) -> None:
        wallet = client.wallets.update(
            wallet_id="wallet_id",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: PrivyAPI) -> None:
        wallet = client.wallets.update(
            wallet_id="wallet_id",
            additional_signers=[
                {
                    "override_policy_ids": ["string"],
                    "signer_id": "signer_id",
                }
            ],
            owner={"public_key": "public_key"},
            owner_id="owner_id",
            policy_ids=["tb54eps4z44ed0jepousxi4n"],
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.update(
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.update(
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(Wallet, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.update(
                wallet_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: PrivyAPI) -> None:
        wallet = client.wallets.list()
        assert_matches_type(SyncCursor[Wallet], wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: PrivyAPI) -> None:
        wallet = client.wallets.list(
            chain_type="solana",
            cursor="x",
            limit=100,
        )
        assert_matches_type(SyncCursor[Wallet], wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(SyncCursor[Wallet], wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(SyncCursor[Wallet], wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_authenticate_with_jwt(self, client: PrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            wallet = client.wallets.authenticate_with_jwt(
                user_jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            )

        assert_matches_type(WalletAuthenticateWithJwtResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_authenticate_with_jwt_with_all_params(self, client: PrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            wallet = client.wallets.authenticate_with_jwt(
                user_jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
                encryption_type="HPKE",
                recipient_public_key="DAQcDQgAEx4aoeD72yykviK+fckqE2CItVIGn1rCnvCXZ1HgpOcMEMialRmTrqIK4oZlYd1",
            )

        assert_matches_type(WalletAuthenticateWithJwtResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_authenticate_with_jwt(self, client: PrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.wallets.with_raw_response.authenticate_with_jwt(
                user_jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletAuthenticateWithJwtResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_authenticate_with_jwt(self, client: PrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            with client.wallets.with_streaming_response.authenticate_with_jwt(
                user_jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                wallet = response.parse()
                assert_matches_type(WalletAuthenticateWithJwtResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_wallets_with_recovery(self, client: PrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            wallet = client.wallets.create_wallets_with_recovery(
                primary_signer={"subject_id": "cm7oxq1el000e11o8iwp7d0d0"},
                recovery_user={
                    "linked_accounts": [
                        {
                            "address": "john@doe.com",
                            "type": "email",
                        }
                    ]
                },
                wallets=[{"chain_type": "ethereum"}, {"chain_type": "solana"}],
            )

        assert_matches_type(WalletCreateWalletsWithRecoveryResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_wallets_with_recovery(self, client: PrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.wallets.with_raw_response.create_wallets_with_recovery(
                primary_signer={"subject_id": "cm7oxq1el000e11o8iwp7d0d0"},
                recovery_user={
                    "linked_accounts": [
                        {
                            "address": "john@doe.com",
                            "type": "email",
                        }
                    ]
                },
                wallets=[{"chain_type": "ethereum"}, {"chain_type": "solana"}],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletCreateWalletsWithRecoveryResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_wallets_with_recovery(self, client: PrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            with client.wallets.with_streaming_response.create_wallets_with_recovery(
                primary_signer={"subject_id": "cm7oxq1el000e11o8iwp7d0d0"},
                recovery_user={
                    "linked_accounts": [
                        {
                            "address": "john@doe.com",
                            "type": "email",
                        }
                    ]
                },
                wallets=[{"chain_type": "ethereum"}, {"chain_type": "solana"}],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                wallet = response.parse()
                assert_matches_type(WalletCreateWalletsWithRecoveryResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: PrivyAPI) -> None:
        wallet = client.wallets.get(
            "wallet_id",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.get(
            "wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.get(
            "wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(Wallet, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_overload_1(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_with_all_params_overload_1(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_signTransaction",
            params={
                "transaction": {
                    "chain_id": "string",
                    "data": "data",
                    "from": "from",
                    "gas_limit": "string",
                    "gas_price": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "to": "to",
                    "type": 0,
                    "value": "string",
                }
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rpc_overload_1(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rpc_overload_1(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rpc_overload_1(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="eth_signTransaction",
                params={"transaction": {}},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_overload_2(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_with_all_params_overload_2(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={
                "transaction": {
                    "chain_id": "string",
                    "data": "data",
                    "from": "from",
                    "gas_limit": "string",
                    "gas_price": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "to": "to",
                    "type": 0,
                    "value": "string",
                }
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rpc_overload_2(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rpc_overload_2(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rpc_overload_2(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.rpc(
                wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="eth_sendTransaction",
                params={"transaction": {}},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_overload_3(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_with_all_params_overload_3(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rpc_overload_3(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rpc_overload_3(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rpc_overload_3(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="personal_sign",
                params={
                    "encoding": "utf-8",
                    "message": "message",
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_overload_4(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_with_all_params_overload_4(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rpc_overload_4(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rpc_overload_4(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rpc_overload_4(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="eth_signTypedData_v4",
                params={
                    "typed_data": {
                        "domain": {"foo": "bar"},
                        "message": {"foo": "bar"},
                        "primary_type": "primary_type",
                        "types": {
                            "foo": [
                                {
                                    "name": "name",
                                    "type": "type",
                                }
                            ]
                        },
                    }
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_overload_5(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_with_all_params_overload_5(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
                "nonce": "string",
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rpc_overload_5(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rpc_overload_5(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rpc_overload_5(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="eth_sign7702Authorization",
                params={
                    "chain_id": "string",
                    "contract": "contract",
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_overload_6(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "hash"},
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_with_all_params_overload_6(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "hash"},
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rpc_overload_6(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "hash"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rpc_overload_6(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "hash"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rpc_overload_6(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="secp256k1_sign",
                params={"hash": "hash"},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_overload_7(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_with_all_params_overload_7(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
            address="address",
            chain_type="solana",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rpc_overload_7(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rpc_overload_7(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rpc_overload_7(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="signTransaction",
                params={
                    "encoding": "base64",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_overload_8(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_with_all_params_overload_8(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
            address="address",
            chain_type="solana",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rpc_overload_8(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rpc_overload_8(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rpc_overload_8(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.rpc(
                wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="signAndSendTransaction",
                params={
                    "encoding": "base64",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_overload_9(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rpc_with_all_params_overload_9(self, client: PrivyAPI) -> None:
        wallet = client.wallets.rpc(
            wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
            address="address",
            chain_type="solana",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rpc_overload_9(self, client: PrivyAPI) -> None:
        response = client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rpc_overload_9(self, client: PrivyAPI) -> None:
        with client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rpc_overload_9(self, client: PrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="signMessage",
                params={
                    "encoding": "base64",
                    "message": "message",
                },
            )


class TestAsyncWallets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.create(
            chain_type="ethereum",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.create(
            chain_type="ethereum",
            additional_signers=[
                {
                    "override_policy_ids": ["string"],
                    "signer_id": "signer_id",
                }
            ],
            owner={"public_key": "public_key"},
            owner_id="owner_id",
            policy_ids=["xxxxxxxxxxxxxxxxxxxxxxxx"],
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.create(
            chain_type="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.create(
            chain_type="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(Wallet, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.update(
            wallet_id="wallet_id",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.update(
            wallet_id="wallet_id",
            additional_signers=[
                {
                    "override_policy_ids": ["string"],
                    "signer_id": "signer_id",
                }
            ],
            owner={"public_key": "public_key"},
            owner_id="owner_id",
            policy_ids=["tb54eps4z44ed0jepousxi4n"],
            privy_authorization_signature="privy-authorization-signature",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.update(
            wallet_id="wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.update(
            wallet_id="wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(Wallet, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.update(
                wallet_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.list()
        assert_matches_type(AsyncCursor[Wallet], wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.list(
            chain_type="solana",
            cursor="x",
            limit=100,
        )
        assert_matches_type(AsyncCursor[Wallet], wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(AsyncCursor[Wallet], wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(AsyncCursor[Wallet], wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_authenticate_with_jwt(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            wallet = await async_client.wallets.authenticate_with_jwt(
                user_jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            )

        assert_matches_type(WalletAuthenticateWithJwtResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_authenticate_with_jwt_with_all_params(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            wallet = await async_client.wallets.authenticate_with_jwt(
                user_jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
                encryption_type="HPKE",
                recipient_public_key="DAQcDQgAEx4aoeD72yykviK+fckqE2CItVIGn1rCnvCXZ1HgpOcMEMialRmTrqIK4oZlYd1",
            )

        assert_matches_type(WalletAuthenticateWithJwtResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_authenticate_with_jwt(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.wallets.with_raw_response.authenticate_with_jwt(
                user_jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletAuthenticateWithJwtResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_authenticate_with_jwt(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.wallets.with_streaming_response.authenticate_with_jwt(
                user_jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                wallet = await response.parse()
                assert_matches_type(WalletAuthenticateWithJwtResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_wallets_with_recovery(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            wallet = await async_client.wallets.create_wallets_with_recovery(
                primary_signer={"subject_id": "cm7oxq1el000e11o8iwp7d0d0"},
                recovery_user={
                    "linked_accounts": [
                        {
                            "address": "john@doe.com",
                            "type": "email",
                        }
                    ]
                },
                wallets=[{"chain_type": "ethereum"}, {"chain_type": "solana"}],
            )

        assert_matches_type(WalletCreateWalletsWithRecoveryResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_wallets_with_recovery(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.wallets.with_raw_response.create_wallets_with_recovery(
                primary_signer={"subject_id": "cm7oxq1el000e11o8iwp7d0d0"},
                recovery_user={
                    "linked_accounts": [
                        {
                            "address": "john@doe.com",
                            "type": "email",
                        }
                    ]
                },
                wallets=[{"chain_type": "ethereum"}, {"chain_type": "solana"}],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletCreateWalletsWithRecoveryResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_wallets_with_recovery(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.wallets.with_streaming_response.create_wallets_with_recovery(
                primary_signer={"subject_id": "cm7oxq1el000e11o8iwp7d0d0"},
                recovery_user={
                    "linked_accounts": [
                        {
                            "address": "john@doe.com",
                            "type": "email",
                        }
                    ]
                },
                wallets=[{"chain_type": "ethereum"}, {"chain_type": "solana"}],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                wallet = await response.parse()
                assert_matches_type(WalletCreateWalletsWithRecoveryResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.get(
            "wallet_id",
        )
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.get(
            "wallet_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(Wallet, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.get(
            "wallet_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(Wallet, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_with_all_params_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_signTransaction",
            params={
                "transaction": {
                    "chain_id": "string",
                    "data": "data",
                    "from": "from",
                    "gas_limit": "string",
                    "gas_price": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "to": "to",
                    "type": 0,
                    "value": "string",
                }
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rpc_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rpc_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="eth_signTransaction",
            params={"transaction": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rpc_overload_1(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="eth_signTransaction",
                params={"transaction": {}},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_with_all_params_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={
                "transaction": {
                    "chain_id": "string",
                    "data": "data",
                    "from": "from",
                    "gas_limit": "string",
                    "gas_price": "string",
                    "max_fee_per_gas": "string",
                    "max_priority_fee_per_gas": "string",
                    "nonce": "string",
                    "to": "to",
                    "type": 0,
                    "value": "string",
                }
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rpc_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rpc_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="eth_sendTransaction",
            params={"transaction": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rpc_overload_2(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.rpc(
                wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="eth_sendTransaction",
                params={"transaction": {}},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_with_all_params_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rpc_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rpc_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="personal_sign",
            params={
                "encoding": "utf-8",
                "message": "message",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rpc_overload_3(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="personal_sign",
                params={
                    "encoding": "utf-8",
                    "message": "message",
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_with_all_params_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rpc_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rpc_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="eth_signTypedData_v4",
            params={
                "typed_data": {
                    "domain": {"foo": "bar"},
                    "message": {"foo": "bar"},
                    "primary_type": "primary_type",
                    "types": {
                        "foo": [
                            {
                                "name": "name",
                                "type": "type",
                            }
                        ]
                    },
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rpc_overload_4(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="eth_signTypedData_v4",
                params={
                    "typed_data": {
                        "domain": {"foo": "bar"},
                        "message": {"foo": "bar"},
                        "primary_type": "primary_type",
                        "types": {
                            "foo": [
                                {
                                    "name": "name",
                                    "type": "type",
                                }
                            ]
                        },
                    }
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_with_all_params_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
                "nonce": "string",
            },
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rpc_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rpc_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="eth_sign7702Authorization",
            params={
                "chain_id": "string",
                "contract": "contract",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rpc_overload_5(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="eth_sign7702Authorization",
                params={
                    "chain_id": "string",
                    "contract": "contract",
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "hash"},
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_with_all_params_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "hash"},
            address="address",
            chain_type="ethereum",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rpc_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "hash"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rpc_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="secp256k1_sign",
            params={"hash": "hash"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rpc_overload_6(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="secp256k1_sign",
                params={"hash": "hash"},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_with_all_params_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
            address="address",
            chain_type="solana",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rpc_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rpc_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="signTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rpc_overload_7(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="signTransaction",
                params={
                    "encoding": "base64",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_with_all_params_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
            address="address",
            chain_type="solana",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rpc_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rpc_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            caip2="-l-f12-k:_--l__36_",
            method="signAndSendTransaction",
            params={
                "encoding": "base64",
                "transaction": "transaction",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rpc_overload_8(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.rpc(
                wallet_id="",
                caip2="-l-f12-k:_--l__36_",
                method="signAndSendTransaction",
                params={
                    "encoding": "base64",
                    "transaction": "transaction",
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rpc_with_all_params_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        wallet = await async_client.wallets.rpc(
            wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
            address="address",
            chain_type="solana",
            privy_authorization_signature="privy-authorization-signature",
            privy_idempotency_key="privy-idempotency-key",
        )
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rpc_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        response = await async_client.wallets.with_raw_response.rpc(
            wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRpcResponse, wallet, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rpc_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        async with async_client.wallets.with_streaming_response.rpc(
            wallet_id="wallet_id",
            method="signMessage",
            params={
                "encoding": "base64",
                "message": "message",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRpcResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rpc_overload_9(self, async_client: AsyncPrivyAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.wallets.with_raw_response.rpc(
                wallet_id="",
                method="signMessage",
                params={
                    "encoding": "base64",
                    "message": "message",
                },
            )
