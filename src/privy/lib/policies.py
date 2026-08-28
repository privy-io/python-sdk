"""Public policy operations."""

from __future__ import annotations

from typing import Any, Callable, cast

from .._types import omit
from .request_url import build_request_url
from ..types.policy import Policy
from .authorization import prepare_request
from .request_options import PrivyRequestOptions
from ..resources.policies import PoliciesResource
from ..types.policy_update_params import PolicyUpdateParams

__all__ = ["PoliciesService"]


class PoliciesService(PoliciesResource):
    def update(
        self,
        policy_id: str,
        *,
        policy_update_params: PolicyUpdateParams,
        request_options: PrivyRequestOptions | None = None,
    ) -> Policy:
        options = request_options or PrivyRequestOptions()
        client = self._client
        body = dict(policy_update_params)
        prepared = prepare_request(
            app_id=client.app_id,
            method="PATCH",
            url=build_request_url(client, f"/v1/policies/{policy_id}"),
            body=body,
            authorization_context=options.authorization_context,
        )
        signature = prepared.headers.get("privy-authorization-signature")
        generated: Any = self
        update = cast(Callable[..., Policy], generated._update)
        return update(
            policy_id,
            **body,
            privy_authorization_signature=signature if signature is not None else omit,
        )
