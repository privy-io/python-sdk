# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["TransferInitiationChannel"]

TransferInitiationChannel: TypeAlias = Union[Literal["p2p_mobile_payment", "other_mobile_payment", "other"], str]
