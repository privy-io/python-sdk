"""Public user operations."""

from ..resources.users.users import UsersResource

__all__ = ["UsersService"]


class UsersService(UsersResource):
    pass
