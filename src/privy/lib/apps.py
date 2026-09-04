"""Public app operations."""

from __future__ import annotations

from typing import Any, cast

from ..types.app_response import AppResponse
from ..resources.apps.apps import AppsResource
from ..types.allowlist_entry import AllowlistEntry
from ..resources.apps.allowlist import AllowlistListResponse
from ..types.user_invite_input_param import UserInviteInputParam
from ..types.allowlist_deletion_response import AllowlistDeletionResponse

__all__ = ["PrivyAppsService"]


class PrivyAppsService(AppsResource):
    def get_allowlist(self) -> AllowlistListResponse:
        return self.allowlist.list(self._client.app_id)

    def invite_to_allowlist(self, entry: UserInviteInputParam) -> AllowlistEntry:
        create: Any = self.allowlist.create
        return cast(AllowlistEntry, create(self._client.app_id, **entry))

    def remove_from_allowlist(self, entry: UserInviteInputParam) -> AllowlistDeletionResponse:
        delete: Any = self.allowlist.delete
        return cast(AllowlistDeletionResponse, delete(self._client.app_id, **entry))

    def get_settings(self) -> AppResponse:
        return self.get(self._client.app_id)
