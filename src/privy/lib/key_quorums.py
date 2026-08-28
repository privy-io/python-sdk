"""Public key quorum operations."""

from __future__ import annotations

from typing import Any, Callable, cast

from .._types import omit
from .request_url import build_request_url
from .authorization import prepare_request
from .request_options import PrivyRequestOptions
from ..types.key_quorum import KeyQuorum
from ..types.key_quorum_id import KeyQuorumID
from ..resources.key_quorums import KeyQuorumsResource
from ..types.success_response import SuccessResponse
from ..types.key_quorum_update_params import KeyQuorumUpdateParams

__all__ = ["KeyQuorumsService"]


class KeyQuorumsService(KeyQuorumsResource):
    def update(
        self,
        key_quorum_id: KeyQuorumID,
        *,
        key_quorum_update_params: KeyQuorumUpdateParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> KeyQuorum:
        options = request_options or PrivyRequestOptions()
        client = self._client
        body = dict(key_quorum_update_params)
        prepared = prepare_request(
            app_id=client.app_id,
            method="PATCH",
            url=build_request_url(client, f"/v1/key_quorums/{key_quorum_id}"),
            body=body,
            authorization_context=options.authorization_context,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        generated: Any = self
        update = cast(Callable[..., KeyQuorum], generated._update)
        return update(
            key_quorum_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
        )

    def delete(
        self,
        key_quorum_id: KeyQuorumID,
        *,
        request_options: PrivyRequestOptions | None = None,
    ) -> SuccessResponse:
        options = request_options or PrivyRequestOptions()
        client = self._client
        prepared = prepare_request(
            app_id=client.app_id,
            method="DELETE",
            url=build_request_url(client, f"/v1/key_quorums/{key_quorum_id}"),
            body={},
            authorization_context=options.authorization_context,
            preserve_empty_body=True,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        generated: Any = self
        delete = cast(Callable[..., SuccessResponse], generated._delete_key_quorum)
        return delete(
            key_quorum_id,
            privy_authorization_signature=signature if signature is not None else omit,
        )
