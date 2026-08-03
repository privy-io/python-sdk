# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .sms_mfa_method import SMSMfaMethod
from .totp_mfa_method import TotpMfaMethod
from .email_mfa_method import EmailMfaMethod
from .passkey_mfa_method import PasskeyMfaMethod

__all__ = ["LinkedMfaMethod"]

LinkedMfaMethod: TypeAlias = Annotated[
    Union[SMSMfaMethod, TotpMfaMethod, PasskeyMfaMethod, EmailMfaMethod], PropertyInfo(discriminator="type")
]
