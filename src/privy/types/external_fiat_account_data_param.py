# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .external_fiat_account_gb_data_param import ExternalFiatAccountGBDataParam
from .external_fiat_account_us_data_param import ExternalFiatAccountUsDataParam
from .external_fiat_account_pix_data_param import ExternalFiatAccountPixDataParam
from .external_fiat_account_iban_data_param import ExternalFiatAccountIbanDataParam
from .external_fiat_account_swift_data_param import ExternalFiatAccountSwiftDataParam

__all__ = ["ExternalFiatAccountDataParam"]

ExternalFiatAccountDataParam: TypeAlias = Union[
    ExternalFiatAccountUsDataParam,
    ExternalFiatAccountGBDataParam,
    ExternalFiatAccountPixDataParam,
    ExternalFiatAccountIbanDataParam,
    ExternalFiatAccountSwiftDataParam,
]
