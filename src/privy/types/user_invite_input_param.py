# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .email_invite_input_param import EmailInviteInputParam
from .phone_invite_input_param import PhoneInviteInputParam
from .wallet_invite_input_param import WalletInviteInputParam
from .email_domain_invite_input_param import EmailDomainInviteInputParam

__all__ = ["UserInviteInputParam"]

UserInviteInputParam: TypeAlias = Union[
    EmailInviteInputParam, EmailDomainInviteInputParam, WalletInviteInputParam, PhoneInviteInputParam
]
