"""Public wallet operations."""

from __future__ import annotations

import base64
from typing import Any, Union, Literal, Callable, TypedDict, cast
from typing_extensions import TypeAlias, override

from pyhpke import PyHPKEError

from .tron import PrivyTronService
from ._hpke import HPKESender, HPKERecipient
from .solana import PrivySolanaService
from .._types import Omit, omit
from .._client import PrivyAPI
from .ethereum import PrivyEthereumService
from .request_url import build_request_url
from .._exceptions import PrivyAPIError
from .jwt_exchange import JWTExchangeService
from ..types.wallet import Wallet
from .authorization import prepare_request
from .request_expiry import RequestExpiryProvider, resolve_request_expiry
from .wallet_entropy import entropy_to_bytes
from .request_options import PrivyRequestOptions
from ..types.owner_id_input import OwnerIDInput
from ..types.owner_input_param import OwnerInputParam
from ..types.raw_sign_response import RawSignResponse
from ..types.wallet_rpc_params import WalletRpcParams
from ..types.policy_input_param import PolicyInputParam
from ..resources.wallets.wallets import WalletsResource
from ..types.wallet_rpc_response import WalletRpcResponse
from ..types.wallet_update_params import WalletUpdateParams
from ..types.wallet_raw_sign_params import WalletRawSignParams
from ..types.wallet_transfer_params import WalletTransferParams
from ..types.additional_signer_input_param import AdditionalSignerInputParam
from ..types.wallet_import_supported_chains import WalletImportSupportedChains
from ..types.wallets.transfer_action_response import TransferActionResponse
from ..types.wallet_entity_assignment_request_body_param import WalletEntityAssignmentRequestBodyParam

__all__ = [
    "ExportPrivateKeyResponse",
    "ExportSeedPhraseResponse",
    "HDWalletImport",
    "PrivateKeyWalletImport",
    "WalletImport",
    "PrivyWalletsService",
]


class ExportPrivateKeyResponse(TypedDict):
    private_key: str


class ExportSeedPhraseResponse(TypedDict):
    seed_phrase: str


class HDWalletImport(TypedDict):
    """An HD wallet seed phrase and derivation index to import."""

    address: str
    chain_type: WalletImportSupportedChains
    entropy_type: Literal["hd"]
    private_key: Union[str, bytes, bytearray]
    index: int


class PrivateKeyWalletImport(TypedDict):
    """A chain-specific private key to import."""

    address: str
    chain_type: WalletImportSupportedChains
    entropy_type: Literal["private-key"]
    private_key: Union[str, bytes, bytearray]


WalletImport: TypeAlias = Union[HDWalletImport, PrivateKeyWalletImport]


class PrivyWalletsService(WalletsResource):
    def __init__(
        self,
        client: PrivyAPI,
        jwt_exchanger: JWTExchangeService | None = None,
        request_expiry_provider: RequestExpiryProvider | None = None,
    ) -> None:
        super().__init__(client)
        self._jwt_exchanger = jwt_exchanger
        self._request_expiry_provider = request_expiry_provider
        self.ethereum = PrivyEthereumService(self)
        self.solana = PrivySolanaService(self)
        self.tron = PrivyTronService(self)

    @override
    def create(
        self,
        *,
        idempotency_key: str | None = None,
        **params: Any,
    ) -> Wallet:
        generated_params: dict[str, Any] = dict(params)
        generated_idempotency_key = generated_params.pop("privy_idempotency_key", omit)
        if idempotency_key is not None and generated_idempotency_key is not omit:
            raise TypeError("idempotency_key and privy_idempotency_key cannot both be supplied")
        generated: Any = super()
        create = cast(Callable[..., Wallet], generated.create)
        return create(
            **generated_params,
            privy_idempotency_key=(idempotency_key if idempotency_key is not None else generated_idempotency_key),
        )

    def import_wallet(
        self,
        *,
        wallet: WalletImport,
        additional_signers: AdditionalSignerInputParam | Omit = omit,
        display_name: str | Omit = omit,
        entity: WalletEntityAssignmentRequestBodyParam | Omit = omit,
        external_id: str | Omit = omit,
        owner: OwnerInputParam | None | Omit = omit,
        owner_id: OwnerIDInput | None | Omit = omit,
        policy_ids: PolicyInputParam | Omit = omit,
    ) -> Wallet:
        """Securely import a private-key or HD wallet using Privy's HPKE flow."""

        import_wallet = cast(dict[str, Any], dict(wallet))
        private_key = cast(Union[str, bytes, bytearray], import_wallet.pop("private_key"))
        if "hpke_config" in import_wallet:
            raise PrivyAPIError("wallet.hpke_config is not supported: encryption parameters are fixed by the SDK")

        entropy_type = cast(str, import_wallet["entropy_type"])
        chain_type = cast(WalletImportSupportedChains, import_wallet["chain_type"])
        entropy = entropy_to_bytes(private_key, entropy_type=entropy_type, chain_type=chain_type)

        generated: Any = self
        init_import = cast(Callable[..., Any], generated._init_import)
        init_response = init_import(**import_wallet, encryption_type="HPKE")
        if init_response.encryption_type != "HPKE":
            raise PrivyAPIError(f"Invalid encryption type: {init_response.encryption_type}")

        encryption_public_key = base64.b64decode(init_response.encryption_public_key, validate=True)
        encapsulated_key, ciphertext = HPKESender().encrypt(encryption_public_key, entropy)
        encrypted_wallet = {
            **import_wallet,
            "encryption_type": "HPKE",
            "encapsulated_key": base64.b64encode(encapsulated_key).decode("ascii"),
            "ciphertext": base64.b64encode(ciphertext).decode("ascii"),
        }
        submit_import = cast(Callable[..., Wallet], generated._submit_import)
        return submit_import(
            wallet=encrypted_wallet,
            additional_signers=additional_signers,
            display_name=display_name,
            entity=entity,
            external_id=external_id,
            owner=owner,
            owner_id=owner_id,
            policy_ids=policy_ids,
        )

    def update(
        self,
        wallet_id: str,
        *,
        wallet_update_params: WalletUpdateParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> Wallet:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        body = dict(wallet_update_params)
        prepared = prepare_request(
            app_id=client.app_id,
            method="PATCH",
            url=build_request_url(client, f"/v1/wallets/{wallet_id}"),
            body=body,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        update = cast(Callable[..., Wallet], generated._update)
        return update(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def export_private_key(
        self,
        wallet_id: str,
        *,
        request_options: PrivyRequestOptions | None = None,
    ) -> ExportPrivateKeyResponse:
        """Securely export a wallet's private key using HPKE."""

        private_key = self._export_decrypted(
            wallet_id,
            export_seed_phrase=False,
            request_options=request_options,
        )
        return {"private_key": private_key}

    def export_seed_phrase(
        self,
        wallet_id: str,
        *,
        request_options: PrivyRequestOptions | None = None,
    ) -> ExportSeedPhraseResponse:
        """Securely export a wallet's seed phrase using HPKE."""

        seed_phrase = self._export_decrypted(
            wallet_id,
            export_seed_phrase=True,
            request_options=request_options,
        )
        return {"seed_phrase": seed_phrase}

    def _export_decrypted(
        self,
        wallet_id: str,
        *,
        export_seed_phrase: bool,
        request_options: PrivyRequestOptions | None,
    ) -> str:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        recipient = HPKERecipient()
        body = {
            "encryption_type": "HPKE",
            "recipient_public_key": recipient.public_key_spki_base64,
            "export_seed_phrase": export_seed_phrase,
        }
        client = self._client
        prepared = prepare_request(
            app_id=client.app_id,
            method="POST",
            url=build_request_url(client, f"/v1/wallets/{wallet_id}/export"),
            body=body,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        expiry_header = prepared.headers.get("privy-request-expiry")
        response = self._export(
            wallet_id,
            encryption_type="HPKE",
            recipient_public_key=recipient.public_key_spki_base64,
            export_seed_phrase=export_seed_phrase,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )
        if response.encryption_type != "HPKE":
            raise PrivyAPIError("Wallet export failed: unsupported encryption type")

        try:
            return recipient.decrypt_base64(response.encapsulated_key, response.ciphertext).decode("utf-8")
        except (PyHPKEError, ValueError, UnicodeDecodeError) as exc:
            raise PrivyAPIError("Wallet export failed: invalid encrypted wallet data") from exc

    def rpc(
        self,
        wallet_id: str,
        *,
        wallet_rpc_request_body: WalletRpcParams,
        idempotency_key: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> WalletRpcResponse:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        body = dict(wallet_rpc_request_body)
        client_values: Any = client
        base_url = client_values.base_url
        prepared = prepare_request(
            app_id=client.app_id,
            method="POST",
            url=f"{str(base_url).rstrip('/')}/v1/wallets/{wallet_id}/rpc",
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
        rpc = cast(Callable[..., WalletRpcResponse], generated._rpc)
        return rpc(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_idempotency_key=idempotency_header if idempotency_header is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def transfer(
        self,
        wallet_id: str,
        *,
        wallet_transfer_params: WalletTransferParams,
        idempotency_key: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> TransferActionResponse:
        """Transfer tokens from a wallet to a destination address."""

        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        body = dict(wallet_transfer_params)
        prepared = prepare_request(
            app_id=self._client.app_id,
            method="POST",
            url=build_request_url(self._client, f"/v1/wallets/{wallet_id}/transfer"),
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
        transfer = cast(Callable[..., TransferActionResponse], generated._transfer)
        return transfer(
            wallet_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
            privy_idempotency_key=idempotency_header if idempotency_header is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )

    def raw_sign(
        self,
        wallet_id: str,
        *,
        wallet_raw_sign_params: WalletRawSignParams,
        idempotency_key: str | None = None,
        request_options: PrivyRequestOptions | None = None,
    ) -> RawSignResponse:
        options = request_options or PrivyRequestOptions()
        request_expiry = resolve_request_expiry(options.request_expiry, self._request_expiry_provider)
        client = self._client
        prepared = prepare_request(
            app_id=client.app_id,
            method="POST",
            url=build_request_url(client, f"/v1/wallets/{wallet_id}/raw_sign"),
            body=dict(wallet_raw_sign_params),
            idempotency_key=idempotency_key,
            authorization_context=options.authorization_context,
            request_expiry=request_expiry,
            jwt_exchanger=self._jwt_exchanger,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        idempotency_header = prepared.headers.get("privy-idempotency-key")
        expiry_header = prepared.headers.get("privy-request-expiry")
        generated: Any = self
        raw_sign = cast(Callable[..., RawSignResponse], generated._raw_sign)
        return raw_sign(
            wallet_id,
            params=wallet_raw_sign_params["params"],
            privy_authorization_signature=signature if signature is not None else omit,
            privy_idempotency_key=idempotency_header if idempotency_header is not None else omit,
            privy_request_expiry=expiry_header if expiry_header is not None else omit,
        )
