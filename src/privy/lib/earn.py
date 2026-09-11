"""Authorized wallet earn operations."""

from __future__ import annotations

from typing import Any, Callable, cast
from typing_extensions import override

from .._types import omit
from .._client import PrivyAPI
from .request_url import build_request_url
from .jwt_exchange import JWTExchangeService
from .authorization import prepare_request
from .request_expiry import RequestExpiryProvider, resolve_request_expiry
from .request_options import PrivyRequestOptions
from ..resources.wallets.earn.earn import EarnResource
from ..resources.wallets.earn.ethereum.ethereum import EthereumResource
from ..resources.wallets.earn.ethereum.incentive import IncentiveResource
from ..types.wallets.earn.ethereum_deposit_params import EthereumDepositParams
from ..types.wallets.earn_deposit_action_response import EarnDepositActionResponse
from ..types.wallets.earn.ethereum_withdraw_params import EthereumWithdrawParams
from ..types.wallets.earn_withdraw_action_response import EarnWithdrawActionResponse
from ..types.wallets.earn.ethereum.incentive_claim_params import IncentiveClaimParams
from ..types.wallets.earn_incentive_claim_action_response import EarnIncentiveClaimActionResponse

__all__ = [
    "PrivyEarnService",
    "PrivyEarnEthereumService",
    "PrivyEarnEthereumIncentiveService",
]


class PrivyEarnEthereumIncentiveService(IncentiveResource):
    """Authorized Ethereum earn incentive operations."""

    def __init__(
        self,
        client: PrivyAPI,
        jwt_exchanger: JWTExchangeService | None = None,
        request_expiry_provider: RequestExpiryProvider | None = None,
    ) -> None:
        super().__init__(client)
        self._jwt_exchanger = jwt_exchanger
        self._request_expiry_provider = request_expiry_provider

    def claim(
        self,
        wallet_id: str,
        *,
        incentive_claim_params: IncentiveClaimParams,
        idempotency_key: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> EarnIncentiveClaimActionResponse:
        """Claim incentive rewards for an Ethereum wallet."""

        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        body = dict(incentive_claim_params)
        prepared = prepare_request(
            app_id=self._client.app_id,
            method="POST",
            url=build_request_url(
                self._client,
                f"/v1/wallets/{wallet_id}/earn/ethereum/incentive/claim",
            ),
            body=body,
            idempotency_key=idempotency_key,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        idempotency_header = prepared.headers.get("privy-idempotency-key")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        claim = cast(Callable[..., EarnIncentiveClaimActionResponse], generated._claim)
        return claim(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_idempotency_key=idempotency_header if idempotency_header is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )


class PrivyEarnEthereumService(EthereumResource):
    """Authorized Ethereum earn operations."""

    def __init__(
        self,
        client: PrivyAPI,
        jwt_exchanger: JWTExchangeService | None = None,
        request_expiry_provider: RequestExpiryProvider | None = None,
    ) -> None:
        super().__init__(client)
        self._jwt_exchanger = jwt_exchanger
        self._request_expiry_provider = request_expiry_provider
        self._incentive = PrivyEarnEthereumIncentiveService(
            client,
            jwt_exchanger,
            request_expiry_provider,
        )

    @property
    @override
    def incentive(self) -> PrivyEarnEthereumIncentiveService:
        return self._incentive

    def deposit(
        self,
        wallet_id: str,
        *,
        ethereum_deposit_params: EthereumDepositParams,
        idempotency_key: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> EarnDepositActionResponse:
        """Deposit assets from an Ethereum wallet into an earn vault."""

        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        body = dict(ethereum_deposit_params)
        prepared = prepare_request(
            app_id=self._client.app_id,
            method="POST",
            url=build_request_url(
                self._client,
                f"/v1/wallets/{wallet_id}/earn/ethereum/deposit",
            ),
            body=body,
            idempotency_key=idempotency_key,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        idempotency_header = prepared.headers.get("privy-idempotency-key")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        deposit = cast(Callable[..., EarnDepositActionResponse], generated._deposit)
        return deposit(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_idempotency_key=idempotency_header if idempotency_header is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def withdraw(
        self,
        wallet_id: str,
        *,
        ethereum_withdraw_params: EthereumWithdrawParams,
        idempotency_key: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> EarnWithdrawActionResponse:
        """Withdraw assets from an earn vault into an Ethereum wallet."""

        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        body = dict(ethereum_withdraw_params)
        prepared = prepare_request(
            app_id=self._client.app_id,
            method="POST",
            url=build_request_url(
                self._client,
                f"/v1/wallets/{wallet_id}/earn/ethereum/withdraw",
            ),
            body=body,
            idempotency_key=idempotency_key,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        idempotency_header = prepared.headers.get("privy-idempotency-key")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        withdraw = cast(Callable[..., EarnWithdrawActionResponse], generated._withdraw)
        return withdraw(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_idempotency_key=idempotency_header if idempotency_header is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )


class PrivyEarnService(EarnResource):
    """First-class wallet earn service."""

    def __init__(
        self,
        client: PrivyAPI,
        jwt_exchanger: JWTExchangeService | None = None,
        request_expiry_provider: RequestExpiryProvider | None = None,
    ) -> None:
        super().__init__(client)
        self._ethereum = PrivyEarnEthereumService(
            client,
            jwt_exchanger,
            request_expiry_provider,
        )

    @property
    @override
    def ethereum(self) -> PrivyEarnEthereumService:
        return self._ethereum
