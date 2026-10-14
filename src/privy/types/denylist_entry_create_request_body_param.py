# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .denylist_email_input_param import DenylistEmailInputParam
from .denylist_phone_input_param import DenylistPhoneInputParam
from .denylist_email_domain_input_param import DenylistEmailDomainInputParam
from .denylist_solana_address_input_param import DenylistSolanaAddressInputParam
from .denylist_ethereum_address_input_param import DenylistEthereumAddressInputParam

__all__ = ["DenylistEntryCreateRequestBodyParam"]

DenylistEntryCreateRequestBodyParam: TypeAlias = Union[
    DenylistEmailInputParam,
    DenylistEmailDomainInputParam,
    DenylistPhoneInputParam,
    DenylistEthereumAddressInputParam,
    DenylistSolanaAddressInputParam,
]
